from django.urls import path
from .views import CarsList,CarDetail

urlpatterns = [
     path('/',CarsList.as_view(), name='Cars_List'),
     path('/<int:pk>/',CarDetail.as_view(),name='Car_Detail'),
    #  path('api-auth/', include('rest_framework.urls'))
]
