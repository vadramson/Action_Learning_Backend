from rest_framework import serializers

from uploadapp.models import File, Clothings, Predictions


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class ClothingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothings
        fields = "__all__"


class PredictionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = "__all__"
