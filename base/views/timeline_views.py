from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import Timeline
from base.serializers import TimelineSerializer


@api_view(['GET'])
def getTimelines(request):
    timelines = Timeline.objects.all().order_by('-lastUpdated')
    serializer = TimelineSerializer(timelines, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createTimeline(request):
    data = request.data

    timeline = Timeline.objects.create(
        title=data['title'],
        description=data['description'],
        imageUrl=data['imageUrl'],
        bgColor=data['bgColor'],
        textColor=data['textColor'],
        titleColor=data['titleColor'],
        borderColor=data['borderColor']
    )

    serializer = TimelineSerializer(timeline, many=False)

    return Response(serializer.data)


@api_view(['PUT'])
def updateTimeline(request, pk):
    data = request.data
    timeline = Timeline.objects.get(id=pk)

    serializer = TimelineSerializer(instance=timeline, data=data, many=False)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    # timeline.title = data['title']
    # timeline.description = data['description']
    # timeline.imageUrl = data['imageUrl']
    # timeline.bgColor = data['bgColor']
    # timeline.textColor = data['textColor']
    # timeline.titleColor = data['titleColor']
    # timeline.borderColor = data['borderColor']

    # timeline.save


@api_view(['DELETE'])
def deleteTimeline(request, pk):
    timeline = Timeline.objects.get(id=pk)
    timeline.delete()
    return Response('Timeline deleted!')
