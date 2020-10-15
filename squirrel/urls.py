from django.urls import path

from . import views


# Allow for namespaces in reverse URLs
app_name = 'squirrel'

urlpatterns = [
    path('', views.index, name='index'),
    path('map/', views.map, name='map'),
    path('sightings/', views.sightings, name='sightings'),
    path('sightings/<int:unique_squirrel_id>/', views.squirrel_details, name='details'),
    path('sightings/add', views.add, name='add'),
    path('sightings/stats', views.stats, name='stats'),
]
