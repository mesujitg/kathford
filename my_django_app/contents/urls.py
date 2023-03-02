from django.urls import path
from contents import views

urlpatterns = [
    path('intro', views.show_about),
    path('contacts', views.show_contacts),
    path('policies', views.show_policies),
]
