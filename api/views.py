from students.models import Student
from .serializers import StudentSerializer 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from .serializers import EmployeeSerializer
from django.http import Http404
from rest_framework import mixins, generics, viewsets
from django.shortcuts import get_object_or_404
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .paginations import CustomPagination
from employees.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter

# function based views
# get all students
'''
@api_view(["GET","POST"])
def studentView(request):
    if request.method == "GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExists:
        return Response({"error":"student not found"}, status=status.HTTP_404_NOT_FOUND)
    # to get single user with pk
    if request.method =="GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # to update user 
    elif request.method == "PUT":

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    # to delete user
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_404_NO_CONTENT)
'''
    

# mixins of student view
# class StudentView(mixins.CreateModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)


# class StudentDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request,pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)



# # generics method
# # class StudentView(generics.ListCreateAPIView):
# #     queryset = Student.objects.all()
# #     serializer_class = StudentSerializer

# # class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = "pk"



# generics 
# class StudentView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = "pk"



# viewset for student
# class StudentViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Student.objects.all()
#         serializer = StudentSerializer(queryset, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    

#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#     def retrieve(self, request, pk):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk:None):
#         student = get_object_or_404(Student, pk=pk)
#         serializer = StudentSerializer(student, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
        

#     def delete(self, request, pk:None):
#         student = get_object_or_404(Student, pk=pk)
#         student.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)    
        

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

'''
# class based views
class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK )
    
    def post(self, request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetail(APIView):
  def get_object(self, pk):
      try:
          employee = Employee.objects.get(pk=pk)
          return employee
      except Employee.DoesNotExist:
          return Http404
      
  def get(self,request,pk):
          employee = self.get_object(pk)
          serializer = EmployeeSerializer(employee)
          return Response(serializer.data, status=status.HTTP_200_OK)
    
  def put(self,request,pk):
      employee = self.get_object(pk)
      serializer = EmployeeSerializer(employee, data = request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_200_OK)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request,pk):
      employee = self.get_object(pk)
      employee.delete()
      return Response(status=status.HTTP_404_NOT_FOUND)
'''


'''
# mixins
# peforming  get,post, put,delete methods using mixins 

class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    

    def post(self, request):
        return self.create(request)
    

class EmployeeDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# to get single employee with their primary key
    def get(self,request, pk):
        return self.retrieve(request, pk)

# to update a single employee detail with their primary key
    def put(self, request, pk):
        return self.update(request, pk)    
    
# to delete the employee with the primary key
    def delete(self, request, pk):
        return self.destroy(request, pk)


# using generics 
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'

'''

'''
# generics of employee
class Employees(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = "pk"
'''

 # view sets
# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmployeeSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def retrieve(self, request, pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmployeeSerializer(employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
#     def delete(self, request, pk):
#         employee = get_object_or_404(Employee, pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_404_NOT_FOUND)

# model view set 
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class= CustomPagination
    filterset_class = EmployeeFilter


class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['blog_title','blog_body']
    ordering_fields=['id','blog_title']


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView): 

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = "pk"





