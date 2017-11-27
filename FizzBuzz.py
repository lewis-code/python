for number in range(101):

 if number == 0:
     print ("[!] Started")

 elif number % 5 + number % 3 == 0:
     print ("[!] FizzBuzz")

 elif number % 5 == 0:
     print ("[!] Buzz")

 elif number % 3 == 0:
     print ("[!] Fizz")

 else:
     print (number)
