from django.contrib import admin
from .models import Branch, Contact, Loanform, Chairman_message
# Register your models here.

admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Chairman_message)


@admin.register(Loanform)
class LoanformAdmin(admin.ModelAdmin):
    list_display = ('name', 'phno', 'regno', 'selbranch','userform', 'date','status')
