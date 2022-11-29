from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import LiveVideo
from .serializers import LiveVideoSerializer


# Create your views here.
@csrf_exempt
def live_video_list(request):
    if request.method == 'GET':
        content = LiveVideo.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "name": "Mới ra mắt",
            "data": list(
                content.values('created', '_id', 'name', 'description', 'slug', 'durationStr', 'coverImage', 'link'))
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LiveVideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def live_video_detail(request, pk):
    try:
        content = LiveVideo.objects.get(pk=pk)
    except LiveVideo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        content = LiveVideo.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "name": "Video của bạn",
            "data": list(
                content.values('created', '_id', 'name', 'description', 'slug', 'durationStr', 'coverImage', 'link'))
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LiveVideoSerializer(content, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        content.delete()
        return HttpResponse(status=204)