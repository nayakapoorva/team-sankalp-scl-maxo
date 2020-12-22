# Generated by Django 3.1.1 on 2020-12-18 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes_conducted', models.IntegerField()),
                ('classes_attended', models.IntegerField()),
                ('percentage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conducted_date', models.DateField(null=True, verbose_name='conducted_date')),
                ('logged_date', models.DateTimeField(auto_now_add=True, verbose_name='logged_date')),
                ('Class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.class', verbose_name='class')),
            ],
        ),
    ]
