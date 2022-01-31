from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import TweetModel
from .forms import TweetForm
from .serializers import TweetSerializer, TweetActionSerializer


def tweet_view_old(request, tweet_id, *args, **kwargs) -> render:
    query = get_object_or_404(TweetModel, pk=tweet_id)
    # query = TweetModel.objects.get(id=tweet_id)
    return render(
        request,
        "tweets/tweet.html",
        context=({"id": query.id, "content": query.content}),
    )


@api_view(["GET"])
def tweet_view(request, tweet_id, *args, **kwargs) -> render:
    query = get_object_or_404(TweetModel, pk=tweet_id)
    serializer = TweetSerializer(query)
    return Response(serializer.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
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
        print(data)
        tweet_id = data.get("id")
        action = data.get("action")
        queryset = TweetModel.objects.filter(id=tweet_id)
        print(queryset)
        if not queryset.exists():
            return Response({}, status=404)
        obj = queryset.first()
        if action == "like":
            obj.likes.add(request.user)
        elif action == "unlike":
            obj.likes.remove(request.user)
        elif action == "retweet":
            pass

    return Response({"message": "Tweet action happened successfully"}, status=200)


@api_view(["GET"])
def tweets_list_json(request, *args, **kwargs) -> Response:
    queryset = TweetModel.objects.all()
    serializer = TweetSerializer(queryset, many=True)
    return Response(serializer.data)


def tweets_list_json_old(request, *args, **kwargs) -> JsonResponse:
    query = TweetModel.objects.all()
    serialize = [
        {"id": item.id, "content": item.content, "likes": 42} for item in query
    ]
    json_response = {"response": serialize}
    return JsonResponse(json_response)


def tweets_list_view(request, *args, **kwargs):
    return render(request, "pages/index.html")


def tweet_create_view_old(request, *args, **kwargs):
    # print(request.META)  # woah
    user = request.user
    if not user.is_authenticated:
        if request.accepts(
            "application/json"
        ):  # if unauthorized ajax call -> 401, else redirect
            user = None
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)

    form = TweetForm(request.POST)
    # redirect_to = request.POST.get("next")
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        form = TweetForm()
        return JsonResponse(obj.serialize(), status=201)

    if form.errors:
        return JsonResponse(form.errors, status=400)

    return render(request, "components/forms.html", context={"form": form})
