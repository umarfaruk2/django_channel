from django.shortcuts import render, HttpResponse
from .models import Chat, Group
from channels.layers import get_channel_layer

def channel_layer(request, group_name):
    group = Group.objects.filter(name=group_name).first()
    chats = []
    print('my enter group...', group)
    if group:
        chats = Chat.objects.filter(group = group)
        print('chats..', chats)
    else:
        group = Group(name=group_name)
        group.save()

    return render(request, 'app/layer.html', {'group_name': group_name, 'chats': chats})


def messageFromOutside(request):
    channel_layer = get_channel_layer()

    channel_layer.group_send(
        'BD',
        {
            'type': 'chat.message',
            'message': 'my message'
        }
    )

    return HttpResponse('Message from client')
