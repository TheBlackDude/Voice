from django import forms
from django.core.exceptions import ValidationError
from .models import Contact, Question

DUPLICATE_QUESTION_ERROR = "Someone have already asked this Question Check the FAQ"
EMPTY_QUESTION_ERROR = "You can't have an empty Question"

class QuestionForm(forms.models.ModelForm):
    
    class Meta:
        model = Question
        fields = ('question',)
        widgets = {
            'question': forms.fields.TextInput(attrs={
                'placeholder': 'Ask Your Question',
                'class': 'form-control',
            }),
        }
        error_messages = {
            'question': {'required': EMPTY_QUESTION_ERROR}
        }

    def validate_unique(self):
        try:
            self.instance.validate_unique()
        except ValidationError as e:
            e.error_dict = {'question': [DUPLICATE_QUESTION_ERROR]}
            self._update_errors(e)


class ContactForm(forms.models.ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')
        widgets = {
            'name': forms.fields.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'form-control',
            }),
            'email': forms.fields.TextInput(attrs={
                'placeholder': 'Your Email',
                'class': 'form-control',
            }),
            'phone': forms.fields.TextInput(attrs={
                'placeholder': 'Your Phone Number',
                'class': 'form-control',
            }),
            'message': forms.Textarea(attrs={
                'placeholder': ' Your Message',
                'rows': '10',
                'cols': '90',
                'class': 'form-control',
            }),
        } 
