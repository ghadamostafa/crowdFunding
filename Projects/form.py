from django.forms import ModelForm
from .models import Projects, Pictures, Categories
from django import forms

from taggit.managers import TaggableManager


class ProjectForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    Details = forms.Textarea()
    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    tags = forms.CharField(widget=forms.TextInput(attrs={
        'id':'tags'
    }))
    max_target = forms.DecimalField(max_value=1000000)
    start_date = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'date'
                                }))
    end_date = forms.DateField(widget=forms.DateInput(attrs=
                                {
                                    'class':'date'
                                }))
    cover = forms.ImageField()

    class Meta:
        model = Projects
        fields = [
            'title','Details','category','tags','max_target'
            ,'start_date','end_date','cover'
        ]

    class ImageForm(ModelForm):
        image = forms.ImageField(label='Image')

        class Meta:
            model = Pictures
            fields = ['image']



