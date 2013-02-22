from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from analysis.forms.system import FeedbackForm
from analysis.models.system import Feedback

class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'system/feedback_add.html'
    success_url = reverse_lazy('feedback_list')

class FeedbackUpdateView(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'system/feedback_update.html'
    success_url = reverse_lazy('feedback_list')

    def get_context_data(self, **kwargs):
        ctx = kwargs
        if self.request.REQUEST.get('redirect'):
            ctx.update({'redirect': self.request.REQUEST.get('redirect')})
        else:
            ctx.update({'redirect': self.request.META['HTTP_REFERER']})

        return ctx

    def get_success_url(self):
        return self.request.REQUEST.get('redirect')

class FeedbackDetailView(DetailView):
    model = Feedback
    template_name = 'system/feedback_detail.html'

class FeedbackListView(ListView):
    model = Feedback
    template_name = 'system/feedback_list.html'
    context_object_name = "feedbacks"
    queryset = Feedback.objects.order_by('-submit_date')
    paginate_by = 10
