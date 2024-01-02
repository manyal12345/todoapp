from django.contrib import admin
from django.urls import path
from base.views import delete_all, home,create,edit,delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",home, name='home'),
    path("create/",create,name='create'),
    path("edit/<int:pk>/",edit,name='edit'),
    path("delete/<int:pk>/",delete,name='delete'),
    path("delete_all/",delete_all,name='delete_all'),
]


