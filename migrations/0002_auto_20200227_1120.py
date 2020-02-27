# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2020-02-27 17:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publishing_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(help_text='should this have date range?'),
        ),
        migrations.AlterField(
            model_name='project',
            name='contact_email_address',
            field=models.EmailField(help_text='boolean or keep some notes', max_length=254),
        ),
        migrations.AlterField(
            model_name='project',
            name='distributor',
            field=models.CharField(help_text='books only', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='issn',
            field=models.CharField(help_text='journals only', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='peer_reviewed',
            field=models.BooleanField(help_text='boolean or keep some notes'),
        ),
        migrations.AlterField(
            model_name='project',
            name='publication_name',
            field=models.CharField(help_text='name of the publication', max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='publication_type',
            field=models.CharField(choices=[('A', 'Book'), ('B', 'Book series'), ('C', 'Briefs'), ('D', 'Conference Proceedings'), ('E', 'Journal'), ('F', 'Magazine'), ('G', 'Monograph Series'), ('H', 'Monograph'), ('I', 'Research reports'), ('J', 'Working Papers'), ('Z', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='project',
            name='regents_owned',
            field=models.BooleanField(help_text='boolean or keep some notes'),
        ),
    ]
