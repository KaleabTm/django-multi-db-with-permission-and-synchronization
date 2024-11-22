from django.shortcuts import render
from guardian.decorators import permission_required

from departments.services import department_create, jobtitle_create
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


# @permission_required('departments.can_create_department', return_403=True)
class DepartmentCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        department_name = serializers.CharField()
        description = serializers.CharField()
        contact_phone = serializers.IntegerField()
        contact_email = serializers.EmailField()
        is_active = serializers.BooleanField()

    def post(self, request):

        serializer = self.InputSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.validated_data

        department = department_create(
            department_name=data['department_name'],
            description=data['description'],
            contact_phone=data['contact_phone'],
            contact_email=data['contact_email'],
            is_active=data['is_active']
        )

        return Response(department, status=status.HTTP_201_CREATED)   


class JobTitleCreateView(APIView):

    class InputSerializers(serializers.Serializer):
        title = serializers.CharField()

    def post(self,request):
        serializer_class = self.InputSerializers

        if not serializer_class.is_valid():
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer_class.validated_data
        position = jobtitle_create(data['title'])

        return Response(f'successfully created a jobtitle {position}', status=status.HTTP_201_CREATED)