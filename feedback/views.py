from django.shortcuts import render, HttpResponse
from .models import Feedback

def feedback(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        sub=request.POST["subject"]
        msg=request.POST["message"]
        obj=Feedback(name=name,email=email,subject=sub,message=msg)
        obj.save()
        return render(request,'feedback.html')
    elif request.method=="GET":
        return render(request,'contact.html')
    else:
        return HttpResponse('Error')

    if request.method=="POST":
        name=request.POST.get("name")
        email = request.POST.get("email")
        sub = request.POST.get("subject")
        msg = request.POST.get("message")

        print(name,email,sub,msg)
    return render(request,'feedback.html')










"""if obj.is_valid():
           obj.save()
        return HttpResponse('Your Feedback is submitted !!')"""


# Create your views here.
from django.shortcuts import render

# Create your views here.
