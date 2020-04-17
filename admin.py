from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .models import (
    Project,
    PublicationType,
    PublishingProgram,
    Contact,
    Subject,
    Campus,
)

admin.site.register(Campus)
admin.site.register(Contact)
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    ordering = ['name']

admin.site.register(PublicationType)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = (
        "contact",
        "subject",
    )
    # autocomplete_fields = ('contact','subject','program') (we are still on django 1.11, so can't use this
    search_fields = [
        "publication_name",
        "program__name",
    ]
    list_filter = (
        "program__campus__name",
        "platform",
        "publication_type__name",
        "subject__name",
    )


class ProjectInline(admin.StackedInline):
    model = Project
    show_change_link = True
    fields = ("publication_name", "publication_type")
    readonly_fields = ("publication_name", "publication_type")


@admin.register(PublishingProgram)
class PublishingProgramAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
    list_filter = ("campus__name",)
    inlines = [ProjectInline]
    filter_horizontal = ('campus',)
