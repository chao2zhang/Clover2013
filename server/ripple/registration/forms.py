# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_username': u"用户已存在",
        'password_mismatch': u"密码不一致",
    }
    username = forms.RegexField(label=u"用户名", max_length=30,
        regex=r'^[\w.@+-]+$',
        error_messages={
            'invalid': u"This value may contain only letters, numbers and "
                         "@/./+/-/_ characters."}
    )
    email = forms.EmailField(label=u"邮箱", max_length=30)
    password1 = forms.CharField(label=u"密码",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=u"确认密码",
        widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ("username",)

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
