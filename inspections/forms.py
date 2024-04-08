# inspections/forms.py
from django import forms
from .models import Inspection

class InspectionForm(forms.ModelForm):
    class Meta:
        model = Inspection
        fields = ['vessel', 'inspection_template', 'date', 'inspector_name']
        # Assuming these are the only fields you want to manually set
