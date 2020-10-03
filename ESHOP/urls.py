"""ESHOP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from Product import views as Product_view
from UserManagement import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Product_view.ShowProducts),
    path('account/',include('django.contrib.auth.urls')),
    path('signup/',user_views.Registerpage),
    path('profile/',user_views.CreateProfile),
    path('profileview/',user_views.ViewProfile),
    path('<int:product_id>',Product_view.ProductDetails),
    path('cart/', Product_view.ViewCart, name='cart'),
    path('updatecart/<int:product_id>', Product_view.AddtoCart, name='update-cart'),
    path('deletefromcart/<int:product_id>', Product_view.RemovefromCart, name='delete-from-cart'),
    path('orderproduct/<int:product_id>', Product_view.CreateOrder, name='order-product'),
    path('orders/', Product_view.UserOrder),
    path('review/<int:product_id>',Product_view.ProductReview, name='review'),
    path('payment/<int:product_id>', Product_view.Payment, name='payment'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
