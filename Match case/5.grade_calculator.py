# 5. Write a program to implement a *grading system* 
# based on marks (A, B, C, D, Fail) using match.
# 90–100 Grade A
# 75–89	 Grade B
# 60–74	 Grade C
# 35–59	 Grade D
# 0–34	 Fail
mark = int(input("Enter your mark : "))
match mark :
    case a if a < 0 or a > 100 :
        print("Enter a valid mark ")
    case a if a >= 90 :
        print("Your grade is 'A'")
    case a if a >= 75  :
        print("Your grade is 'B'")
    case a if a >= 60 :
        print("Your grade is 'C'")
    case a if a >= 35 :
        print("Your grade is 'D'")
    case _ :
        print("fail")
        