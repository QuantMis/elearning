from django.urls import path 
from courses.views import (
    dashboard,
    training,
    question,
    result,
    discussion,
    selection,
    exam_selection,
    exam_question,
)

urlpatterns = [
    path('',dashboard),
    path('training/',training),
    path('question/',question),
    path('result/',result),
    path('discussion/',discussion),
    path('selection/',selection),
    path('selection/exam/',exam_selection),
    path('question/exam/',exam_question),
]
