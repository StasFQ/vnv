from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from user_manager.forms import UserForm, UserEditForm


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_manager/user_list.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_manager/add_user.html', {'form': form})


def edit_user(request, id):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_manager/user_edit.html', {'form': form, 'user': user})


def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'user_manager/user_confirm_delete.html', {'user': user})
