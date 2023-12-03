from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Image

@login_required
def upload_image(request):
    if request.method == 'POST':
        image = request.FILES['image']
        Image.objects.create(user=request.user, image=image)
        return redirect('images')
    return render(request, 'upload_image.html')

def filter_images(request):
    if request.method == 'POST':
        start_date = request.post.get('start_date')
        end_date = request.post.get('end_date')
        images = Image.objects.filter(upload_date__range=[start_date, end_date])

    else:
        images = Image.objects.all()
    return render(request, 'images.html', {'images': images})

