from django.contrib import admin
from contactenquiry.models import contactEnquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display=('name','email','topic','message')

admin.site.register(contactEnquiry,EnquiryAdmin)