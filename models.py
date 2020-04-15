from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.email)


class Campus(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Campus")
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name="Subject")
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class PublicationType(models.Model):
    name = models.CharField(max_length=40, verbose_name="Publication Type")
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class PublishingProgram(models.Model):
    # unit with a publishing activity
    name = models.CharField(
        max_length=254,
        blank=True,
        help_text="unit hosting program",
        verbose_name="Unit",
    )
    notes = models.TextField(blank=True)
    campus = models.ManyToManyField(Campus, blank=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    program = models.ForeignKey(PublishingProgram, verbose_name="Unit with activity")
    publication_name = models.CharField(
        max_length=200, help_text="name of the publication", blank=True,
    )
    publication_type = models.ForeignKey(PublicationType, blank=True,)
    publishing_partner = models.CharField(max_length=200, blank=True,)
    url = models.URLField(blank=True)
    contact = models.ManyToManyField(Contact, verbose_name="Contact", blank=True)
    subject = models.ManyToManyField(Subject, verbose_name="Subject", blank=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        if self.publication_name:
            name = self.publication_name
        else:
            name = f"{self.publication_type} ({self.program})"
        return str(name)
