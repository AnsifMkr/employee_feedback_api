from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    test, RegisterUserView, FeedbackQuestionListView,
    FeedbackSubmissionView, DesignationFeedbackView,
    AdminFeedbackView
)

urlpatterns = [
    path("", test),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('questions/', FeedbackQuestionListView.as_view(), name='questions'),
    path('submit-feedback/', FeedbackSubmissionView.as_view(), name='submit-feedback'),

    path('designation/<str:designation_name>/feedback/', DesignationFeedbackView.as_view(), name='designation-feedback'),
    path('admin/feedback/', AdminFeedbackView.as_view(), name='admin-feedback'),
]
