# Generated by Django 5.1.5 on 2025-02-03 17:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0012_caste_quota_religion_student_caste_student_quota_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programlevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_level', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admission.program'),
        ),
        migrations.AddField(
            model_name='program',
            name='program_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admission.programlevel'),
        ),
    ]
