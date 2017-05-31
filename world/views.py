from django.template import loader
from django.http import HttpResponse

# Create your views here.

def map_view(request):
    template = loader.get_template('world/map.html')
    context = {}
    return HttpResponse(template.render(context, request))
