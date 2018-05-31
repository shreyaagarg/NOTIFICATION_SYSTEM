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