from Users.forms import UserRegisterForm
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from Projects.models import Rates,Featured_projects,Projects,Categories
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from Users.models import Profile


def home(request):
    #highest 5 rated projects
    query='select avg(rate) as rate_avg,Project_Rates.project_id,Project_Rates.id,Projects.title from Project_Rates inner join Projects  on Project_Rates.project_id=Projects.id  group by Project_Rates.Project_id ORDER BY rate_avg DESC LIMIT 5'
    result=Rates.objects.raw(query)

    #latest 5 projects
    latestProjects=Projects.objects.all().order_by('-start_date')[:5]

    #latest 5 featured projects
    featuredProjects=Featured_projects.objects.all().order_by('-featured_date')[:5]

    #list of categories
    categories=Categories.objects.all()

    return render(request, "Users/index.html",
    {"result":result,"featuredProjects":featuredProjects,"latestProjects":latestProjects,"categories":categories})

@csrf_exempt
def categoryProjects(request):
    id=request.POST.get('category_id')
    category=Categories.objects.get(id=id)
    projects=list(Projects.objects.filter(category=category).values())
    return JsonResponse(projects,safe=False)
	
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db() 
            username = form.cleaned_data.get('username')
            user.profile.phone = form.cleaned_data.get('phone')
            user.profile.Img = form.cleaned_data.get('Img') 
            user.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form': form})

def profile(request):
    return HttpResponse("profile")