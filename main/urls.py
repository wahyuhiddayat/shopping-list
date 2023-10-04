from django.urls import path
from main.views import show_main
from main.views import create_product
from main.views import show_xml
from main.views import register 
from main.views import login_user 
from main.views import logout_user
from main.views import edit_product
from main.views import delete_product
from main.views import add_product_ajax
from main.views import get_product_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'), 
    path('register/', register, name='register'), 
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('delete/<int:id>', delete_product, name='delete_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax')
]