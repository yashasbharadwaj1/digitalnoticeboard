from django.urls import path 
from .import views

app_name = 'work'
urlpatterns=[
    path('',views.home,name='home'),
    path('files/',views.FileView.as_view(),name='files'),
    path('form/', views.uploadForm, name='form'),
    path('upload/', views.uploadFile, name='upload'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('category/<category>/', views.CatListView.as_view(), name='category'),

]
