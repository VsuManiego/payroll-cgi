#This program is designed for payroll system in Construction Management Field

print('Welcome!')

Id = input("Enter Employee's Id : ")
print("Emloyee's Id is:" , Id)

Name = input("Enter Employee's Name : ")
print(Name)
	
# Job Position Minimum Salary Rate per hour
General_Contractor_rate = 91.30
Architect_rate = 217.19
Engineer_rate = 217.19
Subcontractor_rate = 47.25
Foreman_rate = 75.51

# Job Positions
job_positions = ["General Contractor", "Architect", "Engineer", "Subcontractor", "Foreman"]

# Looping statement
while True:
	job_position = input("What is your job position? ")
	if job_position in job_positions:
		break

# Morning Time-in and Time-out
print("This is a morning time-in, have a great day at work!")

print("Enter starting time in morning (hrs) : " )
starting_morningtime_hrs = int(input())
print("Enter starting time in morning (mins) : " )
starting_morningtime_mins = int(input())
print("Enter ending time in morning (hrs):")
ending_morningtime_hrs = int(input())
print ("Enter ending time in morning (mins):")
ending_morningtime_mins =int(input())

# Afternoon Time-in and Time-out
print("This is an afternoon time-in, have a great day at work!")

print("Enter starting time in afternoon (hrs) : " )
starting_afternoontime_hrs = int(input())
print("Enter starting time in afternoon (mins) : " )
starting_afternoontime_mins = int(input())
print("Enter ending time in afternoon (hrs):")
ending_afternoontime_hrs = int(input())
print ("Enter ending time in afternoon (mins):")
ending_afternoontime_mins =int(input())

Total_morningtime_hrs = ending_morningtime_hrs - starting_morningtime_hrs
print('The total morning time in hrs is:' ,Total_morningtime_hrs )
Total_morningtime_mins = ending_morningtime_mins - starting_morningtime_mins
print('The total morning time in mins is:' ,Total_morningtime_mins )
Total_afternoontime_hrs = ending_afternoontime_hrs - starting_afternoontime_hrs
print('The total afternoon time in hrs is:' ,Total_afternoontime_hrs )
Total_afternoontime_mins = ending_afternoontime_mins - starting_afternoontime_mins
print('The total afternoon time in mins is:' ,Total_afternoontime_mins )

# Converting mins to hrs
Morning_mins = ((1/60) * Total_morningtime_mins)
print('The total morning mins converted into hrs is:' ,Morning_mins )
Afternoon_mins = ((1/60) * Total_afternoontime_mins)
print('The total afternoon mins converted into hrs is:' ,Afternoon_mins )

#Computing for Total time
Time_morning = Total_morningtime_hrs + Morning_mins
Time_afternoon = Total_afternoontime_hrs + Afternoon_mins
Total_worked_hrs = Time_morning + Time_afternoon
print("Your Total worked hours is:" ,Total_worked_hrs )

#Computing for Salary using the given time
if job_position == "General Contractor":
	Salary = General_Contractor_rate * Total_worked_hrs
	print("Your Salary is:" ,Salary )
	
elif job_position == "Architect":
	Salary = Architect_rate * Total_worked_hrs
	print("Your Salary is:" ,Salary )

elif job_position == "Engineer":
	Salary = Engineer_rate * Total_worked_hrs
	print("Your Salary is:" ,Salary )

elif job_position == "Subcontractor":
	Salary = Subcontractor_rate * Total_worked_hrs
	print("Your Salary is:" ,Salary )

elif job_position == "Foreman":
	Salary = Foreman_rate * Total_worked_hrs
	print('Your Salary is:' ,Salary )

print(Id, Name, job_position, Salary)

def calcuate():
	Id = input("Enter Employee's Id : ")
	print("Emloyee's Id is:" , Id)

	Name = input("Enter Employee's Name : ")
	print(Name)
	
	# Job Position Minimum Salary Rate per hour
	General_Contractor_rate = 91.30
	Architect_rate = 217.19
	Engineer_rate = 217.19
	Subcontractor_rate = 47.25
	Foreman_rate = 75.51

	# Job Positions
	job_positions = ["General Contractor", "Architect", "Engineer", "Subcontractor", "Foreman"]

	# Looping statement
	while True:
		job_position = input("What is your job position? ")
		if job_position in job_positions:
			break

	# Morning Time-in and Time-out
	print("This is a morning time-in, have a great day at work!")

	print("Enter starting time in morning (hrs) : " )
	starting_morningtime_hrs = int(input())
	print("Enter starting time in morning (mins) : " )
	starting_morningtime_mins = int(input())
	print("Enter ending time in morning (hrs):")
	ending_morningtime_hrs = int(input())
	print ("Enter ending time in morning (mins):")
	ending_morningtime_mins =int(input())

	# Afternoon Time-in and Time-out
	print("This is an afternoon time-in, have a great day at work!")

	print("Enter starting time in afternoon (hrs) : " )
	starting_afternoontime_hrs = int(input())
	print("Enter starting time in afternoon (mins) : " )
	starting_afternoontime_mins = int(input())
	print("Enter ending time in afternoon (hrs):")
	ending_afternoontime_hrs = int(input())
	print ("Enter ending time in afternoon (mins):")
	ending_afternoontime_mins =int(input())

	Total_morningtime_hrs = ending_morningtime_hrs - starting_morningtime_hrs
	print('The total morning time in hrs is:' ,Total_morningtime_hrs )
	Total_morningtime_mins = ending_morningtime_mins - starting_morningtime_mins
	print('The total morning time in mins is:' ,Total_morningtime_mins )
	Total_afternoontime_hrs = ending_afternoontime_hrs - starting_afternoontime_hrs
	print('The total afternoon time in hrs is:' ,Total_afternoontime_hrs )
	Total_afternoontime_mins = ending_afternoontime_mins - starting_afternoontime_mins
	print('The total afternoon time in mins is:' ,Total_afternoontime_mins )

	# Converting mins to hrs
	Morning_mins = ((1/60) * Total_morningtime_mins)
	print('The total morning mins converted into hrs is:' ,Morning_mins )
	Afternoon_mins = ((1/60) * Total_afternoontime_mins)
	print('The total afternoon mins converted into hrs is:' ,Afternoon_mins )

	#Computing for Total time
	Time_morning = Total_morningtime_hrs + Morning_mins
	Time_afternoon = Total_afternoontime_hrs + Afternoon_mins
	Total_worked_hrs = Time_morning + Time_afternoon
	print("Your Total worked hours is:" ,Total_worked_hrs )

	#Computing for Salary using the given time
	if job_position == "General Contractor":
		Salary = General_Contractor_rate * Total_worked_hrs
		print("Your Salary is:" ,Salary )
	
	elif job_position == "Architect":
		Salary = Architect_rate * Total_worked_hrs
		print("Your Salary is:" ,Salary )

	elif job_position == "Engineer":
		Salary = Engineer_rate * Total_worked_hrs
		print("Your Salary is:" ,Salary )

	elif job_position == "Subcontractor":
		Salary = Subcontractor_rate * Total_worked_hrs
		print("Your Salary is:" ,Salary )

	elif job_position == "Foreman":
		Salary = Foreman_rate * Total_worked_hrs
		print('Your Salary is:' ,Salary )

	print(Id, Name, job_position, Salary)

f = input("Do you want to calculate again? Type 'Y' character foy YES and 'N' for NO: ")
if f.upper() =='Y':
	calcuate()
elif f.upper()=='N':
	print('Thank you! Come back again.')
else:
	calcuate()

print("Thank you for using the progam!")