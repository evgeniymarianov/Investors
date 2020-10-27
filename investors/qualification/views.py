from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,  JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    DocumentSerializer,
    QualificationStatusSerializer,
    PassportSerializer,
)
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework import generics


# @csrf_exempt
# def investor_status(request, pk):
#     """Получение текущего статуса квалификации"""
#     try:
#         investor = Investor.objects.get(pk=pk)
#     except Investor.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = QualificationStatusSerializer(investor)
#         return JsonResponse(serializer.data)


class PassportView(APIView):
    """Загрузка паспорта (файла)"""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        passport_serializer = PassportSerializer(data=request.data)
        if passport_serializer.is_valid():
            passport_serializer.save()
            return Response(passport_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(passport_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'GET'])
def passport_detail(request, pk):
    """Загрузка паспортных данных (1 шаг)"""
    try:
        passport = Passport.objects.get(pk=pk)
    except Passport.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PassportSerializer(passport)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PassportSerializer(passport, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QualificationStatusView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, изменение и текущего статуса квалификации"""
    queryset = Investor.objects.all()
    serializer_class = QualificationStatusSerializer


class DocumentView(APIView):
    """Загрузка документа о квалификации"""
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        document_serializer = DocumentSerializer(data=request.data)
        if document_serializer.is_valid():
            document_serializer.save()
            return Response(document_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(document_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
