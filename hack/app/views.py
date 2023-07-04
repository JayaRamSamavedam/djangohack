from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Attendence,Student,Session,Review,Room,Team
from .forms import AttendanceForm

from django.urls import reverse

def signin(request):
    # lg = login.objects.all().values()
    if request.method == 'POST':
        username = request.POST.get('uname')
        pass1 = request.POST.get('pass')
        user = authenticate(username=username, password=pass1)
        print(user)
        if user is not None:
            login(request, user)
            return render(request, 'sucess.html',{})
        else:
            # messages.error(request, "wrong credentials"
            return redirect('login')
    return render(request, "login.html", {})


def home(request):
    return render(request,"base.html",{})


def room_display(request):
    context={}
    context["rooms"]=Room.objects.all()
    context["sessions"]=Session.objects.all()
    return render(request,"rooms.html",context)


def handleroom(request):
    a=Room.objects.get(room_no=(request.POST["room"]))
    b=Student.objects.filter(room=a)
    context={}
    context["room"]=a
    context["students"]=b
    session=Session.objects.get(session_no=int(request.POST['session']))
    
    if session.Attendence == True:
        context["session"]=session
        return redirect('attendance/'+str(a)+'/'+str(request.POST['session']))
    else:
        return HttpResponse("Attendence not opened")


def post_attendance(request, room_no, session_no):
    room = Room.objects.get(room_no=room_no)
    session = Session.objects.get(session_no=session_no, Attendence=True)

    if request.method == 'POST':
        form = AttendanceForm(request.POST, session_id=session_no, room_no=room_no)
        if form.is_valid():
            form.save_attendance(session)
            return HttpResponse('attendance_success')  # Redirect to a success page
    else:
        form = AttendanceForm(session_id=session.session_no, room_no=room_no)

    return render(request, 'post_attendence.html', {'form': form})

def room_display_review(request):
    context={}
    context["rooms"]=Room.objects.all()
    context["sessions"]=Session.objects.all()
    return render(request,"rooms_review.html",context)


def handle_review_room(request):
    a=Room.objects.get(room_no=(request.POST["room"]))
    b=Student.objects.filter(room=a)
    context={}
    context["room"]=a
    context["students"]=b
    context["teams"]=Team.objects.filter(room=a)
    session=Session.objects.get(session_no=int(request.POST['session']))
    
    if session.Attendence == True:
        context["session"]=session
        return render(request,'teams.html',context)
    else:
        return HttpResponse("session not activated")

def handle_team(request, session_no, room_no):
    team_id = request.POST.get('team')
    redirect_url = reverse('marks', args=(session_no, room_no, team_id))
    return redirect(redirect_url)


def post_marks(request,session_no,room_no,team_name):
    r = Room.objects.get(room_no=room_no)
    session = Session.objects.get(session_no=session_no, Attendence=True)
    team=Team.objects.get(team_name=team_name)
    a=Student.objects.filter(team=team)
    context={}
    context["students"]=a
    if request.method == 'POST':
        for i in a:
            review_marks=request.POST[str(i.id)]
            Review.objects.update_or_create(
                student=i,
                session=session,
                review_no=session.session_no,
                room=r,
                defaults={'review_marks': review_marks}
            )
        return HttpResponse('attendance_success')  # Redirect to a success page
    return render(request, 'post_marks.html',context=context)
