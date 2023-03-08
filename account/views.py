from django.shortcuts import render, redirect

from .models import *
from .forms import CommentForm, UpdateForm

# Create your views here.

def index(request):
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
        'comment':comment,
        'form':form,
        'cform':cform
        }
    return render(request, 'index.html', context)

def SuccessView(request):
    return render(request, 'success.html')
