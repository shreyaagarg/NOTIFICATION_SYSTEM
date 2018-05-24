from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

branches = [
        ("aero", "Aerospace"),
        ("civil", "Civil"),
        ("cse", "Computer Science"),
        ("ece", "Electronics & Communication"),
        ("elec", "Electrical"),
        ("mech", "Mechanical"),
        ("meta", "Materials & Metallurgical"),
        ("prod", "Production & Industrial"),
    ]

class Student(models.Model):


    years = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
    ]
    sem = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5",5),
        ("6",6),
        ("7",7),
        ("8",8),
    ]

    Name = models.CharField(max_length=50)
    Student_ID = models.CharField(max_length=8, blank=False, unique=True)
    DOB = models.DateField(verbose_name="Date Of Birth" )
    Branch = models.CharField(max_length=4, choices=branches, default="aero")
    Year_Of_Study = models.CharField(max_length=1, choices=years, default="1")
    Semester=models.CharField(max_length=1,choices=sem,default="1")
    Contact_Number = PhoneNumberField(blank=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE , default=None)

    def __str__(self):
        return self.Student_ID + " : " + self.Name

class Faculty(models.Model):

    designations = [  ("prof","Professor"),
                      ("asso" , "Associate Professor"),
                      ("assi" , "Assistant Professor"),
                      ("inst" , "Instructor")
    ]

    Name = models.CharField(max_length=50)
    Faculty_ID = models.CharField(max_length=8, blank=False, unique=True)
    Department =  models.CharField(max_length=4, choices=branches, default="aero")
    Contact_Number = PhoneNumberField(blank=False)
    Designation = models.CharField(max_length=4 , choices=designations , default="prof")
    Qualification = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE , default=None)

    def __str__(self):
        return self.Faculty_ID + " : " + self.Name

class Courses(models.Model):
    Course_Id=models.CharField(max_length=8,blank=False,unique=True)
    Course_Name=models.CharField(max_length=250)

class Semester_Course(models.Model):
    Dept=models.CharField(max_length=100)
    sem=models.CharField(max_length=10)
    Course_Id=models.CharField(max_length=8)



