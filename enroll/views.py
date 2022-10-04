
from django.shortcuts import render
from .forms import StudentRegistration


# Create your views here.
def showdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            print(nm)
            print(em)
            print(pw)
            

    else:
        fm = StudentRegistration()
    return render (request, 'enroll/registration.html', {'form':fm})
