from django.core.exceptions import ValidationError


class Validator ():


    def Check_len_comment(self , value):
        if len(value)<=3:
            raise ValidationError("حداقل کاراکتر مجاز برای کامنت 4 عدد است")
        

    def Check_Phone(self , value):
        if len(value)< 11 or len(value)>11:
            raise ValidationError("تعداد کاراکتر مجاز برای شماره تلفن 11 رقم است")
        
        if not value.isnumeric():
            raise ValidationError("برای شماره تلفن تنها اعداد مجاز هستند")
        


        
