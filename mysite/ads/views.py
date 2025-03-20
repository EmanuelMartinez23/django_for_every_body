from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from ads.models import Ad
from ads.owner import OwnerListView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView, OwnerDetailView


# Create your views here.


class AdListView(OwnerListView):
    template_name = 'ads/ad_list.html'
    model = Ad

class AdDetailView(OwnerDetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'

class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title','price', 'text']

class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']

class AdDeleteView(OwnerDeleteView):
    model = Ad