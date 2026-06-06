from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dotenv import load_dotenv
import google.generativeai as genai 
import os
load_dotenv()
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)
model=genai.GenerativeModel("gemini-3.5-flash")
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
            prompt = f"""
            You are an AI Loan Advisory Assistant.
            Answer in plain text.
            Do not use markdown.
            Do not use headings.
            Do not use ** symbols.
            Do not use bullet points.

            Answer questions about:
            - Loans
            - EMI
            - Banking
            - Finance
            - Credit Score
            - Investments

            User Question:
            {message}
            """
            
            try:
                
                response = model.generate_content(prompt)

                reply = response.text
            except Exception as e:
                
                reply = f"Gemini Error: {str(e)}"

        return Response({
            "user_message": message,
            "ai_reply": reply
        })