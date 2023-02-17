from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="index"),
    path("ziga", views.ziga, name="ziga"),
    path("<str:name>", views.greet, name="greet"),
]
