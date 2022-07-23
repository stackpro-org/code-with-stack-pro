from rest_framework import serializers
from blog.models import Post
from rest_framework.reverse import reverse



class Post_serializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only = True)
    author = serializers.SerializerMethodField(read_only = True)
    category = serializers.SerializerMethodField(read_only = True)  

    class Meta:
        model = Post
        fields = ['url','id','headline','sub_headline','get_image_url','body','slug','publish_status','published','created','category','author']

    def get_author(self,obj):
        return {
            'username': obj.author.username,
            'id':obj.author.id,
        }
    def get_category(self,obj):
        return {
            "category": obj.catagory.name,
            "id": obj.catagory.id,
        }


    def get_url(self, obj): 

        request = self.context.get('request') 

        if request is None:
            return None

        return reverse('blog:detail', kwargs={"pk": obj.pk, "slug":obj.slug}, request=request)







