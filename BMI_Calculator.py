import json
import itertools

#storing inputs
jsonString1 = '{"Gender":"Male","HeightCM":171,"WeightKg":96}'
jsonString2 = '{"Gender":"Male","HeightCM":161,"WeightKg":85}'
jsonString3 = '{"Gender":"Male","HeightCM":180,"WeightKg":77}'
jsonString4 = '{"Gender":"Female","HeightCM":166,"WeightKg":62}'
jsonString5 = '{"Gender":"Female","HeightCM":150,"WeightKg":70}'
jsonString6 = '{"Gender":"Female","HeightCM":167,"WeightKg":82}'
   
#changing the JSON string into a JSON object
jsonObject1 = json.loads(jsonString1)
jsonObject2 = json.loads(jsonString2)
jsonObject3 = json.loads(jsonString3)
jsonObject4 = json.loads(jsonString4)
jsonObject5 = json.loads(jsonString5)
jsonObject6 = json.loads(jsonString6)

#defining a dictionary
dict1={1:jsonObject1,2:jsonObject2,3:jsonObject3,4:jsonObject4,5:jsonObject5,6:jsonObject6}

#creating multiple empty lists for storing the final output 
BMI1=[]
Gender=[]
Heart_Risk=[]
Category=[]

#iterating through dictionary of dictionary
for key,value in dict1.items():
    value=dict1[key]
    H=(value['HeightCM']*0.01)**2
    W=value['WeightKg']
    Gender.append(value['Gender'])
    BMI=W/H
    if(BMI>=40):
        HR='Very High Risk'
        C='Very Severely obese'
    elif(BMI>=35):
        HR='High Risk'
        C='Severely obese'
    elif(BMI>=30):
        HR='Medium Risk'
        C='Moderately obese'
    elif(BMI>=25):
        HR='Enhanced Risk'
        C='Overweight'
    elif(BMI>=18.5):
        HR='Low Risk'
        C='Normal Weight'
    else:
        HR='Malnutrition Risk'
        C='Under Weight'
    BMI1.append(BMI)
    Heart_Risk.append(HR)
    Category.append(C)
    
#printing the final output    
for (a, b, c, d) in zip(BMI1, Gender, Heart_Risk, Category):
    print('BMI:',a,'| Gender:',b,'| Heart_Risk_Status:',c,'| Category:',d)
    
#finding out number of people in overweight category !
count=0
for k in Category:    
    if(k=='Overweight'):
       count+=1

print('\nThe number of people lying in the *Overweight* category are:',count)