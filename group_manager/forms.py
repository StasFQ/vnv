from django import forms

from group_manager.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
