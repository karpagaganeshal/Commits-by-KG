class mulfuns():
        def OddEven():
            Num=int(input("Enter a Number :"))
            if(Num%2==0):
                result = f"{Num} is an Even Number"        
            else:
                result = f"{Num} is an odd Number" 
            print(result)
            return result
            
        def EFM():
            gender=input("Your Gender :")
            age=int(input("Your Age :"))
            if((gender=="Male" or gender=="MALE") and age>=21) or ((gender=="Female" or gender=="FEMALE") and age>=18):
                    print("Eligible")
                    eligibility="Eligible"
            else:
                    print("Not Eligible")
                    eligibility= "Not Eligible"
            return eligibility
        def subfield():
            List = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
            print("Sub-fields in AI are:")
            for subfields in List:
                print(subfields)

        def bmi():
            BMI=float(input("Enter the BMI Index :"))
            if(BMI<18.5):
                print("Under Weight")
                vofbmi="Under Weight"
            elif(BMI<25):
                print("Normal Weight")
                vofbmi="Normal Weight"
            elif(BMI<30):
                print("Over Weight")
                vofbmi="Over Weight"
            elif(BMI<35):
                print("Obesity (class 1)")
                vofbmi="Obesity (class 1)"
            elif(BMI<40):
                print("Obesity (class 2)")
                vofbmi="Obesity (class 2)"
            else:
                print("Obesity (class 3),Sever")
                vofbmi="Obesity (class 3),Sever"
            return vofbmi
        def percentage():
            subject1=int(input(" Subject1 ="))
            subject2=int(input(" Subject2 ="))
            subject3=int(input(" Subject3 ="))
            subject4=int(input(" Subject4 ="))
            subject5=int(input(" Subject5 ="))
            allsubs =(subject1,subject2,subject3,subject4,subject5)
            total=sum(allsubs)
            precentage=total/len(allsubs)
            print(" Total :   ",total)
            print(f" Precentage :{precentage:.12f}")
            precentage=total/len(allsubs)
            return total,precentage
        def triangle():
            Height=int(input("Height : "))
            Breadth=int(input("Breadth : "))
            Area=(Height*Breadth) / 2
            print("Area formula : (Height * Breadth) / 2")
            print("Area of Traiangle is : ",Area)
            
            Height1=int(input("Height1 : "))
            Height2=int(input("Height2 : "))
            Breadth2=int(input("Breadth2 : "))
            Perimeter=Height1+Height2+Breadth2
            print("Perimeter formula : Height1 + Height2 + Breadth2")
            print("Perimeter of Traiangle is : ",Perimeter)
            return Area,Perimeter




    



