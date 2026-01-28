from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.permissions import AllowAny

from apps.accounts.permissions import Is_Admin
from .models import Category
from .serializer import CategoriesListSerializer,CategoriesCreateSerializer


class CategoriesListView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer
    
class CategoriesCreateView(CreateAPIView):
    permission_classes = [Is_Admin]
    queryset = Category.objects.all()
    serializer_class = CategoriesCreateSerializer
    
class CategoriesDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [Is_Admin]
    queryset = Category.objects.all()
    serializer_class = CategoriesListSerializer
    
    lookup_field = "id"