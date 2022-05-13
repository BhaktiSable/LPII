print("Welcome to Expert System")
HeatDiseaseCounter=0
severity=0
Pulse=0
temp=0
questions=["What is your Blood Pressure","What is pulse rate?","What is your Blood cholestrol level",
           "What is Fasting Blood Sugar","What is your Gender","What is you age?",]
YesNo=["Do you exersice for atleast 30 min?","Do you follow healthy diet?"]
for i in range(2):     # for yes/no kind of questions
    print(YesNo[i])
    print()
    ans=input()
    if(i!=1 and ans=='yes'):
        HeatDiseaseCounter+=1
    elif(i==1 and ans=='no'):        # for smell and taste question
        HeatDiseaseCounter+=1
for i in range(6):
    print(questions[i])
    print()
    if(i==0):
        systolic=float(input("Systolic pressure: "))
        diastolic=float(input("Diastolic pressure: "))
        if(systolic==120.0 and diastolic==80.0):
            severity+=0 
        elif(systolic>120 and diastolic<80):
            severity+=2
            HeatDiseaseCounter+=1
    if(i==1):
        ans=int(input())
        if(ans>=60 and ans<=72):
            severity+=0
        elif(ans<60 and ans>85):
            severity+=1
        else:
            severity+=2             
            HeatDiseaseCounter+=1 
            Pulse=1
    if(i==2):
        ns=float(input("Enter Blood Cholestrol level(eg:120.2): "))
        if(ans>=175.0):
            severity+=2             
            HeatDiseaseCounter+=1
            temp=1
        elif(ans<100.0 and ans>=50.0):
            severity+=1
        else:
            severity+=0
    if(i==3):
        bs=float(input("Enter Fasting Blood sugar(eg:120.2): "))
        if(ans>=130.0):
            severity+=2            
            HeatDiseaseCounter+=1
            temp=1
        elif(ans<125.0 and ans>=120.0):
            severity+=1
        else:
            severity+=0
    if(i==4):
        Gen=input("Enter you Gender:")
        if(Gen=="Male"):
            severity=+2
        elif(Gen=="Female"):
            severity=+1
    if(i==5):                           #age
        ans=int(input())
        if(ans>12 and ans<31):
            severity+=0
        elif(ans>31 and ans<51):
            severity+=1
        else:                          
            severity+=2
                   
if(HeatDiseaseCounter>1):
    print('The Patient is probable Heart Patient')
    print()
    if(severity<3):         # based on the value of the variable severity
        print('It looks like the symptoms are mild\nTake Care of your self')
    elif(severity>=2 and severity<=4):
        print('The patient can get an admission in the general ward')
    else:
        print('The patient looks critical')
else:        # if suspision counter is less than 3
    print('It looks like patient is not a Heart Patient')
print()
if(Pulse==1):
    print("Keep monitoring patient's Pulse level")
if(temp==1):
    print("Keep monitoring patient's Pulse")
