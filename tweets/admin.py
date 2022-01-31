from django.contrib import admin

# Register your models here.
from .models import TweetModel, TweetLikeModel


class TweetLikeAdmin(admin.TabularInline):
    model = TweetLikeModel


class TweetAdmin(admin.ModelAdmin):
    inlines = [TweetLikeAdmin]
    list_display = ["__str__", "user"]
    search_fields = ["content", "user__username", "user__email"]

    class Meta:
        model = TweetModel


admin.site.register(TweetModel, TweetAdmin)
