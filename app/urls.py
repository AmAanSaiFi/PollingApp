from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name = 'index'),
    path('details/<int:pk>', views.details.as_view(), name = 'details'),
    path('vote/<int:pk>', views.vote, name = 'vote'),
    path('questionList/',views.questionList.as_view(),name='questionList')
]