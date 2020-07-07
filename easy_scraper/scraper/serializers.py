from rest_framework import serializers

from .models import Link


class LinkSeralizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    address = serializers.CharField(max_length=100, required=True)
    link_name = serializers.CharField(max_length=100, required=True)

    def create(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.link_name = validated_data.get('link_name', instance.link_name)
        instance.save()
        return instance



class LinkModelSerialzier(serializers.Serializer):
    class Meta:
        model = Link
