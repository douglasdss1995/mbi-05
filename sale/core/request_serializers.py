from rest_framework import serializers


class DepartmentPaginatorSerializer(serializers.Serializer):
    qtd_departments = serializers.IntegerField(
        required=False,
        min_value=1,
        max_value=100,
        default=5
    )
