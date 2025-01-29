from django.shortcuts import render
from datetime import datetime
import datetime
from .forms import Comment_main
from .Userauth import Userauths
from django.contrib.auth.models import User
from .models import Comment , Information , Adress , Manage_Contact
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import logout
import jdatetime
from Shop.models import Comment as comm 
from Shop.models import Favorite , Products , Orders
from datetime import timedelta
from django.utils import timezone



# Create your views here.

def main_page (request):
    user_at=Userauths().StateLog(request=request)
    form=Comment_main()
    latest_comments = Comment.objects.filter(Approved=True).order_by('-id')[:4]
    census=Census(request)
    if user_at["State"] == True :

        
        
       
        status_info = False
        info = Information.objects.filter(user = request.user.id).first()
        adresss = Adress.objects.filter(user = request.user.id).first()

        if info == None or adresss == None :
            return render(request=request , template_name="main_page.html" , context={"form":form ,"statuss":status_info, "comment":latest_comments , "user" : user_at , "member":census["member"] , "comment_number":census["comment"]})
        else :
            status_info = True
            return render(request=request , template_name="main_page.html" , context={"form":form ,"statuss":status_info, "comment":latest_comments , "user" : user_at , "member":census["member"] , "comment_number":census["comment"]})
    else :
        return render(request=request , template_name="main_page.html" , context={"form":form , "comment":latest_comments , "user" : user_at , "member":census["member"] , "comment_number":census["comment"]})



def panel(request):

    user_at=Userauths().StateLog(request=request)
    
    if user_at["State"] == True :

        info=Information.objects.filter(user_id = user_at["User"].id).first()
        adresss=Adress.objects.filter(user = user_at["User"].id).first()
        fave=Favorite.objects.filter(user_id = request.user.id).all()

        

        
        products=[]
        for item in fave:
            product=Products.objects.filter(id = item.Product_id).first()
            discounts=product.Discount
            discount_price=(int(discounts) / 100) * int(product.Price)
            final_price=int(product.Price) - discount_price
            products.append({
                "id":product.id,
                "Img" : product.Img,
                "product_name" : product.Name_Product,
                "discount":product.Discount,
                "final_price":"{:,}".format(int(final_price)),
                "price":"{:,}".format(int(product.Price))
            })



        comment_pruduct=comm.objects.filter(User = user_at["User"].id).all()
        coment_int=len(comment_pruduct)

        pay = []

        one_month_ago = timezone.now() - timedelta(days=20)

        payss = Orders.objects.filter(user = request.user.id , created_at__gte = one_month_ago).all()
        
        for item in payss:
            product=Products.objects.filter(id = item.product.id).first()

            pay.append({
                "product_name" : product.Name_Product,
                "quantity" : item.quantity,
                "total_price" : "{:,}".format(int(item.total_price)),
                "ref_id" : item.ref_id

            })

        
        

                
        if info == None and adresss == None:  

            info_bool=False
            adres_bool=False
        
            name=user_at["User"].first_name
            return render(request=request , template_name="panel.html" , context={"user":user_at , "pay":pay , "username" : name,  "info_bool": info_bool , "comm":coment_int , "product":products , "adres_bool":adres_bool})
    
        elif info != None and adresss == None:

            info_bool=True
            adres_bool=False
            
            name=user_at["User"].first_name
            info_date=convert_gregorian_to_jalali(info.Birthday)
        
            return render(request=request , template_name="panel.html" , context={"user":user_at  , "pay":pay , "username" : name ,  "info_bool": info_bool , "info" : info , "date":info_date , "comm":coment_int , "addres":adresss , "products":products , "adres_bool":adres_bool})

        elif info == None and adresss != None:

            info_bool=False
            adres_bool=True
            
            name=user_at["User"].first_name
            
        
            return render(request=request , template_name="panel.html" , context={"user":user_at  , "pay":pay  , "username" : name,  "info_bool": info_bool , "info" : info , "comm":coment_int , "addres":adresss , "products":products , "adres_bool":adres_bool})
        
        
        else:
            
            adres_bool=True
            info_bool=True
            
            name=user_at["User"].first_name
            info_date=convert_gregorian_to_jalali(info.Birthday)
            
            return render(request=request , template_name="panel.html" , context={"user":user_at  , "pay":pay , "username" : name ,  "info_bool": info_bool , "info" : info , "date":info_date , "comm":coment_int , "addres":adresss , "products":products , "adres_bool":adres_bool})
    
    else:
            
        return HttpResponseRedirect("/auth")
        

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

