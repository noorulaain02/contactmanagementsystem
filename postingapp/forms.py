from django import forms
from postingapp.models import Postal


class PostalForm(forms.ModelForm):
    class Meta:
        model = Postal
        fields = "__all__"

