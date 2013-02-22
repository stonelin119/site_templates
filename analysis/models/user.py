from django.db import models

from utils import LabelMeta

class Footprint(models.Model):
    client_model = models.CharField(max_length=40)
    client_OS = models.CharField(max_length=40)
    client_version = models.CharField(max_length=40)
    app_version = models.CharField(max_length=40)
    user_account = models.CharField(max_length=40)
    operation_code = models.IntegerField()
    content = models.CharField(max_length=1024)
    create_time = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return "%s : %s" % (self.user_account, self.operation_code)

    class Meta(LabelMeta):
        db_table = 'user_footprint'
