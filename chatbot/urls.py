from django.urls import path
from .views import CustomLoanChatbotView
urlpatterns=[
    path('chat/',CustomLoanChatbotView.as_view()),
    
]