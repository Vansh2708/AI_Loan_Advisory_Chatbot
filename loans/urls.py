from django.urls import path
from .views import (ApplyloanView,
                    LoanHistoryView,
                    EMICalculatorView,
                    UpdateLoanStatusView,
                    LoanDetailView,
                    LoanEligibilityPredictionView,
                    SmartLoanRecommendationView
)
urlpatterns=[
    path('apply/',ApplyloanView.as_view()),
    path('history/',LoanHistoryView.as_view()),
    path('emi/',EMICalculatorView.as_view()),
    path('update-status/<int:loan_id>/',UpdateLoanStatusView.as_view()),
    path('detail/<int:loan_id>/',LoanDetailView.as_view()),
    path('predict/',LoanEligibilityPredictionView.as_view()),
    path('smart-recommendation/',SmartLoanRecommendationView.as_view()),
    ]