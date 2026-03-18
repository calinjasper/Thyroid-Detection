from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, UserImageForm
from .models import UserImageModel
from PIL import Image, ImageOps
import numpy as np
from tensorflow import keras
from django.conf import settings
import os
from django.contrib.auth.decorators import login_required

# Load the model when the application starts
model_path = os.path.join(settings.BASE_DIR, 'app', 'keras_model.h5')
model = keras.models.load_model(model_path)

@login_required
def profile(request):
    return render(request, 'profile.html')

    
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def landingpage(request):
    return render(request, 'landingpage.html')

def about(request):
    return render(request, 'about.html')


def register(request):
    form = CreateUserForm()
    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register1.html', context)


def loginpage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'registration/login1.html', context)

def logoutusers(request):
    logout(request)
    return redirect('login')



  
def Deploy_8(request):
    if request.method == "POST":
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            try:
                result1 = UserImageModel.objects.latest('id')
                image_path = os.path.join(settings.MEDIA_ROOT, str(result1.image))
                data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
                image = Image.open(image_path).convert("RGB")
                size = (224, 224)
                image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
                image_array = np.asarray(image)
                normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
                data[0] = normalized_image_array
                classes = ['NORMAL', 'TIRADS1','TIRADS2', 'TIRADS3', 'TIRADS4', 'TIRADS5']
                prediction = model.predict(data)
                idd = np.argmax(prediction)
                a = (classes[idd])
                if a == 'NORMAL':
                    b = 'Normal'
                elif a == 'TIRADS1':
                    b = 'Thyroid stage 1'
                elif a == 'TIRADS2':
                    b = 'Thyroid stage 2'
                elif a == 'TIRADS3':
                    b = 'Thyroid stage 3'
                elif a == 'TIRADS4':
                    b = 'Thyroid stage 4'
                elif a == 'TIRADS5':
                    b = 'Thyroid stage 5'
                else:
                    b = 'WRONG INPUT'

                result1.label = a
                result1.save()

                return render(request, 'output.html', {'form': form, 'obj': obj, 'predict': b})
            except Exception as e:
                messages.error(request, f"Error processing image: {e}")
                return redirect('home')
    else:
        form = UserImageForm()
    return render(request, 'model.html', {'form': form})




