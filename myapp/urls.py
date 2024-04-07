from django.urls import path, include
from . import views 





urlpatterns = [
    path('x', views.index, name='index'),
    path('BS_CDN_link/', views.bootstrap_page_cdn_link, name='bootstrap_page_cdn_link'),  # Add this line
    path('BS_installed/', views.BS_Installed, name='bootstrap page'),  # Add this line
    #----------------Website
    path('home_page/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    #----------------DB acesss
    path('add_products/',views.ProductsAdd,name='Add products' ),
    path('all_products/', views.all_products, name='all_products'),
    path('update_product/<int:id>/', views.ProductUpdate, name='product_update'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),

]
