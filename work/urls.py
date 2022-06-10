from django.urls import path 
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('announcements/',views.annoucements,name='announcements'),
    path('publications/',views.publications,name='publications'),
    path('achievements/',views.achievements,name='achievements'),


    path('news/',views.newsindex,name='newsindex'),
    path('search/',views.search,name='search'),
    path('business/',views.business,name='business'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('health/',views.health,name='health'),
    path('Science/',views.Science,name='Science'),
    path('sports/',views.sports,name='sports'),
    path('technology/',views.technology,name='technology'),

]
