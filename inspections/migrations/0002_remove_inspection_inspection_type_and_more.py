# Generated by Django 5.0.4 on 2024-04-05 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inspection',
            name='inspection_type',
        ),
        migrations.RemoveField(
            model_name='inspection',
            name='report',
        ),
        migrations.CreateModel(
            name='InspectionVersion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('inspection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='inspections.inspection')),
            ],
            options={
                'unique_together': {('inspection', 'version_number')},
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('inspection_version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='inspections.inspectionversion')),
            ],
        ),
        migrations.CreateModel(
            name='Subsection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsections', to='inspections.section')),
            ],
        ),
    ]
