from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Candidate, Department
from datetime import date
import io
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your tests here.
class CandidateViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.department = Department.objects.get(name='IT')
        self.candidate = Candidate.objects.create(
            first_name="Ashraf",
            last_name="Alroomi",
            date_of_birth=date(1996, 8, 15),
            start_working_date=date(2020, 1, 1),
            department=self.department,
            resume=self.create_test_resume()
        )

    def test_department_list_view(self):
        url = reverse('department-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def create_test_resume(self):
        content = b'CV'
        buffer = io.BytesIO(content)
        uploaded_file = InMemoryUploadedFile(buffer, None, 'test_resume.pdf', 'application/pdf', len(content), None)
        return uploaded_file

    def test_candidate_registration(self):
        url = reverse('candidate-create')
        resume_file = self.create_test_resume()

        data = {
            "first_name": "Ashraf",
            "last_name": "Alroomi",
            "date_of_birth": "1996-08-30",
            "start_working_date": "2020-01-01",
            "department": "IT",
            "resume": resume_file
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Candidate.objects.count(), 2)
        self.assertEqual(Candidate.objects.last().first_name, 'Ashraf')
        self.assertEqual(Candidate.objects.last().last_name, 'Alroomi')
        self.assertEqual(Candidate.objects.last().department.name, 'IT')

    def test_candidate_list_view(self):
        url = reverse('candidate-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_X_ADMIN='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_candidate_resume_download_view(self):
        url = reverse('candidate-resume', kwargs={'id': self.candidate.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.credentials(HTTP_X_ADMIN='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('application/octet-stream', response['Content-Type'])
        self.assertIn('attachment', response['Content-Disposition'])
