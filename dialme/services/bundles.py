from .functions import update,costcalculator,balcheck

def databundles(request=""):
    normalbundles={
    "dailybundles":{"100 Mbs @ Sh.20":{"bundles":100,"cost":20},"300 Mbs @ Sh.50":{"bundles":300,"cost":50},"1.5 Gb @ Sh.100":{"bundles":1500,"cost":100}},
    "weeklybundles":{"500 Mbs @ Sh.100":{"bundles":500,"cost":100},"2 Gb @ Sh.200":{"bundles":2048,"cost":200},"4 Gb @ Sh.300":{"bundles":4096,"cost":300},"8 Gb @ Sh.500":{"bundles":8192,"cost":8192}},
    "monthlybundles":{"10Gb @ 1000":{"bundles":10240,"cost":1000}}
    }
    if request=="":
        return normalbundles
    else:
        pick=request.POST.get('bundlechoice')
        try:
            bundles=normalbundles.get("dailybundles").get(pick).get("bundles")
            cost=normalbundles.get("dailybundles").get(pick).get("cost")
            
        except:
            try:
                bundles=normalbundles.get("weeklybundles").get(pick).get("bundles")
                cost=normalbundles.get("weeklybundles").get(pick).get("cost")
                
            except:
                bundles=normalbundles.get("monthlybundles").get(pick).get("bundles")
                cost=normalbundles.get("monthlybundles").get(pick).get("cost")
                
        
        message=costcalculator(request,cost)
        
        if message==1:
            message=f"You have successfully bought {bundles}"
            bundlebal=balcheck(request,"bundles")
            update(request,{"bundles":bundles+bundlebal})
        return message
        
        
        


def smsbundles(request=""):
    normalsms={"dailybundles":{"20sms @ 5bob":{"cost":5,"sms":20},"200 sms @ 10bob":{"cost":10,"sms":200},"500 sms @ 20bob":{"cost":20,"sms":500}},
    "weeklybundles":{"400 sms @ 30":{"cost":30,"sms":400},"700 sms @ 50bob":{"cost":50,"sms":700}}}
    if request=="":
        return normalsms
    else:
        pick=request.POST.get('bundlechoice')
        choice=normalsms.get("dailybundles").get(pick)
        if not choice:choice=normalsms.get("weeklybundles").get(pick)

        cost=choice.get("cost")
        sms=choice.get("sms")
            
        message=costcalculator(request,cost)
        
        if message==1:
            message=f"You have successfully bought {sms}"
            smsbal=balcheck(request,"sms")
            update(request,{"sms":sms+smsbal})
        return message