# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from feedback.forms import FeedbackForm


class FeedbackHomePageView(TemplateView):
    
    def get(self, request):
        form = FeedbackForm()
        return render(request, template_name='feedback.html', context={'form': form})

    def post(self, request):
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            print("form is valid")
            print(request.POST)
        else:
            print("form is invalid")
        return render(request, template_name='feedback_submitted.html', context={'form': form})


# class FeedbackSubmittedPageView(TemplateView):
#
#     def get(self, request):
#         err_msg = 'No form submitted'
#         return render(request, template_name='feedback_submitted.html', context={'errorMessage': err_msg})