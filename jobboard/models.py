from django.db import models

# Create your models here.
# model => python class
# model represents a table in the db
# attrs are the fields in the table

# job posting table
class JobPosting(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length = 100)
    description = models.TextField()
    company = models.CharField(max_length = 50)
    salary = models.IntegerField()
    is_active = models.BooleanField(default = False) # only show active jobs


    def __str__(self):
        return f"{self.title} | {self.company}"



# makemigrations
## creates instructions tellings Django how the DB has changed
# migrate : applies above changes
    
# python manage.py makemigrations
# python manage.py migrate
    


# CRUD operations
# model manager - objects
# JobPosting.objects.all()
# JobPosting.objects.get(id=1)
# JobPosting.objects.filter(company='abc tech')

# Django comes with a shell:
# `python manage.py shell` 
# `from jobboard_models import JobPosting`
# JobPosting.objects.all()

# JobPosting.objects.create(title="developer", description="first job", company="abc tech", salary=75000)
    
