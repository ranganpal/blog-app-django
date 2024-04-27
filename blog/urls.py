from django.urls import path
from .views import *

urlpatterns = [
    path('', signup, name='signup'),
    path('signup/', signup, name='signup'),
    path('signedup/', signedup, name='signedup'),
    path('signin/', signin, name='signin'),
    path('signedin/', signedin, name='signedin'),
    path('home/', no_account, name='no_account'),
    path('account/', no_account, name='no_account'),
    path('home/<int:user_id>', home, name='home'),
    path('account/<int:user_id>', account, name='account'),
    path('delete/<int:user_id>', delete, name='delete'),
    path('update/<int:user_id>', update, name='update'),
    path('logout/<int:user_id>', logout, name='logout'),
    path('my-posts/<int:user_id>', my_posts, name='my-posts'),
    path('add-post/<int:user_id>', add_post, name='add-post'),
    path('create-post/<int:user_id>', create_post, name='create-post'),
    path('read-post/<int:post_id>', read_post, name='read-post'),
    path('read-my-post/<int:post_id>', read_my_post, name='read-my-post'),
    path('edit-post/<int:post_id>', edit_post, name='edit-post'),
    path('update-post/<int:post_id>', update_post, name='create-post'),
    path('delete-post/<int:post_id>', delete_post, name='create-post'),
]