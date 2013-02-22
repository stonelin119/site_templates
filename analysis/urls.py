from django import forms
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from analysis.genericviews.system import FeedbackCreateView, \
        FeedbackUpdateView, FeedbackListView, FeedbackDetailView

urlpatterns = patterns('analysis.views.system',
    url(r'^$', TemplateView.as_view(template_name="analysis_base.html"), name="analysis"),
    url(r'feedback/success$',
        'feedback_success',
        name="feedback_success"),
    url(r'feedback/add$',
        FeedbackCreateView.as_view(),
        name="feedback_add"),
    url(r'feedbacks/(?P<pk>\d+)/update$',
        FeedbackUpdateView.as_view(),
        name="feedback_update"),
    url(r'feedbacks$',
        FeedbackListView.as_view(),
        name="feedback_list"),
    url(r'feedbacks/(?P<pk>\d+)$',
        FeedbackDetailView.as_view(),
        name="feedback_detail"),
)
