from django import forms  

class SalarySlipForm(forms.Form):
	company_name = forms.CharField(max_length=255)
	month = forms.CharField(max_length=100)
	employee_id = forms.CharField(max_length=200)
	name = forms.CharField(max_length=255)
	designation = forms.CharField(max_length=200)
	department = forms.CharField(max_length=200)
	joining_date = forms.DateField()
	basic_salary = forms.FloatField()
	allowances = forms.FloatField()
	deduction = forms.FloatField()
	net_salary = forms.FloatField()
	amount_in_words = forms.CharField(max_length=500)
	prepared_by = forms.CharField(max_length=255)
	approved_by = forms.CharField(max_length=255)
