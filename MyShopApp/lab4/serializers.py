from rest_framework import serializers
from .models import Person, Team, MonthBirth


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=50, required=True)
    month_birth = serializers.ChoiceField(choices=MonthBirth)
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all)
    created_at = serializers.DateTimeField()

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.month_birth = validated_data.get('month_birth', instance.month_birth)
        instance.team = validated_data.get('team', instance.team)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, required=True)
    country = serializers.CharField(max_length=2, required=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('country', instance.country)
        instance.save()
        return instance


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'month_birth', 'team', 'created_at']
        read_only_fields = ['id']
