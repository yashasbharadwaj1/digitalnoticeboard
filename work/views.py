from django.shortcuts import render,get_object_or_404
from .models import Files,Post
from django.views import generic
from django.views.generic import ListView
# Create your views here.


def home(request):
    return render(request, 'home.html')



#logics for achievements and announcements implementation
def post_single(request,post):
    post=get_object_or_404(Post,slug=post,status='published')
    return render(request,'posting/single.html',{'post':post})


class CatListView(ListView):
    template_name = 'posting/category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content



def annoucements(request):
    return render(request, 'announcements.html')


def achievements(request):
    return render(request, 'achievements.html')

# logics for publications endpoint implementation
class FileView(generic.ListView):
    model=Files
    template_name='file.html' 
    context_object_name = 'files'
    def get_queryset(self):
        return Files.objects.order_by('-id')




