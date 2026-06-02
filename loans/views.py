from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Loan
import math
from .serializers import LoanSerializer
import joblib
import os
Model_path=os.path.join('ml_models','loan_model.pkl')
model=joblib.load(Model_path)

#Apply Loan View
class ApplyloanView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message":"Loan Application Submitted.",
                "data":serializer.data
            })
        return Response(serializer.errors)
#Loan History View
class LoanHistoryView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        loans=Loan.objects.filter(user=request.user)
        serializer=LoanSerializer(loans,many=True)
        return Response(serializer.data)
#EMI Calculator View
class EMICalculatorView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        principal=float(request.data.get('amount'))
        annual_rate=float(request.data.get('interest_rate'))
        years=int(request.data.get('tenure_years'))
        monthly_rate=annual_rate/(12*100)
        months=years*12
        emi=(
            principal
            *monthly_rate
            *math.pow(1+monthly_rate,months)
        )/(
            math.pow(1+monthly_rate,months)-1
        )
            
        total_payment=emi*months
        total_interest=total_payment-principal
        return Response({
            "loan_amount":principal,
            "monthly_emi":round(emi,2),
            "total_payment":round(total_payment,2),
            "total_interest":round(total_interest,2)
        })
#Update Loan Status View
class UpdateLoanStatusView(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self,request,loan_id):
        try:
            loan=Loan.objects.get(id=loan_id)
        except Loan.DoesNotExist:
            return Response({
                "error":"Loan not Found"
            })
        new_status=request.data.get('status')
        if new_status not in ['approved','rejected']:
            return Response({
                "error":"Invalid Status"
            })
        loan.status=new_status
        loan.save()
        return Response({
            "message":f"loan {new_status} successfully."
        })
#Loan Detail View 
class LoanDetailView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,loan_id):
        try:
            loan=Loan.objects.get(
                id=loan_id,
                user=request.user
            )
        except Loan.DoesNotExist:
            return Response({
                "error":"Loan not found"
            })
        serializer=LoanSerializer(loan)
        return Response(serializer.data)
#Loan Eligiblity Prediction View
class LoanEligibilityPredictionView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        credit_score=int(request.data.get('credit_score'))
        annual_income=float(request.data.get('annual_income'))
        loan_amount=float(request.data.get('loan_amount'))
        prediction=model.predict([[credit_score,annual_income,loan_amount]])[0]
        result="Approved" if prediction==1 else "Rejected"
        return Response({
            "prediction":result
        })
#Smart Recommendation View
class SmartLoanRecommendationView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        credit_score=int(request.data.get('credit_score'))
        annual_income=float(request.data.get('annual_income'))
        loan_amount=float(request.data.get('loan_amount'))
        prediction=model.predict([[
            credit_score,annual_income,loan_amount
        ]])[0]
        approval_status=(
            "Approved"
            if prediction==1
            else "Rejected"
            
        )
        if credit_score>=750:
            risk_score="Low"
        elif credit_score>=650:
            risk_score="Medium"
        else:
            risk_score="High"
        if annual_income>=1000000:
            recommend_loan="Home Loan"
        elif annual_income>=700000:
            recommend_loan="Car Loan"
        elif annual_income>=400000:
            recommend_loan="Education Loan"
        else:
            recommend_loan="Personal Loan"
        if credit_score>=750:
            suggested_interest="8.5%"
        elif credit_score>=650:
            suggested_interest="10.5%"
        else:
            suggested_interest="14%"
        return Response({
            "prediction":approval_status,
            "risk_score":risk_score,
            "recommend_loan":recommend_loan,
            "suggested_interest_rate":suggested_interest
        })
        
            
                    