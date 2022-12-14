from django.shortcuts import render,redirect
from .forms import Itemcreateform, userregistrationform, userloginform
from datetime import datetime
from .models import items,appuser

# Create your views here.
def item_index(request):
    item_list=items.objects.all()
    context={"item_list": item_list}
    return render(request,"items/index.html",context) 
def item_edit(request,id):
    return render(request,"items/edit.html") 
def item_show(request,id):
    data= items.objects.get(id=id)
    context={"data":data}
    return render(request,"items/show.html",context)
def item_delete(request,id):
    data= items.objects.get(id=id)
    data.delete()
    return redirect("items.index") 
def item_update(request):
     if request.method == "POST":
        item_obj=items.objects.get(id=request.POST.get("id"))
        user=appuser.objects.get(id=1)
        item_obj.title= request.POST.get("title")
        item_obj.particulars=request.POST.get("particulars")
        item_obj.lf=request.POST.get("lf")
        item_obj.price=request.POST.get("price")
        item_obj.quantity=request.POST.get("quantity")
        item_obj.total=request.POST.get("total")
        item_obj.added_at=datetime.now()
        item_obj.user=user
        item_obj.save()
    
    return redirect("items.index")

def item_create(request):
    form= Itemcreateform()
    context={"form": form}
    if request.method == "POST":
        item_obj=items()
        user=appuser.objects.get(id=1)
        item_obj.title= request.POST.get("title")
        item_obj.particulars=request.POST.get("particulars")
        item_obj.lf=request.POST.get("lf")
        item_obj.price=request.POST.get("price")
        item_obj.quantity=request.POST.get("quantity")
        item_obj.total=request.POST.get("total")
        item_obj.added_at=datetime.now()
        item_obj.user=user
        item_obj.save()

        # OR - item_obj=Item(title=title,particular=particular)
    return render(request,"items/create.html",context) 



def user_login(request):
    form= userloginform()
    context={"form": form}
    return render(request,"users/login.html",context)
    
def user_registration(request):
    form= userregistrationform()
    context={"form": form}
    if request.method=="POST":
        user=appuser()
        user.full_name=request.POST["full_name"]
        user.email=request.POST["email"]
        user.contact=request.POST["contact"]
        user.password=request.POST["password"]
        user.save()

    return render(request,"users/register.html",context) 