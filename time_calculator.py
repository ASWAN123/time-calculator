days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]




# add_time("11:59 PM", "24:05", "Wednesday") "
# expected = "12:04 AM, Friday (2 days later) "
def add_time(start , duration , *day):
	start = start.replace(":"," ")
	[H , M , MD] =start.split(" ")
	[dH , dM] =duration.split(":")
	# count total of the ahours  and  minutes
	total_hours = int(H)+int(dH)
	total_minutes =int(M)+int(dM)
	# check if minutes above or equal 60 so we can add 1 H 
	if total_minutes>=60:
		total_hours+=1
		total_minutes =total_minutes-60
		if total_hours>=12:
			# devid the  total ahours  by 12  h  
			[t , r ] = divmod(total_hours ,12)
			if r != 0:
				total_hours = r
			else:
				total_hours = 12

			if t > 2 and  MD=="PM":
				[f , d] = divmod(t , 2)
				ttf =int(f)+int(d)

				if day:
					Day =day[0].title()
					x = days.index(Day)+ttf
					MD =f"AM, {days[x]} ({ttf} days later)" if MD =="PM" else "PM"
				else:
					MD =f"AM ({str(ttf)} days later)" if MD =="PM" else "PM"
			else:
				if t > 0 and t % 2 != 0:
					MD ="AM" if MD =="PM" else "PM"
			
	else:
		if total_hours>=12:
			# devid the  total ahours  by 12  h  
			[t , r ] = divmod(total_hours ,12)	
			# print(t , r)
			total_hours = r
			# print(total_hours)

			if t > 2 and  MD=="PM":
				[f , d] = divmod(t , 2)
				ttf =int(f)+int(d)
				data=[]
				if day:
					Day =day[0].title()
					# print(Day)
					x = days.index(Day)+ttf
					i = 0
					gid = 1
					while i < x:
						d = days.index(days[gid])
						data.append(d)
						if d == 6:
							gid=0
						else:
							gid+=1
						i+=1
					# print(data)

					MD =f"AM, {days[data[-1]]} ({ttf} days later)" if MD =="PM" else "AM"
					# print(MD)
				else:
					MD =f"AM ({ttf} days later)" if MD =="PM" else "PM"
			else:
				if t > 0 and t % 2 != 0:
					MD ="AM (next day)" if MD =="PM" else "PM"

			if t  % 2 == 0 :
				if day:
					Day =day[0].title()
					[f , d] = divmod(t , 2)
					ttf =int(f)+int(d)
					x =days.index(Day)+ttf
					MD =f"AM, {days[x]} (next day)" if MD =="AM" else "PM"
				else:
					MD ="AM (next day)" if MD =="AM" else "PM"


		else:
			if day:
				Day =day[0].title()
				MD =MD+", "+Day



	new_time = str(total_hours) + ":"+ f"{total_minutes:02d}"+" "+MD
	return new_time 




# minute ahours  normal  calcualtion
# minute above 60 or  == and  ahours  normal 
# minutes  above 60 or == and  ahours more than  12
# mminute  under  60  but  ahours  more  than  12  



