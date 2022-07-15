from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('societe/', views.SocieteList.as_view()),
    path('societe/<int:id>', views.SocieteDetail.as_view()),
    path('particulier/', views.ParticulierList.as_view()),
    path('particulier/<int:id>', views.ParticulierDetail.as_view()),
    path('guest/', views.GuestList.as_view()),
    path('guest/<int:id>', views.GuestDetail.as_view()),
    path('rdv/', views.RdvList.as_view()),
    path('rdv/<int:id>', views.RdvDetail.as_view()),
]
