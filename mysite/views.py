from django.views.generic import TemplateView

# Create your views here.

#--- TemplateView
class HomeView(TemplateView):
    template_name = 'home.html'
