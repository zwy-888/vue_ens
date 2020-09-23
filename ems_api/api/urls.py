from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from api import views

urlpatterns = [
    # url(r'^login/', obtain_jwt_token),
    path('login/', views.UserAPIView1.as_view({'post': 'login'})),
    path('register/', views.UserAPIView.as_view({'post': 'register'})),
    path('emp/', views.EmployeeGenericAPIView.as_view()),
    path('emp/<str:id>/', views.EmployeeGenericAPIView.as_view()),
]
