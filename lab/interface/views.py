from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseRedirect
from . models import User
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, "index/home.html")

def branches(request):
    return render(request, "index/branches.html")

def create(request):
    names = [
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chhattisgarh",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Telangana",
        "Tripura",
        "Uttar Pradesh",
        "Uttarakhand",
        "West Bengal"
    ]
    if request.method == "POST":
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        address = request.POST["address"]
        name = request.POST["name"]
        test = request.POST["test"]
        print(email, phonenumber, address, name, test)
        user = User(name=name, email=email, address=address, phone=phonenumber)
        user.save()
    return render(request, "index/create.html",{"names" : names})


def status(request):
    submissions = User.objects.all()

    return render(request, "index/status.html" , )


def contact(request):
    return render(request, "index/contact.html")

def lists(request):
    return render(request, "index/lists.html")