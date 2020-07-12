from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from .models import Details
import json
import datetime,time

# Create your views here.
@csrf_protect
def index(request):

    if request.method=="POST":
        name = request.POST.get('name', '')
        Address = request.POST.get('address', '')
        phone = request.POST.get('contact', '')
        rice = request.POST.get('rice', '')
        Pulse = request.POST.get('pulse', '')
        Salt = request.POST.get('salt', '')
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        tim = time.strftime("%I:%M:%S %p")
        amt = int(rice)*50+int(Pulse)*90+int(Salt)*28
        data = Details(name=name,cont_no=phone,address=Address,date= date,time=tim, rice=rice,daal=Pulse,salt=Salt,amount = amt)
        data.save()
        d = Details.objects.values()
        x = len(d)
        dic ={'total':amt,'price':[int(rice)*50,int(Pulse)*90,int(Salt)*28],'date':date,'time':tim,'address':Address,'contact':phone,'name':name,'id':x}
        return render(request, 'order/bill.html', dic)
    return render(request, 'order/index.html')


@csrf_protect
def analysis(request):
    print(request)
    if request.method == "POST":
        date = request.POST.get('date','')
        date = datetime.datetime.strptime(date,'%Y-%m-%d')
        #date = date.strftime('%Y-%m-%d')
        d = Details.objects.filter(date=date)
        print(d)
        return render(request,'order/analysis.html',{'orders':d})
    
    d = Details.objects.values()
    
    return render(request,'order/analysis.html',{'orders':d})