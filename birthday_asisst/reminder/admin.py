from django.contrib import admin
from .models import Remind_member
from validator import Validator

# Register your models here.

class ReminderAdmin(admin.ModelAdmin):
    list_display = ("Full_name" , "Date_remind" , "Befor_day_remind")

    
    def formfield_for_dbfield(self, db_field, **kwargs):
        valid = Validator()

        formfild = super().formfield_for_dbfield(db_field , **kwargs)
        return formfild

admin.site.register(Remind_member , ReminderAdmin)