def convert_jalali_to_gregorian(year , month , day):

    try:

        gregorian_date = jdatetime.date(year , month , day).togregorian()
        return gregorian_date.strftime('%Y-%m-%d')
    
    except Exception as e:
        print(f"Error converting date: {e}")
        return None


def Save_Comment(request):
    if request.method == "POST":
        form = Comment_main(request.POST)
        user_at=Userauths().StateLog(request=request)
        if user_at["State"] == True:
            if form.is_valid():
                new_comment = Comment(
                    Full_name=form.data["Full_name"],
                    Comment_message=form.data["Message"],
                    Phone=form.data["Phone"],
                    Approved=False,
                    Created_at=datetime.datetime.now()
                )            
                new_comment.save()
                return HttpResponse("true")
            else:
                return HttpResponse("form is not valid")
        else:
           
            return HttpResponse("false")
        

def Save_information(request):
     
     
     if request.method == "POST":
        user_at=Userauths().StateLog(request=request)
        info=Information.objects.filter(user_id = user_at["User"].id)
        
        if len(info) == 0:
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            birthday=request.POST.get("birthday")
            date_jdate = jdatetime.datetime.strptime(birthday , "%Y-%m-%d")
            user_instance = User.objects.get(id=user_at["User"].id)
            date_object = convert_jalali_to_gregorian(date_jdate.year , date_jdate.month , date_jdate.day)
           

            info_all_email=Information.objects.filter(Email = email).exists()
            info_all_phone=Information.objects.filter(Phone = phone).exists()

            if info_all_email :
                return HttpResponse("email exist")
            elif info_all_phone :
                return HttpResponse("phone exist")
            elif len(phone)!= 11:
                return HttpResponse("phone erore")
            elif not phone.isnumeric():
                return HttpResponse("phone numeric")
            else:   
                information = Information(
                    user=user_instance,  
                    Phone=phone,
                    Email=email,
                    Birthday=date_object
                    )                  
                information.save()
                return HttpResponse("true")
        else:
            return HttpResponse("exist")

def Save_Adress(request):
     
    if request.method == "POST":
        user_at=Userauths().StateLog(request=request)
        adress=request.POST.get("adress")
        vahed=request.POST.get("vahed")
        plak=request.POST.get("plak")
        postcode=request.POST.get("post-code")
        if vahed.isnumeric() and plak.isnumeric() and postcode.isnumeric():
            if len(postcode)==10:
                full_adress=f"{adress} / واحد : {vahed} / پلاک : {plak} / کد پستی : {postcode}"
                user_instance = User.objects.get(id=user_at["User"].id)
                Adresses = Adress(
                        user=user_instance,
                        adress=full_adress,   
                        )                  
                Adresses.save()
                return HttpResponse("true")
            else:
                return HttpResponse("postcode not 10")
        else:
            return HttpResponse("not numeric")


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/")


def Census(request):
    member=User.objects.all()
    comment=Comment.objects.all()
    user_number=len(member)
    comment_number=len(comment)
    dic={"member":user_number , "comment":comment_number}
    return dic

def Save_message(request):
    try:
        user = request.user
        title = request.POST.get("title-message")
        message = request.POST.get("text-message")
        created_at = datetime.date.today()

        message_contact = Manage_Contact(user = user , Title = title , Caption = message , Created_at = created_at)
        message_contact.save()
        return HttpResponse("true")
        
    
    except:

        return HttpResponse("false")