from djoser.serializers import UserSerializer as DjoserUserSerializer


class DjoserUserSerializerWithRef(DjoserUserSerializer):
    class Meta(DjoserUserSerializer.Meta):
        ref_name = 'DjoserUser'
