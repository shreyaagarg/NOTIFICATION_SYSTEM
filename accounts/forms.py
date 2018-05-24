from django import forms
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