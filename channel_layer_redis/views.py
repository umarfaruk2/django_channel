from django.shortcuts import render

def channel_layer(request):
    return render(request, 'layer.html')