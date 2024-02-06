# Django Job Board App Demo

## How to Set up

- `python -m venv env`
- `source env/bin/activate`
- `pip install django`
- `django-admin startproject config .`
- `python manage.py startapp jobboard`
- Update `INSTALLED_APPS` in `settings.py`
- Update `views.py` and `urls.py`

## Django Models
- `python manage.py makemigrations`
- `python manage.py migrate`

## CRUD Operations
- `python manage.py shell` to enter the shell
- `from jobboard.models import JobPosting`
- `JobPosting.objects.all()`
- `JobPosting.objects.get(id=1)`
- `JobPosting.objects.create(title='full stack developer', description='an awesome job', company='ABC tech', salary=120000)`
- `job = JobPosting.objects.get(id=1)`
- `job`
- `job.description = "A good job"` to update the description
- `job.save()`

## Django Admin
- `python manage.py createsuperuser` ( enter username and password)
- Go to `http:localhost:8000/admin`and login

## Update `admin.py`
- `admin.site.register(JobPosting)`

## Update `models.py` 
so that it doesn’t show JobPosting Object in the Panel

```python
def __str__(self):
        return f"{self.title} | {self.company}"
```


