# OPEN FILES FOR DATA
zeeshan = open("ZeeshanEx.txt", "a+")
amir = open("AmirEx.txt", "a+")
furqan = open("FurqanEx.txt", "a+")
zeeshan_food = open("ZeeshanFo.txt", "a+")
amir_food = open("AmirFo.txt", "a+")
furqan_food = open("FurqanFo.txt", "a+")


# SELECT THE USER
def getuser():
    """
    THIS FUNCTION IS USED FOR SECLECTING USERS THERE ARE THREE USERS FOR SELECT ONE
    OF THE USER USE NUMBER FROM 1 TO 3
    """
    print("Select one of the below option")
    print("1 for Zeeshan")
    print("2 for Amir hayat")
    print("3 for Furqan")
    user = int(input())
    return user


def getDate():
    """
    THIS FUNCTION IS USER FOR GETING DATE AND TIME CURRENTLY
    """
    import datetime
    return datetime.datetime.now()


def userWork():
    """
        THIS FUNCTION IS USED FOR TAKING NUMBER
        1 IS USED FOR EXERCISE AND
        2 FOR FOOD
        """
    print("Select 1 for Exercise and 2 for Food")
    work = int(input())
    return work


def dataInsertion(name):
    """
        THIS FUNCTION IS USED FOR INSERTING DATA
        YOU WILL GIVE TODAY EXRCISE OR FOOD AND THAT
        WILL BE SAVE IN YOUR FILE
        """
    work = userWork()
    date1 = [getDate(), ]
    if work == 1:
        print("Which Exercise u did")
        exercise = input()

        if name == "zeeshan":
            zeeshan.write('date =' + repr(date1))
            zeeshan.write("Exercise" + exercise + "\n")
        elif name == "amir":
            amir.write('date =' + repr(date1))
            amir.write("Exercise" + exercise + "\n")
        else:
            furqan.write('date =' + repr(date1))
            furqan.write("Exercise" + exercise + "\n")
    elif work == 2:
        print("Enter which food yout Eat today")
        food = input()
        if name == "zeeshan":
            zeeshan_food.write('date =' + repr(date1))
            zeeshan_food.write("Food" + food + "\n")

        elif name == "amir":
            amir_food.write('date =' + repr(date1))
            amir_food.write("Food" + food + "\n")

        else:
            furqan_food.write('date =' + repr(date1))
            furqan_food.write("Food" + food + "\n")

    else:
        print("Select Wrong Option")


def dataretrive(name):
    """
        THIS FUNCTION IS USED FOR RETRIVEING DATA FROM FILES
        """
    zeeshan.seek(0)
    zeeshan_food.seek(0)
    amir_food.seek(0)
    amir.seek(0)
    furqan.seek(0)
    furqan_food.seek(0)
    work = userWork()
    if work == 1:
        if name == "zeeshan":
            lines = zeeshan.readlines()
            for line in lines:
                print(line)
        elif name == "amir":
            lines = amir.readlines()
            for line in lines:
                print(line)
        else:
            lines = furqan.readlines()
            for line in lines:
                print(line)

    elif work == 2:
        if name == "zeeshan":
            lines = zeeshan_food.readlines()
            for line in lines:
                print(line)
        elif name == "amir":
            lines = amir_food.readlines()
            for line in lines:
                print(line)
        else:
            lines = furqan_food.readlines()
            for line in lines:
                print(line)
    else:
        print("Select Wrong Option")


print("Enter 1 for Inserting data"
      "Enter 2 for Retriveing data")
data = int(input())

if data == 1:
    userInsert = getuser()

    if userInsert == 1:
        dataInsertion("zeeshan")
    elif userInsert == 2:
        dataInsertion("amir")
    elif userInsert == 3:
        dataInsertion("furqan")
    else:
        print("YOU SELECT WRONG OPTION")

elif data == 2:
    userRetrive = getuser()

    if userRetrive == 1:
        dataretrive("zeeshan")
    elif userRetrive == 2:
        dataretrive("amir")
    elif userRetrive == 3:
        dataretrive("furqan")
    else:
        print("YOU SELECT WRONG OPTION")

else:
    print("PLEASE SELECT 1 OR 2")
    print("THANKS")

"""CLOSE THE FILE"""
zeeshan.close()
amir.close()
furqan.close()
zeeshan_food.close()
amir_food.close()
furqan_food.close()
