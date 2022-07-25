from accounts import views
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView


urlpatterns = [
    path('', views.homebase, name='homebase'),
    path('adminclick', views.adminclick, name='adminclick'),
    path('doctorsignup', views.doctorsignup, name='doctorsignup'),
    path('patientsignup', views.patientsignup, name='patientsignup'),
    path('doctorlogin', LoginView.as_view(template_name='doctorlogin.html')),
    path('patientlogin', LoginView.as_view(template_name='patientlogin.html')),
    path('doctorclick', views.doctorclick, name='doctorclick'),
    path('patientclick', views.patientclick, name='patientclick'),
    path('afterlogin', views.afterlogin,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index.html'),name='logout'),
    path('patientdashboard', views.patientdashboard, name='patientdashboard'),
    path('doctordashboard', views.doctordashboard, name='doctordashboard'),
    path('admindashboard', views.admindashboard, name='admindashboard'),

]