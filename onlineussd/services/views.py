from django.shortcuts import render

# Create your views here.

def services(request):
    services={'Top Up':'Top Up',"Okoa":"Okoa",'Buy bundles':'Buy bundles',"Buy SMS":"Buy SMS",'Bonga':'Bonga','Mpesa':'Mpesa'}
    return render(request,'services/serviceshome.html',services)
