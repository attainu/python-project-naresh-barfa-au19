

class ValidateCar:
    
    def input_car(car_no):
        print(car_no)
        is_valid = True
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        digit = "0123456789"
        if(len(car_no) != 13):
            return False
        if(car_no[1].upper() not in alpha):
            is_valid = False
        if(car_no[6].upper() not in alpha):
            is_valid = False
        if(car_no[7].upper() not in alpha):
            is_valid = False
        if(car_no[0].upper() not in alpha):
            is_valid = False
        if(car_no[5] != "-"):
            is_valid = False
        if( car_no[8] != "-"):
            is_valid = False
        if(car_no[2] != "-"):
            is_valid = False
        if(car_no[4] not in digit):
            is_valid = False
        if(car_no[9] not in digit):
            is_valid = False
        if(car_no[10] not in digit):
            is_valid = False
        if( car_no[11] not in digit):
            is_valid= False
        if(car_no[3] not in digit):
            is_valid = False
        if(car_no[12] not in digit):
            is_valid = False
        print(is_valid,"is_valid")
        return is_valid


    def genrateCarNo(car_no):
        outpt = ""
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for ch in car_no:
            if(ch.upper() in alpha):
                outpt += ch.upper()
            else:
                outpt += ch
        return outpt

    def colorVal(color):
        is_valid = True
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if(len(color) <3):
            return False
        for ch in color:
            if(ch.upper() not in alpha):
                return False
        return is_valid
