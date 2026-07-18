from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NotificationSettings, UserSettings
from .serializers import NotificationSettingsSerializer, UserSettingsSerializer
import uuid

class NotificationSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = NotificationSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj, created = NotificationSettings.objects.get_or_create(user=self.request.user)
        return obj

class UserSettingsView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSettingsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj, created = UserSettings.objects.get_or_create(user=self.request.user)
        return obj

class EnableTwoFactorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        settings, _ = UserSettings.objects.get_or_create(user=request.user)
        settings.two_factor_enabled = True
        settings.save()
        return Response({
            "qrCode": "mock_qr_code_url", 
            "secret": "mock_secret"
        }, status=status.HTTP_200_OK)

class DisableTwoFactorView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        settings, _ = UserSettings.objects.get_or_create(user=request.user)
        settings.two_factor_enabled = False
        settings.save()
        return Response(status=status.HTTP_200_OK)

class ExportUserDataView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        import json
        from django.http import HttpResponse

        user_data = {
            "email": request.user.email,
            "name": request.user.name,
        }
        response = HttpResponse(json.dumps(user_data), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="user_data_export.json"'
        return response
