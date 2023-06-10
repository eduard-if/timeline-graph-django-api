from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import Timeline, Item
from base.serializers import TimelineSerializer, ItemSerializer

from datetime import datetime


@api_view(['GET'])
def getTimelines(request):
    timelines = Timeline.objects.all().order_by('-lastUpdated')
    serializer = TimelineSerializer(timelines, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createTimeline(request):
    data = request.data

    if data['title'] == '':
        data['title'] = f'Untitled {datetime.now()}'

    if data['bgColor'] == '':
        data['bgColor'] = '#343a40'
    if data['textColor'] == '':
        data['textColor'] = '#f8f9fa'
    if data['titleColor'] == '':
        data['titleColor'] = '#f8f9fa'
    if data['borderColor'] == '':
        data['borderColor'] = '#343a40'

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


@api_view(['DELETE'])
def deleteTimeline(request, pk):
    timeline = Timeline.objects.get(id=pk)
    timeline.delete()
    return Response('Timeline deleted!')


@api_view(['GET'])
def getItems(request, pk):
    try:
        timeline = Timeline.objects.get(id=pk)
        items = timeline.item_set.all()
    except Timeline.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializerItems = ItemSerializer(items, many=True)
    serializerTimeline = TimelineSerializer(timeline, many=False)
    return Response({'timeline': serializerTimeline.data, 'items': serializerItems.data})


@api_view(['POST'])
def createItem(request, pk):
    data = request.data

    timeline = Timeline.objects.get(id=pk)

    item = Item.objects.create(
        timeline=timeline,
        title=data['title'],
        start=data['start'],
        end=data['end'],
        type=data['type'],
        style=data['style']
    )

    serializerItem = ItemSerializer(item, many=False)
    serializerTimeline = TimelineSerializer(timeline, many=False)
    return Response({'timeline': serializerTimeline.data, 'item': serializerItem.data})


@api_view(['PUT'])
def updateItem(request, pk, id):
    data = request.data

    try:
        timeline = Timeline.objects.get(id=pk)
        item = Item.objects.get(id=id, timeline=timeline)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializerItem = ItemSerializer(instance=item, data=data, many=False)
    serializerTimeline = TimelineSerializer(timeline, many=False)

    if serializerItem.is_valid():
        serializerItem.save()

    return Response({'timeline': serializerTimeline.data, 'item': serializerItem.data})


@api_view(['DELETE'])
def deleteItem(request, pk, id):

    try:
        timeline = Timeline.objects.get(id=pk)
        item = Item.objects.get(id=id, timeline=timeline)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response(f'Item with id: {id} from Timeline: {timeline.id} deleted!')
