from django.urls import path
from . import views

app_name = "manager_app"

urlpatterns = [
    path('',views.index_page,name="index_page"),
    path("category",views.category_page,name="category_page" ),
    path('category/delete/<category_id>/',views.delete_category,name="delete_category"),
    path('category/subcategory/<category_id>/',views.sub_category,name="sub_category"),
    path('category/subcategory/<category_id>/delete/<sub_category_id>/',views.delete_sub_category,name="delete_sub_category"),


    path("founditem/add/",views.add_found_item_page,name="add_found_item_page"),


    
]