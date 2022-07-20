from rest_framework import views, response, filters,generics
from bills.models import Bill
from bills.serializers import BillSerializer
import pylightxl as xl

from bills.utils import validate_bill


# {"filename":"bills.xlsx"}
class CreateBillsView(views.APIView):

    def post(self, request):
        filename = request.data.get('filename')
        db = xl.readxl(filename)
        data = list(db.ws(db.ws_names[0]).rows)

        validated_data = validate_bill(data)
        serializer = BillSerializer(data=validated_data,many = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return response.Response(serializer.data)


class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['client_name', 'client_org']
