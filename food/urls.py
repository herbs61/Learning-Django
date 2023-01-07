from . import views
from django.urls import path

app_name = 'food'
urlpatterns = [
    path('',views.index,name='index'),
      #to be able to type the id number and get the 
    # particular food details
    path('<int:item_id>/',views.detail,name='detail'),
    path('item/',views.item,name='item'),
    #Add items
  path('add/',views.create_item,name='create_item'),
  #Edit
 path('update/<int:id>/',views.update_item,name='update_item'),
  #Delete
 path('delete/<int:id>/',views.delete_item,name='delete_item'),
]