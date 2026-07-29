# 8. Write a program to print action based on a *traffic signal color*
# (Red, Yellow, Green) using match.

signal = input("Enter the colour of the signal : ").strip().lower()
match signal :
    case "red" :
        print("Stop")
    case "yellow" :
        print("Slow down / Prepare to stop")
    case "green" :
        print("Go")    
    case _ :
        print("Enter valid colour name like (Red, Yellow, Green)")
        