# Generated by Django 3.2.23 on 2024-02-01 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publishing_projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campus',
            options={'verbose_name_plural': 'Campuses'},
        ),
        migrations.AlterField(
            model_name='project',
            name='contact',
            field=models.ManyToManyField(blank=True, related_name='projects', to='publishing_projects.Contact', verbose_name='Contact'),
        ),
        migrations.AlterField(
            model_name='project',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='publishing_projects.publishingprogram', verbose_name='Unit with activity'),
        ),
        migrations.AlterField(
            model_name='project',
            name='publication_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='publishing_projects.publicationtype'),
        ),
    ]
