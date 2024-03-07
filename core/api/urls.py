from home.views import index,person,PersonAPI
from django.urls import path

urlpatterns=[
    path('index/',index),
    path('person/',person),
    path('persons/',PersonAPI.as_view())
]