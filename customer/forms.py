from .models import issue
from django import forms
from courier.models import company

class IssueForm(forms.ModelForm):
	class Meta:
		model = issue
		fields = ('order_id', 'title','content','user_id')






class  OrderForm(forms.Form):

	#track_id = forms.CharField(max_length=20,label='track id')
	receiver = forms.CharField(max_length=20)
	receiver_address = forms.CharField(max_length=50,label='receiver address')
	r_postcode = forms.CharField(max_length=20, label='receiver postcode')
	receiver_phone = forms.CharField(max_length=20, label='receiver phone')

	sender = forms.CharField(max_length=20)
	sender_address = forms.CharField(max_length=50,label='sender address')
	s_postcode = forms.CharField(max_length=20, label='sender postcode')
	sender_phone = forms.CharField(max_length=20, label='sender phone')
	#price = forms.CharField(max_length=20, type='hidden')
	# sender = models.ForeignKey(user, to_field='user_id', on_delete=models.CASCADE)
	weight = forms.CharField(max_length=20, label='weight(KG)')
	#status = forms.CharField(max_length=20)
	company_id = forms.ChoiceField(label='Company', choices=((x.company_id, x.name+'  '+x.price+'$/KG') for x in company.objects.all()))
	#company_id = forms.ChoiceField()
	#choices=[('aupost','AU Post'),('dhl','DHL')]
	#delivery_staff = forms.CharField(max_length=20)


