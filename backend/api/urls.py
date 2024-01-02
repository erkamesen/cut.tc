from django.urls import path
from . import views

urlpatterns = [
    path('code/', views.CodeListCreateView.as_view(), name="codes"),
    path('code/<int:pk>/', views.BCodeRetrieveUpdateDestroyView.as_view(), name="code"),
    path('redirect-url/', views.RedirectURLListCreateView.as_view(), name="redirect-urls"),
    path('redirect-url/<int:pk>/', views.RedirectURLRetrieveUpdateDestroyView.as_view(), name="redirect-url"),
]