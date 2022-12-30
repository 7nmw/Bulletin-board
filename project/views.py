from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView
from .models import *
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .forms import NoticeForm, ResponsesForm, BaseRegisterForm, SubscribeForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .filters import ResponsesFilter
from django.http import HttpResponseRedirect



class NoticeList(ListView):
    model = Notice
    template_name = 'Notice.html'
    context_object_name = 'notice'


class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'sign/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context


class NoticeCreate(PermissionRequiredMixin, CreateView):
    form_class = NoticeForm
    model = Notice
    template_name = 'create_notice.html'
    permission_required = 'project.add_notice'  # добавление права создание объекта
    success_url = reverse_lazy('start_page')


class NoticeUpdate(PermissionRequiredMixin, UpdateView):
    form_class = NoticeForm
    model = Notice
    template_name = 'notice_edit.html'
    permission_required = 'project.change_notice'  # добавление права изменение содержание объекта
    success_url = reverse_lazy('start_page')


class ResponsesList(PermissionRequiredMixin, ListView):
    model = Responses
    form = ResponsesFilter
    template_name = 'all_responses.html'
    context_object_name = 'responses'
    permission_required = 'project.view_responses'  # добавление права создание объекта


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponsesFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


def AcceptedResponses(request, pk):
    Responses.objects.filter(pk=pk).update(accepted=True)
    return HttpResponseRedirect(reverse('responses'))

def RefuseResponses(request, pk):
    Responses.objects.filter(pk=pk).update(accepted=False)
    return HttpResponseRedirect(reverse('responses'))

def DeleteResponses(request, pk):
    Responses.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse('responses'))


class ResponsesCreate(PermissionRequiredMixin, CreateView):
    form_class = ResponsesForm
    model = Responses
    template_name = 'create_responses.html'
    permission_required = 'project.add_responses'  # добавление права создание объекта
    success_url = reverse_lazy('start_page')



class SubscriberView(CreateView):
    model = SubscribersCategory
    form_class = SubscribeForm
    template_name = 'subscribe.html'
    success_url = reverse_lazy('start_page')

    def form_valid(self, form):
        subscribe = form.save(commit=False)
        subscribe.subscriber = User.objects.get(pk=self.request.user.id)
        return super(SubscriberView, self).form_valid(form)