# given a specific time, compute the angle(s) between the hour and minute hands of an analog clock

def hands_angles(t):
    h = t.split(':')[0]
    m =  t.split(':')[1]

   
    hang1 = 360 * ( int(h)/12 )
    hang2 = (360/5)*(int(m)/60)

    minang = 360 * ( int(m)/60 )
    print (hang1, hang2)
    print(minang)
    return 



if __name__ == '__main__':
    
    time_check = "3:20"
    angs = hands_angles(time_check)