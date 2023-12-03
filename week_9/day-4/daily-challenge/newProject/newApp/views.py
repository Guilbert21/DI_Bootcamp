from django.shortcuts import render
from .models import Image
from .form import ImageForm
# import Pillow

def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # print(form.cleaned_data["image"].file.__dict__)
            Image_final = (Image.objects.get(id= 1))

            return render(request, 'index.html', {"uploaded_image": Image_final,"form":form})
    else:
        form = ImageForm()
    return render(request,"index.html",{"form":form})


