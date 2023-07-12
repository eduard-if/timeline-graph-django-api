from django.urls import path
from base.views import timeline_views as views

urlpatterns = [
    path('<str:orderBy>', views.getTimelines, name='timelines'),
    path('create/', views.createTimeline, name='timelines-create'),
    path('<str:pk>/update/', views.updateTimeline, name='timelines-update'),
    path('<str:pk>/delete/', views.deleteTimeline, name='timelines-delete'),
    path('<str:pk>/items/', views.getItems, name='timeline-items'),
    path('<str:pk>/items/create/', views.createItem,
         name='timeline-items-create'),
    path('<str:pk>/items/update/<str:id>',
         views.updateItem, name='timeline-items-update'),
    path('<str:pk>/items/delete/<str:id>',
         views.deleteItem, name='timeline-items-delete'),
]
