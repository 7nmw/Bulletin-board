from django.contrib import admin
from django.urls import path, include

from . import views
from .views import NoticeList, NoticeCreate, NoticeUpdate, ResponsesList, ResponsesCreate, BaseRegisterView, IndexView, SubscriberView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', NoticeList.as_view(), name='start_page'),
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('create/', NoticeCreate.as_view(), name='notice_create'),
    path('<int:pk>/update/', NoticeUpdate.as_view(), name='notice_update'),
    path('responses/', ResponsesList.as_view(), name='responses'),
    path('acceptedResponses/<int:pk>', views.AcceptedResponses, name='AcceptedResponses'),
    path('refuseResponses/<int:pk>', views.RefuseResponses, name='RefuseResponses'),
    path('deleteResponses/<int:pk>', views.DeleteResponses, name='DeleteResponses'),
    path('createResponses/', ResponsesCreate.as_view(), name='Responses_create'),
    path('', IndexView.as_view(template_name='sign/index.html'), name='index'),
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),

]