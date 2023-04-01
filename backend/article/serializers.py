from rest_framework import serializers

from .models import Group, Student, AccessPending


class StudentSerializer(serializers.Serializer):
    StudentId = serializers.CharField()
    name = serializers.CharField(max_length=255)
    email = serializers.CharField()
    AboutStudent = serializers.CharField()
    AccessCheck = serializers.BooleanField()
    Group = serializers.CharField()



class GroupSerializer(serializers.Serializer):
    GroupName = serializers.CharField(max_length=120)
    description = serializers.CharField()
    
    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.StudentId = validated_data.get('StudentId', instance.StudentId)
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.AboutStudent = validated_data.get('AboutStudent', instance.AboutStudent)
        instance.Group = validated_data.get('Group', instance.Group)
        instance.GroupName = validated_data.get('GroupName', instance.GroupName)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class ConnectedDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessPending
        fields = ('DeviceName', 'connected_at', 'status')