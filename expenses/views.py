
### receipt upload start ***
from rest_framework.parsers import (
    FileUploadParser,
    MultiPartParser, 
    FormParser,
)
from rest_framework import status
import pytesseract
from rest_framework.views import APIView
from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView,
    DestroyAPIView,
    RetrieveUpdateAPIView,
    UpdateAPIView,
    CreateAPIView,
    get_object_or_404
    )

from rest_framework.permissions import(
    AllowAny,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated
)

from .models import Expense

from .serializers import (
    ExpenseCreateSerializer,
    ExpenseDetailSerializer,
    ExpenseListSerializer,
    UpdateExpenseSerializer,
    ExpenseUploadSerializer,
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

from rest_framework.exceptions import ParseError
from PIL import Image
from scripts import ocr

### upload receipt *** !!!!
        
class UploadReceipt(APIView):

    parser_classes = [FileUploadParser,]

    def put(self, request, *args, **kwargs):
        file_serializer = ExpenseUploadSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#### Create Expense
class ExpenseCreate(CreateAPIView):
    parser_classes = [FormParser, MultiPartParser]

    queryset = Expense.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ExpenseCreateSerializer



###  ** list answers ---- and add/create
class ExpenseList(ListAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = Book.objects.all()
    serializer_class = ExpenseListSerializer
    ### pagination 



### ** Expense details 
class ExpenseDetail(RetrieveAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Expense.objects.all()
    serializer_class = ExpenseDetailSerializer

    
### ** Expense delete   
class ExpenseDelete(DestroyAPIView):
    ### only author can update and delete ... 
    queryset = Expense.objects.all()
    serializer_class = ExpenseCreateSerializer
    permission_classes = [IsOwnerOrReadOnly]


### ** Expense update  
class ExpenseUpdate(RetrieveUpdateAPIView):
    queryset = Expense.objects.all()
    serializer_class = UpdateExpenseSerializer
    permission_classes = [IsOwnerOrReadOnly]



