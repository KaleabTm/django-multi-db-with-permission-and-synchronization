from rest_framework.views import APIView
from rest_framework import status
from rest_framework import serializers
from .services import create_post
from rest_framework.response import Response
from guardian.decorators import permission_required

# Create your views here.

@permission_required('posts.can_create_post', return_403=True)
class PostCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        title=serializers.CharField()
        content=serializers.CharField()

    def post(self,request):
        serializer_class = self.InputSerializer(request.data)

        if serializer_class.is_valid():
            data = serializer_class.validated_data()

            post = create_post(
                    title=data['title'],
                    content=data['content'],
                    )
            return Response(post, status=status.HTTP_201_CREATED)
        return Response(serializer_class.error_messages, status=status.HTTP_400_BAD_REQUEST)




