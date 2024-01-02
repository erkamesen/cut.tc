from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BaseURLSerializer, RedirectURLSerializer
from .models import BaseURL, RedirectURL
from rest_framework.authtoken.models import Token
# Create your views here.


class BaseURLListCreateView(ListCreateAPIView):
    queryset = BaseURL.objects.all()
    serializer_class = BaseURLSerializer
    
    
class BaseURLRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = BaseURL.objects.all()
    serializer_class = BaseURLSerializer
    lookup_field = "pk"
    
    
class RedirectURLListCreateView(ListCreateAPIView):
    queryset = RedirectURL.objects.all()
    serializer_class = RedirectURLSerializer
    
    
class RedirectURLRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = RedirectURL.objects.all()
    serializer_class = RedirectURLSerializer
    lookup_field = "pk"
    
    
class ProfilListCreateView(ListCreateAPIView):
    queryset = ...  
    serializer_class = ... 
    lookup_field = ...
    class Meta:
       ...
    
    
class ProfilRetrieveUpdateDestryoView(RetrieveUpdateDestroyAPIView):
    queryset = ...  
    serializer_class = ... 
    lookup_field = ...
    class Meta:
       ...
