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
    path('room_display_review',room_display_review,name='room_display_review'),
    path("handle_review_room",handle_review_room,name="handle_review_room"),
    path("handle_team/<session_no>/<room_no>",handle_team,name="handle_team"),
    path("marks/<session_no>/<room_no>/<team_name>",post_marks,name="marks")
]