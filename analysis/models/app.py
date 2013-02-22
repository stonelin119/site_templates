from django.db import models

from utils import LabelMeta

class App(models.Model):
    app_code = models.IntegerField()
    app_name = models.CharField(max_length=8)

    def __unicode__(self):
        return self.app_name

    class Meta(LabelMeta):
        db_table = 'app'

class AppVersion(models.Model):
    app = models.ForeignKey(App)
    client_OS = models.CharField(max_length=40)
    version = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s (%s-%s)" % (self.app.app_name, self.client_OS, self.version)

    class Meta(LabelMeta):
        db_table = 'app_version'

class AppOperation(models.Model):
    version = models.ForeignKey(AppVersion)
    operation_code = models.IntegerField(max_length=3)
    operation_name = models.CharField(max_length=16)

    def __unicode__(self):
        return self.operation_name

    class Meta(LabelMeta):
        db_table = 'app_operation'
