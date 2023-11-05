from django.shortcuts import render

def channel_layer(request, group_name):
    return render(request, 'layer.html', {'group_name': group_name})