from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer



User = get_user_model()

@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data, status=200)



@api_view(['POST'])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response('Пост успешно создан', status=201)
    

@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return Response('Пост успешно удален', status=204)


@api_view(['PATCH'])
def patch_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(instance=post, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

@api_view(['PUT'])
def put_post(requiest, pk):
    post = get_object_or_404(Post, id=pk)
    serializer = PostSerializer(instance=post, data=requiest.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)