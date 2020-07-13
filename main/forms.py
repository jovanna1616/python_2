from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    occupation = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ("username", "email", "occupation", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.occupation = self.cleaned_data["occupation"]
        if (commit):
            user.save()

        return user