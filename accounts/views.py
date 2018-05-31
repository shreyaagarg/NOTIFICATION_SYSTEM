<<<<<<< HEAD
from .forms import SignUp_student_form
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

def StuSignUpView(request):
    if request.method == 'POST':
        form = SignUp_student_form(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
    form = SignUp_student_form()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html',variables)
=======
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Signup_student_form, Signup_faculty_form
from DepUpdate.models import  AuthFaculty


def StuSignUpView(request):

    if request.method == "POST":
        form = Signup_student_form(request.POST)
        values = request.POST

        instance = form.save(commit=False)
        username = values['Student_ID']
        password = values.get('password',None)
        email = values['email']
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        my_group = Group.objects.get(name="Students")
        user.groups.add(my_group)
        instance.user = user
        instance.save()
        user = authenticate(username=username,password=password)
        login(request,user)
    return redirect('Notification:StuHome', stu_id=request.user.id)


def StuLogInView(request):

    if request.method == "POST":
        user = form.get_user()
        login(request,user)
        return redirect('Notification:StuHome' , stu_id=request.user.id)
    else:
        error_message = ""

    return render(request , 'accounts/StuLogIn.html' , {'form':form, 'error_message':error_message})


def FacSignUpView(request):
    if request.method == "POST":
        form = Signup_faculty_form(request.POST)
        try:
            values = request.POST
            object = AuthFaculty.objects.get(FID = values['Faculty_ID'])

            if ( values['Faculty_ID'] , values['Name'] , values['Department'] , values['Designation'] ) == ( object.FID , object.Name , object.Department , object.Designation ):

                if form.is_valid():

                    instance = form.save(commit=False)
                    username = values['Faculty_ID']
                    password = values.get('password',None)
                    email = values['email']

                    user = User.objects.create_user(username=username, email=email)
                    user.set_password(password)
                    user.save()
                    my_group = Group.objects.get(name="Faculty")
                    user.groups.add(my_group)
                    instance.user = user
                    instance.save()

                    user = authenticate(username=username,password=password)
                    login(request,user)

                    return redirect('Notification:FacHome', fac_id=user.id)


            else:
                error_messages = """Your are not an authenticated member of this institution.
                Kindly contact your respective department"""
                return render(request, 'accounts/FacSignUp.html', {'form': form , 'error_messages' : error_messages})

        except Exception as e:
            print(e)
            error_messages = """Your are not an authenticated member of this institution.
                Kindly contact your respective department"""
            return render(request, 'accounts/FacSignUp.html', {'form': form,  'error_messages' : error_messages})

    else:
        form = Signup_faculty_form()

    return render(request , 'accounts/FacSignUp.html' , {'form' : form})


def FacLogInView(request):
    if request.method == "POST":

        form = AuthenticationForm(data=request.POST)
        error_message = "Invalid Credentials"
        if form.is_valid():

            user = form.get_user()
            login(request,user)
            return redirect('Notification:FacHome' , fac_id= request.user.id)
    else:
        error_message = ""
        form = AuthenticationForm()
    return render(request , 'accounts/FacLogIn.html' , {'form':form,'error_message':error_message})


@login_required(login_url='/accounts/StuSignUp')
def Proflogout(request):

    logout(request)

    return redirect('index')

@login_required(login_url='/accounts/StuLogIn')
def select(request):

    try:
        group = request.user.groups.get(name='Faculty')
        return redirect('Notification:FacHome',fac_id=request.user.id)
    except:
        return redirect('Notification:StuHome', stu_id=request.user.id)
>>>>>>> be5dcb8f5f1fd5814428c6495c12182a11069597
