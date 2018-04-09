from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from df import views

urlpatterns = [
    # path('', views.df_result),
    path('<str:text>/', views.df_result),
]

urlpatterns = format_suffix_patterns(urlpatterns)
