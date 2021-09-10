from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
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
    template_name = "good_create.html"
    success_url = reverse_lazy('goods:index')

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def save_good_form(self, request, form, template_name):
        data = dict()
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                data['form_is_valid'] = True
                goods = Good.objects.all()
                data['html_good_list'] = render_to_string('good_list.html', {
                    'goods': goods
                })
            else:
                data['form_is_valid'] = False
        context = {'form': form}
        data['html_form'] = render_to_string(template_name, context, request=request)
        return JsonResponse(data)
