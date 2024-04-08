# Generated by Django 5.0.4 on 2024-04-05 16:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspections', '0002_remove_inspection_inspection_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='section',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=1024)),
                ('order', models.PositiveIntegerField(default=0)),
                ('comment_required', models.BooleanField(default=False)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='inspections.section')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inspections.question')),
            ],
        ),
        migrations.DeleteModel(
            name='Subsection',
        ),
    ]