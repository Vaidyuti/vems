from rest_framework import serializers

from .models import Generation, Load, Prosumer, Storage


class GenerationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Generation
        fields = (
            "url",
            "prosumer",
            "category_group",
            "category",
            "installed_capacity",
            "efficiency",
            "asset_value",
            "payback_period",
        )


class LoadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Load
        fields = (
            "url",
            "prosumer",
            "max_power",
            "is_dr_adaptive",
        )


class ProsumerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prosumer
        fields = (
            "url",
            "user",
            "location",
            "max_import_power",
            "max_export_power",
            "is_dr_adaptive",
            "category",
        )
        read_only_fields = ("user",)


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Storage
        fields = (
            "url",
            "prosumer",
            "category",
            "installed_capacity",
            "usable_capacity",
            "health",
        )
