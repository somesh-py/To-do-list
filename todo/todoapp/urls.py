from django.urls import path
from . import views


urlpatterns = [
    path('',views.index.as_view(),name='index'),
    path('<pk>/update',views.update.as_view(),name='update'),
    path('<pk>/delete',views.delete.as_view(),name='delete'),

]
