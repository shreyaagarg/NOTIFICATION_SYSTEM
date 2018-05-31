from django.contrib.auth.models import Group
from django.forms import ModelForm
from .models import Notif


class NotificationForm(ModelForm):

    class Meta:
        model = Notif
        fields = ['title' , 'related_course' , 'uploaded_for']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['related_course'].widget.attrs['class'] = 'form-control dropdown-toggle'
        self.fields['uploaded_for'].widget.attrs['class'] = 'form-control dropdown-toggle'
        self.fields['uploaded_for'].queryset = Group.objects.exclude(name="Faculty")