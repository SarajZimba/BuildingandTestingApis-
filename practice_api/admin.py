from django.contrib import admin
from practice_api.models import *

# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter=('company',)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee, EmployeeAdmin)