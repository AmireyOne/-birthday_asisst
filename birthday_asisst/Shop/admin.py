from django.contrib import admin
from .models import Products , Comment , Questions , Orders, SellerWallet
import datetime
import jdatetime
from django.utils.html import format_html
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

# Register your models here.




class ProductAdmin(admin.ModelAdmin):
    list_display = ("Name_Product", "Price", "Discount")
    search_fields = ('Name_Product',)  # امکان جستجو
    list_filter = ('Price',)  # امکان فیلتر

    def get_queryset(self, request):
        """
        فیلتر کردن محصولات نمایش داده شده بر اساس کاربر وارد شده.
        """
        qs = super().get_queryset(request)
        # بررسی اینکه کاربر عضو گروه فروشندگان باشد
        if request.user.groups.filter(name='فروشنده').exists():
            return qs.filter(seller=request.user)  # فروشنده فقط محصولات خودش را می‌بیند
        elif request.user.is_superuser:
            return qs  # ادمین کل سایت همه محصولات را می‌بیند
        return qs.none()  # اگر عضو گروه فروشندگان نبود، هیچ محصولی را نبیند

    def save_model(self, request, obj, form, change):
        """
        تنظیم خودکار فروشنده به کاربر فعلی هنگام ذخیره.
        """
        if not obj.pk:  # اگر محصول جدید باشد
            obj.seller = request.user
        super().save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        """
        فقط اجازه ویرایش محصولات خود کاربر را می‌دهد.
        """
        # بررسی اینکه کاربر عضو گروه فروشندگان باشد
        if request.user.groups.filter(name='فروشنده').exists():
            if obj is None:
                return True  # نمایش لیست محصولات
            return obj.seller == request.user  # ویرایش فقط در صورتی مجاز است که کاربر مالک باشد
        elif request.user.is_superuser:
            return True  # ادمین کل اجازه تغییر دارد
        return False  # اگر عضو گروه فروشندگان نبود، اجازه ویرایش ندارد

    def has_delete_permission(self, request, obj=None):
        """
        فقط اجازه حذف محصولات خود کاربر را می‌دهد.
        """
        # بررسی اینکه کاربر عضو گروه فروشندگان باشد
        if request.user.groups.filter(name='فروشنده').exists():
            if obj is None:
                return True  # نمایش لیست محصولات
            return obj.seller == request.user  # حذف فقط در صورتی مجاز است که کاربر مالک باشد
        elif request.user.is_superuser:
            return True  # ادمین کل اجازه حذف دارد
        return False  # اگر عضو گروه فروشندگان نبود، اجازه حذف ندارد

 
 

   

class CommentAdmin(admin.ModelAdmin):
    list_display = ("User" , "Comment_text" , "Approved")
    list_filter =("Approved" ,)


class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ("User" , "Question" , "Approved")       
    list_filter = ('Approved' ,)  # امکان فیلتر

    
    def get_queryset(self, request):
        """
        محدود کردن سوالات به سوالات محصولات متعلق به فروشنده وارد شده
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # ادمین اصلی همه سوالات را می‌بیند
        
        # بررسی عضویت کاربر در گروه فروشندگان
        if request.user.groups.filter(name="فروشنده").exists():
            return qs.filter(Product_id__seller=request.user)  # فقط سوالات محصولات فروشنده
        return qs.none()  # کاربر مجاز نیست سوالی ببیند

    def has_change_permission(self, request, obj=None):
        """
        اجازه تغییر فقط در صورتی که محصول متعلق به فروشنده باشد.
        """
        if obj is None:
            return request.user.groups.filter(name="فروشنده").exists()  # نمایش لیست سوالات برای فروشندگان
        
        return obj.Product_id.seller == request.user  # مالکیت محصول بررسی شود

    def has_delete_permission(self, request, obj=None):
        """
        اجازه حذف فقط در صورتی که محصول متعلق به فروشنده باشد.
        """
        if obj is None:
            return request.user.groups.filter(name="فروشنده").exists()  # نمایش لیست سوالات برای فروشندگان
        
        return obj.Product_id.seller == request.user  # مالکیت محصول بررسی شود
  


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("user_name" , "product" , "quantity" , "created_at_shamsi")
    list_filter = ('created_at' ,)  # امکان فیلتر
    search_fields = ('ref_id',)





    def get_queryset(self, request):
        """
        محدود کردن سوالات به سوالات محصولات متعلق به فروشنده وارد شده
        """
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # ادمین اصلی همه سوالات را می‌بیند
        
        # بررسی عضویت کاربر در گروه فروشندگان
        if request.user.groups.filter(name="فروشنده").exists():
            return qs.filter(seller=request.user)  # فقط سوالات محصولات فروشنده
        return qs.none()  # کاربر مجاز نیست سفارشی ببیند

    def has_change_permission(self, request, obj=None):
        """
        اجازه تغییر فقط در صورتی که محصول متعلق به فروشنده باشد.
        """
        if obj is None:
            return request.user.groups.filter(name="فروشنده").exists()  # نمایش لیست سفارش‌ها برای فروشندگان
        
        return obj.seller == request.user  # مالکیت محصول بررسی شود

    def has_delete_permission(self, request, obj=None):
        """
        اجازه حذف فقط در صورتی که محصول متعلق به فروشنده باشد.
        """
        if obj is None:
            return request.user.groups.filter(name="فروشنده").exists()  # نمایش لیست سفارش‌ها برای فروشندگان
        
        return obj.seller == request.user  # مالکیت محصول بررسی شود

    def created_at_shamsi(self, obj ):
        """
        نمایش تاریخ به صورت شمسی
        """
       
        # تبدیل تاریخ میلادی به شمسی
        
        persian_date = jdatetime.date.fromgregorian(date=obj.created_at.date()).strftime('%Y/%m/%d')
        return format_html(f"<span>{persian_date}</span>")
        

    created_at_shamsi.short_description = "تاریخ ثبت"  # تغییر عنوان فیلد در لیست


    

    def changelist_view(self, request, extra_context=None):
        if request.user.groups.filter(name="فروشنده").exists():
            extra_context = extra_context or {}

            # محاسبه فروش امروز و موجودی کیف پول
            seller = request.user  # فرض بر این است که فروشنده لاگین کرده است
            sales_today = Orders.objects.filter(
                seller=seller,
                created_at__date=datetime.date.today()
            ).count()

            wallet = SellerWallet.objects.filter(seller=seller).first()
            wallet_balance = "{:,}".format(int(wallet.balance)) if wallet else 0

            today = datetime.datetime.now()
            persian_date_today = jdatetime.date.fromgregorian(date=today).strftime('%Y/%m/%d')

            seller_name= User.objects.filter(id = request.user.id).first()
            

            # افزودن داده‌ها به extra_context
            extra_context['today_sale'] = f"{sales_today} عدد"
            extra_context['wallet'] = f"{wallet_balance} تومان"
            extra_context['today'] = f"{persian_date_today}"
            extra_context['seller_name'] = f"{seller_name.first_name}"

            
            # ارسال extra_context به view اصلی
            return super().changelist_view(request, extra_context=extra_context)





admin.site.register(Products , ProductAdmin)
admin.site.register(Comment , CommentAdmin)
admin.site.register(Questions , QuestionAdmin)
admin.site.register(Orders , OrdersAdmin)
