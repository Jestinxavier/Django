from rest_framework.generics import ListCreateAPIView
from .models import Category
from .serializers import CategorySerializer
from .pagination import CategoryPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination
    
class CategoryBulkImportView(APIView):

    def create_or_update_category(self, data, parent=None):
        category, created = Category.objects.update_or_create(
            name=data['name'],
            parent=parent,
            defaults={}
        )

        children = data.get('children', [])

        for child in children:
            self.create_or_update_category(child, category)

        return category

    def post(self, request):
        categories = request.data

        if not isinstance(categories, list):
            return Response(
                {"error": "Expected list of categories"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for category_data in categories:
            self.create_or_update_category(category_data)

        return Response(
            {"message": "Bulk import successful"},
            status=status.HTTP_201_CREATED
        )

    def create_or_update_category(self, data, parent=None):
        category, created = Category.objects.update_or_create(
            name=data['name'],
            parent=parent,
            defaults={}
        )

        children = data.get('children', [])

        for child in children:
            self.create_or_update_category(child, category)

        return category

    def post(self, request):
        categories = request.data

        if not isinstance(categories, list):
            return Response(
                {"error": "Expected a list of categories"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for category_data in categories:
            self.create_or_update_category(category_data)

        return Response(
            {"message": "Categories imported successfully"},
            status=status.HTTP_201_CREATED
        )

    def create_or_update_category(self, data, parent=None):
        category, created = Category.objects.update_or_create(
            name=data['name'],
            parent=parent,
            defaults={}
        )

        children = data.get('children', [])

        for child in children:
            self.create_or_update_category(child, category)

        return category

    def post(self, request):
        categories = request.data

        if not isinstance(categories, list):
            return Response(
                {"error": "Expected a list of categories"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for category_data in categories:
            self.create_or_update_category(category_data)

        return Response(
            {"message": "Categories imported successfully"},
            status=status.HTTP_201_CREATED
        )