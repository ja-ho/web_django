from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView

from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

from taggit.models import Tag

# Create your views here.

class TagMixin(object):
    def get_context_data(self, kwargs):
        context = super(TagMixin, self).get_context_data(kwargs)
        context['tags'] = Tag.objects.all()
        return context

#--- TemplateView
class TagTV(TagMixin, TemplateView):
    template_name = 'tagging/taggit_cloud.html'

#--- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

## post tagging object list
class PostTOL(TagMixin, ListView):
    model = Post
    template_name = 'tagging/tagging_post_list.html'
    paginate_by = '3'
    #context_object_name = 'objects'

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('slug'))


#--- DetailView
class PostDV(DetailView):
    model = Post


#--- Archive View
class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    template_name = 'blog/post_today.html'
    date_field = 'modify_date'

