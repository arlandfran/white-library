from django import forms
from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(max_length=128)
    email = forms.EmailField()
    subject = forms.CharField(max_length=128)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}))

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field == 'sku':
                placeholder = field.upper()
            elif self.fields[field].required:
                placeholder = field.replace('_', ' ').title() + '*'
            else:
                placeholder = field.replace('_', ' ').title()
            self.fields[field].widget.attrs['placeholder'] = placeholder

    def get_info(self):
        """Returns formatted information"""
        data = super().clean()

        name = data.get('name').strip()
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')

        msg = f'Hi {name},'
        msg += '\n\nThank you for contacting White Library regarding: {subject}'
        msg += f'\n\n{message}'
        msg += f'\n\nWe will get back to you soon to: {email}, thanks again for getting in touch.'
        msg += '\n\nHave a great day!'

        return subject, msg, email

    def send(self):

        subject, msg, email = self.get_info()

        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
