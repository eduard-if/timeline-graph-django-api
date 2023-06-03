from django.urls import path
from base.views import timeline_views as views

urlpatterns = [
    path('', views.getTimelines, name='timelines')
]
