from django.urls import path

from .views import *
urlpatterns = [
    # path("att",att,name="att"),
    # path("handle",handle_att,name="handle"),
    # path("marks",post_marks,name="marks"),
    path("login",signin,name="login"),
    path("home",home,name="home"),
    path("room/<room_no>",handleroom,name="room"),
    path("room_display",room_display,name="room_display"),
    path("handle_room",handleroom,name="handle_room"),
    path('attendance/<room_no>/<session_no>', post_attendance, name='post_attendence'),
]