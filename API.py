#Getting informarion from RTO API
 import requests
import json
import xmltodict
vehicle_reg_no =text.strip() #NumberPlate deteted
username = "Enter Your User name here"# put your API_user name here..
url = "http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber=" + vehicle_reg_no + "&username="+username
url=url.replace(" ","%20")
print(url)
r = requests.get(url)
n = xmltodict.parse(r.content)
k = json.dumps(n)
df = json.loads(k)
l=df["Vehicle"]["vehicleJson"]
p=json.loads(l)
s="Your car's details are:\n"+"Owner name: "+str(p['Owner'])+"\n"+"Car Company: "+str(p['CarMake']['CurrentTextValue'])+"\n"+"Car Model: "+str(p['CarModel']['CurrentTextValue'])+"\n"+"Fuel Type: "+str(p['FuelType']['CurrentTextValue'])+"\n"+"Registration Year: "+str(p['RegistrationYear'])+"\n"+"Insurance: "+str(p['Insurance'])+"\n"+"Vehicle ID: "+str(p['VechileIdentificationNumber'])+"\n"+"Engine No.: "+str(p['EngineNumber'])+"\n"+"Location RTO: "+str(p['Location'])
print(s) 
