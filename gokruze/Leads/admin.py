from django.contrib import admin
from django.contrib.auth.models import Group
from Leads.models import Leads
import csv
from django.http import HttpResponse

admin.site.index_title = "Welcome, Lets Manage Leads With Ease"
admin.site.site_header = "GoKruze Lead Manager Admin"
admin.site.site_title = "GoKruze Lead Manager Admin Portal"

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


# Register your models here.
class LeadsAdmin(admin.ModelAdmin,ExportCsvMixin):
    search_fields = ["Lead_No","Full_Name", "Company_Name", "Pick_Up_Location","Drop_Location"]
    list_filter = ["Lead_Status", "Company_Name"]
    list_display = [
        "Lead_No",
        "Date_of_Lead",
        "Full_Name",
        "Shift_Start",
        "Shift_End",
        "Pick_Up_Location",
        "Drop_Location",
        "Lead_Status",
        "Remark",
    ]
    list_editable = ["Lead_Status","Remark"]
    actions = ["export_as_csv"]


admin.site.register(Leads,LeadsAdmin)
admin.site.unregister(Group)