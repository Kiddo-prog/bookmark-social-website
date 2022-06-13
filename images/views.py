import imp
from django.shortcuts import get_object_or_404, render, redirect
from images.forms import ImageForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from images.models import Images

# Create your views here.


def create_image(request):
    if request.method == "POST":
        form = ImageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            new_image.user = request.user
            new_image.save()
            messages.success(request, "Image created successfully")
            return redirect(new_image.get_absolute_url())
        else:
            messages.error(request, "Error creating image")

    else:
        form = ImageForm()
    return render(request, "images/create.html", {"form": form})


def image_detail(request, id, slug):
    image = get_object_or_404(Images, id=id, slug=slug)
    return render(request, "images/detail.html", {"image": image})

@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')

    if image_id and action:
        try:
            image = Images.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'error'})