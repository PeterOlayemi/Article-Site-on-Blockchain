from django.shortcuts import render, redirect

from .models import *
from .forms import CommentForm, UpdateForm

# Create your views here.

def index(request):
    image1=Image1.objects.all()
    image2=Image2.objects.all()
    image3=Image3.objects.all()
    image4=Image4.objects.all()
    image5=Image5.objects.all()
    image6=Image6.objects.all()
    image7=Image7.objects.all()
    image8=Image8.objects.all()
    image9=Image9.objects.all()
    comment=Comment.objects.order_by('-date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CommentForm()

    if request.method == 'POST':
        cform = UpdateForm(request.POST)
        if cform.is_valid():
            cform.save()
            return redirect('success')
    else:
        cform = UpdateForm()

    context={
        'image1':image1,
        'image2':image2,
        'image3':image3,
        'image3':image3,
        'image4':image4,
        'image5':image5,
        'image6':image6,
        'image7':image7,
        'image8':image8,
        'image9':image9,
        'comment':comment,
        'form':form,
        'cform':cform
        }
    return render(request, 'index.html', context)

def SuccessView(request):
    image3 = Image3.objects.all()
    return render(request, 'success.html', {'image3':image3})
