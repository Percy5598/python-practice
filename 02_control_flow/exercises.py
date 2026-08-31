# We can use and, or, not, >= or ==   
age = int(input("Enter your age: "))
years_experience = int(input("Years of work experience: "))
finnish_level = input("Finnish level (A1/A2/B1/B2/C1): ")
if age >= 18 and years_experience >= 1 and finnish_level in ["B1", "B2", "C1"]:
    print("You are eligible for the job!")
else:
    print("You are not eligible for the job.")          
