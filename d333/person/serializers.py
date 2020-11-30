from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Person


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    surn = serializers.CharField(max_length=20)
    pasw1 = serializers.CharField(max_length=20)
    pasw2 = serializers.CharField(max_length=20)
    status = serializers.IntegerField(min_value=0, max_value=1)

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs.get("pasw1") == attrs.get("pasw2"):
            ex = Person.objects.filter(name=attrs.get('name'),
                                       surn=attrs.get('surn'))
            if ex and len(ex) > 0:
                instance = ex[len(ex) - 1]
                PersonSerializer.update(self, instance, attrs)
                raise ValidationError({"request_data_status": "Was updated."})
            else:
                return attrs
        else:
            raise ValidationError(detail="Passwords is not correct: '"'{}'"' is not '"'{}'"'"
                                         .format(attrs.get("pasw1"), attrs.get("pasw2")))

    def update(self, instance, validated_data):
        ex = Person.objects.filter(pk=instance.id)
        ex.update(**validated_data)
        if len(ex) > 0:
            instance = ex[len(ex) - 1]
        instance.save()
        return ex
