from django.shortcuts import render
from django import forms
from django.shortcuts import get_object_or_404
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Users.models import Users
from Projects.form import ProjectForm
from django.http import HttpResponse,HttpResponseRedirect
from Projects.models import Projects,Tags,Pictures
from .models import Categories
from django.db.models import Q
from taggit.models import Tag



def project(request,Id):
	return HttpResponse(Id)

def search(request):
	l=[]
	value=request.GET['searchFor']
	titleSearch = Projects.objects.filter(Q(Title__icontains=value))
	tagSearch=Tags.objects.filter(Q(name__icontains=value ))
	for item in tagSearch:
		projects=item.project_tags_set.all()
		for p in projects:
			l.append(p.project)
	# Tags.objects.filter(Q(name__icontains='physics' ))[0].project_tags_set.all()[0].project.Title
	res=set(l+list(titleSearch))
	return render(request,"Users/SearchResult.html",{"result":res})

# def create_project(request):
# 	# obj=Tags.objects.get(name=tags)
# 	ImageFormSet = modelformset_factory( Pictures , form=ImageForm,extra=4)
# 	if request.method == 'POST':
# 		form=ProjectForm(request.POST)
# 		formset = ImageFormSet(request.POST,request.FILES)
# 		if form.is_valid() and formset.is_valid():
# 			project = form.save(commit = False)
# 			project.user = request.user
# 			project.save()
# 			for form in formset.cleaned_data:
# 				image = form['image']
# 				photo = Pictures(project = project,image = image)
# 				photo.save()
# 				form.save_m2m()
# 			messages.success(request,"project saved")
# 			return render(request, 'userProfile.html')
# 		else:
# 			print(form.errors,formset.errors)
# 	else:
# 		form = ProjectForm()
# 		formset = ImageFormSet(queryset=Pictures.objects.none())
# 	return render(request, 'add_project.html',
def create_project(request,id):
    ImageFormSet = modelformset_factory( Pictures , form=ProjectForm.ImageForm,extra=4)
    if request.method == 'POST':
        form=ProjectForm(request.POST or None)
        formset = ImageFormSet(request.POST,request.FILES,queryset = Pictures.objects.none())
        if form.is_valid() and formset.is_valid():
            project = form.save(commit = False)
            project.user = Users.objects.get(id=id)
            project.save()
            for f in formset.cleaned_data:
                image = f['name']
                photo = Pictures(project = project,image = image)
                photo.save()
            form.save_m2m()
            messages.success(request,"project saved")
            return HttpResponse("success")
        else:
            print(form.errors,formset.errors)
    else:
        form = ProjectForm()
        formset = ImageFormSet(queryset=Pictures.objects.none())
    return render(request, 'add_project.html',
                  {'projectForm':form,'formset':formset},
                  )

def show_project(request):
    # project = Projects.objects.all().filter(id=id)
    project = get_object_or_404(Projects, id = id)
    project_tags = project.project_tags_set.all()
    project_images=project.pictures_set.all()

    context = {
        "project" : project,
        "project_images":project_images,
        "project_tags":project_tags
    }
    return render(request,'project_show.html',context)

