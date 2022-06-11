from django.urls import path 
from .import views

app_name = 'mynews'
urlpatterns=[
    path('mynews/',views.newsindex,name='newsindex'),
    path('search/',views.search,name='search'),
    path('business/',views.business,name='business'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('health/',views.health,name='health'),
    path('Science/',views.Science,name='Science'),
    path('sports/',views.sports,name='sports'),
    path('technology/',views.technology,name='technology'),
]