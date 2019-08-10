from django import  forms
from . import models
from groups.models import Group


class PostForm(forms.ModelForm):
    class Meta:
        fields = ("message", "groups")
        model = models.Post

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        if user is not None:
            self.fields["groups"].queryset = Group.objects.filter(members=user)