from django.shortcuts import render , HttpResponse
from home.models import Contact
from django.contrib import messages


def index(request):
   
    return HttpResponse("This is home page")

def contactus(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        code = request.POST.get('code')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, code=code, phone=phone,desc=desc)
        contact.save()
        messages.success(request,"Thanks,we'll take a look at your query soon!")
    return render(request,'contactus.html')

def home(request):
    
    context = {
        'variable' : "gaurav sharma"
    }
    messages.success(request, 'Welcome get 10% off use your coupon code "PLEASE"')
    return render(request,'index.html',context)

def coffee(request):
    return render(request,'coffee.html')
    
    
def starter(request):
    return render(request,'starter.html')
# Create your views here.
