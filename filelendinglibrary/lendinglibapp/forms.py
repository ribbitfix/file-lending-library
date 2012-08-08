from django import forms

class UserEmailForm(forms.Form):
    email = forms.EmailField()
    
    def save(self, user):
        user.email = self.cleaned_data['email']