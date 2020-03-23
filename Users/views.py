from django.shortcuts import render
from django.http import HttpResponse
from Projects.models import Rates,Featured_projects


# dic[]
def home(request):
	#highest 5 rated projects
	query='select avg(rate) as rate_avg,Project_Rates.project_id,Project_Rates.id,Projects.title from Project_Rates inner join Projects  on Project_Rates.project_id=Projects.id  group by Project_Rates.Project_id ORDER BY rate_avg DESC LIMIT 5'
	result=Rates.objects.raw(query)

	#latest 5 featured projects
	featuredProjects=Featured_projects.objects.all().order_by('-featured_date')[:5]
	print(featuredProjects)
	print(result)
	#latest 5 projects

	#list of categories

	return render(request, "Users/index.html", {"result":result,"featuredProjects":featuredProjects})

	