from django.conf.urls import url

from .views import PersonAPI

urlpatterns = [

    url(r'person/', PersonAPI.as_view())

]