from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model


from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    ChangePasswordSerializer,
)

User = get_user_model()


# -------------------------
# AUTH VIEWS
# -------------------------

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data,
            context={"request": request}  # ✅ CRITICAL FIX
        )
        serializer.is_valid(raise_exception=True)

        # ✅ serializer.validate() already returned the user
        user = serializer.validated_data

        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserProfileSerializer(user).data,
        })


class LogoutView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        return Response({"detail": "Logged out successfully"})


# -------------------------
# USER (ME)
# -------------------------

class MeView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/users/me/
    PUT    /api/users/me/
    DELETE /api/users/me/
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not user.check_password(serializer.validated_data["old_password"]):
            return Response(
                {"detail": "Wrong password"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(serializer.validated_data["new_password"])
        user.save()
        return Response({"detail": "Password updated successfully"})


class UserStatsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk=None):
        user = request.user
        if pk and str(pk) != str(user.id):
            return Response(status=status.HTTP_403_FORBIDDEN)
            
        return Response({
            "totalSkills": user.skills.count(),
            "totalProjects": user.projects.count(),
            "completedProjects": user.projects.filter(status="completed").count(),
            "activeProjects": user.projects.exclude(status="completed").count(),
            "memberSince": user.date_joined.strftime("%Y-%m-%dT%H:%M:%SZ") if user.date_joined else None,
        })


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/users/:id/
    PUT    /api/users/:id/
    DELETE /api/users/:id/
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj != self.request.user:
            self.permission_denied(self.request, message="Not allowed to access other users.")
        return obj

class AvatarUploadView(generics.GenericAPIView):
    """
    POST /api/users/:id/avatar/
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        if str(pk) != str(request.user.id):
            return Response(status=status.HTTP_403_FORBIDDEN)

        avatar = request.FILES.get('avatar')
        if not avatar:
            return Response({"detail": "No avatar file provided"}, status=status.HTTP_400_BAD_REQUEST)

        request.user.avatar = avatar
        request.user.save()

        # Build full URL if request is available, else relative
        avatar_url = request.build_absolute_uri(request.user.avatar.url) if request.user.avatar else None

        return Response({"avatar": avatar_url}, status=status.HTTP_200_OK)
