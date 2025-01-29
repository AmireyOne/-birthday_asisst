from django.urls import path 
from . import views


urlpatterns = [
    path('shop_page', views.shop_page , name="صفحه فروشگاه" ),
    path('product/<int:ID>', views.product_page , name="صفحه محصول" ),
    path('get-comments/<int:ID>/', views.get_comments, name='دریافت نظرات'),
    path('add-comments', views.add_comment, name='افزودن نظرات'),
    path('add-question', views.add_question, name='افزودن سوال'),
    path('comment/<int:comment_id>/<str:action>/', views.toggle_like, name='toggle_like'),
    path('add-favorite', views.add_favorite, name='افزودن به علاقه مندی ها'),
    path('managecart', views.ManageCart, name='مدیریت سبد خرید'),
    path('cart/count', views.cart_item_count, name='تعداد کالا در سبد خرید'),
    path('cart_page', views.Cart_page, name='سبد خرید'),
    path('deletecart', views.Deletecart, name=' حذف سبد خرید'),
    path('pay/<str:pay>/<str:product_id>/<str:seler_id>/<str:number>/<str:cart_id>', views.pays, name=' پرداخت'),
    path('filters/<str:filters>', views.product_list, name='product_list'),
    path('all_product', views.product_list_all, name='product_list_all'),
    path('resualt_pay/<str:pay>/<str:product_id>/<str:seler_id>/<str:number>/<str:cart_id>', views.resualt_pay, name=' نتیجه پرداخت'),
    path('Account_settlement', views.Account_settlement, name='تسویه'),

    
]