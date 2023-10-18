import time

timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
print("Current date amnd time is:",timestamp)
timestamp1 = time.strftime("%H")
timestamp2 = time.strftime("%M")
timestamp3 = time.strftime("%S")
if(int(timestamp1) < 12):
  print("Good Morning")
elif(int(timestamp1) >= 12 and int(timestamp1) < 17):
  print("Good afternoon")
elif(int(timestamp1) >= 17 and int(timestamp1) < 20):
  print("Good evening")
else:
  print( "Good night")
  