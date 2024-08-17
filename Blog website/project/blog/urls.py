
from django.urls import path
from .views import ListBlog,DetailBlog
urlpatterns = [
 
    path('',ListBlog,name="list"),
    path('bolg/<id>',DetailBlog,name="detail")
]