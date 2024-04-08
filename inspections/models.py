# inspections/models.py
from django.db import models
from django.contrib.auth import get_user_model
from vessels.models import Vessel

User = get_user_model()


class InspectionTemplate(models.Model):
    title = models.CharField(max_length=255)
    comments_enabled = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Template: {self.title} - Comments Enabled: {'Yes' if self.comments_enabled else 'No'}"


class Section(models.Model):
    inspection_template = models.ForeignKey(InspectionTemplate, related_name='sections', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        questions_count = self.questions.count()
        return f"{self.title} (Order: {self.order}, Questions: {questions_count})"


class Question(models.Model):
    section = models.ForeignKey(Section, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    order_for_customer = models.PositiveIntegerField(default=0)
    order_for_inspector = models.PositiveIntegerField(default=0)
    comment_required = models.BooleanField(default=False)

    def __str__(self):
        return f"Question: {self.text}"


class Inspection(models.Model):
    vessel = models.ForeignKey(Vessel, related_name='inspections', on_delete=models.CASCADE)
    inspection_template = models.ForeignKey(InspectionTemplate, related_name='used_inspections',
                                            on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField()
    inspector_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Inspection for {self.vessel.name} on {self.date}"


class InspectionResponse(models.Model):
    inspection = models.ForeignKey(Inspection, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.CharField(max_length=255, blank=True, null=True)  # Adjust based on your response types
    photo = models.ImageField(upload_to='inspection_responses/', blank=True, null=True)
    additional_comment = models.TextField(blank=True, null=True)


class Comment(models.Model):
    inspection = models.ForeignKey(Inspection, related_name='comments', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f"Comment by {self.author} on {self.question.text}"


class Photo(models.Model):
    question = models.ForeignKey(Question, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='question_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Photo for question {self.question.id} uploaded at {self.uploaded_at}"
