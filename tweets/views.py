from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import TweetModel


def tweet_view(request, tweet_id, *args, **kwargs) -> render:
    query = get_object_or_404(TweetModel, pk=tweet_id)
    # query = TweetModel.objects.get(id=tweet_id)

    return render(
        request,
        "pages/tweet.html",
        context=({"id": query.id, "content": query.content}),
    )


def tweets_list_json(request, *args, **kwargs) -> JsonResponse:
    query = TweetModel.objects.all()
    serialize = [
        {"id": item.id, "content": item.content, "likes": 42} for item in query
    ]
    json_response = {"response": serialize}
    return JsonResponse(json_response)


def tweets_list_view(request, *args, **kwargs):
    return render(request, "pages/index.html")
