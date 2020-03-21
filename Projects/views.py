from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Projects.models import Pictures,Projects
from Projects.form import ProjectForm
from .models import Categories
from taggit.models import Tag
from django import forms


#hyssien123
#123

def create_project(request):
    ImageFormSet = modelformset_factory( Pictures , form=ProjectForm.ImageForm,extra=4)
    if request.method == 'POST':
        form=ProjectForm(request.POST)
        formset = ImageFormSet(request.POST,request.FILES,queryset = Pictures.objects.none())
        if form.is_valid() and formset.is_valid():
            project = form.save(commit = False)
            project.user = request.user
            project.save()
            for form in formset.cleaned_data:
                image = form['image']
                photo = Pictures(project = project,image = image)
                photo.save()
                form.save_m2m()
            messages.success(request,"project saved")
            return render(request, 'userProfile.html')
        else:
            print(form.errors,formset.errors)
    else:
        form = ProjectForm()
        formset = ImageFormSet(queryset=Pictures.objects.none())
    return render(request, 'add_project.html',
                  {'projectForm':form,'formset':formset},
                  )

def show_project(request,id):
    # project = Projects.objects.all().filter(id=id)
    project = get_object_or_404(Projects, id = id)
    project_tags = project.tags_set.all()
    project_images=project.image_set.all()

    context = {
        "project" : project,
        "project_images":project_images,
        "project_tags":project_tags
    }
    return render(request,'project_show.html',context)

