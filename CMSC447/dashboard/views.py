from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from django.shortcuts import redirect

# Create your views here.

from dashboard.forms import DocumentForm

def home(request):
    titles = ["t1", "t2", "t3", "t4"]
    return render(request, 'home.html', {'titles': titles});

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {
        'form': form
    })