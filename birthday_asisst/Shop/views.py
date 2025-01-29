from django.shortcuts import render
from django.core.paginator import Paginator
from main_page.Userauth import Userauths
from main_page.models import Adress , Information
from django.http import HttpResponseRedirect , HttpResponse
from .models import Products , Questions , Comment , CommentLike , Favorite , Cart , SellerWallet , Orders
from django.contrib.auth.models import User
import jdatetime
import datetime
from django.http import JsonResponse
from .forms import Form_Questions , Form_Comments
from django.shortcuts import get_object_or_404
import requests , json
from django.db.models import Q
from decimal import Decimal
import http.client

# Create your views here.

def shop_page(request):
    user_at = Userauths().StateLog(request=request)
    product=Products.objects.all()
    products=[]
    for item in product:
        discounts=item.Discount
        discount_price=(int(discounts) / 100) * int(item.Price)
        final_price=int(item.Price) - discount_price
        products.append({
            "id":item.id,
            "Img" : item.Img,
            "product_name" : item.Name_Product,
            "discount":item.Discount,
            "final_price":"{:,}".format(int(final_price)),
            "price":"{:,}".format(int(item.Price))
        })

    if user_at["State"] == True:
        name = user_at["User"].first_name

        return render(request=request, template_name='home_shop.html', context={"user": user_at  , "products" : products}  )
    else:
        return render(request=request, template_name='home_shop.html', context={ "products" : products , "user": user_at})
    

def product_page(request , ID):
    user_at = Userauths().StateLog(request=request)

    fave=Favorite.objects.filter(Product_id=ID , user_id=request.user.id)
    if len(fave) != 0 :
        favorite=True
    else:
        favorite=False   
    
    questions=Questions.objects.filter(Product_id = ID , Approved=True).all()
    questions_list=[]
    #قیمت ها و تخفیفات
    product=Products.objects.filter(id = ID).first()
    discounts=product.Discount
    discount_price=(int(discounts) / 100) * int(product.Price)
    final_price=int(product.Price) - discount_price

    #سوال ها
    formQ=Form_Questions()


    for item in questions:
        name=User.objects.filter(id = item.User_id).first()
        #تبدیل تاریخ میلادی به شمسی
        jalali_date = convert_gregorian_to_jalali(item.Created_at)

        questions_list.append({
            "name":name.first_name,
            "question":item.Question,
            "Answer":item.Answer,
            "date":jalali_date

        })

    #نظرات
    form=Form_Comments()
    comment_list=[]
    comments=Comment.objects.filter(Product_id = ID , Approved=True).order_by('-Created_at').all()

    for item in comments:
        name=User.objects.filter(id = item.User_id).first()
        #تبدیل تاریخ میلادی به شمسی
        jalali_date = convert_gregorian_to_jalali(item.Created_at)

        comment_list.append({
            "name":name.first_name,
            "comment_title":item.Title,
            "comment_text":item.Comment_text,
            "date":jalali_date,
            "ids":item.id,
            'likes': item.likes.filter(is_like=True).count(),  # تعداد لایک‌ها
            'dislikes': item.likes.filter(is_like=False).count(),  # تعداد دیسلایک‌ها

        })



    return render(request=request, template_name='product.html',
                   context={"product" : product ,
                            "final_price":"{:,}".format(int(final_price)) ,
                            "question":questions_list  ,
                            "id":ID ,
                            "form":form,
                            "formQ":formQ,
                            "comment_list":comment_list,
                            "fave":favorite,
                            "user":user_at


                            }  )



def convert_gregorian_to_jalali(gregorian_date):

    
    """
    تبدیل تاریخ میلادی به جلالی
    """
    try:
        # تاریخ میلادی باید به صورت شیء datetime وارد شود
        jalali_date = jdatetime.date.fromgregorian(date=gregorian_date)  # استفاده از متد fromgregorian برای تبدیل
        # تبدیل میلادی به جلالی
        return jalali_date.strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error converting date: {e}")
        return None    


