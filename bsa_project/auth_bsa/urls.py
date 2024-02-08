from django.urls import path
from . import views
from .views import DomainListCreateAPIView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('domains/', DomainListCreateAPIView.as_view(), name='domain-list-create'),
    path('domains/<int:pk>/', DomainRetrieveUpdateDestroyAPIView.as_view(), name='domain-retrieve-update-destroy'),
]