from rest_framework import serializers

from test_app.models import Category, Product, Tag, Image, Promotion


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',
                  'image')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id',
                  'name')

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'src', 'name')





class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    tags = TagSerializer(many=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id',
                  'name',
                  'price',
                  'tags',
                  'category',
                  'images',
                  'serial',
                  'description',
                  'created_at')

    def get_category(self, instance):
        return CategorySerializer(instance.category).data

    def get_images(self, instance):
        images = Image.objects.filter(product=instance)
        if images:
            images = ImagesSerializer(images, many=True).data
        return images


class PromotionSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotion
        fields = ('id',
                  'name',
                  'product',
                  'image')

    def get_product(self, instance):
        return ProductSerializer(instance.product).data

    def get_image(self, instance):
        return ImagesSerializer(instance.image).data



