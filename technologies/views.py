# backend/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from technologies.models import Technology
from .serializers import TechnologySerializer

class TechnologyListView(APIView):
    def get(self, request):
        techs = Technology.objects.all()
        serializer = TechnologySerializer(techs, many=True)
        return Response(serializer.data)
