from django.core.urlresolvers import reverse
from django.contrib.formtools.preview import FormPreview
from django.http import HttpResponseRedirect

from analysis.forms.system import FeedbackForm

class FeedbackFormPreview(FormPreview):
    def done(self, request, cleaned_data):
        form = FeedbackForm(request.POST)
        form.save()

        return HttpResponseRedirect(reverse('feedback_success'))
