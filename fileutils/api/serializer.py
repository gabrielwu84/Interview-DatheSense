from rest_framework import serializers
import os

from fileutils.models import Upload

class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upload
        fields =  "__all__"

class UploadSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
       default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = Upload
        fields = "__all__"
