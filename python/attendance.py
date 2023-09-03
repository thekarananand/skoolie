import csv
# track=[7, 5, 1, 1]
def ReadAttendance(rollno):
    total=0
    present=0
    absent=0
    with open("python\CT.csv","r") as obj:
        fobj=csv.reader(obj)
        next(fobj)
        for i in fobj:
            if i[0]==rollno:
                break
        # print(i)
        for j in range(1,8):
            total=total+1
            if i[j]=='1':
                present=present+1
            if i[j]=='0':
                absent+=1
        # print(total)
        # print(present)
        # print(absent)
        cancel=total-(present+absent)
        # print(cancel)
        track=[total,present,absent,cancel]
        # print(track)
        # presentperc(track)
        return(track)
# ReadAttendance('21109055')
def presentperc(track):
    return(int((track[1]/(track[0]-track[3]))*100))
    # print(int((track[1]/(track[0]-track[3]))*100))
# presentperc(track)

