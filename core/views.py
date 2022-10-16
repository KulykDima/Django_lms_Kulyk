from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse


def index(request):
    return render(request, 'students/index.html')


class CustomUpdateBaseView:
    model = None
    form_class = None
    success_url = None
    template_name = None

    @classmethod
    def update(cls, request, pk):
        obj = get_object_or_404(cls.model, id=pk)
        form = cls.form_class(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(cls.success_url))

        return render(request, cls.template_name, {'form': form})