def get_comments(request , ID):
        
    comments = Comment.objects.filter(Product_id=ID , Approved = True).order_by('-Created_at')
    comments_list = [
        {
            'User_name': comment.User.first_name,  # نام‌گذاری خواناتر
            'Title': comment.Title,
            'Comment_text': comment.Comment_text,
            'created_at': convert_gregorian_to_jalali(comment.Created_at),
            'comment_id': comment.id,
            'likes': comment.likes.filter(is_like=True).count(),  # تعداد لایک‌ها
            'dislikes': comment.likes.filter(is_like=False).count(),  # تعداد دیسلایک‌ها
        }
        for comment in comments
    ]
    return JsonResponse({'comments': comments_list})



def add_comment(request):
    
    user_at=Userauths().StateLog(request=request)
    comments = Comment.objects.filter(User_id = user_at["User"].id )
    form = Form_Comments(request.POST)
    if user_at["State"]== True :
        if request.method == "POST":
           if form.is_valid():
                for item in comments:
                   if item.Title == form.data["Title"] and item.Comment_text == form.data["Comment"] :
                       return HttpResponse("exist")                  
                
                new_comment = Comment(
                    Product_id_id=request.POST.get("id-product"),
                    User_id=user_at["User"].id,
                    Title=form.data["Title"],
                    Comment_text=form.data["Comment"],
                    Approved=False,   
                    Created_at=datetime.datetime.now()
                )            
                new_comment.save()
                return HttpResponse("true")
               
           else:
               return HttpResponse("not valid")
        else:
           return HttpResponse("erorr")
    else:
        return HttpResponseRedirect("/auth")
    




def add_question(request):
    user_at=Userauths().StateLog(request=request)
    questions = Questions.objects.filter(User_id = user_at["User"].id )
    form = Form_Questions(request.POST)
    if user_at["State"]== True :
        if request.method == "POST":
           if form.is_valid():
                for item in questions:
                   if item.Question == form.data["question"] :
                       return HttpResponse("exist")
                   
                new_question = Questions(
                    Product_id_id=request.POST.get("id-product-question"),
                    User_id=user_at["User"].id,
                    Question=form.data["question"],
                    Approved=False,   
                    Created_at=datetime.datetime.now()
                )            
                new_question.save()
                return HttpResponse("true")
               
           else:
               return HttpResponse("not valid")
        else:
           return HttpResponse("erorr")
    else:
        return HttpResponseRedirect("/auth")
    




def toggle_like(request, comment_id, action):
    if request.method == 'POST':
        user = request.user
        comment = get_object_or_404(Comment, id=comment_id)
        
        is_like = True if action == "like" else False

        # بررسی اگر کاربر قبلاً لایک یا دیسلایک کرده
        like_obj, created = CommentLike.objects.get_or_create(comment=comment, user=user)

        if not created and like_obj.is_like == is_like:
            # حذف لایک/دیسلایک در صورت تکرار همان عمل
            like_obj.delete()
            return JsonResponse({'status': 'removed'})
        else:
            # ذخیره یا تغییر لایک/دیسلایک
            like_obj.is_like = is_like
            like_obj.save()

            # شمارش تعداد لایک‌ها و دیسلایک‌ها
            likes_count = comment.likes.filter(is_like=True).count()
            dislikes_count = comment.likes.filter(is_like=False).count()

            return JsonResponse({
                'status': 'updated',
                'likes': likes_count,
                'dislikes': dislikes_count
            })

    return JsonResponse({'error': 'Invalid request'}, status=400)





def add_favorite(request):
    user_at = Userauths().StateLog(request=request)
    if user_at["State"] == True :
        if request.method == "POST":
                product_ids = request.POST.get("product_id")
                product = Favorite.objects.filter(Product_id=product_ids , user_id=request.user.id)  
                if len(product) == 0:
                    faver=Favorite(Product_id = product_ids , user_id=request.user.id)
                    faver.save()
                    return JsonResponse({"status": "added", "message": "محصول به علاقه‌مندی‌ها افزوده شد."})
                else:
                    product.delete()
                    return JsonResponse({"status": "delete", "message": "محصول از علاقه‌مندی‌ها حذف شد."})
                
        else:
            return JsonResponse({"status": "error", "message": "درخواست نامعتبر است."})
    else:
        HttpResponseRedirect("/auth")    
        

