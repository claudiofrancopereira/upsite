from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'albums'

urlpatterns = [  
   path( '', views.albums_list, name = 'list' ),
   path( 'create/', views.albums_create, name = 'create' ),
   path( '<slug:slug>/', views.albums_detail, name = 'detail' )
  
]
