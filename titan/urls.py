from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('commande_titan/', views.Commande_TitanList.as_view()),
    path('commande_titan/<int:id>', views.Commande_TitanDetail.as_view()),
    path('bl_titan/', views.Bon_Livraison_TitanList.as_view()),
    path('bl_titan/<int:id>', views.Bon_Livraison_TitanDetail.as_view()),
]
