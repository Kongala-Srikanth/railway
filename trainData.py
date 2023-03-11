def hyd_delhi():
	
	train_no = [
		 "Telangana Express (Train No. 12723)",
	     "Telangana Express (Train No. 12723)",
		 "Telangana Express (Train No. 12723)",
		 "Telangana Express (Train No. 12723)",
		 "Telangana Express (Train No. 12723)",
		 "Telangana Express (Train No. 12723)",
		 "Telangana Express (Train No. 12723)"]
	places = [
	'Hyderabad',
	'Kazipet Junction',
	'Ramagundam',
	'Balharshah Junction',
	'agpur Junction',
	'Bhopal Junction',
	'Jhansi Junction'
	]
	time = [
	'Departure time 06:25 AM',
	'Arrival time 08:28 AM',
	'Arrival time 10:18 AM',
	'Arrival time 12:20 PM',
	'Arrival time 03:05 PM',
	'Arrival time 01:30 AM',
	'Arrival time 04:25 AM'
	]
	prices = [
	['Sleeper Class: INR 605, AC 3 Tier: INR 1,605, AC 2 Tier: INR 2,360, 	AC 1 Tier: INR 3,970'],
	['Sleeper Class: INR 1,000, AC 3 Tier: INR 1,985, AC 2 Tier: INR 2,920, AC 1 Tier: INR 4,895'],
	['Sleeper Class: INR 1,195, AC 3 Tier: INR 2,285, AC 2 Tier: INR 3,350, AC 1 Tier: INR 5,630'],
	['Sleeper Class: INR 1,365, AC 3 Tier: INR 2,530, AC 2 Tier: INR 3,710, AC 1 Tier: INR 6,215'],
	['Sleeper Class: INR 1,795, AC 3 Tier: INR 3,095, AC 2 Tier: INR 4,560, AC 1 Tier: INR 7,615'],
	['Sleeper Class: INR 2,235, AC 3 Tier: INR 4,415, AC 2 Tier: INR 6,480, AC 1 Tier: INR 10,865'],
	['Sleeper Class: INR 2,545, AC 3 Tier: INR 4,965, AC 2 Tier: INR 7,270, AC 1 Tier: INR 12,165']
	]
	reach = [
	 'Reaching time in Delhi - 07:00 AM (next day)',
	 'Reaching time in Delhi - 04:10 AM (next day)',
	 'Reaching time in Delhi - 05:10 AM (next day)',
	 'Reaching time in Delhi - 07:40 AM (next day)',
	 'Reaching time in Delhi - 11:10 AM (next day)',
	 'Reaching time in Delhi - 07:00 AM (next day)',
	 'Reaching time in Delhi - 10:55 AM (next day)'
	 ]
	


	my_zip = zip(train_no, places, time, prices, reach)


	return my_zip

def hyd_tirupati():


	train_no = ["12763/12764 Padmavati Express"]
	
	places = ["Hyderabad Deccan Nampally (HYB)"]


	time = ["05:30 AM (HYB)"]

	prices = ["AC Chair Car: INR 625 / Sleeper Class: INR 205 / Second Seating: INR 120"]

	reach = ["12:35 PM (TPTY)"]
	
	my_zip = zip(train_no, places, time, prices, reach)


	return my_zip


def hyd_vizag():


	train_no = [
		"Godavari Express (Train No. 12727/12728)",
		"Visakha Express (Train No. 17015/17016)",
		"Konark Express (Train No. 11019/11020)"
		]
	
	places = [
		"Hyderabad Deccan Nampally (HYB)",
		"Warangal, Vijayawada, and Rajahmundry",
		"Warangal, Vijayawada, and Rajahmundry"
	   ]


	time = ["05:25 PM","08:45 PM","11:20 PM"]

	prices = [
		"Sleeper Class: INR 260 / AC 3 Tier: INR 705 / AC 2 Tier: INR 1,010 / AC First Class: INR 845 ",
		"Sleeper Class: INR 255 / AC 3 Tier: INR 690 / AC 2 Tier: INR 995 / AC First Class: INR 825",
		"Sleeper Class: INR 295 / AC 3 Tier: INR 785 / AC 2 Tier: INR 1,125 / AC First Class: INR 1,890"
		]

	reach = ["07:45 AM on the next day","07:35 AM on the next day"," 07:40 AM on the next day"]
	
	my_zip = zip(train_no, places, time, prices, reach)


	return my_zip


def hyd_mumbai():


	train_no = [
		"Hussain Sagar Express (Train No. 12702)",
		"Mumbai Express (Train No. 17032)",
		"Devagiri Express (Train No. 17057)"
		]
	
	places = [
		"Hyderabad",
		"Hyderabad",
		"Hyderabad"
	   ]


	time = ["02:55 PM"," 07:35 AM (next day)","05:40 PM (next day)"]

	prices = [
		"Sleeper Class: INR 260 / AC 3 Tier: INR 705 / AC 2 Tier: INR 1,010 / AC First Class: INR 845 ",
		"Sleeper Class: INR 255 / AC 3 Tier: INR 690 / AC 2 Tier: INR 995 / AC First Class: INR 825",
		"Sleeper Class: INR 295 / AC 3 Tier: INR 785 / AC 2 Tier: INR 1,125 / AC First Class: INR 1,890"
		]

	reach = ["07:10 AM (next day)","07:35 AM (next day)"," 05:40 PM (next day)"]
	
	my_zip = zip(train_no, places, time, prices, reach)


	return my_zip



def hyd_karantaka():


	train_no = [
		"Kacheguda - KSR Bengaluru Express (Train No. 17603/17604)",
		"Hyderabad - KSR Bengaluru Express (Train No. 12657/12658)",
		"Rayalaseema Express (Train No. 17429/17430)"
		]
	
	places = [
		"Hyderabad",
		"Hyderabad",
		"Rayalaseema "
	   ]


	time = ["08:00 PM"," 04:30 PM","03:30 PM"]

	prices = [
		" INR 390, AC 3 Tier - INR 1075, AC 2 Tier - INR 1570, AC First Class - INR 2610",
		"INR 390, AC 3 Tier - INR 1075, AC 2 Tier - INR 1570, AC First Class - INR 2610",
		"SINR 230, AC 3 Tier - INR 630, AC 2 Tier - INR 905, AC First Class - INR 1480"
		]

	reach = ["08:45 AM (next day)","05:50 AM (next day)","06:00 AM (next day)"]
	
	my_zip = zip(train_no, places, time, prices, reach)


	return my_zip



def hyd_tamilnadu():


	train_no = [
		"Charminar Express (Train No. 12759/12760)",
		"Tamil Nadu Express (Train No. 12621/12622)",
		]
	
	places = [
		"Hyderabad",
		"Hyderabad",
	   ]


	time = ["06:40 PM","06:25 PM"]

	prices = [
		" INR 390, AC 3 Tier - INR 1075, AC 2 Tier - INR 1570, AC First Class - INR 2610",
		"INR 390, AC 3 Tier - INR 1075, AC 2 Tier - INR 1570, AC First Class - INR 2610",
		]

	reach = ["08:20 AM on the next day","06:10 AM on the next day"]
	
	my_zip = zip(train_no, places, time, prices, reach)


	return my_zip




def note():
	note_text = "Note: The prices and timings mentioned above are subject to change. It is recommended to check the latest train schedules and prices on the Indian Railways website or mobile app before booking your ticket."
	return note_text