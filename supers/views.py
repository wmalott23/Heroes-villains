from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from super_types.models import SuperType
from super_types.serializers import SuperTypeSerializer
from .serializers import SuperSerializer
from .models import Super

# Create your views here.

@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        type_param = request.query_params.get('type')
        custom_response_dict = {}
        supers = SuperType.objects.all()
        sup_response = Super.objects.all()
        if type_param:
            supers = SuperType.objects.filter(type=type_param)
            sup_response = Super.objects.filter(super_type__type=type_param)
        for each in supers:
            super_serializer = SuperSerializer(sup_response, many=True)
            custom_response_dict[each.type] = {
                "supers": super_serializer.data
            }
        return Response(custom_response_dict)
    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    name = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(name)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(name, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
