from django import forms
from .models import Projects, Rates, user_donations


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['Title', 'Details', 'id', 'target', 'end_date']


class DonationForm(forms.ModelForm):
    class Meta:
        model = user_donations
        fields = ['user', 'project', 'Amount']

    def clean_sku(self):
        if self.instance:
            return self.instance.sku
        else:
            return self.fields['sku']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ['rate', 'project', 'user']
