from django.urls import path 
from courses.views import (
    dashboard,
    training,
    question,
    result,
)

urlpatterns = [
    path('',dashboard),
    path('training/',training),
    path('question/',question),
    path('result/',result),
]
