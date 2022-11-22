from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import LiveTv
from .serializers import LiveTvSerializer


# Create your views here.
@csrf_exempt
def live_tv_list(request):
    if request.method == 'GET':
        content = LiveTv.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "name": "Kênh TV",
            "data": list(
                content.values('created', '_id', 'name', 'description', 'slug', 'type', 'coverImage', 'horizontalImage',
                               'needLogin', 'price', 'link'))
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LiveTvSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def live_tv_detail(request, pk):

    try:
        content = LiveTv.objects.get(pk=pk)
    except LiveTv.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LiveTvSerializer(content)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LiveTvSerializer(content, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        content.delete()
        return HttpResponse(status=204)
