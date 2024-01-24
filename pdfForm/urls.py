from django.urls import path
from pdfForm import views

app_name = 'pdfForm'

urlpatterns = [
	path('generate_pdf/', views.GeneratePdf.as_view(), name='generate_pdf'),
]