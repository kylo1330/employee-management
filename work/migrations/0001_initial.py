# Generated by Django 5.0.2 on 2024-11-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_details',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
                ('work_type', models.CharField(max_length=30)),
            ],
        ),
    ]
