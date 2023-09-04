from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        params = {
            "username": request.user.username,
            "firstName":request.user.first_name,
            "lastName":request.user.last_name,
        }

        return render(request, 'index.html', params)
    else:
        return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username');
        password = request.POST.get('password');
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("/records/"+username)
        else:
            return redirect("/")


def logout(request):
    auth_logout(request)
    return redirect("/")


def records(request, username):
    if request.user.is_authenticated and request.user.username==username:
        user = User.objects.get(email=username)
        services = ServiceRecords.objects.filter(user=user)
        params={
            "username":request.user.username,
            "services": services
            
        }
        return render(request, 'records.html', params)
    else:
        return render(request, 'records.html')


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        user = User.objects.create_user(username=email,
                                 email=email,
                                 password=password)
        user.first_name = fname
        user.last_name = lname
        user.save()
        Customers(fname=fname, lname=lname, email=email, user=user, contact=contact, password=password).save()
        return redirect('/records/'+email)
    else:
        return render(request, "register.html")


def addService(request):
    user = User.objects.get(id=request.user.id)
    ServiceRecords(user=user, service=request.POST['serviceName'], email=request.POST['username'], password=request.POST['password']).save()
    return redirect("/records/"+request.user.username)


def editService(request, username, id):
    user = User.objects.get(id=request.user.id)
    if request.method=='POST':
        svc = ServiceRecords.objects.get(user=user, id=id)
        svc.service=request.POST.get('serviceName'+str(id))
        svc.email=request.POST.get('username'+str(id))
        svc.password=request.POST.get('password'+str(id))
        print('sdg: '+svc.email)
        svc.save()
    return redirect("/records/"+request.user.username)

def deleteService(request, id):
    ServiceRecords.objects.get(id=id).delete()
    return redirect("/records/"+request.user.username)

