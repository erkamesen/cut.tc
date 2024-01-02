from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CodeSerializer, RedirectURLSerializer
from .models import Code, RedirectURL
from rest_framework.authtoken.models import Token
# Create your views here.


class CodeListCreateView(ListCreateAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
    
    
class BCodeRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Code.objects.all()
    serializer_class = CodeSerializer
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
