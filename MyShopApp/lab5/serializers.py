import datetime

from rest_framework import serializers
from .models import Person, Team, MonthBirth


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.username')
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    month_birth = serializers.ChoiceField(choices=MonthBirth.choices, default=MonthBirth.choices[0][0])
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())
    created_at_month = serializers.IntegerField()
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.month_birth = validated_data.get('month_birth', instance.month_birth)
        instance.team = validated_data.get('team', instance.team)
        instance.created_at_month = validated_data.get('created_at_month', instance.created_at_month)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance

    def validate_first_name(self, first_name):
        if not first_name.isalpha():
            raise serializers.ValidationError("Nazwa nie powinna zawierać wartości liczbowych!")
        return first_name

    def validate_created_at_month(self, created_at_month):
        if created_at_month > datetime.datetime.today().month:
            raise serializers.ValidationError("Dane w polu 'miesiac_dodania' są nieprawidłowe!")
        return created_at_month
        
class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    country = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance
