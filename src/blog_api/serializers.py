from rest_framework import serializers
from blog.models import Post
from rest_framework.reverse import reverse



class Post_serializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only = True)
    writer = serializers.SerializerMethodField(read_only = True)
    category = serializers.SerializerMethodField(read_only = True)  
    category = serializers.SerializerMethodField(read_only = True)  
    thumbnail_url = serializers.SerializerMethodField(read_only = True)  

    class Meta:
        model = Post
        fields = ['url','id','headline','sub_headline','thumbnail_url','body','slug','publish_status','published','created','category','writer']

    def get_writer(self,obj):
        return {
            'username': obj.author.username,
            'id':obj.author.id,
            
        }
    def get_category(self,obj):
        
        return {
            "category": obj.catagory.name,
            "id": obj.catagory.id,
        }


    def get_thumbnail_url(self, obj):
      
        request = self.context.get("request")
        return request.build_absolute_uri(obj.get_image_url())


    def get_url(self, obj): 

        request = self.context.get('request')
        

        if request is None:
            return None

        return reverse('blog:detail', kwargs={"pk": obj.pk, "slug":obj.slug}, request=request)







