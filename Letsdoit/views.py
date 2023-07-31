from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse

# Create your views here.

class Home(View):

    template_name = 'simple.html'

    def get(self, request, *args, **kwargs):
        context = {
            'message': 'Hello, this is a simple template!',
            'some_variable': 42,
        }
        return render(request, self.template_name, context)

def home(request):
    context = {"name": "saraj"}
    # return render(request, 'simple.html')
    return JsonResponse(context)