from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Products(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products' , verbose_name="فروشنده" , null=True)  # فروشنده
    Img = models.ImageField( verbose_name="عکس محصول")
    Name_Product = models.CharField(max_length=100 ,verbose_name="نام محصول")
    Caption = models.TextField(max_length=1000 , verbose_name="توضیح کوتاه")
    Price = models.CharField(max_length=15 , verbose_name="قیمت اصلی")
    Discount = models.CharField(max_length=3 , verbose_name="تخفیف")
    Description = models.TextField(blank=True, null=True , verbose_name="توضیحات کامل محصول")
    selected_options = models.TextField(
        blank=True, null=True
        , verbose_name="مناسب هدیه به"
    )  # ذخیره گزینه‌ها به صورت رشته

    def __str__(self):
        return self.Name_Product


    class Meta :
        verbose_name="محصول"
        verbose_name_plural="محصولات"
   


class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    Product_id = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        verbose_name="محصول"
    )
    User = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="کاربر" )
    Question = models.TextField(max_length=250 , verbose_name="متن سوال" )
    Answer = models.TextField(max_length=250, null=True , verbose_name="جواب")
    Approved = models.BooleanField(default=False , verbose_name="حالت نمایش")
    Created_at = models.DateField(auto_now_add=True , verbose_name="نوشته شده در")
    class Meta :
        verbose_name="سوال"
        verbose_name_plural="سوال ها"


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    Product_id = models.ForeignKey(Products, on_delete=models.CASCADE ,verbose_name="محصول" )
    User = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="کاربر"
    )
    Title = models.CharField(max_length=200 , verbose_name="موضوع نظر")
    Comment_text = models.TextField(max_length=1000 , verbose_name="متن نظر")
    Created_at = models.DateField(auto_now_add=True , verbose_name="ساخته شده در")
    Approved = models.BooleanField(default=False , verbose_name="حالت نمایش")
    class Meta :
        verbose_name="نظر"
        verbose_name_plural="نظر ها"


class CommentLike(models.Model):
    id = models.AutoField(primary_key=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=False)


class Favorite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Product = models.ForeignKey(Products, on_delete=models.CASCADE)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="کاربر")
    Product = models.ForeignKey(Products, on_delete=models.CASCADE , verbose_name="محصول")
    NumberProduct = models.IntegerField(default=1 , verbose_name="تعداد محصول")
    FinalPrice = models.TextField(max_length=50 , null=True , verbose_name="قیمت نهایی")
    Message = models.TextField(null=True , verbose_name="متن همراه با هدیه")


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="فروشنده" , related_name='buyer_orders' , null=True)
    user_name = models.CharField( verbose_name="مشتری" , max_length=200 , null=True)
    user_adress = models.TextField( verbose_name="آدرس مشتری" , null=True)
    user_phone = models.TextField( verbose_name="تلفن مشتری" , null=True)
    product = models.ForeignKey('Products', on_delete=models.CASCADE, verbose_name="محصول")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="فروشنده" , related_name='seller_orders')
    quantity = models.PositiveIntegerField(default=1, verbose_name="تعداد")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="مبلغ کل")
    message_order = models.TextField( verbose_name="پیام همراه با سفارش" , null=True)
    ref_id = models.CharField(max_length=15 , null= True , unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")

    def __str__(self):
        return f"سفارش  {self.product}"
    
    class Meta:
        verbose_name = "سفارش"
        verbose_name_plural = "سفارش‌ها"

   
    

    
class SellerWallet(models.Model):
    seller = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="فروشنده")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="موجودی کیف پول")

    class Meta:
        verbose_name = "کیف پول فروشنده"
        verbose_name_plural = "کیف پول فروشندگان"

    def __str__(self):
        return f"موجودی شما برابر است با : {self.balance}"    
