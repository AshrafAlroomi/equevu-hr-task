# Generated by Django 4.2.1 on 2023-05-04 01:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


def create_departments(apps, schema_editor):
    Department = apps.get_model('applicants', 'Department')
    DEPARTMENT_CHOICES = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('FIN', 'Finance'),
    ]
    for dept_choice in DEPARTMENT_CHOICES:
        Department.objects.create(name=dept_choice[0])


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(
                    choices=[('IT', 'Information Technology'), ('HR', 'Human Resources'), ('FIN', 'Finance')],
                    max_length=3, unique=True)),
            ],

        ),

        migrations.RunPython(create_departments),

        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('start_working_date', models.DateField()),
                ('resume', models.FileField(upload_to='resumes/', validators=[
                    django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
                ('department',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicants.department')),
            ],
        ),
    ]
