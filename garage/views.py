from django.shortcuts import render
from django.views import generic
# Create your views here.
from client.models import HelpProvider, BreakDownRequest


class GarageHome(generic.TemplateView):
    template_name = 'garage/admin_home.html'


class GarageUpdateView(generic.UpdateView):
    model = HelpProvider
    fields = ['facility_name', 'zone', 'photo', 'description']
    success_url = '/'
    template_name = 'garage/update.html'

    def get_object(self, queryset=None):
        return HelpProvider.objects.get(manager=self.request.user)


class GarageCreateView(generic.CreateView):
    model = HelpProvider
    fields = ['facility', 'zone', 'photo', 'description']
    success_url = '/'
    template_name = ''


class Trip(generic.TemplateView):
    template_name = 'garage/trip.html'

    def get_context_data(self, **kwargs):
        ctx = super(Trip, self).get_context_data(**kwargs)
        ctx['id'] = BreakDownRequest.objects.filter(requesting_client=self.request.user).latest('id')
        return ctx


class TripListViewSuccess(generic.ListView):
    model = BreakDownRequest
    template_name = 'garage/list.html'

    def get_queryset(self):
        return BreakDownRequest.objects.filter(requesting_client=self.request.user).filter(status=5)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(TripListViewSuccess, self).get_context_data(**kwargs)
        ctx['cancel'] = 'finished'
        return ctx


class TripListViewCancelled(generic.ListView):
    model = BreakDownRequest
    template_name = 'garage/list.html'

    def get_queryset(self):
        return BreakDownRequest.objects.filter(requesting_client=self.request.user).filter(status__lt=5)

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(TripListViewCancelled, self).get_context_data(**kwargs)
        ctx['cancel'] = 'Cancelled'
        return ctx


