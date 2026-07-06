from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    
    path('dashboard/', dashboard, name='dashboard'),

    path('apply-loan/', apply_loan, name='apply_loan'),

    path('my-loans/', my_loans, name='my_loans'),

    path('recommendation/', recommendation, name='recommendation'),

    path('chatbot/', chatbot_page, name='chatbot'),
    
    path('login/', login_page, name='login'),

path('register/', register_page, name='register'),
path("profile/", profile, name="profile"),
path("logout/", logout_page, name="logout"),
] 