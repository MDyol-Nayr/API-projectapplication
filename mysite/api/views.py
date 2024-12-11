from rest_framework.response import Response
from rest_framework.decorators import api_view
from blog.models import Post
from .serializers import PostSerializer

@api_view(['GET'])
def viewPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def viewPostDetail(request, pk):
    try:
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

@api_view(['POST'])
def addPosts(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Post created successfully!', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def updatePost(request, pk):
    try:
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data, partial=(request.method == 'PATCH'))
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Post updated successfully!', 'data': serializer.data})
        return Response(serializer.errors, status=400)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)

@api_view(['DELETE'])
def deletePost(request, pk):
    try:
        post = Post.objects.get(id=pk)
        post.delete()
        return Response({'message': 'Post deleted successfully!'}, status=200)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=404)
