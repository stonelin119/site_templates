from datetime import datetime

from django.http import HttpResponse

from analysis.models.user import Footprint

def footprint(req):
    client_model = req.POST.get('client_model', '')
    client_OS = req.POST.get('client_OS')
    client_version = req.POST.get('client_version')
    app_version = req.POST.get('app_version')
    user_account = req.POST.get('user_account')
    operation_code = req.POST.get('operation_code')
    content = req.POST.get('content')

    Footprint.objects.create(client_model=client_model,
            client_OS=client_OS,
            client_version=client_version,
            app_version=app_version,
            user_account=user_account,
            operation_code=operation_code,
            content=content)

    return HttpResponse(str(operation_code), mimetype='text/plain')
