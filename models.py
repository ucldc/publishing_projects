from django.db import models


PUB_TYPE_CHOICES = [
    ('A', 'Book',),
    ('B', 'Book series',),
    ('C', 'Briefs',),
    ('D', 'Conference Proceedings',),
    ('E', 'Journal',),
    ('F', 'Magazine',),
    ('G', 'Monograph Series',),
    ('H', 'Monograph',),
    ('I', 'Research reports',),
    ('J', 'Working Papers',),
    ('Z', 'Other',),
]


class Project(models.Model):
    publication_name = models.CharField(
        max_length=200,
        help_text='name of the publication',
    )
    publication_type = models.CharField(
        max_length=1,
        choices=PUB_TYPE_CHOICES,
    )
    campus = models.CharField(max_length=4)
    campus_unit = models.CharField(max_length=200)
    publishing_partner = models.CharField(max_length=200)
    regents_owned = models.BooleanField(
        help_text='boolean or keep some notes',
    )
    url	= models.URLField()
    #Primary Contact	
    contact_email_address = models.EmailField(
        help_text='boolean or keep some notes',
    )
    subject = models.CharField(max_length=200)	# Controlled vocabulary?
    peer_reviewed = models.BooleanField(
        help_text='boolean or keep some notes',
    )
    active = models.BooleanField(
        help_text='should this have date range?',
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

    def __str__(self):
        return self.publication_name

#class Book():
#    distributor


#class Journal():
#    ISSN 	Journals only
