from django.urls import path,include

from bills.views import BillListView, CreateBillsView

urlpatterns = [
    path('upload', CreateBillsView.as_view()),
    path('list', BillListView.as_view())

]
