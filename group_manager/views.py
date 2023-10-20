from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from group_manager.forms import GroupForm, GroupEditForm
from group_manager.models import Group


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group_manager/group_list.html', {'groups': groups})


def add_group(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm()
    return render(request, 'group_manager/add_group.html', {'form': form})


def edit_group(request, id):
    group = get_object_or_404(Group, pk=id)
    if request.method == 'POST':
        form = GroupEditForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')
    else:
        form = GroupForm(instance=group)
    return render(request, 'group_manager/edit_group.html', {'form': form, 'group': group})


def delete_group(request, group_id):
    group = get_object_or_404(Group, pk=group_id)
    user = request.user

    if request.method == 'POST':
        if user not in group.members.all():
            group.delete()
            return redirect('group_list')
        else:
            error_message = "You cannot delete the group as you are a member of it."
            return render(request, 'group_manager/delete_group.html', {'group': group, 'error_message': error_message})

    return render(request, 'group_manager/delete_group.html', {'group': group})
