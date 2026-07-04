from django.urls import path
from .views import CustomLoanChatbotView
urlpatterns=[
    path("",CustomLoanChatbotView.as_view()),
    
]