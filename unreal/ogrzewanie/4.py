#https://arkusze.pl/maturalne/informatyka-2017-maj-matura-stara-rozszerzona-odpowiedzi.pdf
#https://technikprogramista.pl/kurs/zadania-maturalne-z-informatyki/lekcja/ogrzewanie-2017-pr/


#pytanie 
#brutforce albo jakas madra funkcja ??

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

drewno_history = []


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
         drewno += 468
   ###

   
   if(time_zone == "rano" and week_days_index in [6,7]):
      if(drewno >= 26):
         drewno -= 26
      else:
         print("закончилось дерево утром", date)

   

   time_zone = "wieczor"
   
   if(time_zone == "wieczor"):
      if(drewno < 26):
         print("закончилось дерево вечер", date)
         gaz_wieczor += 1
      else:
         drewno_wieczor += 1
         drewno -= 26
   
   ### koniec
   drewno_history.append([drewno, date])
   week_days_index += 1


