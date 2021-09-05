from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import Good
from .forms import GoodItemForm


class GoodsListView(ListView):
    model = Good
    template_name = "items_index.html"
    fields = ['title']
    context_object_name = 'goods_list'

    def get_queryset(self):
        items = Good.objects.all()
        return items


class GoodsCreate(CreateView):
    model = Good
    form_class = GoodItemForm
    template_name = "create_good.html"
    success_url = reverse_lazy('goods:index')

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/goods/')