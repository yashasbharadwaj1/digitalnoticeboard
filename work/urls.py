from django.urls import path 
from .import views
urlpatterns=[
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('business/',views.business,name='business'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('health/',views.health,name='health'),
    path('Science/',views.Science,name='Science'),
    path('sports/',views.sports,name='sports'),
    path('technology/',views.technology,name='technology'),



]
#Your API key is: 3b39469e194c4d3ebc071e858ca902d3