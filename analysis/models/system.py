# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

from utils import LabelMeta

class Feedback(models.Model):
    user_name = models.CharField("name", max_length=48, blank=True)
    user_phone = models.CharField("phone", max_length=48, blank=True)
    user_email = models.EmailField("email", max_length=240, blank=True)
    content = models.CharField("feedback", max_length=3072)
    submit_date = models.DateTimeField(auto_now_add=True, editable=False)

    def __unicode__(self):
        return ' : '.join([self.user_name, self.user_phone, self.user_email])

    @models.permalink
    def get_absolute_url(self):
        return ('feedback_detail', [str(self.id)])

    class Meta(LabelMeta):
        db_table = u'system_feedback'
