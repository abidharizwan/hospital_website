from django import forms
from .models import Contact




class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),

        }
        labels = {
            'p_name': "Patient Name:",
            'p_phone': "Patient Phone:",
            'p_email': "Patient Email:",
            'doc_name': "Doctor Name:",
            'booking_date' : "Booking Date",
        }
class ContactForm(forms.ModelForm):
     class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'contact_date' : DateInput(),

        }
        