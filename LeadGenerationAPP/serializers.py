from rest_framework import serializers 
from LeadGenerationAPP.models import Employee
from LeadGenerationAPP.models import  States
from LeadGenerationAPP.models import Cities
from LeadGenerationAPP.models import Manager
from LeadGenerationAPP.models import Customer
from LeadGenerationAPP.models import Administrator
from LeadGenerationAPP.models import CallDetail
class EmployeeSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Employee
        fields = ('id', 'firstname', 'lastname', 'dob', 'gender', 'emailid', 'mobileno', 'address', 'state', 'city', 'designation','managerid', 'photograph','password')
        
class StatesSerializer(serializers.ModelSerializer):    
    class Meta:
        model = States
        fields = ('id','stateid', 'statename')
   

class CitiesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Cities
        fields = ('id','stateid','cityid','cityname')
        
class ManagerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Manager
        fields = ('id','firstname', 'lastname', 'dob', 'gender', 'emailid', 'mobileno', 'address', 'state', 'city', 'photograph','password')
        
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ('id','firstname', 'lastname', 'dob', 'emailid', 'mobileno','alternateno','organizationname', 'address', 'state', 'city', 'photograph')
        
class AdminSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Administrator
        fields = ('id','mobileno','adminname','password')  
        
        
class CallSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallDetail
        fields = ('id', 'customerid', 'customername', 'callerid', 'status', 'callername', 'currentdate', 'phonestatus', 'conversation', 'leadstatus','mobileno')