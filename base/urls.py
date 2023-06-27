from django.contrib import admin
from django.urls import path
from parking import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.main, name='main'),  # главная страница
    path('create_transaction', views.create_transaction, name='create_transaction'),  
    path('delete_transaction/<int:id>/', views.delete_transaction, name='delete_transaction'), 
    path('edit_transaction/<int:pk>/', views.edit_transaction, name='edit_transaction'),
]
