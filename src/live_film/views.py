from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import LiveFilm
from .serializers import LiveFilmSerializer


# Create your views here.
@csrf_exempt
def live_film_list(request):
    if request.method == 'GET':
        content = LiveFilm.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "name": "Phim thịnh hành",
            "data": list(
                content.values('created', '_id', 'coverImage', 'coverImageH', 'description', 'slug', 'type', 'link'))
        }
        return JsonResponse(data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LiveFilmSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def live_film_detail(request, pk):
    try:
        content = LiveFilm.objects.get(pk=pk)
    except LiveFilm.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        content = LiveFilm.objects.all()
        data = {
            "errorCode": 200,
            "message": "Successful.",
            "data": list(
                content.values('created', '_id', 'coverImage', 'coverImageH', 'description', 'slug', 'type', 'link'))
        }
        return JsonResponse(data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LiveFilmSerializer(content, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        content.delete()
        return HttpResponse(status=204)