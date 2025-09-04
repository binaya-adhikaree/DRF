from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename="employees")
router.register('students', views.StudentViewSet, basename="students")


urlpatterns = [
    path('', include(router.urls)),


    # path('employees/', views.Employees.as_view()),
    # path('employee/<int:pk>/', views.EmployeeDetail.as_view()),


    # path("students/",views.StudentView.as_view() ),
    # path("student/<int:pk>/", views.StudentDetailView.as_view()),

    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

    # path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    # path('comments/<int:pk>/', views.CommentDetailView.as_view())

    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),


]


