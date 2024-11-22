from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .services import create_users, user_org_relation
from departments.models import JobTitle

# Create your views here.

class UserCreateView(APIView):
    class UserSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        phone_number = serializers.CharField()
        email = serializers.CharField()
        password = serializers.CharField()

    def post(self,request):
        serializer_class = self.UserSerializer(data=request.data)

        if not serializer_class.is_valid():
            print("Validation Errors:", serializer_class.errors)  # Log for debugging
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer_class.validated_data
        hashed_password = make_password(data['password'])

        user = create_users(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=hashed_password,
                phone_number=data['phone_number'],
            )
        user_serialized = self.UserSerializer(user)

        return Response(user_serialized.data, status=status.HTTP_201_CREATED)
        


class UserOrgRelationCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        user = serializers.CharField()
        organization = serializers.CharField()
        position = serializers.CharField()
        is_active = serializers.BooleanField()

    def post(self,request):
        serializer_class = self.InputSerializer(data=request.data)

        if not serializer_class.is_valid():
            print("Validation Errors:", serializer_class.errors)  # Log for debugging
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer_class.validated_data

        position = JobTitle.objects.get(title=data['position'])

        relation=user_org_relation(
            user=data['user'],
            organization=data['organization'],
            position=position,
            is_active=data['is_active']
        )

        return Response(f"User {relation.user.first_name} is assigned {relation.position} positon at {relation.organization.org_name}",status=status.HTTP_201_CREATED)

