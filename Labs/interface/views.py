from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import User, Test
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, "index/home.html")

def branches(request):
    return render(request, "index/branches.html")
tests = [   'Blood Test' ,'Urinalysis' ,'X-ray'
  ,'Electrocardiogram'
  ,'CT Scan (Computed Tomography)'
  ,'MRI (Magnetic Resonance Imaging)'
  ,'Blood Pressure Measurement'
  ,'Cholesterol Test'
  ,'Complete Blood Count (CBC)'
  ,'Blood Sugar Test (Glucose Test)'
  ,'Liver Function Test'
  ,'Kidney Function Test'
  ,'Pregnancy Test'
  ,'Thyroid Function Test'
  ,'HIV Test'
  ,'Hepatitis Test'
  ,'Stool Test'
  ,'Bone Density Test'
  ,'Pap Smear (Cervical Smear)'
  ,'Mammogram'
  ,'Prostate-Specific Antigen (PSA) Test'
  ,'Allergy Test'
  ,'Pulmonary Function Test '
  ,'Vision Test'
  ,'Hearing Test'
  ,'Skin Biopsy' ]
def create(request):
    if request.method == "POST":
        try:
            email = request.POST.get("email")
            phonenumber = request.POST.get("phonenumber")
            address = request.POST.get("address")
            name = request.POST.get("name")
            test = request.POST.get("test")
            
            if not all([email, phonenumber, address, name, test]):
                messages.error(request, "All fields are required.")
                return render(request, "index/create.html", {"tests": tests})
            
            user = User(name=name, email=email, address=address, phone=phonenumber)
            test_model = Test(name=name, email=email, test=test, test_status=False)
            user.save()
            test_model.save()
            
            messages.success(request, "Test booked successfully!")
            return redirect("status")
        except Exception as e:
            messages.error(request, "An error occurred while booking the test.")
            return render(request, "index/create.html", {"tests": tests})
    
    return render(request, "index/create.html", {"tests": tests})

def status(request):
    if request.method == "POST":
        email = request.POST.get("email")
        number = request.POST.get("contact")
        
        if not email and not number:
            messages.error(request, "Please provide either email or contact number.")
            return render(request, "index/status.html")
        
        try:
            user_emails = User.objects.filter(phone=number).values_list('email', flat=True) if number else []
            tests = Test.objects.filter(Q(email=email) | Q(email__in=user_emails))
            
            if tests.exists():
                return render(request, "index/status.html", {"test": tests})
            else:
                messages.info(request, "No test found with the provided email or contact number.")
                return render(request, "index/status.html")
        except Exception as e:
            messages.error(request, "An error occurred while searching for tests.")
            return render(request, "index/status.html")
    
    return render(request, "index/status.html")



def contact(request):
    return render(request, "index/contact.html")

def lists(request):
    return render(request, "index/lists.html", {"tests": tests})