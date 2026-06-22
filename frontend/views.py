from django.shortcuts import render,redirect
from loans.models import Loan
import requests

def home(request):
    return redirect('/login/')

def dashboard(request):

    total_loans = Loan.objects.count()

    approved = Loan.objects.filter(
        status="approved"
    ).count()

    rejected = Loan.objects.filter(
        status="rejected"
    ).count()

    pending = Loan.objects.filter(
        status="pending"
    ).count()

    context = {
        "total": total_loans,
        "approved": approved,
        "rejected": rejected,
        "pending": pending
    }

    return render(
        request,
        "dashboard.html",
        context
    )



def apply_loan(request):

    message = None

    if request.method == "POST":

        token = request.session.get("access")

        payload = {

            "loan_type":
            request.POST["loan_type"],

            "amount":
            request.POST["amount"],

            "tenure_years":
            request.POST["tenure_years"]

        }

        response = requests.post(

            "http://127.0.0.1:8000/api/loans/apply/",

            json=payload,

            headers={
                "Authorization":
                f"Bearer {token}"
            }

        )

        data = response.json()

        if "message" in data:

            message = data["message"]

    return render(
        request,
        "apply_loan.html",
        {
            "message": message
        }
    )

def my_loans(request):

    token = request.session.get("access")

    response = requests.get(

        "http://127.0.0.1:8000/api/loans/history/",

        headers={
            "Authorization":
            f"Bearer {token}"
        }

    )

    loans = response.json()

    return render(
        request,
        "my_loans.html",
        {
            "loans": loans
        }
    )

def recommendation(request):

    result = None

    if request.method == "POST":

        payload = {

            "credit_score":
            request.POST["credit_score"],

            "annual_income":
            request.POST["annual_income"],

            "loan_amount":
            request.POST["loan_amount"]

        }

        token = request.session.get("access")

        response = requests.post(

            "http://127.0.0.1:8000/api/loans/smart-recommendation/",

            json=payload,

            headers={
                "Authorization":
                f"Bearer {token}"
            }

        )

        result = response.json()

    return render(

        request,

        "recommendation.html",

        {"result": result}
    )

def chatbot_page(request):

    reply = None

    if request.method == "POST":

        token = request.session.get("access")

        payload = {

            "message":
            request.POST["message"]

        }

        response = requests.post(

            "http://127.0.0.1:8000/api/chatbot/chat/",

            json=payload,

            headers={
                "Authorization":
                f"Bearer {token}"
            }

        )

        data = response.json()

        reply = data.get("ai_reply")

    return render(

        request,

        "chatbot.html",

        {
            "reply": reply
        }
    )

def login_page(request):

    if request.method == "POST":

        response = requests.post(

            "http://127.0.0.1:8000/api/users/login/",

            json={

                "username":
                request.POST["username"],

                "password":
                request.POST["password"]

            }

        )

        data = response.json()

        if "access" in data:

            request.session["access"] = data["access"]

            request.session["refresh"] = data["refresh"]

            return redirect("/dashboard/")

    return render(
        request,
        "login.html"
    )

def register_page(request):

    message = None

    if request.method == "POST":

        response = requests.post(

            "http://127.0.0.1:8000/api/users/register/",

            json={

                "username":
                request.POST["username"],

                "email":
                request.POST["email"],

                "password":
                request.POST["password"]

            }

        )

        data = response.json()

        if response.status_code == 201:

            return redirect("/login/")

        else:

            message = data

    return render(
        request,
        "register.html",
        {
            "message": message
        }
    )