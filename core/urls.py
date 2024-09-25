from django.urls import path

from .views import PdfUploadView, upload_page

urlpatterns = [
    path("", upload_page, name="upload-page"),
    path("upload/", PdfUploadView.as_view(), name="pdf-upload"),
]
