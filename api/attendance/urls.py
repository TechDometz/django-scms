from django.urls import path, include
from rest_framework.routers import DefaultRouter
from attendance.views import (
	AttendanceStatusViewSet, TeachersAttendanceViewSet, 
	TeachersAttendanceListView, TeachersAttendanceDetailView,TeachersAttendanceBulkCreateView)

'''
router = DefaultRouter()
router.register(r'status', AttendanceStatusViewSet)
router.register(r'teachers-attendance', TeachersAttendanceViewSet)

urlpatterns = [
	path('', include(router.urls))
]
'''

urlpatterns = [
	path('teachers-attendance/', TeachersAttendanceListView.as_view(), name="students-list"),
    path('teachers-attendance/<int:pk>/', TeachersAttendanceDetailView.as_view(), name="student-detail"),
	path("teachers-attendance/bulk/", TeachersAttendanceBulkCreateView.as_view(), name="teachers-attendance-bulk"),
]