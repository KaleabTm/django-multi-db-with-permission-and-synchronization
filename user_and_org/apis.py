from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from user_and_org.services import create_users, user_org_relation

# Create your views here.

class UserCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        first_name = serializers.CharField()
        last_name = serializers.CharField()
        phone_number = serializers.CharField()
        email = serializers.CharField()
        password = serializers.CharField()

    def post(self,request):
        serializer_class = self.InputSerializer(request.data)

        if serializer_class.is_valid():
            ...
            data = serializer_class.validated_data

            user = create_users(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                password=data['password'],
                phone_number=data['phone_number']
            )

            return Response(user, status=status.HTTP_201_CREATED)
        
        # If data is not valid, return errors
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)  


class UserOrgCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        user = serializers.CharField()
        organization = serializers.CharField()
        position = serializers.CharField()
        is_active = serializers.BooleanField()

    def post(self,request):
        serializer_class = self.InputSerializer(request.data)

        if serializer_class.is_valid():

            data = serializer_class.validated_data()

            relation=user_org_relation(
                user=data['user'],
                organization=data['organization'],
                position=data['position'],
                is_active=data['is_active']
            )

            return Response(relation,status=status.HTTP_201_CREATED)

        return Response(serializer_class.error_messages,status=status.HTTP_400_BAD_REQUEST)



