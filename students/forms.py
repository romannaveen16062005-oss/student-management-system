
from django import forms
from django.utils import timezone
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            'register_number',
            'full_name',
            'email',
            'phone',
            'department',
            'course',
            'date_of_birth',
            'address',
        ]

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            ),
            'address': forms.Textarea(
                attrs={'rows': 3}
            ),
        }

    def clean_register_number(self):
        register_number = self.cleaned_data['register_number'].strip().upper()

        if not register_number:
            raise forms.ValidationError(
                "Register number is required."
            )

        return register_number

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()

        if not full_name:
            raise forms.ValidationError(
                "Student name is required."
            )

        return full_name

    def clean_phone(self):
        phone = self.cleaned_data['phone'].strip()

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number must contain digits only."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must contain exactly 10 digits."
            )

        return phone

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']

        if date_of_birth >= timezone.localdate():
            raise forms.ValidationError(
                "Date of birth must be in the past."
            )

        return date_of_birth
