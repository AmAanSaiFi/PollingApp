from rest_framework import serializers
from .models import Question,Choice
        

class choiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            'choice_text',
            'votes'
        ]

class questionSerializer(serializers.ModelSerializer):
    choices = choiceSerializer(many=True)
    class Meta:
        model = Question
        fields = [
            'id',
            'question_text',
            'pub_date',
            'choices',
        ]