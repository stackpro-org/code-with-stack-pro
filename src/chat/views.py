from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from account.models import Account
from .models import PersonalChat
from django.conf import settings

def chat(request):

    template = 'chat.html'

    return render(request, template_name=template)




def room(request, room_name):


    return render(request, 'room.html', {'room_name': room_name})


def friend_list(request):

    friends = Account.objects.all()

    context = {
        'friends': friends,
    }

    return render(request, 'chat/friends.html', context=context)



def get_or_create_partner(user1,user2):
    try:
        partner=PersonalChat.objects.get(user1=user1, user2=user2)
    except PersonalChat.DoesNotExist:
        try:

            partner=PersonalChat.objects.get(user1=user2, user2=user1)

        except PersonalChat.DoesNotExist:

            partner=PersonalChat(
                user1=user1,
                user2=user2
            )
            partner.save()
    return partner


@login_required
def personal_chat(request, id):

    user1 = request.user
    user2 = Account.objects.get(id=id)

    friends = Account.objects.all()
    profile = Account.objects.get(id=request.user.id)

    partner = get_or_create_partner(user1,user2)


    if partner:
        context = {
            'chatgroup':partner,
            'groups_participated':friends,
            'profile':profile,
            'user2': user2,
            'GIPHY_URL': settings.GIPHY_URL,
            'API_KEY': settings.API_KEY,
        }
        
        return render(request, 'chat/room.html', context=context)
    
 