import past_paper_question_4a

valid = False
while valid == False:
    denary = int(input("Enter a denary number: "))
    if denary >= 1 and denary <= 255:
        print(past_paper_question_4a.toBinary(denary))
        valid = True
    else:
        print("Invalid input, try again.")