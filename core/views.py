from django.shortcuts import render, redirect, HttpResponse
from .forms import ImageForm
from io import BytesIO
from PIL import Image
import base64

# Create your views here.
def img_yolo(request):
    
    form = ImageForm()
    
    if request.method == 'POST':
        img = Image.open(request.FILES['image'])
        img = img.resize((200, 200))
        buffer = BytesIO()
        img.save(buffer, "PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode('utf-8')
        context = {
            'form': form,
            'img_str': img_str,
        }


        return render(request, 'index.html', context)

    context = {
        'form': form
    }

    return render(request, 'index.html', context)