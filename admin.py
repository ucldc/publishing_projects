from django.contrib import admin

# Register your models here.
from .models import Project

#class ProjectAdmin(admin.ModelAdmin):
    #pass
#admin.site.register(Project, ProjectAdmin)

#admin.site.register(Project)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    # include all fields without typing all fieldnames
    # https://stackoverflow.com/a/18774202/1763984
    list_display = [field.name for field in Project._meta.get_fields()]
