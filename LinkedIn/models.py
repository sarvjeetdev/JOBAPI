from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=100)  # e.g., "50,000 - 70,000"
    description = models.TextField()
    job_type = models.CharField(max_length=50) 
    posted_date = models.DateField(auto_now_add=True)
    experience_level = models.CharField(max_length=50)  # e.g., "Entry-level", "Senior"
    apply_link = models.URLField(max_length=500, blank=True, null=True)  # New field for application link

    def __str__(self):
        return f"{self.title} at {self.company}"
