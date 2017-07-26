from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.http.response import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# class CreateUserView(CreateAPIView):
#     """
#     Create a new User
#     """
#     model = User
#     permission_classes = (permissions.AllowAny, )
#     serializer_class = UserSerializer
#
#     def post(self, request):
#         data = request.data.copy()
#         class_object1= Class.objects.filter(school_name=request.data['school'],
#                                             class_name=request.data['student_class'])
#         if class_object1:
#             class_object1 = class_object1[0]
#         else:
#             class_object1 = None
#             data['student_class'] = ""
#             # return Response(data={'code': '3', 'message': '找不到班级!'}, status=status.HTTP_201_CREATED)
#
#         class_object2 = Class.objects.filter(school_name=request.data['school_second'],
#                                              class_name=request.data['student_class_second'])
#         if class_object2:
#             class_object2 = class_object2[0]
#         else:
#             class_object2 = None
#             data['student_class_second'] = ""
#             # return Response(data={'code': '3', 'message': '找不到班级!'}, status=status.HTTP_201_CREATED)
#         print(data)
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save(student_class=class_object1, student_class_second=class_object2)
#             return Response(data={'code': '0', 'message': 'Success!'}, status=status.HTTP_201_CREATED)
#         else:
#             return Response("Error!", status=status.HTTP_400_BAD_REQUEST)
#

# Create your views here.
def register(request):
    return HttpResponse("<h1>This is register page</h1>")

