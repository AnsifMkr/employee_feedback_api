from rest_framework import generics, permissions
from django.utils.timezone import make_aware
from datetime import datetime
from .models import FeedbackQuestion, FeedbackSubmission
from .serializers import UserSerializer, FeedbackQuestionSerializer, FeedbackSubmissionSerializer


from django.http import JsonResponse
def test(request):
    return JsonResponse({"status": "API is running"})



class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer



class FeedbackQuestionListView(generics.ListAPIView):
    serializer_class = FeedbackQuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        f_type = self.request.query_params.get('feedback_type')
        return FeedbackQuestion.objects.filter(feedback_type=f_type) if f_type else FeedbackQuestion.objects.all()



class FeedbackSubmissionView(generics.CreateAPIView):
    serializer_class = FeedbackSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {"request": self.request}



class DesignationFeedbackView(generics.ListAPIView):
    serializer_class = FeedbackSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        designation_name = self.kwargs['designation_name']
        return FeedbackSubmission.objects.filter(designation__name=designation_name)



class AdminFeedbackView(generics.ListAPIView):
    serializer_class = FeedbackSubmissionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        qs = FeedbackSubmission.objects.all()
        designation = self.request.query_params.get('designation')
        department = self.request.query_params.get('department')
        start = self.request.query_params.get('start_date')
        end = self.request.query_params.get('end_date')

        if designation:
            qs = qs.filter(designation__name=designation)
        if department:
            qs = qs.filter(employee__department=department)
        if start and end:
            start_dt = make_aware(datetime.strptime(start, "%Y-%m-%d"))
            end_dt = make_aware(datetime.strptime(end, "%Y-%m-%d"))
            qs = qs.filter(created_at__range=[start_dt, end_dt])

        return qs
