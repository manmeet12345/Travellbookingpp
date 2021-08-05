from django.urls import path
from . import views

urlpatterns = [
    path('moreinfo',views.info,name="moreinfo")
]