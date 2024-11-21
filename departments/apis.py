from django.shortcuts import render
from guardian.decorators import permission_required

from departments.services import department_create, jobtitle_create
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status


@permission_required('departments.can_create_department', return_403=True)
class DepartmentCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        department_name = serializers.CharField()
        description = serializers.CharField()
        contact_phone = serializers.IntegerField()
        contact_email = serializers.EmailField()
        is_active = serializers.BooleanField()

    def post(self, request):

        serializer = self.InputSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data

            department = department_create(
                department_name=data['department_name'],
                description=data['description'],
                contact_phone=data['contact_phone'],
                contact_email=data['contact_email'],
                is_active=data['is_active']
            )

            return Response(department, status=status.HTTP_201_CREATED)
        
        # If data is not valid, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      


class JobTitleCreateView(APIView):

    class InputSerializers(serializers.Serializer):
        title = serializers.CharField()

    def post(self,request):
        serializer_class = self.InputSerializers
        input_vaidate = serializer_class.validated_data

        if input_vaidate:
            jobtitle_create(serializer_class.data)

            return Response(f'successfully created a jobtitle {serializer_class.data}', status=status.HTTP_201_CREATED)
        
        return Response(f'faild to created a jobtitle {serializer_class.data}', status=status.HTTP_400_BAD_REQUEST)