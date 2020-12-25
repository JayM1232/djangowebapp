from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home_page'),path('/download_section/',views.secondpg,name='download_section'),path('/converter_section/',views.convert,name="converter_section"),path('/contactus/',views.contact,name="contactus")
]