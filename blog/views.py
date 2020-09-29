from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayarchiveView

from blog.models import Post
# Create your views here.

#--ListView
class PostLV(ListView):
    model = post
    template_name='blog/post_all.html'
    context_object_name='posts'
    paginate_by = 2

#--Detailview
class PostDV(DetaiView):
    model = Post

#--ArchiveView
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostDAV(DatArchiveView):
    model = Post
    date_field='modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'
    
