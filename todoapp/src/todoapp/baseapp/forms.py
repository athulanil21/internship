from django import forms
from django.forms import DateInput
from django.forms import Select
from django.forms import TextInput
from .models import Task, Book
from django.utils.translation import gettext_lazy as _

Choice_Priority = [
    ('', 'Open this select priority'),
    ('1', 'High priority'),
    ('2', 'Middle priority'),
    ('3', 'Low priority'),
]

Choice_Status = [
    ('', 'Open this select status'),
    ('1', 'Completed'),
    ('2', 'Working'),
    ('3', 'Pending'),
]


class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['is_deleted', ]
        fields = ['name', 'priority', 'status', 'created']
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control',
                                     'placeholder': 'task task task'}),
            'priority': Select(attrs={'class': 'required form-select  ',
                                      'placeholder': 'Select priority'},
                               choices=Choice_Priority),
            'status': Select(attrs={'class': 'required form-select  ',
                                    'placeholder': 'Select status'},
                             choices=Choice_Status),
            'created': DateInput(attrs={'class': 'required form-control  ',
                                        'placeholder': 'Date',
                                        'type': 'date', 'data-format': 'yyyy-MM-dd'}),
        }
        error_messages = {
            'name': {
                'required': _("Task field is required."),
            },
            'priority': {
                'required': _("Priority field is required."),
            },
            'status': {
                'required': _("Status field is required."),
            },
            'created': {
                'required': _("Date field is required."),
            },
        }
        labels = {
            "name": "Task",
            "priority": "Select priority",
            "status": "Select status",
            "created": "Date",
        }


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         exclude = ['is_deleted', ]
#         fields = ['title', 'author', 'published', 'price']
#         widgets ={
#             'title': TextInput(attrs={'class': 'required form-control',
#                                       'placeholder': 'title title title'}),
#             'author': TextInput(attrs={'class': 'required form-control',
#                                       'placeholder': 'task task task'}),
#             'published': DateInput(attrs={'class': 'required form-control  ',
#                                       'placeholder': 'Date',
#                                       'type': 'date', 'data-format': 'yyyy-MM-dd'}),
#             'price': TextInput(attrs={'class': 'required form-control',
#                                       'placeholder': 'task task task'}),
#             choices = Choice_Status),
#         }
#         error_messages = {
#             'title': {
#                 'required': _("title field is required."),
#             },
#             'price': {
#                 'required': _("price field is required."),
#             }
#         }
