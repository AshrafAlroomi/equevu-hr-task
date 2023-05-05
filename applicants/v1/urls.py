from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.CandidateListView.as_view(), name='candidate-list'),
    path('candidate/', views.CandidateRegistrationView.as_view(), name='candidate-create'),
    path('candidates/<int:id>/resume/', views.CandidateResumeDownloadView.as_view(), name='candidate-resume'),
    path('departments/', views.DepartmentListView.as_view(), name='department-list'),
]
