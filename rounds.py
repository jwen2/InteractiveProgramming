
rounds = 0
number = 0
print("Would you like to increase transmission, symptoms, or the diseases abilities ?")
round_user_choice = input('Type T, S, A, or hit the space bar to skip\n')
x = 0
if (round_user_choice == ' '):
    print('You have skipped your upgrade for this turn')

elif(round_user_choice == 'T'):
    print("You can upgrade the pathogen's transmission by increasing \n1. airborne \n2. rodent \n3. meat")
    number = input('Type 1, 2, or 3 to upgrade a specific one\n')
    print ('Round ' + str(rounds) + ' user chose to upgrade T ' + str(number));
elif(round_user_choice == 'S'):
    print("You can upgrade the pathogen's symptoms by increasing \n1. insomnia \n2. necrosis \n3. inflammation")
    number = int(input('Type 1, 2, or 3 to upgrade a specific one\n'))
    print ('Round ' + str(rounds) + ' user chose to upgrade S ' + str(number));
elif(round_user_choice == 'A'):
    print("You can upgrade the pathogen's abilities by increasing \n1. drug resitance \n2. cold resistance \n3. hereditary")
    number = int(input('Type 1, 2, or 3 to upgrade a specific one\n'))
    print ('Round ' + str(rounds) + ' user chose to upgrade A ' + str(number));
else: #other/user error
    print('Please try again')
