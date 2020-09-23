from django.shortcuts import render

# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import User, Employee
from api.serializer import UserModelSerializer, EmpModelSerializer, UserModelSerializer1
from utils.response import APIResponse


# 这里可以使用非标接口ModelViews
class UserAPIView(ModelViewSet):

    @staticmethod
    def register(request, *args, **kwargs):
        print('111111111')
        request_data = request.data
        print('44444', request_data)
        print('33333', request)
        serializer = UserModelSerializer(data=request_data, context={"request": request_data})
        # 做校验才会走钩子 ，反序列化要使用data=
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        data = UserModelSerializer(user_obj).data
        return APIResponse(200, True, results=data)


class UserAPIView1(ModelViewSet):
    authentication_classes = []
    permission_classes = []

    @staticmethod
    def login(request, *args, **kwargs):
        print('2222222222')
        print(request.data)
        username = request.data.get('account')
        password = request.data.get('pwd')
        print(username, password)
        # user_obj = User.objects.filter(username=username, password=password).first()

        # if user_obj:
        #     print("开始")
        #     data = UserModelSerializer1(user_obj).data
        #     print('11111', data)
        serializer = UserModelSerializer1(data=request.data)
        ser = serializer.is_valid()
        if ser:
            data = UserModelSerializer1(serializer.obj).data
            token = serializer.token
            print("获取token")
            print(token)

            return APIResponse(200, True, results=data, token=token)
        return APIResponse(400, False)


class EmployeeGenericAPIView(ListModelMixin, GenericAPIView, CreateModelMixin, DestroyModelMixin, UpdateModelMixin,
                             RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmpModelSerializer
    lookup_field = 'id'

    # 登陆时获取所有的员工信息   （单个 ，所有 ）
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        # print('1111', kwargs)
        if 'id' in kwargs:
            response = self.retrieve(request, *args, **kwargs)  # 查询单个 用谁就继承谁
            return APIResponse(200, True, results=response.data)
        else:
            response = self.list(request, *args, **kwargs)  # list 查询所有
            return APIResponse(200, True, results=response.data)
        # response = self.list(request, *args, **kwargs)
        # # response = self.(request, *args, **kwargs)
        # return APIResponse(200, True, results=response.data)

    # 添加 （单个）
    def post(self, request, *args, **kwargs):
        emp_obj = self.create(request, *args, **kwargs)
        return APIResponse(200, True, results=emp_obj.data)

    # 删除 （单个）
    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)
        return APIResponse(200, True, )

    # 更新
    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        print(response, type(response))
        return APIResponse(200, True, results=response.data)
