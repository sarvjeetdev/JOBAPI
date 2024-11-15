import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

LINKEDIN_API_URL = "https://jobapi-nu.vercel.app/linkedin/jobs/"
NAUKRI_API_URL = "https://jobapi-nu.vercel.app/naukri/jobs/"
GLASSDOOR_API_URL = "https//jobapi-nu.vercel.app/glassdoor/jobs/"
class IntegratedJobsView(APIView):
    
    def get(self, request):
        try:
            # Fetch data from LinkedIn API
            linkedin_response = requests.get(LINKEDIN_API_URL)
            linkedin_data = linkedin_response.json() if linkedin_response.status_code == 200 else []
            print("priniting Linkedin Data",len(linkedin_data))
            # Fetch data from Naukri API
            naukri_response = requests.get(NAUKRI_API_URL)
            naukri_data = naukri_response.json() if naukri_response.status_code == 200 else []
            print("Pirinting naukri data",len(naukri_data))
            # Fetch data from Glassdoor API
            glassdoor_response = requests.get(GLASSDOOR_API_URL)
            glassdoor_data = glassdoor_response.json() if glassdoor_response.status_code == 200 else []
            print("Pirinting naukri data",len(glassdoor_data))
            # Combine data from all three sources
            all_jobs = []
            for job in linkedin_data:
                job['source'] = 'LinkedIn'
                all_jobs.append(job)
                
            for job in naukri_data:
                job['source'] = 'Naukri'
                all_jobs.append(job)
                
            for job in glassdoor_data:
                job['source'] = 'Glassdoor'
                all_jobs.append(job)

            # Optionally, you can cache data in the database here if needed
            return Response(all_jobs, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
