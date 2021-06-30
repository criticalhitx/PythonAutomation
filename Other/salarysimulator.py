#Gaji Simulator
base = int(input('Current salary: '))
asr = int(input('Annual Salary Raise: '))
salary=base
for age in range(23,50):
    salary=int(salary*(1+asr/100))
    print('Age: ',age,' Salary: ',salary)
