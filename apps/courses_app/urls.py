from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('courses/new', views.newcourse),
    path('courses/areyousure/<int:idn>', views.areyousure),
    path('courses/destroy/<int:idn>', views.destroy),
    ]