# tiny library to return a digit in seven segment form
# used https://roboindia.com/tutorials/raspberry-seven-segment
# not sure why 1 is off, and 0 is on

def digits(string digit):
    if digit == clr:
        return([1,1,1,1,1,1,1])
    elif digit == 0:
        return([0,0,0,0,0,0,1])
    elif digit == 1:
        return([1,0,0,1,1,1,1])
    elif digit == 2:
        return([0,0,1,0,0,1,0])
    elif digit == 3:
        return([0,0,0,0,1,1,0])
    elif digit == 4:
        return([1,0,0,1,1,0,0])
    elif digit == 5:
        return([0,1,0,0,1,0,0])
    elif digit == 6:
        return([0,1,0,0,0,0,0,])
    elif digit == 7:
        return([0,0,0,1,1,1,1])
    elif digit == 8:
        return([0,0,0,0,0,0,0])
    elif digit == 9:
        return([0,0,0,1,1,0,0,])