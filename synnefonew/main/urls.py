from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name='index'),
    path('student/',views.student,name='student'),
    
    
]