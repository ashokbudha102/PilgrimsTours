from django.shortcuts import render
from Products_Details.models import Destination
from django.http import JsonResponse
def home_list(request):
    context=Destination.objects.all()
    return render(request,'Home/home.html',{'products':context})

def home_detail_view(request,slug):
    data=Destination.objects.get(slug=slug)
    data2=data.additional_feature.all()
    text=request.GET.get('')
    if request.is_ajax():
        return JsonResponse({'data':data2},status=200)

    return render(request,'Home/home_detail.html',{'data':data,'data2':data2})