def Cart_page(request):
    user_at = Userauths().StateLog(request=request)
    adresss=Adress.objects.filter(user = request.user.id ).first()
    informations=Information.objects.filter(user = request.user.id).first()
    fullname=request.user.first_name
    status_code=0
    if user_at["State"] == True :
        if informations != None and adresss != None :
            status_code=1
            cart_list=[]
            cart_list_id=[]
            status=False
            
            product_cart=Cart.objects.filter(user=request.user.id)
            phone=informations.Phone
            email=informations.Email
            adress=adresss.adress
            
            pro_id = 0
            
            
            if len(product_cart) != 0 :
                
                status=True

                for items in product_cart :
                    pro_id  = items.id

                    product=Products.objects.filter(id = items.Product_id)
                    for item in product :
                        discounts=item.Discount
                        discount_price=(int(discounts) / 100) * int(item.Price)
                        price_with_discount=int(item.Price) - discount_price
                        sood=discount_price * items.NumberProduct
                        final_price=(int(item.Price) - discount_price) * items.NumberProduct

                        cart_list.append({
                            "name":item.Name_Product ,
                            "img": item.Img ,
                            "first_price" : "{:,}".format(int(item.Price)),
                            "final_price":"{:,}".format(int(final_price)),
                            "final_prices": int(final_price),
                            "sood" : "{:,}".format(int(sood)),
                            "numbers" : items.NumberProduct,
                            "price_with_discount" : "{:,}".format(int(price_with_discount)),
                            "pro_id": items.id,
                            "message": items.Message,
                            "product_id":item.id,
                            "seler_id":item.seller.id


                            
                        })

            new_product_list = []
            new_product = Products.objects.all().order_by('-id')[:5]
            print(new_product)
            for item in new_product :
                discounts=item.Discount
                discount_price=(int(discounts) / 100) * int(item.Price)
                final_price=int(item.Price) - discount_price
                new_product_list.append(
                    {
                        "name_new_product" : item.Name_Product,
                        "new_discount" : discounts,
                        "new_price" : "{:,}".format(int(item.Price)),
                        "new_final_price":"{:,}".format(int(final_price)),
                        "new_img":item.Img,
                        "new_id" : item.id


                    }
                )



            return render(request=request , template_name='cart.html' , context={"user": user_at ,"pro_id" : pro_id , "product_item" : cart_list,"new_product" : new_product_list ,  "status":status , "fullname":fullname , "phone":phone ,"email":email , "adress": adress , "st_code" : status_code}) 
        else:
            return render(request=request , template_name='cart.html' , context={"user": user_at , "fullname":fullname , "st_code" : status_code , "new_product" : new_product_list})
    else:
        return HttpResponseRedirect("/auth")    

def cart_item_count(request):
   
    count_cart=len(Cart.objects.filter(user_id = request.user.id))
    return JsonResponse({'count': count_cart})

def ManageCart(request):
    user_at = Userauths().StateLog(request=request)
    if user_at["State"] == True :
        if request.method == "POST":
                product_ids = request.POST.get("product_id")
                number = request.POST.get("num-product")
                final_price = request.POST.get("price-product")
                Message = request.POST.get("message-product")
                print(final_price)
                product = Cart.objects.filter(Product_id=product_ids , user_id=request.user.id , NumberProduct=number , FinalPrice=final_price)  
                if len(product) == 0:
                    cart_product=Cart(Product_id=product_ids , user_id=request.user.id , NumberProduct=number , FinalPrice=final_price , Message=Message)
                    cart_product.save()
                    return JsonResponse({"status": "added", "message": "محصول به سبد خرید افزوده شد."})
                else:
                    
                    return JsonResponse({"status": "exist", "message": "این محصول در سبد خرید شما موجود است"})
                
        else:
            return JsonResponse({"status": "error", "message": "درخواست نامعتبر است."})
    else:
        HttpResponseRedirect("/auth")  



