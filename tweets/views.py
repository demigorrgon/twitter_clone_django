from django.shortcuts import render, get_object_or_404

# from django.conf import settings
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from .models import TweetModel
# from .serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer


def tweets_list_view(request, *args, **kwargs):
    return render(request, "pages/index.html")


# def tweet_view_old(request, tweet_id, *args, **kwargs) -> render:
#     query = get_object_or_404(TweetModel, pk=tweet_id)
#     # query = TweetModel.objects.get(id=tweet_id)
#     return render(
#         request,
#         "tweets/tweet.html",
#         context=({"id": query.id, "content": query.content}),
#     )


# def tweets_list_json_old(request, *args, **kwargs) -> JsonResponse:
#     query = TweetModel.objects.all()
#     serialize = [
#         {"id": item.id, "content": item.content, "likes": 42} for item in query
#     ]
#     json_response = {"response": serialize}
#     return JsonResponse(json_response)


# def tweet_create_view_old(request, *args, **kwargs):
#     # print(request.META)  # woah
#     user = request.user
#     if not user.is_authenticated:
#         if request.accepts(
#             "application/json"
#         ):  # if unauthorized ajax call -> 401, else redirect
#             user = None
#             return JsonResponse({}, status=401)
#         return redirect(settings.LOGIN_URL)

#     form = TweetForm(request.POST)
#     # redirect_to = request.POST.get("next")
#     if form.is_valid():
#         obj = form.save(commit=False)
#         obj.user = user
#         obj.save()
#         form = TweetForm()
#         return JsonResponse(obj.serialize(), status=201)

#     if form.errors:
#         return JsonResponse(form.errors, status=400)

#     return render(request, "components/forms.html", context={"form": form})
