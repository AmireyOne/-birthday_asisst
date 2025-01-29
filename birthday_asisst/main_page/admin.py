from django.contrib import admin
from .models import Comment , Information , Adress , Manage_Contact
from validator import Validator
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ("Full_name" , "Comment_message" , "Approved")
    list_filter =("Approved" ,)

    
    def formfield_for_dbfield(self, db_field, **kwargs):
        valid = Validator()

        formfild = super().formfield_for_dbfield(db_field , **kwargs)
        if db_field.name == "Comment_message"  :
            formfild.validators.append(valid.Check_len_comment)  
        return formfild
    
    
        
        

class InformationAdmin(admin.ModelAdmin):
    list_display = ("user" , "Phone" , "Email")

    def formfield_for_dbfield(self, db_field, **kwargs):
        valid = Validator()

        formfild = super().formfield_for_dbfield(db_field , **kwargs)
        if db_field.name == "Phone"  :
            formfild.validators.append(valid.Check_Phone)  
        return formfild

class AdressAdmin(admin.ModelAdmin):
    list_display = ("user" , "adress" )    



class manage_contactAdmin(admin.ModelAdmin):
    list_display=("user" , "Title" , "Caption")

admin.site.register(Comment , CommentAdmin)
admin.site.register(Information , InformationAdmin)
admin.site.register(Adress , AdressAdmin)
admin.site.register(Manage_Contact , manage_contactAdmin)