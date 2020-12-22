# Generated by Django 3.1.1 on 2020-12-18 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50, null=True, unique=True)),
                ('department_short_form', models.CharField(max_length=4, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50, null=True)),
                ('subject_short_form', models.CharField(max_length=4, null=True)),
                ('credits', models.CharField(max_length=1, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.department')),
            ],
            options={
                'unique_together': {('department', 'subject_short_form')},
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.CharField(max_length=2, null=True)),
                ('chapter_name', models.CharField(max_length=50, null=True)),
                ('link', models.URLField()),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='academics.department', verbose_name='department')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.subject', verbose_name='subject')),
            ],
            options={
                'unique_together': {('department', 'subject', 'chapter_number')},
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='1', max_length=3)),
                ('section_name', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1)),
                ('link', models.URLField(null=True)),
                ('timetable', models.URLField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.department')),
            ],
            options={
                'unique_together': {('semester', 'section_name', 'department')},
            },
        ),
    ]
