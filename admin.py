from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .models import Project, PublicationType, PublishingProgram, Contact, Subject, Campus
# from .forms import PublicationTypeChangeListForm

#class ProjectAdmin(admin.ModelAdmin):
    #pass
#admin.site.register(Project, ProjectAdmin)

admin.site.register(Campus)
admin.site.register(Contact)
admin.site.register(Subject)


@admin.register(PublishingProgram)
class PublishingProgramAdmin(admin.ModelAdmin):
    # filter_horizontal = ('projects',)
    # autocomplete_fields = ('projects',)
    search_fields = ['name',]
    list_filter = ('campus__name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # include all fields without typing all fieldnames
    # https://stackoverflow.com/a/18774202/1763984
    # list_display = [field.name for field in Project._meta.get_fields()]
    filter_horizontal = ('contact','subject',)
    autocomplete_fields = ('contact','subject',)
    search_fields = ['publication_name', 'program__name']
    list_filter = ('program__campus__name', 'publication_type__name', 'subject__name')


@admin.register(PublicationType)
class PublicationTypeAdmin(admin.ModelAdmin):
    pass

"""
class ProjectTypeChangeList(ChangeList):

    def __init__(self, request, model, list_display,
        list_display_links, list_filter, date_hierarchy,
        search_fields, list_select_related, list_per_page,
        list_max_show_all, list_editable, model_admin):

        super(ProjectTypeChangeList, self).__init__(request, model,
            list_display, list_display_links, list_filter,
            date_hierarchy, search_fields, list_select_related,
            list_per_page, list_max_show_all, list_editable, 
            model_admin)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['action_checkbox', 'name', 'publication_type']
        self.list_display_links = ['name']
        self.list_editable = ['publication_type']


    def get_changelist(self, request, **kwargs):
        return ProjectTypeChangeList

    def get_changelist_form(self, request, **kwargs):
        return PublicationTypeChangeListForm
"""


