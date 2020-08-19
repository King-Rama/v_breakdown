from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render

from account.forms import ClientRegisterForm


def client_register(request):
    if request.method == 'POST':
        form = ClientRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            f_name = form.cleaned_data['username']
            user.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, f'Welcome {f_name}')
            return redirect('client:home')
    else:
        form = ClientRegisterForm()
    return render(request, 'registration/register.html', {'form': form})
