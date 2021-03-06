from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('offre_hahitantsoa/', views.Offre_HahitantsoaList.as_view()),
    path('offre_hahitantsoa/<int:id>', views.Offre_HahitantsoaDetail.as_view()),
    path('paiemement_hahitantsoa/', views.Paiement_HahitantsoaList.as_view()),
    path('paiemement_hahitantsoa/<int:id>',
         views.Paiement_HahitantsoaDetail.as_view()),
    path('commande_hahitantsoa/', views.Choix_Sol_HahitantsoaList.as_view()),
    path('commande_hahitantsoa/<int:id>',
         views.Choix_Sol_HahitantsoaDetail.as_view()),
    path('package_hahitantsoa/', views.Package_HahitantsoaList.as_view()),
    path('package_hahitantsoa/<int:id>',
         views.Package_HahitantsoaDetail.as_view()),
    path('choix_sol_hahitantsoa/', views.Choix_Sol_HahitantsoaList.as_view()),
    path('choix_sol_hahitantsoa/<int:id>',
         views.Choix_Sol_HahitantsoaDetail.as_view()),
    path('draperie_hahitantsoa/', views.Draperie_HahitantsoaList.as_view()),
    path('draperie_hahitantsoa/<int:id>',
         views.Draperie_HahitantsoaDetail.as_view()),
    path('decoration_hahitantsoa/', views.Decoration_HahitantsoaList.as_view()),
    path('decoration_hahitantsoa/<int:id>',
         views.Decoration_HahitantsoaDetail.as_view()),
    path('effet_hahitantsoa/', views.Effet_Sepciaux_HahitantsoaList.as_view()),
    path('effet_hahitantsoa/<int:id>',
         views.Effet_Sepciaux_HahitantsoaDetail.as_view()),
    path('lumiere_hahitantsoa/', views.Lumieres_HahitantsoaList.as_view()),
    path('lumiere_hahitantsoa/<int:id>',
         views.Lumieres_HahitantsoaDetail.as_view()),
    path('type_fete_hahitantsoa/', views.Type_Fete_HahitantsoaList.as_view()),
    path('type_fete_hahitantsoa/<int:id>',
         views.Type_Fete_HahitantsoaDetail.as_view()),
    path('bl_hahitantsoa/', views.Bon_Livraison_HahitantsoaList.as_view()),
    path('bl_hahitantsoa/<int:id>',
         views.Bon_Livraison_HahitantsoaDetail.as_view()),
]
