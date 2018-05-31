from django import forms
<<<<<<< HEAD
from .models import Student
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class SignUp_student_form(forms.ModelForm):

    username=forms.CharField(label='Username', max_length=30)
    email=forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)',
                                widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1=self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError('Passwords do not match.')

    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the  underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')


    
=======
from .models import Student,Faculty

class Signup_student_form(forms.ModelForm ):

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:

        fields = ['Name' , 'Student_ID' , 'DOB', 'Branch' , 'Year_Of_Study' ,'Semester', 'Contact_Number','email',
                  'password']
        model = Student

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Branch'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
        self.fields['Year_Of_Study'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
        self.fields['Semester'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
        self.fields['Contact_Number'].widget.attrs['class'] = 'form-control'


class Signup_faculty_form(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput() , )

    class Meta:
        model = Faculty
        fields = ['Name' , 'Faculty_ID' , 'Department',  'Designation' , 'Qualification'  , 'Contact_Number',
                  'email','password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['Department'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
        self.fields['Designation'].widget.attrs['class'] = 'form-control btn btn-default dropdown-toggle'
        self.fields['Contact_Number'].widget.attrs['class'] = 'form-control'
>>>>>>> be5dcb8f5f1fd5814428c6495c12182a11069597
