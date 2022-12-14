from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from enroll.forms import StudentRegistrations
from enroll.models import User

# Create your views here.


def add_show(request):
    if request.method == 'POST':
        form = StudentRegistrations(request.POST)
        if form.is_valid():
            # form.save()
            nm = form.cleaned_data['name']
            em = form.cleaned_data['email']
            pw = form.cleaned_data['password']
            # reg = User(name=nm, email=em)
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            form = StudentRegistrations()
    else:
        form = StudentRegistrations()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': form, 'stud': stud})


def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        form = StudentRegistrations(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = User.objects.get(pk=id)
        form = StudentRegistrations(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': form})
