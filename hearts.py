# Written by Edgar Martinez
# 05 / 01 / 2024
# Description:
#   - This program prints a heart sequence repeatedly
#   - for cretain number of lines.

if __name__ == "__main__":

    import time

    # let's define the heart string list,
    # it's a set of lines,
    # each line contains sections of the heart.

    string = []
    string.append("- - - - * - - - * - - - -\n")
    string.append("- - - * - * - * - - * - -\n")
    string.append("- - * - - - * - - - - * -\n")
    string.append("- - * - - - - - - - - * -\n")
    string.append("- - - * - - - - - - * - -\n")
    string.append("- - - - * - - - - * - - -\n")
    string.append("- - - - - * - - * - - - -\n")
    string.append("- - - - - - -*- - - - - -\n")

    # append a space in between each heart
    string.append("- - - - - - - - - - - - -\n")
    string.append("- - - - - - - - - - - - -\n")
    
    # now let's print this lovely heart for a number of times.
    times = input("Hello! How many hearts do you want?... ")
    times = int(times)
    print()

    # create a long string from the string list
    msg = ""
    
    for line in string:
        msg += line

    # replace dashes (-) by white spaces ()
    msg = msg.replace("-", " ")

    # print the string to the console for n times
    for iteration in range(times):
        print("- - - H E A R T # @ - - -\n".replace("@", str(iteration + 1)))
        print(msg)
        time.sleep(1)
    print()
    print("This is the end.")

    

