from django.db import connection

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from LeadGenerationAPP.models import Employee
from LeadGenerationAPP.models import  States
from LeadGenerationAPP.models import Cities

from LeadGenerationAPP.serializers import EmployeeSerializer
from LeadGenerationAPP.serializers import StatesSerializer
from LeadGenerationAPP.serializers import CitiesSerializer
from django.http.response import JsonResponse
from .import tuple_to_dict
from django.shortcuts import redirect
from django.views.decorators.clickjacking import xframe_options_exempt

#============================ Employee_InterFace ===============================================================
# Create your views here.
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def EmployeeInterface(request):
    return render(request,"Employee.html",{})  
@xframe_options_exempt
def DisplayAllEmployee(request):
    return render(request,"DisplayAllEmployee.html",{})   

#============================ Employee Submit ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def EmployeeSubmit(request):
  if request.method == 'POST':
    #employee_data = request.GET.dict()
    #print("Employeeeeeeeeeeeee",request.data)
    employee_serializer = EmployeeSerializer(data=request.data)
  
    if employee_serializer.is_valid():
        employee_serializer.save()
        return render(request,"Employee.html",{"message":"Record Submitted Successfully"})
  return render(request,"Employee.html",{"message":"Server Error:Fail to Submit Record"})

'''
@api_view(['GET', 'POST', 'DELETE'])
def Employee_List(request):
   if request.method=='GET':
    #employee_list=Employee.objects.all() 
    employee_list=Employee.objects.raw('select E.* from leadgenerationapp_employee E')  
    employee_serializer = EmployeeSerializer(employee_list,many=True)
    #print("Employee",employee_serializer.data)
    return JsonResponse(employee_serializer.data,safe=False)
   return JsonResponse({},safe=False) 
'''

#============================ Employee List ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_List(request):
   if request.method=='GET':
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadgenerationapp_manager M where M.id=E.managerid) as mfirstname,(select M.lastname from leadgenerationapp_manager M where M.id=E.managerid) as mlastname from leadgenerationapp_employee E"
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictAll(cursor)
    return JsonResponse(data,safe=False)
   return JsonResponse({},safe=False) 

#============================ Employee_List_BY_ID ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_List_By_Id(request):
   if request.method=='GET':
    employeeid=request.GET['employeeid']
    cursor=connection.cursor() 
    q="select E.*,(select S.statename from leadgenerationapp_states S where S.stateid=E.state) as statename,(select C.cityname from leadgenerationapp_cities C where C.cityid=E.city) as cityname,(select M.firstname from leadgenerationapp_manager M where M.id=E.managerid) as mfirstname,(select M.lastname from leadgenerationapp_manager M where M.id=E.managerid) as mlastname from leadgenerationapp_employee E where E.id={0}".format(employeeid)
    #print(q)
    cursor.execute(q)
    data=tuple_to_dict.ParseToDictOne(cursor)
    data['dob']=str(data['dob'])

    if(data['gender']=='Male'):mg=True 
    else:mg=False
    
    if(data['gender']=='Female'):fg=True 
    else:fg=False
    
    return render(request,"EmployeeById.html",{'record':data,'mgender':mg,'fgender':fg})
  
   return JsonResponse({},safe=False)  

#============================ State_List ========================================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def State_List(request):
   if request.method=='GET':
    state_list=States.objects.all() 
    state_serializer = StatesSerializer(state_list,many=True)
    return JsonResponse(state_serializer.data,safe=False)
   return JsonResponse({},safe=False) 
      
#============================ City_List ===============================================================     
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def City_List(request):
  if request.method=='GET':
    city_list=Cities.objects.raw("select * from leadgenerationapp_cities where stateid={0}".format(request.GET['stateid']))
    city_serializer = CitiesSerializer(city_list,many=True)
    return JsonResponse(city_serializer.data,safe=False)
  return JsonResponse({},safe=False)

#============================ Employee_Update_Delete ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_Update_Delete(request):
   if request.method=='GET':
      btn=request.GET['btn']
      if(btn=='Edit'):
       employee=Employee.objects.get(pk=request.GET['id']) 
       employee.firstname=request.GET['firstname']
       employee.lastname=request.GET['lastname']
       employee.password=request.GET['password']
       employee.dob=request.GET['dob']
       employee.gender=request.GET['gender']
       employee.emailid=request.GET['emailid']
       employee.mobileno=request.GET['mobileno']
       employee.address=request.GET['address']
       employee.state=request.GET['state']
       employee.city=request.GET['city']
       employee.designation=request.GET['designation']
       employee.managerid=request.GET['managerid']

       employee.save()
      else:
        employee=Employee.objects.get(pk=request.GET['id']) 
        employee.delete()  
   return redirect('/api/displayallemployee')


#============================ Employee_Display_Picture ===============================================================
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def Employee_Display_Picture(request):
   if request.method=='GET':
      return render(request,"EmployeePicture.html",{"id":request.GET['employeeid'],"employeename":request.GET['employeename'],'picture':request.GET['picture']})

#============================ Update_Employee_Image ===============================================================  
@xframe_options_exempt
@api_view(['GET', 'POST', 'DELETE'])
def UpdateEmployeeImage(request):
  
  if request.method == 'POST':
     employee=Employee.objects.get(pk=request.POST['id']) 
     employee.photograph=request.FILES['photograph']
     employee.save()
     return redirect('/api/displayallemployee')
 
