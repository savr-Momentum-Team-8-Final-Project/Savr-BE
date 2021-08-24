
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
    UploadReceiptSerializer
)
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response

from rest_framework.exceptions import ParseError
from PIL import Image
import numpy as np
from scripts import ocr
from django.views.decorators.csrf import csrf_exempt

#### Create Expense
class ExpenseCreate(CreateAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = ExpenseCreateSerializer

   
#### upload photo is working 
class ReceiptView(APIView):
## this part is working !!
    permission_classes = [AllowAny]
<<<<<<< HEAD
    parser_classes = [MultiPartParser, FormParser]
=======
    parser_classes = [MultiPartParser,FormParser]
>>>>>>> 833f4978d470c55fec64d7b122004a415e777b1a

    def post(self, request, *args, **kwargs):
        expense = get_object_or_404(Expense.objects.all(),pk=self.kwargs['pk'])
        # serializer = UploadReceiptSerializer(data=request.data)
        
        
        if "file" in request.data:
            file=request.data["file"]
            expense.file.save(file.name, file, save=True)
            pil_img = Image.open(expense.file)
            ### img to array
            img = np.array(pil_img)
            
            expense.content = ocr.OcrReceipt(img)      
            expense.save()

        serializer = UploadReceiptSerializer(expense)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        

        
        
        

    def get(self,request, *args, **kwargs):
        expense = get_object_or_404(Expense.objects.all(),pk=self.kwargs['pk'])
        if "file" in request.data:
            file=request.data["file"]
            expense.file.save(file.name, file, save=True)
            pil_img = Image.open(expense.file)
            ### img to array
            img = np.array(pil_img)
            
            expense.content = ocr.OcrReceipt(img) 
        serializer = UploadReceiptSerializer(expense)

        return Response(serializer.data)




###  ** list answers ---- and add/create
class ExpenseList(ListAPIView):
    queryset = Expense.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    # queryset = Book.objects.all()
    serializer_class = ExpenseListSerializer



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



