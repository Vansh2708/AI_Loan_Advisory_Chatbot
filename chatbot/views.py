from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rag.rag_pipeline import ask_rag


class CustomLoanChatbotView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        message = request.data.get("message", "").strip()

        if not message:
            return Response({
                "error": "Message is required."
            }, status=400)

        reply = ""
        sources = []

        try:

            lower_message = message.lower()

            # Greeting only
            if lower_message in [
                "hi",
                "hello",
                "hey",
                "good morning",
                "good afternoon",
                "good evening"
            ]:

                reply = (
                    "Hello! I am your AI Loan Advisory Assistant. "
                    "Ask me anything about loans, eligibility, EMI, "
                    "interest rates, RBI guidelines, or loan documents."
                )

            else:

                rag_response = ask_rag(message)

                reply = rag_response["answer"]

                sources = rag_response["sources"]

        except Exception as e:

            return Response({
                "error": str(e)
            }, status=500)

        return Response({

            "user_message": message,

            "ai_reply": reply,

            "sources": sources

        })