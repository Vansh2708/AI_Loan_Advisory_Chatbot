from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class CustomLoanChatbotView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        message = request.data.get("message").lower()

        
        if "emi" in message:

            reply = (
                "EMI means Equated Monthly Installment. "
                "It is the fixed monthly payment made "
                "towards loan repayment."
            )

        
        elif "credit score" in message:

            reply = (
                "A credit score above 700 is considered good. "
                "Higher scores improve loan approval chances."
            )

        
        elif "home loan" in message:

            reply = (
                "Home loans usually require stable income, "
                "good credit history, and proper documents."
            )

        
        elif "personal loan" in message:

            reply = (
                "Personal loans are unsecured loans "
                "with flexible usage."
            )

        
        elif "car loan" in message:

            reply = (
                "Car loans help finance vehicle purchases "
                "with monthly EMI payments."
            )

        
        elif "education loan" in message:

            reply = (
                "Education loans support tuition fees "
                "and academic expenses."
            )


        elif "eligible" in message:

            reply = (
                "Loan eligibility depends on income, "
                "credit score, employment status, "
                "and repayment capacity."
            )

        
        elif "interest" in message:

            reply = (
                "Interest rates depend on loan type, "
                "credit score, and repayment duration."
            )

        
        elif "hello" in message or "hi" in message:

            reply = (
                "Hello! I am your AI Loan Advisory Assistant. "
                "How can I help you today?"
            )

        
        else:

            reply = (
                "Please ask loan-related questions such as "
                "EMI, credit score, home loan, "
                "interest rate, or eligibility."
            )

        return Response({
            "user_message": message,
            "ai_reply": reply
        })