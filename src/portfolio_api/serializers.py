
from rest_framework import serializers
from rest_framework.reverse import reverse
from portfolio.models import Portfolio, Category

#........................to have category 1st way 1................................
# class Catagory_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('id', 'name')


class Portfolio_serializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField(read_only = True)

    # ........................to have category 2nd way 1................................
    category = serializers.SerializerMethodField(read_only = True)


    # catagory = Catagory_Serializer() # to have category 1st way 2

    class Meta:
        model = Portfolio
        fields = ['url','title', 'client_name', 'project_date', 
        'Project_url', 'image1', 'image2', 'image3', 
        'image4','description', 'category']


    # ........................to have category 2nd way 2...............................
    def get_category(self,obj):
        return {
            'name': obj.catagory.name,
            'id': obj.catagory.id
        }
    
    def get_url(self, obj): 

        request = self.context.get('request') 

        # print('absolute url.............', request.build_absolute_uri())

        if request is None:
            return None

        return reverse("retrive", kwargs={"title": obj.title, "pk": obj.pk}, request=request)


        



    