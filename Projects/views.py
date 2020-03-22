from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Projects, Pictures, Rates
from Users.models import Users
# connect  view with form
from .forms import ProjectForm, DonationForm, RatingForm
import json
from django.db.models import Sum
from django.db import IntegrityError


def project_details(request, id):
    request.session['user_id'] = 2 #static ,change it to dynamic when merge
    print("****")
    print(request.session['user_id'])
    request.session['project_id'] = id
    project_details = Projects.objects.get(id=id)
    pictures=Pictures.objects.filter(project=id)
    context = {
        "project_details": project_details,
        "project_picture": pictures,
        "range": range(5),
        "user_id": request.session['user_id'],

    }
    return render(request, "project_details.html", context)


def edit_project(request, id):
    project = get_object_or_404(Projects, id=id)
    print(request.method)
    if request.method == 'POST':
        print("555")
        print(request.POST)
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            new_form = form.save(commit=False)
            print("n")
            print(project.user)
            print("m")
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
    user = get_object_or_404(Users, id=2) #edit to id = id from session (login user)
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():

            new_form = form.save(commit=False)
            new_form.user = project.user
            # new_form.project = Projects.id
            new_form.save()
    else:
        form = DonationForm(initial={'project': project, 'user': user})
    context = {
        "form": form,
    }
    return render(request, "donation.html", context)


def save(request):
    print("this sa ve rate method")
    uid = request.session['user_id'] #uid referes to the session user_id
    pid = request.session.get('project_id')
    p = Projects.objects.get(id=pid)
    x = Projects.objects.get(id=uid)

    ratedindex = request.POST.get('ratedIndex')
    print(ratedindex)
    uID = request.POST.get('user_id') #uID refers to the local storage user_id
    ratedindex += 1
    if uID != 0:
        u = Rates(rate=ratedindex)
        u.user = x
        u.project = p
        u.save()
    else:
        Rates.objects.filter(user=uID).update(rate=ratedindex)
    return HttpResponse(json.dumps({'uid': uid}), content_type="application/json")
    num_of_rates = Rates.objects.get(id).count()

    total = Rates.objects.filter(id=uID).aggregate(Sum('rate'))
    avg = total/num_of_rates
    print(avg)
    context = {
        'avg': avg,
    }
    return render(request, "project_details.html", context)
