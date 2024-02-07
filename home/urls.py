from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.Home, name='home'),
    path('search/', views.Search, name='search'),
    path('searchs/', views.BigSearch, name='big-search'),

    path('etude_sol/', views.Etude_sol, name='etude_sol'),

    path('emploi/', views.EmploiList, name='emploi'),
    path('emploi/<str:slug>/', views.DetailEmploi, name='detail_emploi'),

    path('appel_d_offre/', views.Appel, name='appel'),
    path('immobilier/', views.Immobilier, name='immobilier'),
    path('entrepreneur/', views.EntrepreneurView, name='entrepreneur'),
    path('service/', views.ServiceView, name='service'),
    path('partenariat/', views.PartenariatView, name='partenariat'),
    path('commissionaire/add/', views.AddCommissionaireView, name='commissionaire'),
    path('achat/', views.AchatView, name='achat'),
    path('assistance_emploi/', views.assistance_emploi, name='assistance_emploi'),

    path('formations/', views.FormationList, name='formation'),
    path('formation/<str:slug>/', views.DetailFormation, name='detail_formation'),
    path('sujet/<str:slug>/', views.FormationBySubject, name='formation_par_sujet'),

    path('Followformation/<str:slug>/', views.FollowFormation, name='follow_formation'),
    path('Unfollowformation/<str:slug>/', views.UnfollowFormation, name='unfollow_formation'),

    path('contact/', views.Contact, name='contact'),
    path('about/', views.about, name='about'),
]
