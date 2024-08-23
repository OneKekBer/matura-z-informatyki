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
drewno_wieczor = 0
drewno_delivery_counter = 0
gaz_wieczor = 0


for date in all_days:
   arr = date.split("-")
   day = arr[2]
   
   time_zone = "rano" # | wieczor


   if(week_days_index == 8):
       week_days_index = 1

   ####
   if(week_days_index == 5):
      if(drewno < 100):
         drewno_delivery_counter += 1
         drewno += 300
   ###

   
   if(time_zone == "rano" and week_days_index in [6,7]):
      if(drewno >= 26):
         drewno -= 26

   

   time_zone = "wieczor"
   
   if(time_zone == "wieczor"):
      if(drewno < 26):
         gaz_wieczor += 1
      else:
         drewno_wieczor += 1
         drewno -= 26

   ### koniec
   week_days_index += 1

print(drewno_delivery_counter)
print(gaz_wieczor)
print(drewno_wieczor)