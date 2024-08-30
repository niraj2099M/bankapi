from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, viewsets
from .models import Banks,Branches
from .serializiers import BankSerializer,BranchSerializer
# Create your views here.



class BankList (generics.ListAPIView):
    queryset=Banks.objects.all()
    serializer_class=BankSerializer




@api_view(['POST'])
def branch_details(request):
    ifsc = request.data.get("ifsc")    
    
    try:
        branch=Branches.objects.get(ifsc=ifsc)
        serializer = BranchSerializer(branch, many=False)
        return Response(serializer.data)         
    except Exception:
        return Response({"error": "Invalid IFSC code"}, status=400)
    



