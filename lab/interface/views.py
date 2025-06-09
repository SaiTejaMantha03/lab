from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseRedirect
from . models import User,Test
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
        email = request.POST["email"]
        phonenumber = request.POST["phonenumber"]
        address = request.POST["address"]
        name = request.POST["name"]
        test = request.POST["test"]
        print(email, phonenumber, address, name, test)
        user = User(name=name, email=email, address=address, phone=phonenumber)
        test_model = Test(name=name, email=email, test=test, test_status=False)
        user.save()
        test_model.save()
        return HttpResponseRedirect("/status")
    return render(request, "index/create.html",{"tests": tests})

def status(request):
    # if request.method == "POST":
    #     email = request.POST.get("email")
    #     number = request.POST.get("contact")
    #     tests = Test.objects.filter(Q(email=email) | Q(email__in=User.objects.filter(phone=number).values_list('email', flat=True)))
    #     if tests.exists():
    #         return render(request, "index/status.html", {"test": tests})
    #     else:
    #         return render(request, "index/status.html", {"error": "No test found with the provided email or contact number."})
    # return render(request, "index/status.html")
    #def status(request):
    if request.method == "POST":
        email = request.POST.get("email")
        number = request.POST.get("contact")
        print("Email:", email)
        print("Contact:", number)
        user_emails = User.objects.filter(phone=number).values_list('email', flat=True)
        print("User emails for contact:", list(user_emails))
        tests = Test.objects.filter(Q(email=email) | Q(email__in=user_emails))
        print("Tests found:", tests)
        if tests.exists():
            return render(request, "index/status.html", {"test": tests})
        else:
            return render(request, "index/status.html", {"error": "No test found with the provided email or contact number."})
    return render(request, "index/status.html")



def contact(request):
    return render(request, "index/contact.html")

def lists(request):

    return render(request, "index/lists.html", {"tests": tests}, )