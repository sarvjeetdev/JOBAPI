# LinkedIn/management/commands/generate_jobs.py
from django.core.management.base import BaseCommand
from LinkedIn.models import Job
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate a large number of job entries'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of jobs to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        job_titles = [
            "Software Engineer", "Data Scientist", "Backend Developer",
            "Frontend Developer", "UI/UX Designer", "Machine Learning Engineer",
            "Project Manager", "DevOps Engineer", "System Analyst"
        ]
        employment_types = ["Full-time", "Part-time", "Contract", "Internship"]
        
        for _ in range(total):
            Job.objects.create(
                title=random.choice(job_titles),
                company=fake.company(),
                description=fake.text(max_nb_chars=200),
                location=fake.city(),
                salary_range=f"{random.randint(50000, 120000)}-{random.randint(121000, 200000)}",
                job_type=random.choice(employment_types)
            )

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} job entries'))
