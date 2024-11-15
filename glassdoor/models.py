from django.db import models

class JobPost(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)  # e.g., "70,000 - 100,000"
    job_description = models.TextField()
    job_type = models.CharField(max_length=50)  # e.g., "Full-time", "Part-time"
    posted_date = models.DateField(auto_now_add=True)
    experience_level = models.CharField(max_length=50)  # e.g., "Junior", "Senior"
    apply_link = models.URLField(max_length=200)


    def __str__(self):
        return f"{self.title} at {self.company_name}"
