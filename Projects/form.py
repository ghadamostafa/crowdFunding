from django.forms import ModelForm
from .models import Projects, Pictures,Categories
from django import forms
from taggit.managers import TaggableManager


class ProjectForm(ModelForm):
    Title = forms.CharField(widget=forms.TextInput())
    Details = forms.Textarea()
    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    # cover = forms.ImageField()
    tags = forms.CharField(widget=forms.TextInput(attrs={
        'id':'tags'
    }))
    target = forms.DecimalField(max_value=1000000)
    start_date = forms.DateField(required=False,widget=forms.DateInput(attrs=
                                {
                                    'class':'date'
                                }))
    end_date = forms.DateField(required=False,widget=forms.DateInput(attrs=
                                {
                                    'class':'date'
                                }))

    class Meta:
        model = Projects
        fields = [
            'Title','Details','category','tags','target'
            ,'start_date','end_date'
        ]
class ImageForm(ModelForm):
        image = forms.ImageField(required=False,label='Image')
        class Meta:
            model = Pictures
            fields = ['image']
