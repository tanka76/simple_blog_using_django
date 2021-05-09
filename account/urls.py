from django.urls import path
from theblog import views
from .views import Userreg,Userprofile,Passwordchangeview
#from django.contrib.auth import views as auth_views
from .views import password_success,Showprofileview,Editprofileview,Createprofileview

urlpatterns = [

    path('register/', Userreg.as_view(), name="register"),
    path('profile/', Userprofile.as_view(), name="edit_profile"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_passowrd.html')),
    path('password/', Passwordchangeview.as_view(template_name='registration/change_passowrd.html'), name="change_password"),
    path('password_success/',password_success, name="password_success"),
    path('<int:pk>profile/', Showprofileview.as_view(), name="show_profile"),
    path('<int:pk>profile_page/', Editprofileview.as_view(), name="edit_profile"),
    path('create_profile_page/', Createprofileview.as_view(), name="create_profile_page"),
]
