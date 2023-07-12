from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from base.models import Timeline, Item
from base.serializers import TimelineSerializer, ItemSerializer

from datetime import datetime


@api_view(['GET'])
def getTimelines(request, orderBy):
    timelines = Timeline.objects.all().order_by(orderBy)
    serializer = TimelineSerializer(timelines, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def createTimeline(request):
    data = request.data

    if data['title'] == '':
        data['title'] = f'Untitled {datetime.now()}'

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
    return Response({'timeline_id': pk})


@api_view(['GET'])
def getItems(request, pk):
    try:
        timeline = Timeline.objects.get(id=pk)
        items = timeline.item_set.all()
    except Timeline.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializerItems = ItemSerializer(items, many=True)
    serializerTimeline = TimelineSerializer(timeline, many=False)

    response_data = {'timeline': serializerTimeline.data,
                     'items': serializerItems.data}

    for item in response_data['items']:
        if item['end'] is None:
            del item['end']

    return Response(response_data)


@api_view(['POST'])
def createItem(request, pk):
    data = request.data

    timeline = Timeline.objects.get(id=pk)

    if data['end'] == '':
        data['end'] = None

    item = Item.objects.create(
        timeline=timeline,
        title=data['title'],
        start=data['start'],
        end=data['end'],
        type=data['type'],
        style=data['style'],
        content=data['content'],
        notesDetails=data['notesDetails'],
        bgColor=data['bgColor'],
        textColor=data['textColor'],
        borderColor=data['borderColor'],
        fontSize=data['fontSize'],
        fontStyle=data['fontStyle'],
        fontWeight=data['fontWeight']
    )

    serializerItem = ItemSerializer(item, many=False)
    serializerTimeline = TimelineSerializer(timeline, many=False)

    response_data = {'timeline': serializerTimeline.data,
                     'item': serializerItem.data}

    if response_data['item']['end'] is None:
        del response_data['item']['end']

    return Response(response_data)


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
