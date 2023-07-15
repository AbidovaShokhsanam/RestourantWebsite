from django import forms
from apps.models import My_User, Message, Message1, Newss


class UsersCreationForm(forms.ModelForm):
    class Meta:
        model = My_User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'job', 'image')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = "__all__"


class MessageForm1(forms.ModelForm):
    class Meta:
        model = Message1
        fields = "__all__"


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Newss
        fields = '__all__'
