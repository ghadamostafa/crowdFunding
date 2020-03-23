from django.shortcuts import render
from django.shortcuts import get_object_or_404
# connect  view with form
from .forms import ProjectForm, DonationForm, RatingForm
from .form import ImageForm,ProjectCreationForm
import json
from django.db.models import Sum
from django.db import IntegrityError
from django import forms
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Users.models import Users
from django.http import HttpResponse, HttpResponseRedirect
from Projects.models import Projects, Tags, Pictures, Rates, user_donations,project_tags
from .models import Categories
from django.db.models import Q
from taggit.models import Tag


def project_details(request, id):
    request.session['user_id'] = 3  # static ,change it to dynamic when merge
    print("****")
    request.session['project_id'] = id
    project_details = Projects.objects.get(id=id)
    pictures = Pictures.objects.filter(project=id)
    for i in pictures:
        print(i.image)

    context = {
        "project_details": project_details,
        "project_picture": pictures,
        "user_id": request.session['user_id'],

    }
    return render(request, "project_details.html", context)


def edit_project(request, id):
    project = get_object_or_404(Projects, id=id)
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            new_form = form.save(commit=False)
            print(project.user)
            new_form.user = project.user
            new_form.save()
    else:
        form = ProjectForm(instance=project)
        print("else")

    context = {
        "form": form,
    }
    return render(request, "project_edit.html", context)


def donate(request, id):
    project = get_object_or_404(Projects, id=id)
    user = get_object_or_404(Users, id=1)  # edit to id = id from session (login user)
    donation_before = user_donations.objects.filter(user=1, project=id)
    if not donation_before:
        print("new one")
        if request.method == 'POST':
            form = DonationForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = user
                new_form.save()
        else:
            form = DonationForm(initial={'project': project, 'user': user})
        context = {
            "form": form,
        }
        return render(request, "donation.html", context)
    else:
        old_amount = donation_before[0].Amount
        if request.method == 'POST':
            form = DonationForm(request.POST)
            n = int(request.POST['Amount']) + int(old_amount)
            user_donations.objects.filter(user=request.POST['user'], project=request.POST['project']).update(Amount=n)
        else:
            form = DonationForm(initial={'project': project, 'user': user})
        context = {
            "form": form,
        }
        return render(request, "donation.html", context)


def save(request):
    print("this sa ve rate method")
    #uid = request.session['user_id']  # uid referes to the session user_id
    #pid = request.session.get('project_id')
    p = Projects.objects.get(id=2)
    x = Projects.objects.get(id=2)
    ratedindex = request.POST.get('ratedIndex')
    print(ratedindex)
    uID = request.POST.get('user_id')  # uID refers to the local storage user_id
    ratedindex += 1
    if uID != 0:
        u = Rates(rate=ratedindex)
        u.user = x
        u.project = p
        u.save()
    else:
        Rates.objects.filter(user=uID).update(rate=ratedindex)
    return HttpResponse(json.dumps({'uid': 2}), content_type="application/json")
    num_of_rates = Rates.objects.get(id).count()

    # total = Rates.objects.filter(id=uID).aggregate(Sum('rate'))
    # avg = total / num_of_rates
    # print(avg)
    # context = {
    #     'avg': avg,
    # }
    # return render(request, "project_details.html", context)


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
	return render(request, "Users/SearchResult.html",{"result":res})

def create_project(request,id):
    ImageFormSet = modelformset_factory( Pictures , form=ImageForm,extra=4)
    if request.method == 'POST':
        form=ProjectCreationForm(request.POST or None)
        formset = ImageFormSet(request.POST,request.FILES,queryset = Pictures.objects.none())
        if form.is_valid() and formset.is_valid():
            project = form.save(commit=False)
            project.user = Users.objects.get(id=id)
            project.save()
            tag=Tags.objects.create(name=form.cleaned_data.get('tags'))
            ProjectTags=project_tags.objects.create(tag=tag,project=project)
            for f in formset.cleaned_data:
                image = f.get('image')
                photo = Pictures(project = project,image = image)
                photo.save()
            form.save_m2m()
            messages.success(request,"project saved")
            return HttpResponse("Welcome")
        else:
            print(form.errors, formset.errors)
    else:
        form = ProjectCreationForm()
        formset = ImageFormSet(queryset=Pictures.objects.none())
    return render(request, 'add_project.html',
                  {'projectForm': form, 'formset': formset},
                  )
