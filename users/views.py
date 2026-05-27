from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .serializers import RegisterSerializer

class RegisterView(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message":"User regsitered successfully"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors)
class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user=request.user
        data={
            "username":user.username,
            "email":user.email,
            "phone":user.phone,
            "credit_score":user.credit_score,
            "annual_income":user.annual_income
        }
        return Response(data)
