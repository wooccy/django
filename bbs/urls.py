from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from bbs import views

urlpatterns = [
    path('', views.bbs_list),
    path('<int:pk>/', views.bbs_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
