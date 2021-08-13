
### receipt upload start ***
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
### receipt upload end ***


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
)

from .permissions import IsOwnerOrReadOnly

 ### receipt upload start ***
import pytesseract
import cv2
import json
from django.views.decorators.csrf import csrf_exempt

try:
    from PIL import Image
except: 
    import Image
 ### receipt upload end ***

#### Create Expense
class ExpenseCreate(CreateAPIView):
    
    ### receipt upload start ***
    ## form** 
    form_class = Expense

    parser_classes = (MultiPartParser, FormParser)
    ### receipt upload end ***

    queryset = Expense.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ExpenseCreateSerializer

    ### receipt upload start ***
    # def form_valid(self, form):
    #     upload = self.request.FILES['file']
    #     print(type(pytesseract.image_to_string(Image.open(upload))))
    #     return super().form_valid(form)
@csrf_exempt
def process_image(request):
    if request.method == 'POST':
        response_data = {}
        upload = request.FILES['file']
        content = pytesseract.image_to_string(Image.open(upload))
        response_data['content'] = content

        return JsonResponse(response_data)

    ### receipt upload start ***


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



