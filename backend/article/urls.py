from django.urls import path
from .views import ArticleView, OneAuthorView

app_name = "Students"

urlpatterns = [
    path('Group/', ArticleView.as_view()),
    path('Student/<int:pk>', OneAuthorView.as_view()),
]
