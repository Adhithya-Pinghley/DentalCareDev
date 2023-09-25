from django.forms import ModelForm
from .models import Appointment
from django import forms
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput


class AppointmentSet(forms.Form):
    # my_date_field = forms.DateField(widget=DatePickerInput)
    # my_time_field = forms.TimeField(widget=TimePickerInput)
    my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)

class AppointmentSetForm(ModelForm):
    class Meta:
        model = Appointment
        
        fields = ['subject', 'time', 'notes']

        widgets = {
            'time' : DateTimePickerInput(),
            
        }

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"
# class TimeInput(forms.TimeInput, forms.DateInput):
#     timeInputType = 'time'
#     dateinputType = 'date'

# class AppointmentForm(ModelForm):
    # hour = forms.TimeField(widget=forms.Select(choices=[
    #     (hour, hour) for hour in range(0, 24)   
    # ]))
    # min = forms.TimeField(widget=forms.Select(choices=[
    #     (min, min) for min in range(0, 60)
    # ]))

    # class Meta:
    #     model = Appointment
    #     fields = ['time', 'date']
    #     widgets = {
    #         'time': TimeInput(),
    #     }
    #     # field_classes = {
    #     #     'time': 'form-control col-md-6',
    #     #     'min': 'form-control col-md-6',
    #     # }