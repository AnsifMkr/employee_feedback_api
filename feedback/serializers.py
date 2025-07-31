from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Designation, Employee, FeedbackQuestion, FeedbackSubmission, FeedbackAnswer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = ['id', 'name']


class FeedbackQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackQuestion
        fields = ['id', 'question_text', 'feedback_type']


class FeedbackAnswerSerializer(serializers.ModelSerializer):
    question_text = serializers.CharField(source='question.question_text', read_only=True)

    class Meta:
        model = FeedbackAnswer
        fields = ['question', 'question_text', 'rating', 'comment']


class FeedbackSubmissionSerializer(serializers.ModelSerializer):
    employee = serializers.IntegerField(write_only=True)
    employee_name = serializers.SerializerMethodField(read_only=True)
    designation = serializers.CharField()
    submitted_by = serializers.SerializerMethodField()
    answers = FeedbackAnswerSerializer(many=True)

    class Meta:
        model = FeedbackSubmission
        fields = ['id', 'employee', 'employee_name', 'designation', 'submitted_by', 'created_at', 'answers']
        read_only_fields = ['submitted_by', 'employee_name']

    def get_employee_name(self, obj):
        return obj.employee.user.username if obj.employee else None

    def get_submitted_by(self, obj):
        return obj.submitted_by.username if obj.submitted_by else None

    def create(self, validated_data):
        from .models import Employee
        employee_id = validated_data.pop('employee')
        try:
            employee_obj = Employee.objects.get(id=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError({"employee": "Employee not found."})

        designation_name = validated_data.pop('designation')
        designation_obj, _ = Designation.objects.get_or_create(name=designation_name)

        answers_data = validated_data.pop('answers')
        request = self.context.get('request')

        submission = FeedbackSubmission.objects.create(
            employee=employee_obj,
            designation=designation_obj,
            submitted_by=request.user,
            **validated_data
        )

        for ans in answers_data:
            FeedbackAnswer.objects.create(submission=submission, **ans)

        return submission

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['designation'] = instance.designation.name
        return rep
