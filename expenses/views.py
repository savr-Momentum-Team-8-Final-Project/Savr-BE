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

#### Create Expense
class ExpenseCreate(CreateAPIView):
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