from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
# In order to use a classed Generic View, Import ListView and Detailview 

from bookmark.models import Bookmark

#Import class Model to search Table info.

class BookmarkLV(ListView):
    model = Bookmark
# BookmarkLV is a view to show a record of Bookmark Record List
# It's inherited Generic view.
# In case of Inherit Listview,

class BookmarkDV(DetailView):
    model = Bookmark
#BookmarkDV is a view to show detail info of certain records of a Table.
