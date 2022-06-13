from django.contrib import admin

from accounts.models import Profile
from images.models import Images

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth", "photo")


@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "image", "created")
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("created",)
