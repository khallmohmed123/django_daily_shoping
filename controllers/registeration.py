import time
from django.shortcuts import render_to_response ,redirect
from users.models import User
from django.conf import settings
import os

def register(request):
    title="registrations"
    return render_to_response("register/registeration.html", locals())
def mkuser(request):
    g=request.POST.get("gender")
    name=request.POST.get("name")
    email=request.POST.get("email")
    pass_wb=request.POST.get("password")
    image=request.FILES.get("image")
    image_name=str(time.time())+"_"+image.name
    image_sub='uploaded/'+str(image_name)
    image_path = os.path.join(settings.BASE_DIR,"public",str(image_sub))
    with open(image_path,"wb+") as destination:
        for chunk in image:
            destination.write(chunk)
    user=User(name=name,email=email,password=pass_wb,image=image_sub)
    user.save()
    request.session["email"] = email
    request.session["name"] = name
    request.session["image"] = image_sub
    response = redirect('/')
    return response
def logout(request):
    del request.session["user"]
    response = redirect('/')
    return response
def login(request):
    title="registrations"
    return render_to_response("register/login.html", locals())
def do_login(request):
    email=request.POST.get("email")
    pass_wb=request.POST.get("password")
    user_obj=User.objects.filter(email=email,password=pass_wb)
    if user_obj.count() > 0:
        request.session["user"]={"name":user_obj[0].name ,"email":user_obj[0].email,"image":user_obj[0].image}
    else:
        print("error")
    response = redirect('/')
    return response