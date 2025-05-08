from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label="name", max_length=50)
    email = forms.EmailField(label="email")
    feedback_type = forms.ChoiceField(choices=[('general', 'General'), ('bug', 'Bug Report'), ('feature', 'Feature Request')])
    message = forms.Text.Field(label='feedback', widget=forms.Textarea)