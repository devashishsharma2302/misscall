from __future__ import unicode_literals, absolute_import

import json
from django.http.response import HttpResponse
from rest_framework.views import APIView

from testmisscall.models import Call


def health_check(request):
    return HttpResponse("OK", status=200)


class SaveCall(APIView):
    permission_classes = []
    authentocation_classes = []

    def post(self, request):
        Call.objects.create(data=json.dumps(request.data))
        return HttpResponse("OK", status=200)
