from django.db import connection

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def Dashboard(request):
       
    if request.method == 'GET':
        
        cursor = connection.cursor()
        q = "select count(*) as Hot from leadgenerationapp_calldetail where leadstatus='Hot'"
        cursor.execute(q)
        hot = tuple_to_dict.ParseToDictAll(cursor)
          
        cursor = connection.cursor()
        q = "select count(*) as Warm from leadgenerationapp_calldetail where leadstatus='Warm'"
        cursor.execute(q)
        warm = tuple_to_dict.ParseToDictAll(cursor)
    
        cursor = connection.cursor()
        q = "select count(*) as Cold from leadgenerationapp_calldetail where leadstatus='Cold'"
        cursor.execute(q)
        cold = tuple_to_dict.ParseToDictAll(cursor)
            
        cursor = connection.cursor()
        q = "select count(*) as Freeze from leadgenerationapp_calldetail where leadstatus='Freeze'"
        cursor.execute(q)
        freeze = tuple_to_dict.ParseToDictAll(cursor)


        cursor = connection.cursor()
        q = "select count(*) as NotConnected from leadgenerationapp_calldetail where phonestatus='Not Connected'"
        cursor.execute(q)
        notconnected = tuple_to_dict.ParseToDictAll(cursor)
        
        cursor = connection.cursor()
        q = "select count(*) as Connected from leadgenerationapp_calldetail where phonestatus='Connected'"
        cursor.execute(q)
        connected = tuple_to_dict.ParseToDictAll(cursor)
       
        cursor = connection.cursor()
        q = "select count(*) as Total from leadgenerationapp_calldetail"
        cursor.execute(q)
        total = tuple_to_dict.ParseToDictAll(cursor)
         
       
        return render(request, "Dashboard.html", {"hot":hot, "warm":warm, "cold":cold, "freeze":freeze, "connected": connected, "notconnected": notconnected, "total":total,})
        


@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def HotCall(request):
    
    if request.method == 'GET':
        cursor = connection.cursor()
        q = "select *  from leadgenerationapp_calldetail where leadstatus='Hot' "
        cursor.execute(q)
        data=tuple_to_dict.ParseToDictAll(cursor)
        return JsonResponse(data, safe=False)
    return JsonResponse({}, safe=False)

@xframe_options_exempt
def DisplayHotCalls(request):
    return render(request,"DisplayHotCalls.html",{})