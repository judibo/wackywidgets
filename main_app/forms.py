from django.forms import ModelForm, Form, CharField
from .models import Widget


class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']