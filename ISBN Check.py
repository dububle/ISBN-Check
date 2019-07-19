isbn = input("Enter ISBN number(XXX-X-XXX-XXXXX-X): ")
while isbn != 'q':
    num = []
    weights = [1,3,1,3,1,3,1,3,1,3,1,3]
    total = 0
    check = 0
    for i in range(len(isbn)):
        if isbn[i].isdigit() == False and isbn[i] != '-' or isbn[3] != "-" or isbn[5] != "-" or isbn[9] != "-" or isbn[15] != "-":
            print("Error. Please re-enter ISBN number.")
            isbn = input("Enter ISBN number(XXX-X-XXX-XXXXX-X): ")

    for i in range(len(isbn)-1):
        if isbn[i].isdigit() == True:
            num.append(isbn[i])

    for i in range(len(num)):
        num[i] = int(num[i])
        total += (num[i]*weights[i])

    remain = total%10
    if remain == 0:
        check = 0
    else:
        check = 10 - remain

    print('The ISBN no. to check is:',isbn)
    print('Weighted sum is:',total)
    print('Calculated check digit:',check)
    if isbn[16] == str(check):
        print('The ISBN number is correct.')
    else:
        print('The ISBN number is wrong.')
    
    isbn = input("Enter ISBN number(XXX-X-XXX-XXXXX-X): ")
