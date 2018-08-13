from django import forms
from .models import Personal, Stats
import datetime
from .choices import waiting_years

class PersonalForm(forms.Form):
	full_name = forms.CharField()
	date_of_birth = forms.CharField()
	address = forms.CharField(widget=forms.Textarea)
	temp_address = forms.BooleanField(required=False)
	telephone = forms.CharField()
	num_in_household = forms.IntegerField()
	num_children = forms.IntegerField()
	waiting_list_time = forms.ChoiceField(choices=waiting_years)
    
    # class Meta:
    #     fields = [
    #             'full_name', 
    #             'date_of_birth', 
    #             'address', 
    #             'temp_address',
    #             'telephone',
    #             'num_in_household',
    #             'num_children',
    #             'waiting_list_time',
    #     ]
        

class StatsForm_postcode(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['postcode']
        
class StatsForm_theme(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['theme']

class ComplaintsForm(forms.Form):
    # create fields, view
    description = CharField(widget=forms.Textarea)
    action = CharField(widget=forms.Textarea)
    response = CharField(widget=forms.Textarea)
    remedy = CharField(widget=forms.Textarea)