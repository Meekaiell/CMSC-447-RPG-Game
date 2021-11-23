from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from django.shortcuts import redirect

# Create your views here.

from dashboard.forms import DocumentForm

from dashboard import Question

#homepage for a basic user. 
#displays available materials to the user
def student(request):
    titles = ["t1", "t2", "t3", "t4"]
    return render(request, 'student.html', {'titles': titles})

#page for file upload
#saves file if it is valid
def admin(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin')
    else:
        form = DocumentForm()
    return render(request, 'admin.html', {'form' : form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if username == "admin" and password == "admin" :
            return redirect('admin')

        if username == "student" and password == "student" :
            return redirect('student')
        
    return render(request, 'login.html')