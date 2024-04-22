

# Create your views here.
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job

def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})

def upload_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        company = request.POST.get('company')
        image = request.FILES.get('image')
        Job.objects.create(title=title, description=description, image=image)
        return redirect('index')
    return render(request, 'uploads.html')

def delete_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    if request.method == 'POST':
        job.delete()
        return redirect('index')
    return render(request, 'delete_job.html', {'job': job})