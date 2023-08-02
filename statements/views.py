from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from .models import Statement

def statement(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        items=request.POST["address"]
        total=request.POST["total"]
        mode=request.POST["modepayment"]
        bill=Statement(name=name,email=email,phone=phone,address=address,total=total,items=items,modepayment=mode)
        bill.save()
        return render(request,'orderdone.html')
    elif request.method == "GET":
        return render(request,'payment.html')
    else:
        return HttpResponse ('Error !!')


# Create your views here.
