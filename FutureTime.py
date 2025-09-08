#FutureTime.py
#Name:Tavita Afata
#Date:7/9/2025
#Assignment:Future time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  print("Current time:", currentHour, ":", currentMinute)  

  moreHours = int(input("Enter number of hours to add: "))
  moreMins = int(input("Enter number of minutes to add: "))


  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60  

  futureHours = (currentHour + moreHours + extraHour) % 24

  print("Future time: {:02d}:{:02d}".format(futureHours, futureMins))

if __name__ == '__main__':
  main()
