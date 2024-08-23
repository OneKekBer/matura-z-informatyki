from datetime import datetime, timedelta

start_date = datetime(2015, 9, 15)
end_date = datetime(2016, 3, 31)

all_days = []
current_date = start_date
while current_date <= end_date:
    all_days.append(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)

drewno = 550

week_days_index = 2 # dni tygodnia
#1 - pon
#2 - wtorek
#3 - sroda
#4 - czwartek
#5 - piatek
#6 - sobota
#7 - niedziela


for date in all_days:
   arr = date.split("-")
   day = arr[2]
   
   time_zone = "rano" # | wieczor


   if(week_days_index == 8):
       week_days_index = 1
   ####

   if(time_zone == "rano" and week_days_index in [6,7]):
      drewno -= 26

   if(drewno < 100):
      print(date, week_days_index, time_zone)
      drewno += 300


   time_zone = "wieczor"
   
   if(time_zone == "wieczor"):
      drewno -= 26

   ###
   if(drewno < 100):
      print(date, week_days_index, time_zone)
      drewno += 300

   week_days_index += 1