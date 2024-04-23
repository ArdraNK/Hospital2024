
from django.shortcuts import render

from myapp.forms import BookingForm
from myapp.models import Doctors, department


# Create your views here.
def show(request):
    return render(request,'Base.html')

def homes(request):
    return render(request,'Home.html')

def aboutus(request):
    return render(request,'About.html')

def booking(request):
    return render(request,'Booking.html')

def form(request):
    Form1= BookingForm()
    dict2 = {"myform": Form1}
    if request.method == 'POST':
        Form1=BookingForm(request.POST)
        if Form1.is_valid():
            Form1.save()

    return render(request,'Booking.html',dict2)



def doctors_list(request):

        return render(request, 'Doctors.html')
def displayfunction(request):
    s1 = Doctors.objects.all()
    context = {'doc': s1}
    return render(request, 'Doctors.html', context)



def Department(request):
    return render(request,'Department.html')

def showmsg(request):
    k1 =department.objects.all()
    dict={'dep':k1}
    return render(request,'Department.html',dict)

def contactus(request):
    return render(request,'Contact.html')
