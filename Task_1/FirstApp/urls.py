from django.urls import path
from . import views


urlpatterns = [

    path('create/',views.CreateClient.as_view()),
    path('showClientProject/<int:pk>/',views.ClientAndProject.as_view())

]