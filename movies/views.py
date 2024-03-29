from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status,viewsets

from .models import Show
from .serializers import ShowSerializer,ShowDetailSerializer


@api_view(['GET'])
def shows_list(request):
    show = Show.objects.all()
    serializer = ShowSerializer(show,many=True).data
    return Response({'data':serializer}
                    ,status=status.HTTP_200_OK)

@api_view(['GET'])
def shows_detail(request,pk):
    show = get_object_or_404(Show,id=pk)
    serializer = ShowDetailSerializer(show).data
    return Response({'data':serializer}
                    ,status=status.HTTP_200_OK)

class ShowViewSets(viewsets.ModelViewSet):
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
    