def Deletecart(request):

    if request.method == "POST":
    
        ids = request.POST.get("id")
        print(ids)
        product = Cart.objects.filter(
                id=ids,
            )
        print(len(product))
        if len(product) != 0:
            product.delete()
            return HttpResponse("true")
        else:
            return HttpResponse("none")
    else:
        return HttpResponse("valid")    
    


def pays(request , pay , product_id , seler_id , number , cart_id):
    

    url = "https://sandbox.zarinpal.com/pg/v4/payment/request.json"

    payload = {
        "merchant_id": "1fb03834-82dd-4aa3-8952-eee217ad2f30",
        "amount": pay,
        "currency" : "IRT",
        "callback_url": "http://127.0.0.1:8000/shop/resualt_pay/"+pay+"/"+product_id+"/"+seler_id+"/"+ number +"/"+cart_id,
        "description": product_id,
        "metadata": {
            "seler_id": seler_id,
            "number": number,
            "product_id": product_id,
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    response_dict = json.loads(response.text)
    authority = response_dict.get("data", {}).get("authority", None)
    


    return HttpResponseRedirect("https://sandbox.zarinpal.com/pg/StartPay/"+authority)


def resualt_pay(request , pay , product_id , seler_id , number , cart_id):
    

    Authority = request.GET.get("Authority")
    url = "https://sandbox.zarinpal.com/pg/v4/payment/verify.json"

    # داده‌های درخواست
    payload = {
        "merchant_id": "1fb03834-82dd-4aa3-8952-eee217ad2f30",
        "amount": pay,
        "authority": Authority
    }

    # هدرهای درخواست
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # ارسال درخواست POST
    response = requests.post(url, json=payload, headers=headers)
    response_dict = json.loads(response.text)
    code = response_dict.get("data", {}).get("code", None)
    
    card_pan = response_dict.get("data", {}).get("card_pan", None)
    ref_id = response_dict.get("data", {}).get("ref_id", None)
  
    walet=SellerWallet.objects.filter(seller=seler_id).first() 
   
    
    user= User.objects.filter(id = request.user.id).first()
    user_info = Information.objects.filter(user = request.user.id).first()
    user_adresss = Adress.objects.filter(user = request.user.id).first()

    product=Products.objects.filter(id = product_id).first()

    user_seler=User.objects.filter(id = seler_id).first()
    product_in_cart = Cart.objects.filter(id = cart_id).first()
    pay_mony = (5 / 100) * int(pay)
    walet_pay = int(pay) - int(pay_mony)
   
    if code == 100:
        new_order = Orders(
                    user = user,
                    user_name=user.first_name,
                    user_adress=user_adresss.adress,
                    user_phone=user_info.Phone,
                    product=product,
                    seller=user_seler,
                    quantity=number,
                    ref_id = ref_id,
                    message_order = product_in_cart.Message ,
                    total_price=Decimal(walet_pay),
                    created_at=datetime.datetime.now()
                )            
        new_order.save()

        if walet != None :
            old_walet = walet.balance 
            new_walet = old_walet + Decimal(walet_pay)
            walet.balance = new_walet
            walet.save()
        else :
            new_walets = SellerWallet(seller = user_seler , balance = Decimal(walet_pay))
            new_walets.save()    

        
        product_in_cart.delete()

        return render(request=request , template_name="resualt_pay.html" , context={"message":"پرداخت با موفقیت انجام شد ✔" , "card_pan":card_pan , "ref_id":ref_id , "price":"{:,}".format(int(pay))})
    else:
        return render(request=request , template_name="resualt_pay.html" , context={"message":"پرداخت انجام نشد ❌"} )
        


def product_list(request, filters):
    user_at = Userauths().StateLog(request=request)
    # دریافت تمامی محصولات با فیلتر
    all_products = Products.objects.filter(Q(Name_Product__icontains=filters) | Q(selected_options__icontains=filters)).order_by('id')  # جستجو بر اساس فیلتر

    # مقداردهی صفحه‌بندی
    paginator = Paginator(all_products, 12)  # تعداد محصولات در هر صفحه (10)

    # دریافت شماره صفحه از پارامترهای URL
    page_number = request.GET.get('page')

    # دریافت صفحه جاری
    page_obj = paginator.get_page(page_number)

    # محاسبه قیمت نهایی با قالب‌بندی سه‌رقمی
    for product in page_obj:
        discounts = product.Discount
        discount_price = (int(discounts) / 100) * int(product.Price)
        final_price = int(product.Price) - discount_price
        # قالب‌بندی سه‌رقمی
        product.formatted_final_price = "{:,}".format(int(final_price))
        product.formatted_original_price = "{:,}".format(int(product.Price))

      

    # ارسال داده‌ها به قالب
    return render(request, 'filter_product.html', {'products': page_obj , "title" : filters , "user" : user_at})


def product_list_all(request):
    user_at = Userauths().StateLog(request=request)
    # دریافت تمامی محصولات با فیلتر
    all_products = Products.objects.all().order_by('-id')  # جستجو بر اساس فیلتر

    # مقداردهی صفحه‌بندی
    paginator = Paginator(all_products, 12)  # تعداد محصولات در هر صفحه (10)

    # دریافت شماره صفحه از پارامترهای URL
    page_number = request.GET.get('page')

    # دریافت صفحه جاری
    page_obj = paginator.get_page(page_number)

    # محاسبه قیمت نهایی با قالب‌بندی سه‌رقمی
    for product in page_obj:
        discounts = product.Discount
        discount_price = (int(discounts) / 100) * int(product.Price)
        final_price = int(product.Price) - discount_price
        # قالب‌بندی سه‌رقمی
        product.formatted_final_price = "{:,}".format(int(final_price))
        product.formatted_original_price = "{:,}".format(int(product.Price))

      

    # ارسال داده‌ها به قالب
    return render(request, 'filter_product.html', {'products': page_obj , "title" : "همه محصولات", "user" : user_at})    

def send_sms( message):
    conn = http.client.HTTPSConnection("api.sms.ir")
    payload = json.dumps({
        "lineNumber": 30007487130754,
        "messageTexts": [
          message,  
        ],
        "mobiles": [
          "09035404612",
        ],
        "senddatetime": None
      })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'X-API-KEY': 'YtEKfmrrr5Fxpyl8CQYX8nqWaKDYWMD24SSnsq0eXNSVRiNZ'
      }
    conn.request("POST", "/v1/send/likeToLike", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return(data.decode("utf-8"))


def Account_settlement(request):
    walet = SellerWallet.objects.filter(seller=request.user).first()
    user = User.objects.filter(id=request.user.id).first()
    if walet.balance == 0 :

        if not walet or not user:
            return JsonResponse({"success": False, "message": "اطلاعات کاربر یا کیف پول یافت نشد."})

        message = f"فروشنده سایت ، آقا/خانم : {user.first_name} درخواست تسویه حساب به مبلغ {"{:,}".format(int(walet.balance))} تومان را دارند ."
        try:
            resualt = send_sms(message)
            response_dict = json.loads(resualt)
            status = response_dict["status"]
            ms = response_dict["message"]
            

            if status == 1:
                walet.balance = 0
                walet.save()
                return JsonResponse({"success": True, "message": "درخواست تسویه حساب شما تایید و برای مدیر ارسال شد . ظرف 24 ساعت آینده به حساب شما واریز میشود"})
            else:
                return JsonResponse({"success": False, "message": "خطایی رخ داد لطفا بعدا تلاش کنید"})
            
        except Exception as e:
            return JsonResponse({"success": False, "message": f"خطایی رخ داد: {str(e)}"})

    else:
        return JsonResponse({"success": False, "message": "مبلغ کیف پول شما کمتر از حد مجاز برای تسویه است"})









