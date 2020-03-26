from datetime import date
today = int(date.today().weekday())
print(today)
if today < 4: 
        print('Yes, unfortunately today is a weekday.')

else:
         print('It is the weekend, yay!')