from django.forms import ModelForm, Textarea

from analysis.models.system import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        widgets = {'content': Textarea(attrs={'cols': 80, 'rows': 10}),}

    '''
    def clean(self):
        cleaned_data = super(FeedbackForm, self).clean()
        user_name = cleaned_data.get("user_name")
        user_phone = cleaned_data.get("user_phone")

        if not user_name and not user_phone:
            msg = "pls fill in at least one of name and phone"
            self._errors["user_name"] = self.error_class([msg])
            self._errors["user_phone"] = self.error_calss([msg])

            del cleaned_data["user_name"]
            del cleaned_data["user_phone"]
    '''
