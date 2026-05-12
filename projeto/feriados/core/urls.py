from django.urls import path
from . import views
from django.urls import path
from .views import FeriadoListCreateView, FeriadoDetailView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.feriados),
    path('json_simprao', views.json_simprao),
    path('api/feriados/', FeriadoListCreateView.as_view(), name='api_feriados_list_create'),
    path('api/feriados/<int:pk>/', FeriadoDetailView.as_view(), name='api_feriados_detail'),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]