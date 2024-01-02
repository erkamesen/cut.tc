from django.urls import path
from . import views

urlpatterns = [
    path('base-url/', views.BaseURLListCreateView.as_view(), name="base-urls"),
    path('base-url/<int:pk>/', views.BaseURLRetrieveUpdateDestroyView.as_view(), name="base-url"),
    path('redirect-url/', views.BaseURLListCreateView.as_view(), name="redirect-urls"),
    path('redirect-url/<int:pk>/', views.BaseURLRetrieveUpdateDestroyView.as_view(), name="redirect-url"),
]