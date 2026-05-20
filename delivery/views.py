# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import Driver
# from .forms import DriverForm, DriverUpdateForm

from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Driver
from .forms import DriverForm, DriverUpdateForm



# def delivery_home(request):
#     return render(request, 'delivery/delivery_home.html')


class DeliveryHomeView(TemplateView):
    template_name = 'delivery/delivery_home.html'



# def delivery_list(request):
#     drivers = Driver.objects.all()
#     return render(request, 'delivery/delivery_list.html', {'drivers': drivers})

class DeliveryListView(ListView):
    model = Driver
    template_name = 'delivery/delivery_list.html'
    context_object_name = 'drivers'



# def delivery_detail(request, pk):
#     driver = get_object_or_404(Driver, pk=pk)
#     return render(request, 'delivery/delivery_detail.html', {'driver': driver})


class DeliveryDetailView(DetailView):
    model = Driver
    template_name = 'delivery/delivery_detail.html'
    context_object_name = 'driver'





# @login_required
# def delivery_create(request):
#     if request.method == "POST":
#         form = DriverForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery_list')
#     else:
#         form = DriverForm()
#     return render(request, 'delivery/delivery_form.html', {'form': form})


class DeliveryCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    form_class = DriverForm
    template_name = 'delivery/delivery_form.html'
    success_url = reverse_lazy('delivery_list')





# @login_required
# def delivery_update(request, pk):
#     driver = get_object_or_404(Driver, pk=pk)
#     if request.method == "POST":
#         form = DriverUpdateForm(request.POST, instance=driver)
#         if form.is_valid():
#             form.save()
#             return redirect('delivery_list')
#     else:
#         form = DriverUpdateForm(instance=driver)
#     return render(request, 'delivery/delivery_form.html', {'form': form})


class DeliveryUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    form_class = DriverUpdateForm
    template_name = 'delivery/delivery_form.html'
    success_url = reverse_lazy('delivery_list')





# @login_required
# def delivery_delete(request, pk):
#     driver = get_object_or_404(Driver, pk=pk)
#     if request.method == "POST":
#         driver.delete()
#         return redirect('delivery_list')
#     return render(request, 'delivery/delivery_confirm_delete.html', {'driver': driver})


class DeliveryDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = 'delivery/delivery_confirm_delete.html'
    success_url = reverse_lazy('delivery_list')
    context_object_name = 'driver'

# API Views
from rest_framework.generics import ListCreateAPIView
from .serializers import DriverSerializer

class DriverListCreateAPI(ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

