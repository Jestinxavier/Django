from django.urls import path
from .views import CategoryListCreateView
from .views import CategoryBulkImportView

urlpatterns = [
    path('', CategoryListCreateView.as_view(), name='categories'),
    path('bulk-import/', CategoryBulkImportView.as_view(), name='bulk-import'),
]
