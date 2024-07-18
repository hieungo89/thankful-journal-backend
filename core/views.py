from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import EntrySerializer
from .models import Entries

# Create your views here.
def frontend(request):
  context = { }
  return render(request, "index.html", context)

@api_view(['GET', 'POST'])
def entry(request):
    if request.method == 'GET':
        entry = Entries.objects.all()
        serializer = EntrySerializer(entry, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def entry_detail(request, pk):
    try:
        entry = Entries.objects.get(pk=pk)
        print('entry to delete', entry)
    except Entries.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
