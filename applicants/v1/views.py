from django.http import HttpResponse
from rest_framework import generics, permissions
from applicants.models import Candidate, Department
from .serializers import CandidateSerializer, DepartmentSerializer


class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.META.get("HTTP_X_ADMIN") == "1"


class CandidateRegistrationView(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CandidateListView(generics.ListAPIView):
    permission_classes = [IsAdminUser]
    queryset = Candidate.objects.order_by('-registration_date')
    serializer_class = CandidateSerializer


class CandidateResumeDownloadView(generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        response = HttpResponse(instance.resume, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{instance.resume.name}"'
        return response


class DepartmentListView(generics.ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
