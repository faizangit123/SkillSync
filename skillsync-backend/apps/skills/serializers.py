from rest_framework import serializers
from .models import Skill


class SkillSerializer(serializers.ModelSerializer):
    yearsOfExperience = serializers.IntegerField(
        source="years_of_experience", required=False, default=0
    )
    createdAt = serializers.DateTimeField(source="created_at", read_only=True)
    updatedAt = serializers.DateTimeField(source="updated_at", read_only=True)
    userId = serializers.IntegerField(source="user.id", read_only=True)

    class Meta:
        model = Skill
        fields = (
            "id",
            "userId",
            "name",
            "category",
            "proficiency",
            "yearsOfExperience",
            "createdAt",
            "updatedAt",
        )
        read_only_fields = ("id", "createdAt", "updatedAt", "userId")
