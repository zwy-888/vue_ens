import re

from rest_framework import exceptions, serializers
from rest_framework.permissions import IsAdminUser
from rest_framework.serializers import ModelSerializer
from rest_framework.throttling import UserRateThrottle
# from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User

        fields = ('username', 'real_name', 'password', 'gender',)
        extra_kwargs = {
            'username': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'min_length': '长度不够',
                    'required': '用户名必须填写'
                }
            },
            'real_name': {
                'required': True,
            },
            'password': {
                'required': True,
            }
        }

    def validate_username(self, value):
        print('1111111111', value)
        user1 = User.objects.filter(username=value).first()
        if user1:
            raise exceptions.ValidationError("用户名已存在")
        return value

    def validate(self, attrs):
        print("111", attrs)
        request = self.context.get('request')
        print("22222", request)
        pwd = attrs.get("password")
        re_pwd = request.get('re_pwd')
        print('1111', re_pwd)
        # 自定义校验规则  两次密码不一致  则无法保存对象
        if pwd != re_pwd:
            raise exceptions.ValidationError("两次密码不一致")
        return attrs


class UserModelSerializer1(ModelSerializer):
    # class Meta:
    #     model = User
    #     fields = ('username', 'real_name', 'password', 'gender',)
    #     extra_kwargs = {
    #         'username': {
    #             'required': True,
    #             'min_length': 2,
    #             'error_messages': {
    #                 'min_length': '长度不够',
    #                 'required': '用户名必须填写'
    #             }
    #         },
    #         'real_name': {
    #             'required': True,
    #         },
    #         'password': {
    #             'required': True,
    #         }
    #     }
    #
    #     def validate(self, attrs):
    #         username = attrs.get("username")
    #         password = attrs.get("password")
    #
    #         # 对于前端传递的参数格式进行验证  邮箱  用户名  手机号
    #         # if re.match(r'.+@.+', account):
    #         user_obj = User.objects.filter(username=username).first()
    #         # elif re.match(r'1[3-9][0-9]{9}', account):
    #         #     user_obj = User.objects.filter(phone=account).first()
    #         # else:
    #         #     user_obj = User.objects.filter(username=account).first()
    #
    #         # 判断用户是否存在 且用户密码是否正确
    #         if user_obj and user_obj.check_password(password):
    #             # 签发token
    #             payload = jwt_payload_handler(user_obj)  # 生成载荷
    #             token = jwt_encode_handler(payload)  # 生成token
    #             # print('token', token)
    #             self.token = token
    #             self.obj = user_obj
    #         return attrs
    account = serializers.CharField(write_only=True)
    pwd = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["account", "pwd", "username", "email"]

        extra_kwargs = {
            "username": {
                "read_only": True,
            },
            # "phone": {
            #     "read_only": True,
            # },
            "email": {
                "read_only": True,
            },
        }

    # 完成token的生成
    def validate(self, attrs):
        print(self)
        print(attrs)
        print('钩子')
        account = attrs.get("account")
        pwd = attrs.get("pwd")
        print('account', account, pwd)

        # 对于前端传递的参数格式进行验证  邮箱  用户名  手机号
        # # if re.match(r'.+@.+', account):
        user_obj = User.objects.filter(username=account).first()
        # elif re.match(r'1[3-9][0-9]{9}', account):
        #     user_obj = User.objects.filter(phone=account).first()
        # else:
        #     user_obj = User.objects.filter(username=account).first()

        # 判断用户是否存在 且用户密码是否正确
        if user_obj: #and user_obj.check_password(pwd)
            # 签发token
            print("签发token")
            payload = jwt_payload_handler(user_obj)  # 生成载荷
            token = jwt_encode_handler(payload)  # 生成token
            print('token', token)
            self.token = token
            self.obj = user_obj

        return attrs


class EmpModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        extra_kwargs = {
            'emp_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'min_length': '长度不够',
                    'required': '用户名必须填写'
                }
            },
        }
