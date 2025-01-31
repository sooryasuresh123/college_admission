# Generated by Django 5.1.5 on 2025-01-30 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_program'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=100)),
                ('stud_adm_no', models.CharField(max_length=20, unique=True)),
                ('aadhaar', models.CharField(max_length=12, unique=True)),
                ('abc_id', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('dob', models.DateField()),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_mob', models.CharField(max_length=15)),
                ('house_name', models.CharField(max_length=100)),
                ('post', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('date_of_joining', models.DateField()),
                ('income', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('egrantz', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('blood_group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B-'), ('O+', 'O-'), ('AB+', 'AB-')], max_length=5)),
                ('identification_mark', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
