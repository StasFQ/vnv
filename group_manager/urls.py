from django.urls import path

from group_manager.views import group_list, add_group, edit_group, delete_group

urlpatterns = [
    path('', group_list, name='group_list'),
    path('add/', add_group, name='add_group'),
    path('<int:id>/edit/', edit_group, name='edit_group'),
    path('<int:group_id>/delete/', delete_group, name='delete_group')
]
