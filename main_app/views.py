from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.
def index(request):
    model = Widget
    widgets = Widget.objects.all()
    form = WidgetForm
    return render(request, 'index.html', {'widgets': widgets, 'form': form})

def add_widget(request):
   form = WidgetForm(request.POST)
   form.save()
   return redirect('index')

def widget_delete(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    widget.delete()
    return redirect('index')