from django.urls import path
from .views import (

    dynamic_view,
    delete_view,
    product_create_view,
    product_details
    
)

urlpatterns = [

    path('details/', product_details, name='product_details'),
    path('dynamic/<int:my>/', dynamic_view, name='dynamic_details'),
    path('dynamic/<int:my>/delete/', delete_view, name='delete'),
    path('create/', product_create_view, name='create'),   
]
