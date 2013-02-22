from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

from analysis.forms.system import FeedbackForm

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')
        else:
            form = FeedbackForm()

    return render(request, 'feedback.html', {'form', form})

def feedback_success(request):
    return render_to_response('system/feedback_success.html')
