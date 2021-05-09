from django.urls import path
from theblog import views
from .views import Home, ArticleDetail, Addpostview, Updatepostview, Deletepostview, Addcategoryview, Categoryview


urlpatterns = [

    path('home', Home.as_view(), name="home"),
    path('detail/<int:pk>', ArticleDetail.as_view(), name="article_detail"),
    path('addblog/', Addpostview.as_view(), name="add_post"),
    path('edit/<int:pk>', Updatepostview.as_view(), name="update_post"),
    path('delete/<int:pk>', Deletepostview.as_view(), name="delete_post"),
    path('addcategory/', Addcategoryview.as_view(), name="add_category"),
    path('category/<str:cats>', Categoryview, name="category"),
    
]