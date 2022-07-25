from django.urls import path,include
from app import views



urlpatterns = [
    
    path('home/',views.index, name='index'),
    path('index2/',views.index2, name='index2'),
    path('',views.index3, name='index3'),
    path('emp/',views.emp, name='emp'),
    path('empproduct/',views.empproduct, name='empproduct'),
    path('product/',views.product, name='product'),
    path('addproduct/',views.addproduct,name='addproduct'),
    path('editproduct/',views.editproduct, name='editproduct'),
    path('productreport/',views.productreport, name='productreport'),
    path('empreport/',views.empreport, name='empreport'),
    path('emphome/',views.emphome, name='emphome'),
    path('role/',views.role, name='role'),
    path('rolelist/',views.rolelist, name='rolelist'),
    path('sign/',views.sign, name='sign'),
    path('forget/',views.forget, name='forget'),
]