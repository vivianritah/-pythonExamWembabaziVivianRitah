# regno. DCSE/0093/SS


def studentGrades():

    mark = int(input("Enter mark scored:\t"))
    if mark >=90 and mark <=100:
        print("Grade A")
    elif mark>=80 and mark<=89:
        print("Grade B")
    elif mark>=70 and mark<=79:
        print("Grade C")
    elif mark>=60 and mark<=69:
        print("Grade D")
    elif mark>=50 and mark<=59:
        print("Grade E")
    else:
        print("Fail")
studentGrades()