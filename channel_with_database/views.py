from django.shortcuts import render
from .models import Chat, Group

def channel_layer(request, group_name):
    group = Group.objects.filter(name = group_name).first()

    if group:
        chats = Chat.objects.filter(group = group)
    else:
        # group = Group.objects.create(name = group_name)
        group = Group(name = group_name)
        group.save()

    return render(request, 'layer.html', {'group_name': group_name, 'chats': chats})