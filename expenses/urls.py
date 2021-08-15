from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from .views import (
    ExpenseCreate,
    ExpenseList,
    ExpenseDetail,
    ExpenseDelete,
    ExpenseUpdate,
    UploadReceipt,
)

urlpatterns = [
    path('', ExpenseList.as_view(), name='expense_list'),
    path('create/', ExpenseCreate.as_view(), name='expense_create'),
    path('upload/', UploadReceipt.as_view(), name='receipt_upload'),
    path('<int:pk>/', ExpenseDetail.as_view(), name='expense_detail'),
    path('<int:pk>/edit/', ExpenseUpdate.as_view(), name='expense_update'),
    path('<int:pk>/delete/', ExpenseDelete.as_view(), name='expense_delete'),
]