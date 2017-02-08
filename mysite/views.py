from django.shortcuts import render,redirect,HttpResponseRedirect,redirect
from django.http import HttpResponse
from .models import Mqtt,Gps
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.admin import User
from django.contrib.auth import authenticate, login as auth_login, logout
import requests

# Create your views here.


def login(request):
    return render(request,"loginPage.html", {})

def beta(request):
    return HttpResponseRedirect('http://kranioz.com/static/demo/index2.html')

@login_required
def home(request):
    all_entries = Gps.objects.order_by("-time")
    table_entries = Gps.objects.order_by("-time")
    latest = Gps.objects.last()
    # print(latest.lat)
    url = "http://kranioz.com/api/map/?format=json"
    r = requests.get(url)
    draw = r.json()
    print(r.json())
    context_pass = {
        "objects":table_entries,
        "lat":latest.lat,
        "lng":latest.lng,
        "drawable":draw,
        "mapobjects":all_entries
    }
    return render(request,'baseAdmin.html',context_pass)

def store(request):
    message = request.GET.get("q")
    topic = request.GET.get("t")

    if message:
        print(str(message))
        m = Mqtt(msg=message)
        m.time = timezone.now()
        m.topic = topic
        m.save()
        return HttpResponse("OK,data stored in database")
    else:
        return redirect("mysite:home")


def log_data(request):
    if request.method == 'GET':
        lat_info = request.GET.get("lat")
        lng_info = request.GET.get("lng")
        bat = request.GET.get("bat")
        device_info = request.GET.get("id")
        this_object = Gps(lat=lat_info,lng=lng_info,deviceId=device_info,speed=bat)
        this_object.save()
        #print(lat_info)
        return HttpResponse("Ok")
    else:
        return HttpResponse("NotOk")


def latest_entry(request):
    queryset = Gps.objects.last()
    object_pk = queryset.pk
    #print(object_pk)
    url = str(object_pk)
    url = "/api/"+ url + "/" + "?format=json"
    print(url)
    return redirect(url)


def Homelogin(request):
    if request.method == 'POST':
        username = request.POST.get("loginemail")
        loginpassword = request.POST.get("loginpassword")
        # messages.success(request, "printed post data sussesfully\n" + username +"\n" + request.POST.get("loginpassword") )
        user = authenticate(username=username, password=loginpassword)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                messages.success(request, "You have been securely logged in")
                return redirect("mysite:homePage")
            else:
                messages.success(request, "The password is valid, but the account has been disabled!"
                                          " Please contact us, mail : bosch@makervillage.in")
                return redirect("mysite:login")
        else:
            messages.success(request, "The username and password were incorrect,or you may not activated.check your mail for activation link ")
            return redirect("mysite:login")

    return redirect("mysite:login")


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out Succesfully")
    return HttpResponseRedirect('/login/')
