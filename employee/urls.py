from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('personnel/', views.PersonnelList.as_view()),
    path('personnel/<int:id>', views.PersonnelDetail.as_view()),
    path('congee/', views.CongeelList.as_view()),
    path('congee/<int:id>', views.CongeeDetail.as_view()),
    path('historique/', views.HistoriqueList.as_view()),
    path('historique/<int:id>', views.HistoriqueDetail.as_view()),
    path('salaire/', views.SalaireList.as_view()),
    path('salaire/<int:id>', views.SalaireDetail.as_view()),
]
