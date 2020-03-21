from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects,Tags
from django.db.models import Q

# | Q(category.name__icontains=value)
# Create your views here.
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
