from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from django.shortcuts import redirect

#from dashboard import SQL_Database

from dashboard.forms import DocumentForm

from dashboard import Question

# d = SQL_Database("cat","root","maggie")

# Create your views here.

#homepage for a basic user. 
#displays available materials to the user
def home(request):
    titles = ["t1", "t2", "t3", "t4"]
    return render(request, 'home.html', {'titles': titles});

#page for file upload
#saves file if it is valid
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
