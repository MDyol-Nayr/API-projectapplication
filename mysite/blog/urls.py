from django.urls import path
from .views import blog_list,blog_detail,blog_delete,blog_create,blog_update,like_post,dislike_post
urlpatterns = [
    path('',blog_list),
    path('create/',blog_create),
    path('<id>/',blog_detail),
    path('<id>/delete/',blog_delete), 
    path('<id>/update/',blog_update), 
    path('<id>/like/', like_post, name='like_post'),  
    path('<id>/dislike/', dislike_post),
    
    
]