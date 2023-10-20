from django.urls import path
#
from user_manager.views import user_list, add_user, edit_user, delete_user

#
urlpatterns = [
    path('', user_list, name='user_list'),
    path('add/', add_user, name='add_user'),
    path('<int:id>/edit/', edit_user, name='edit_user'),
    path('user/<int:user_id>/delete/', delete_user, name='delete_user'),
 ]
