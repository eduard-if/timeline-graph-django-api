from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import Timeline
from base.serializers import TimelineSerializer


@api_view(['GET'])
def getTimelines(request):
    timelines = Timeline.objects.all()
    serializer = TimelineSerializer(timelines, many=True)
    return Response(serializer.data)
