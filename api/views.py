from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponseServerError, Http404
from django.shortcuts import render
from sshmanager.models import Token, Host


def config_file(request):
    if 'HTTP_X_API_TOKEN' not in request.META:
        return HttpResponseServerError('Token Header not present')

    try:
        token = Token.objects.get(token=request.META['HTTP_X_API_TOKEN'])
    except ObjectDoesNotExist:
        raise Http404('Invalid Token')

    hosts = Host.objects.filter(owner=token.owner, active=True)

    response = render(request, 'config_file.html', {'hosts': hosts})
    response.content_type = 'text/plain'

    return response
