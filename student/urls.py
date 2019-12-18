from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # URL for Authentication
    path('user/login/', views.loginView, name='login'),
    path('user/register', views.register, name='register'),
    # URL for Timetable
    path('timetable', views.timetable, name="timetable"),
    path('timetable/save', views.timetableSave, name="ttSave"),
    # URL for Attendance 
    path('attendace', views.attendance, name='attendance'),
    # URL for Task List
    path('tasks', views.tasks, name="tasks"),
    path('tasks/new', views.newTask, name='newTask'),
    path('tasks/edit/<int:pk>', views.editTask, name='editTask'),
    path('tasks/delete/<int:pk>', views.deleteTask, name='deleteTask'),
    # URL for Notes
    path('notes', views.notes, name="notes"),
    path('notes/new', views.newNote, name='newNote'),
    path('notes/edit/<int:pk>', views.editNote, name='editNote'),
    path('notes/delete/<int:pk>', views.deleteNote, name='deleteNote'),
    # URL for Community Forum
    path('community/', views.community, name='community'),
    path('community/threads/<int:pk>', views.topic, name='showTopic'),
    path('community/threads/new', views.createTopic, name='createTopic'),
    path('community/threads', views.topicList, name='threads'),
    path('community/search', views.search, name='search'),
    path('community/members', views.members, name='members'),
    path('community/suggestions', views.suggestions, name='suggestions'),
    # URL for Market
    path('market', views.market, name='market'),
    # URL for Dashboard and Profile
    path('dashboard', views.dashboard, name='dashboard'),
    # URL for Settings
    path('settings/', views.settings, name='settings'),
    path('settings/general', TemplateView.as_view(template_name="settings/general.html"), name='general'),
    path('settings/manager', TemplateView.as_view(template_name="settings/manage.html"), name='manage'),
]