# naukri/models.py

from django.db import models

class JobListing(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)  # Renamed to 'company'
    place = models.CharField(max_length=255)  # Renamed to 'place' for location
    salary = models.CharField(max_length=100)  # Renamed to 'salary' for salary_range
    job_description = models.TextField()  # Renamed to 'job_description'
    job_category = models.CharField(max_length=50)  # Renamed to 'job_category' for job_type
    post_date = models.DateField(auto_now_add=True)  # Renamed to 'post_date'
    experience = models.CharField(max_length=50)  # Renamed to 'experience' for experience_level
    link = models.URLField(max_length=200)  # Renamed to 'link' for apply link

    def __str__(self):
        return f"{self.title} at {self.company}"
