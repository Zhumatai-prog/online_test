from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import *

admin.site.register(Course)

@admin.register(Question, Result)
class ViewAdmin(ImportExportModelAdmin):
    pass
