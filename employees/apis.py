# from django.contrib.auth import authenticate, login as auth_login, logout 
# from rest_framework.response import Response
# from rest_framework import serializers, status
# from rest_framework.views import APIView

# class LoginView(APIView):
#     class InputSerializer(serializers.Serializer):
#         email = serializers.EmailField()
#         password = serializers.CharField()

#     def post(self, request):
#         try:
#             serializer = self.InputSerializer(data=request.data)

#             serializer.is_valid()

#             data = serializer.validated_data

#             email = data['email']

#             password = data['password']
            
#             user = authenticate(request, username=email, password=password)

#             if user is not None:
#                 auth_login(request, user)
#                 return Response({'message': 'Login successful', 'user_id': user.id}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
#         except serializers.ValidationError as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         except Exception as e:
#             return Response({'error: '+ str(e)}, status=status.HTTP_400_BAD_REQUEST)

# class LogoutView(APIView):
#     def post(self, request):
#         # Log the user out
#         logout(request)
#         return Response({'message': 'Logout successful'})