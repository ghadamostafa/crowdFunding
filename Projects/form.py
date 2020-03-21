from django.forms import ModelForm
from .models import Projects, Pictures,Categories
from django import forms
from taggit.managers import TaggableManager
from django.forms import formset_factory

# categories_list=[]
# res=Categories.objects.all()
# i=0
# for item in res:
#     i+=1
#     categories_list.append((i,item.name))
# categories=tuple(categories_list)


class ProjectForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class':'form-control'
    }))
    Details = forms.Textarea()
    category = forms.ModelChoiceField(queryset=Categories.objects.all())
    tags = TaggableManager()
    max_target = forms.DecimalField(max_value=1000000)
    start_date = forms.DateField(widget=forms.DateInput)
    end_date = forms.DateField(widget=forms.DateInput)
    # cover = forms.ImageField()

    class Meta:
        model = Projects
        fields = [
            'title','Details','category','tags','max_target'
            ,'start_date','end_date','cover'
        ]

# class ImageForm(ModelForm):

#     class Meta:
#         model=Pictures
#         fields = ['image']