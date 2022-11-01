from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView

from accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


class AccountRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'


class AccountLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'User <{self.request.user}> has successfully logged in')
        # messages.error(self.request, f'User <{self.request.user}> has successfully logged in')
        # messages.info(self.request, f'User <{self.request.user}> has successfully logged in')
        # messages.warning(self.request, f'User <{self.request.user}> has successfully logged in')
        return response

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next

        return reverse('home')


class AccountLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'logout.html'


@login_required
def account_view(request):
    return render(request, 'profile_view.html')


class AccountUpdateView(LoginRequiredMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(request, 'update_a.html', {'user_form': user_form, "profile_form": profile_form})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return HttpResponseRedirect(reverse('accounts:profile_view'))
