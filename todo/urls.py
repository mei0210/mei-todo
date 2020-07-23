from django.urls import path
# from .views import todo # couese-33
from .views import Todolist, TodoDetail, TodoCreate, TodoDelete, TodoUpdate# couese-36 # couese-37  

urlpatterns = [
    # path('a/', todo), # couese-33
    path('list/', Todolist.as_view(), name='list'), # couese-36
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'), # couese-37 
    path('create/', TodoCreate.as_view(), name='create'),   
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'), # couese-37 
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'), # couese-37 
]
