# Generated by Django 5.0.4 on 2024-04-05 16:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0004_question_response'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='inspections.question'),
        ),
    ]
