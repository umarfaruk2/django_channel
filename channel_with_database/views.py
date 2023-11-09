from django.shortcuts import render
from .models import Chat, Group

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
