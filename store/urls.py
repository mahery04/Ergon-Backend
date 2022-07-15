from django.urls import path

from . import views

urlpatterns = [
    path('inventaire/', views.InventaireList.as_view()),
    path('inventaire/<int:id>', views.InventaireDetail.as_view()),
    path('entree_sortie/', views.Entree_SortieList.as_view()),
    path('entree_sortie/<int:id>', views.Entree_SortieDetail.as_view()),
    path('depot/', views.DepotList.as_view()),
    path('depot/<int:id>', views.DepotDetail.as_view()),
]
