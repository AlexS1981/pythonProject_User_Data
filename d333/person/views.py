from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PersonSerializer
# Create your views here.


class PersonAPI(APIView):
    def post(self, request):
        """
        127.0.0.1:8000/person/person/
        body = '''{"name": "20chars",
                   "surn": "20chars",
                   "pasw1": "20chars",
                   "pasw2": "confirm",
                   "status": "int(0 or 1)"}'''
        :param request:
        :return:
        """
        serialiser = PersonSerializer(data=request.data)
        serialiser.is_valid(raise_exception=True)
        instance = serialiser.save()
        return Response(PersonSerializer(instance).data)
