# Generated by Django 5.1.5 on 2025-02-06 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0020_role_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scholarship_type', models.CharField(max_length=50)),
            ],
        ),
    ]
