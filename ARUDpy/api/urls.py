from django.urls import path,include
from .views import TodoAPIView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', TodoAPIView)

urlpatterns = [
    path('', include(router.urls)),
    # path('', TodoAPIView.as_view(), name='todo'),
]
