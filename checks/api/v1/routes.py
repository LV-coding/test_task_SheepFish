from django.urls import path
from checks.api.v1.views import CreateCheckViewSet, CheckListViewSet

urlpatterns = [
    path("new", CreateCheckViewSet.as_view(), name="checks-create"),
    path("", CheckListViewSet.as_view(), name="checks"),
]
