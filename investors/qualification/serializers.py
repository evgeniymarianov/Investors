from rest_framework import serializers
from .models import *


class DocumentSerializer(serializers.ModelSerializer):

    class Meta():
        model = Document
        fields = "__all__"


class QualificationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Investor
        fields = ['qualification_status',]


class PassportSerializer(serializers.ModelSerializer):

    class Meta():
        model = Passport
        fields = "__all__"
