
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('update_password/', views.update_password, name='update_password'),
    path('product/', views.product, name='product'),
    path('product/<int:pk>', views.product, name='product'),
    #path('category/<str:foo>', views.category, name='category'),
    path('category/<str:category_name>/', views.category_view, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
]
