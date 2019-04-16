# hello/urls.py

from django.conf.urls import url
from feedback import views


urlpatterns = [
    url(r'^$', views.FeedbackHomePageView.as_view()),
    # url(r'^feedback_submitted/$', views.FeedbackSubmittedPageView.as_view()),
]