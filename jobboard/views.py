from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import JobPosting
# Create your views here.
def index(request):
    #jobs = JobPosting.objects.all()
    # print(jobs)
    active_jobs = JobPosting.objects.filter(is_active = True)
    context = {
        'jobs':active_jobs,
        'pageTitle':"Job Page"
    }
    return render(request,'jobboard/index.html', context)
    
# job detail page
def job_detail(request,postId):
    # job_post = JobPosting.objects.get(pk=postId) #pk or id both work
    job_post = get_object_or_404(JobPosting, pk=postId, is_active=True)
    context = {
        'posting':job_post,
        'pageTitle':"Detail Page"
    }
    return render(request,'jobboard/detail.html', context)