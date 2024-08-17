from django.shortcuts import get_object_or_404, render
from .models import Myblog
# Create your views here.
def ListBlog(request):
    obj=Myblog.objects.all()
    return render(request,"list.html",{"list":obj})

def DetailBlog(request,id):
    obj=get_object_or_404(Myblog,id=id)
    return render(request,"detail.html",{"detail":obj})