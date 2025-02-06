# Generated by Django 5.1.5 on 2025-02-06 05:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0025_remove_scholarship_scholarship_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScholarshipType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='scholarship',
            name='scholarship_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admission.scholarshiptype'),
        ),
    ]
