from django import forms
from .models import User, Notice, Responses, SubscribersCategory
from django.contrib.auth.forms import UserCreationForm
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class BaseRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "password1",
                  "password2", )


#добавление в группу при регистрации
class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='basic')
        basic_group.user_set.add(user)
        return user


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = [
            'author_name',
            'category_notice',
            'header',
            'content',
        ]


class ResponsesForm(forms.ModelForm):
    class Meta:
        model = Responses
        fields = [
            'responses_comment',
            'user_responses',
            'text_responses',
        ]


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribersCategory
        fields = ['category']
