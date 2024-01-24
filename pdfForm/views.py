from django.shortcuts import render
from .forms import SalarySlipForm
from django.views import View
from django.http import HttpResponse
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePdf(View):
	form_class = SalarySlipForm
	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, 'form.html', {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			data = {
			"company_name":request.POST['company_name'],
			"month":request.POST['month'],
			"employee_id":request.POST['employee_id'],
			"name":request.POST['name'],
			"designation":request.POST['designation'],
			"department":request.POST['department'],
			"joining_date":request.POST['joining_date'],
			"basic_salary":request.POST['basic_salary'],
			"allowances":request.POST['allowances'],
			"deduction":request.POST['deduction'],
			"net_salary":request.POST['net_salary'],
			"amount_in_words":request.POST['amount_in_words'],
			"prepared_by":request.POST['prepared_by'],
			"approved_by":request.POST['approved_by']
			}
			pdf = render_to_pdf('saved_form.html', data)
			return HttpResponse(pdf, content_type='application/pdf')
		else:
			HttpResponse("Error occured.")
		
		

