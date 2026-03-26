from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User #because we are extending the UserCreationForm class we should write the model
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super().save(commit=False)  #super()-> Call the original save() method from UserCreationForm
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user