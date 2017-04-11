from __future__ import unicode_literals, absolute_import
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view


def health_check(request):
    return HttpResponse("OK", status=200)


@api_view(['GET'])
def call(request, *args, **kwargs):
    """
    Renders the squealy authoring interface template
    """

    return HttpResponse(status=status.HTTP_200_OK)

