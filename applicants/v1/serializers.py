from rest_framework import serializers
from applicants.models import Department, Candidate


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField()

    class Meta:
        model = Department
        fields = ['name', 'code']


class CandidateSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(slug_field='code', queryset=Department.objects.all())
    years_of_experience = serializers.ReadOnlyField()

    class Meta:
        model = Candidate
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'years_of_experience', 'start_working_date',
                  'department', 'resume']
        read_only_fields = ['id']
