import io
import random

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from App.models import UserT


def index(request):
    print("***************index*****************")
    return render(request,'index.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    print("****************register")
    if request.method == "GET":
        return render(request,'register.html')

    elif request.method == "POST":
        usertel = request.POST.get("usertel")
        res_user = UserT.objects.filter(tel=usertel)
        print(res_user)
        if len(res_user) == 0:
            return HttpResponse("OK")
        else:
            return HttpResponse("existed")
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # tel = request.POST.get('tel')
        # if UserT.objects.filter(Q(username=username),Q(tel=tel)) != []:
        #     render(request,'register.html')
        # else:
        #     user = UserT()
        #     user.username = username
        #     user.password = password
        #     user.tel = tel
        #     user.save()
        #     response = redirect("app:index")
        #     response.set_cookie("username",username)
        #     return response
    #return render(request,'register.html')


# from PIL import ImageFont,ImageDraw,Image
#
#
# def verificationcode(request):
#     width =100
#     height =50
#     color = (random.randrange(256),random.randrange(256),random.randrange(256))
#     img = Image.new("RGB", (width,height), color)
#
#     buff = io.BytesIO()
#     img.save(buff,'png')
#     return HttpResponse(buff.getvalue(), "image/png")


def project(request):
    print("***************product*****************")
    return render(request,'product.html')