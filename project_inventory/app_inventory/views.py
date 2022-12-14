from django.shortcuts import render
from .forms import Itemcreateform, userregistrationform, userloginform
from datetime import datetime
from .models import item,appuser

# Create your views here.
def item_index(request):
    return render(request,"items/index.html") 
def item_edit(request):
    return render(request,"items/edit.html") 
def item_show(request):
    return render(request,"items/show.html") 

def item_create(request):
    form= Itemcreateform()
    context={"form": form}
    if request.method=="post":
        item=Item()
        user=appuser.objects.get(id=1)
        item.title= request.POST.get("title")
        item.particular=request.POST.get("particular")
        item.lf=request.POST.get("lf")
        item.price=request.POST.get("price")
        item.quantity=request.POST.get("quantity")
        item.total=request.POST.get("total")
        item.added_at=datetime.now()
        item.user=save
        item.save()

        # item=Item(title=title,)
    return render(request,"items/create.html",context) 

def user_login(request):
    form= userloginform()
    context={"form": form}
    return render(request,"items/login.html",context)
    
def user_registration(request):
    form= userregistrationform()
    context={"form": form}
    return render(request,"items/registration.html",context) 