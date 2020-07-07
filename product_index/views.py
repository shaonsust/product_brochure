from .models import App
from .serializers import AppListSerializer, AppDetailSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class AppList(ListAPIView):
    """
    API endpoint that allows all apps to be taken.
    """
    serializer_class = AppListSerializer
    queryset = App.objects.all()


class AppDetail(RetrieveAPIView):
    """
    API endpoint that allows user to get single app's details information.
    """
    serializer_class = AppDetailSerializer
    queryset = App.objects.all()
