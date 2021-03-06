# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-17 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Campus')),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=80, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_name', models.CharField(blank=True, help_text='name of the publication', max_length=200)),
                ('platform', models.CharField(choices=[('E', 'eScholarship'), ('U', 'UC Press'), ('O', 'Other'), ('S', 'Self-Published')], default='O', max_length=1)),
                ('publishing_partner', models.CharField(blank=True, max_length=200)),
                ('url', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('contact', models.ManyToManyField(blank=True, to='publishing_projects.Contact', verbose_name='Contact')),
            ],
        ),
        migrations.CreateModel(
            name='PublicationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Publication Type')),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublishingProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='unit hosting program', max_length=254, verbose_name='Unit')),
                ('notes', models.TextField(blank=True)),
                ('campus', models.ManyToManyField(blank=True, to='publishing_projects.Campus')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Subject')),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publishing_projects.PublishingProgram', verbose_name='Unit with activity'),
        ),
        migrations.AddField(
            model_name='project',
            name='publication_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='publishing_projects.PublicationType'),
        ),
        migrations.AddField(
            model_name='project',
            name='subject',
            field=models.ManyToManyField(blank=True, to='publishing_projects.Subject', verbose_name='Subject'),
        ),
    ]
