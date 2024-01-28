from django.db import connection
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.clickjacking import xframe_options_exempt
from LeadGenerationAPP.models import Manager
from LeadGenerationAPP.models import States
from LeadGenerationAPP.models import Cities


from LeadGenerationAPP.serializers  import ManagerSerializer
from LeadGenerationAPP.serializers  import StatesSerializer
from LeadGenerationAPP.serializers  import CitiesSerializer
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect


#============================ Manager Interface ===============================================================
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerInterface(request):
    return render(request,"Manager.html",{})

#============================ Display All Manager ===============================================================
@xframe_options_exempt
def DisplayAllManager(request):
    return render(request,"DisplayAllManager.html",{})

#============================ Manager_Submit =====================================================================
@xframe_options_exempt
@api_view(['GET','POST','DELETE'])
def ManagerSubmit(request):
   if request.method == 'POST':
      #employee_data = request.GET.dict()
      #print("employeeeeee",request.data)
      manager_serializer = ManagerSerializer(data=request.data)
      if manager_serializer.is_valid():
        manager_serializer.save()
        return render(request,"Manager.html",{"message":"Record Submitted Successfully"})
     
      
      return render(request,"Manager.html",{"message":"Fail to Submit Record"})
    
'''
@api_view(['GET','POST','DELETE'])
def Manager_List(request):
  if request.method=='GET':
    manager_list=Manager.objects.all()
    manager_serializer=ManagerSerializer(manager_list,many=True)
    #print("Employee",employee_serializer.data)
    return JsonResponse(manager_serializer.data,safe=False)
  return JsonResponse({},safe=False)
'''
#============================ Manager_List ====================================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Manager_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname from leadgenerationapp_manager E"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
   return JsonResponse({},safe=False) 
 
#============================ Manager_List_BY_ID ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Manager_List_By_Id(request):
   if request.method=='GET':
    managerid=request.GET['managerid']
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname from leadgenerationapp_manager E where E.id={0}".format(managerid)
    print(q)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])

    if(data['gender']=='Male'):mg=True 
    else:mg=False
    
    if(data['gender']=='Female'):fg=True 
    else:fg=False
    
    return render(request,"ManagerById.html",{'record':data,'mgender':mg,'fgender':fg})
  
   return JsonResponse({},safe=False)  
 
#============================ Manager_Update_Delete ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Manager_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       manager=Manager.objects.get(pk=request.GET['id']) 
       manager.firstname=request.GET['firstname']
       manager.lastname=request.GET['lastname']
       manager.password=request.GET['password']
       manager.dob=request.GET['dob']
       manager.gender=request.GET['gender']
       manager.emailid=request.GET['emailid']
       manager.mobileno=request.GET['mobileno']
       manager.address=request.GET['address']
       manager.state=request.GET['state']
       manager.city=request.GET['city']
       
       manager.save()
      else:
        manager=Manager.objects.get(pk=request.GET['id']) 
        manager.delete()  
   return redirect('/api/displayallmanager')
 
 
#============================ Manager_Display_Picture ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Manager_Display_Picture(request):
   if request.method=='GET':
      return render(request,"ManagerPicture.html",{"id":request.GET['managerid'],"managername":request.GET['managername'],'picture':request.GET['picture']})


#============================ Update_Manager_Image ===============================================================   
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def UpdateManagerImage(request):
  
  if request.method == 'POST':
     employee=Manager.objects.get(pk=request.POST['id']) 
     employee.photograph=request.FILES['photograph']
     employee.save()
     return redirect('/api/displayallmanager')

  