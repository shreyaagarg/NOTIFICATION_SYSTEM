from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, response
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from DepUpdate.models import course
from Notification.models import Notif
from Notification.serializers import NotifSerializer
from Notification_system import settings
from accounts.models import Faculty, Student
from .forms import NotificationForm
import nexmo

def send_message(sender , reciever, message):

    client = nexmo.Client(key=settings.KEY , secret=settings.SECRET)
    string = str(message)
    response = client.send_message({'from': sender, 'to': reciever, 'text': string})
    response = response['messages'][0]

    if response['status'] == '0':
        return "SENT"
    else:
        return "ERROR"

def is_member_faculty(user):
    return user.groups.filter(name='Faculty').exists()

def is_member_student(user):
    return not user.groups.filter(name='Faculty').exists()


@user_passes_test(is_member_faculty, login_url='/accounts/FacLogIn')
@login_required(login_url='/accounts/FacLogIn')
def FacHome(request , fac_id):
    user = get_object_or_404(User , pk=fac_id)
    object = Faculty.objects.get(user=user)
    return render(request, 'Notification/FacHome.html' , { 'object': object , 'faculty':user})


@user_passes_test(is_member_faculty,login_url='/accounts/FacLogIn')
@login_required(login_url='/accounts/FacLogIn')
def create_notif(request , fac_id):

    if request.method == "POST":

        group = Group.objects.get(id=request.POST['uploaded_for'])
        users = User.objects.filter(groups=group)
        keys = []
        values = []
        sender = Faculty.objects.get(user=request.user).Contact_Number
        string = request.POST['title'] + " "
        new_object = Notif(
            title=request.POST['title'] ,
            uploaded_by=request.user,
            related_course=course.objects.get(id=request.POST['related_course']),
            uploaded_for=group
        )

        new_object.save()
        for user in users:
            receiver = Student.objects.get(Student_ID=user.username).Contact_Number
            keys.append(str(user.username))
            values.append(send_message(str(sender),
                                       str(receiver) ,
                                       request.POST['title'])
                          )

        zipped = list(zip(keys,values))
        new_object.status = str(zipped)
        new_object.save()


        return render(request, 'Notification/NewNotifCreate.html' , { 'status' : zipped })

    else:
        form = NotificationForm()

    return render(request , 'Notification/NotifCreate.html' , {'form':form})


@user_passes_test(is_member_student, login_url='/accounts/StuLogIn')
@login_required(login_url='/accounts/StuLogIn')
def StuHome(request , stu_id):
    user = get_object_or_404(User , pk=stu_id)
    object = Student.objects.get(user=user)
    return render(request, 'Notification/StuHome.html' , { 'object': object , 'faculty':user})


@user_passes_test(is_member_student, login_url='/accounts/StuLogIn')
@login_required(login_url='/accounts/StuLogIn')
def show_stu_notif(request ,stu_id):

    user = get_object_or_404(User, pk=stu_id)
    all_groups = user.groups.all()

    list_of_notifications = []
    for group in all_groups:
        try:
            list_of_notifications += Notif.objects.filter(uploaded_for=group)
        except ObjectDoesNotExist:
            pass
    return render(request, 'Notification/show_stu_notif.html', {"notifications": list_of_notifications})


class NotifList(APIView):

    def get(self, request):

        notifications = Notif.objects.all()
        serializer = NotifSerializer(notifications, many=True)
        return Response(serializer.data)

    def post(self):
        pass






