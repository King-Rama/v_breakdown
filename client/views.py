from chartjs.views.lines import BaseLineChartView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
# Create your views here.
from django.views.generic import TemplateView

from account.models import User
from .forms import ClientPrimary, ClientSecondary, UserUpdateForm
from .models import BreakDownRequest


class Home(generic.TemplateView):
    template_name = 'client/base.html'


def home_page(request):
    return render(request, 'client/welcome/index.html', {})


# class EmergenceCreateView(LoginRequiredMixin, generic.CreateView):
#     model = BreakDownRequest
#     template_name = 'client/welcome/emergency.html'
#     form_class = ClientPrimary
#
#     def get_context_data(self, **kwargs):
#         ctx = super(EmergenceCreateView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             ctx['form'] = ClientPrimary(self.request.POST)
#             ctx['inlines'] = ClientSecondary(self.request.POST)
#         else:
#             ctx['form'] = ClientPrimary()
#             ctx['form2'] = ClientSecondary()
#         return ctx
#
#     def get_success_url(self):
#         return reverse('client:emergency-detail', kwargs={'pk': self.object.pk})
#
#     def form_valid(self, form):
#         ctx = self.get_context_data()
#         form1 = form.save(commit=False)
#         form1.requesting_client = self.request.user
#         form1.save()
#         form2 = ctx['form2']
#         if form2.is_valid() and form.is_valid():
#             self.object = form.save() # saves Father and Children
#             return redirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form))
#
#     def form_invalid(self, form):
#         return self.render_to_response(self.get_context_data(form=form))
#


class EmergenceCreateView(LoginRequiredMixin, generic.CreateView):
    model = BreakDownRequest
    fields = ['breakdown_description', 'towing', 'flat_tire', 'engine_down', 'client_zone']
    template_name = 'client/welcome/emergency.html'
    success_url = '/'

    # def get_success_url(self):
    #     return redirect(reverse('client:emergency-detail', kwargs={'pk': self.object.pk}))

    def form_valid(self, form):
        client = form.save(commit=False)
        client.requesting_client = self.request.user
        client.save()
        return super(EmergenceCreateView, self).form_valid(form)

#
# @login_required
# def emergence(request):
#     if request.method == 'POST':
#         form1 = ClientPrimary(request.POST)
#         form2 = ClientSecondary(request.POST)
#
#         if form1.is_valid() and form2.is_valid():
#             client = form1.save(commit=False)
#             client.requesting_client = request.user
#             client.save()
#             form1.save()
#             rec = BreakDownRequest.objects.filter(requesting_client=request.user).latest('id')
#             return redirect('client:emergency-detail', rec.id)
#
#     else:
#         form1 = ClientPrimary()
#         form2 = ClientSecondary()
#     return render(request, 'client/welcome/emergency.html', {'form': form1,
#                                                              'form2': form2})


class EmergenceDetailView(LoginRequiredMixin, generic.DetailView):
    model = BreakDownRequest
    template_name = 'client/welcome/request_detail.html'


class Trip(generic.TemplateView):
    template_name = 'client/welcome/trip.html'

    def get_context_data(self, **kwargs):
        ctx = super(Trip, self).get_context_data(**kwargs)
        ctx['id'] = BreakDownRequest.objects.filter(requesting_client=self.request.user).latest('id')
        return ctx


class TripListViewSuccess(generic.ListView):
    model = BreakDownRequest
    template_name = 'client/welcome/list.html'

    def get_queryset(self):
        return BreakDownRequest.objects.filter(requesting_client=self.request.user).filter(status=5)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(TripListViewSuccess, self).get_context_data(**kwargs)
        ctx['cancel'] = 'finished'
        return ctx


class TripListViewCancelled(generic.ListView):
    model = BreakDownRequest
    template_name = 'client/welcome/list.html'

    def get_queryset(self):
        return BreakDownRequest.objects.filter(requesting_client=self.request.user).filter(status__lt=5)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(TripListViewCancelled, self).get_context_data(**kwargs)
        ctx['cancel'] = 'Cancelled'
        return ctx


class EditProfile(generic.UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'client/welcome/form.html'
    context_object_name = 'profile'
    success_url = reverse_lazy('client:emergency')

    def get_object(self, queryset=None):
        return self.request.user


def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.add_message(request, messages.SUCCESS, 'Your password was successfully updated!')
            return redirect('grade:index')
        else:
            messages.add_message(request, messages.ERROR, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'client/welcome/change_password.html', {
        'form': form
    })


class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 'Saturday', 'Sunday']

    def get_providers(self):
        """Return names of datasets."""
        return ["Finished", "Cancelled"]

    def get_data(self):
        """Return 3 datasets to plot."""
        week1 = BreakDownRequest.objects.filter(created__week_day=1).filter(status=5).count()
        week2 = BreakDownRequest.objects.filter(created__week_day=2).filter(status=5).count()
        week3 = BreakDownRequest.objects.filter(created__week_day=3).filter(status=5).count()
        week4 = BreakDownRequest.objects.filter(created__week_day=4).filter(status=5).count()
        week5 = BreakDownRequest.objects.filter(created__week_day=5).filter(status=5).count()
        week6 = BreakDownRequest.objects.filter(created__week_day=6).filter(status=5).count()
        week7 = BreakDownRequest.objects.filter(created__week_day=7).filter(status=5).count()

        week11 = BreakDownRequest.objects.filter(created__week_day=1).filter(status__lt=5).count()
        week21 = BreakDownRequest.objects.filter(created__week_day=2).filter(status__lt=5).count()
        week31 = BreakDownRequest.objects.filter(created__week_day=3).filter(status__lt=5).count()
        week41 = BreakDownRequest.objects.filter(created__week_day=4).filter(status__lt=5).count()
        week51 = BreakDownRequest.objects.filter(created__week_day=5).filter(status__lt=5).count()
        week61 = BreakDownRequest.objects.filter(created__week_day=6).filter(status__lt=5).count()
        week71 = BreakDownRequest.objects.filter(created__week_day=7).filter(status__lt=5).count()

        return [[1, 0, 3, 1, 7, 3, 1],
                [1, 2, 0, 1, 2, 2, 1]]


line_chart = TemplateView.as_view(template_name='client/welcome/statistics.html')
line_chart_json = LineChartJSONView.as_view()


class Statics(generic.TemplateView):
    template_name = 'client/welcome/statistics.html'


class ClientDetailView(generic.TemplateView):
    template_name = 'client/welcome/detail.html'
