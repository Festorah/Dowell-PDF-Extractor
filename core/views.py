import fitz
import spacy
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from pymongo.errors import DuplicateKeyError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")


def upload_page(request):
    return render(request, "core/index.html")


class PdfUploadView(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, "core/index.html")

    def post(self, request, *args, **kwargs):
        try:
            # Get the uploaded PDF file and email from request
            file = request.FILES.get("file")
            email = request.data.get("email")

            if not file:
                return JsonResponse({"error": "No file uploaded"}, status=400)

            if not email:
                return JsonResponse({"error": "Email is required"}, status=400)

            # Check if email already exists in MongoDB
            collection = settings.MONGO_COLLECTION
            if collection.find_one({"email": email}):
                return JsonResponse({"error": "Email already exists"}, status=400)

            # Read PDF file with PyMuPDF (fitz)
            pdf_document = fitz.open(stream=file.read(), filetype="pdf")
            text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                text += page.get_text()

            if not text:
                return JsonResponse({"error": "Empty PDF content"}, status=400)

            # Use SpaCy to process the extracted text
            doc = nlp(text)

            # Extract tokens and their POS tags
            pos_tags = [{"token": token.text, "pos": token.pos_} for token in doc]

            data = {"tile": file.name, "email": email, "post_tags": pos_tags}

            # Insert data into MongoDB (Handle duplicate email)
            collection = settings.MONGO_COLLECTION

            try:
                collection.insert_one(data)
            except DuplicateKeyError:
                return JsonResponse({"error": "Email already exists"}, status=400)

            return JsonResponse(
                {"message": "File processed successfully", "tags": pos_tags}
            )

        except Exception as e:
            # Handle any errors and return a JSON response
            return JsonResponse({"error": str(e)}, status=500)
