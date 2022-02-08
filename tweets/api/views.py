from rest_framework.pagination import PageNumberPagination
from django.shortcuts import render, get_object_or_404

# from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..models import TweetModel
from ..serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer


@api_view(["GET"])
def tweet_view(request, tweet_id, *args, **kwargs) -> render:
    query = get_object_or_404(TweetModel, pk=tweet_id)
    serializer = TweetSerializer(query)
    return Response(serializer.data)


@api_view(["GET"])
def tweet_feed_view(request, *args, **kwargs):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    queryset = TweetModel.objects.all()
    paginated_queryset = paginator.paginate_queryset(queryset, request)
    serializer = TweetSerializer(paginated_queryset, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    # print(serializer.data)
    return Response({}, status=400)


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    query = get_object_or_404(TweetModel, pk=tweet_id)
    query.delete()
    return Response({"message": "Deleted successfully"}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def tweet_action_view(request, *args, **kwargs):
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        queryset = TweetModel.objects.filter(id=tweet_id)
        if not queryset.exists():
            return Response({}, status=404)
        obj = queryset.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "retweet":
            parent_obj = obj
            parent_content = parent_obj.content
            new_tweet = TweetModel.objects.create(
                user=request.user,
                content=parent_content,
                parent=parent_obj,
            )
            serializer = TweetSerializer(new_tweet)
            print(serializer.data)
            return Response(serializer.data, status=201)
    return Response({"message": "Invalid data has been provided"}, status=403)


@api_view(["GET"])
def tweets_list_json(request, *args, **kwargs) -> Response:
    queryset = TweetModel.objects.all()
    serializer = TweetSerializer(queryset, many=True)
    return Response(serializer.data)
