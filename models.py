from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=254, unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.email


class Campus(models.Model):
    name = models.CharField(max_length=40, unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=40, unique=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PublicationType(models.Model):
    name = models.CharField(max_length=40,)
    notes = models.TextField(blank=True)

    def __str__(self):
        return str(self.name)


class PublishingProgram(models.Model):
    # unit with a publishing activity
    name = models.CharField(max_length=254, blank=True, help_text='unit hosting program')
    notes = models.TextField(blank=True)
    campus = models.ManyToManyField(Campus, blank=True)

    def __str__(self):
        return str(self.name)


class Project(models.Model):
    program = models.ForeignKey(PublishingProgram)
    publication_name = models.CharField(
        max_length=200,
        help_text='name of the publication',
        blank=True,
    )
    publication_type = models.ForeignKey(PublicationType, blank=True,)
    publishing_partner = models.CharField(
        max_length=200,
        blank=True,
    )
    #regents_owned = models.BooleanField(
        #help_text='boolean or keep some notes',
        #blank=True,
    #)
    url	= models.URLField(blank=True)
    #Primary Contact	
    contact = models.ManyToManyField(Contact, blank=True)
    subject = models.ManyToManyField(Subject, blank=True)
    active = models.BooleanField(
        help_text='should this have date range?',
        default=True,
        blank=True,
    ) # start and stop dates

    distributor = models.CharField(
        max_length=200,
        help_text='books only',
        blank=True,
    )
    issn = models.CharField(
        max_length=200,
        help_text='journals only',
        blank=True,
    )
    notes = models.TextField(blank=True)

    def __str__(self):
        if self.publication_name:
            name = self.publication_name
        else:
            print(self.publication_type)
            name = self.publication_type
        return str(name)




#class Book():
#    distributor
#class Journal():
#    ISSN 	Journals only

