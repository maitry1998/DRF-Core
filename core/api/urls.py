from home.views import index,person,PersonAPI,PeopleViewset
from django.urls import path,include

# from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people', PeopleViewset, basename='people')
urlpatterns = router.urls

urlpatterns=[
    path('index/',index),
    path('person/',person),
    path('persons/',PersonAPI.as_view()),
    path("",include(router.urls))

]