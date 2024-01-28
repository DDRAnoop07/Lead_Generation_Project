from django.db import connection

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


from LeadGenerationAPP.models import CallDetail
from LeadGenerationAPP.serializers import CallSerializer
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def CallDetailSubmit(request):
    if request.method == 'POST':
       
        print("calldetail      :",request.data)
        call_serializer = CallSerializer(data=request.data)
        if call_serializer.is_valid():
            call_serializer.save()
            return render(request, "CallDetail.html", {"message": "Record Submitted Successfully"})

        return render(request, "CallDetail.html", {"message": "Fail to Submit Record"})


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Call_Customer_By_Id(request):
   if request.method=='GET':
    customerid=request.GET['customerid']
    cursor=connection.cursor()
    q="select Cu.*,(select S.statename from leadgenerationapp_states S where S.stateid=Cu.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=Cu.city) as cityname from leadgenerationapp_customer Cu where Cu.id={0}".format(customerid)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])
    print("Customer:",data)
    
    keys=list(request.session.keys())
    print("SESSION:",keys,request.session['ADMIN'])
    user={'caller':keys[0]}
    if("ADMIN" in keys):
        user['id']=request.session['ADMIN'][0]['id']
        user['name']=request.session['ADMIN'][0]['adminname']
    elif("MANAGER" in keys):
        user['id']=request.session['MANAGER'][0]['id']
        user['name']=request.session['MANAGER'][0]['firstname']+" "+request.session['MANAGER'][0]['lastname']    
    elif("EMPLOYEE" in keys):
        user['id']=request.session['EMPLOYEE'][0]['id']
        user['name']=request.session['EMPLOYEE'][0]['firstname']+" "+request.session['EMPLOYEE'][0]['lastname']    

    return render(request,"CallDetail.html",{'record':data,'user':user})
  
   return JsonResponse({},safe=False)


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def DisplayCallDetails(request):
     return render(request, "DisplayCallDetails.html")


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def CallDetails_List(request):
    if request.method=='GET':
        # calldetail_list=CallDetail.objects.all()
        calldetail_list=CallDetail.objects.raw("SELECT * FROM leadgeneration.leadgenerationapp_calldetail;")
        calldetail_serializer=CallSerializer(calldetail_list,many=True)
        print("data:",calldetail_serializer.data)
        return JsonResponse(calldetail_serializer.data,safe=False)
    return JsonResponse({},safe=False)
    
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def CallDetails_List_By_Date(request):
    if request.method=='GET':
        cursor=connection.cursor()
        q="SELECT * FROM leadgenerationapp_calldetail where currentdate>='{0}' and currentdate<='{1}' ".format(request.GET['from'],request.GET['to'])
        print(q)
        cursor.execute(q)
        data=tuple_to_dict.ParseToDictAll(cursor)       
        print("data:",data)
        return JsonResponse(data,safe=False)
        # return render(request,'CallDetails.html',{'record':data})

    return JsonResponse({},safe=False)

@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def CallDetails_List_By_LeadStatus(request):
    if request.method=='GET':
        cursor=connection.cursor()
        q="SELECT * FROM leadgeneration.leadgenerationapp_calldetail where leadstatus='{0}' ".format(request.GET['leadstatus'])
        print(q)
        cursor.execute(q)
        data=tuple_to_dict.ParseToDictAll(cursor)       
     #    print("data:",data)
        return JsonResponse(data,safe=False)
        # return render(request,'DisplayCallDetails.html',{'record':data})
        
    return JsonResponse({},safe=False)


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def CallDetails_List_By_PhoneStatus(request):
    if request.method=='GET':
        phonestatus=request.GET['phonestatus']
     #    print("leadstatus:",phonestatus)
        cursor=connection.cursor()
        q="SELECT * FROM leadgeneration.leadgenerationapp_calldetail where phonestatus='{0}' ".format(phonestatus)
        print(q)
        cursor.execute(q)
        data=tuple_to_dict.ParseToDictAll(cursor)       
     #    print("data:",data)
        return JsonResponse(data,safe=False)

    return JsonResponse({},safe=False)


