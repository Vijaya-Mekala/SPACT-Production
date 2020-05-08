from django.urls import path
from . import views

urlpatterns =[
    path('',views.NewRequest, name='NewRequest'),
    path('SubmitToResult',views.SubmitToResult, name='SubmitToResult')
]