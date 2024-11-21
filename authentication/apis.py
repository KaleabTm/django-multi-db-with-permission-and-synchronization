from django.contrib.auth import authenticate, login as auth_login, logout 
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.views import APIView



class LoginView(APIView):
    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def post(self, request):
        # Deserialize the request data
        serializer = self.InputSerializer(data=request.data)
        
        # Validate the input
        if serializer.is_valid():
            # Get the validated data
            data = serializer.validated_data
            email = data['email']
            password = data['password']
            
            # Authenticate the user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # If authentication is successful, log the user in
                auth_login(request, user)
                return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
            else:
                # Invalid credentials
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Invalid data
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)



class LogoutView(APIView):
    def post(self, request):
        # Log the user out
        logout(request)
        return Response({'message': 'Logout successful'})


