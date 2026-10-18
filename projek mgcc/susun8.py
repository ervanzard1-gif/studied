import random
a1='a1'
a2='a2'
a3='a3'
a4='a4'
a5='a5'
a6='a6'
a7='a7'
a8='a8'

b1='b1'
b2='b2'
b3='b3'
b4='b4'
b5='b5'
b6='b6'
b7='b7'
b8='b8'

c1='c1'
c2='c2'
c3='c3'
c4='c4'
c5='c5'
c6='c6'
c7='c7'
c8='c8'

#start game

datas=['1 ','2 ','3 ','4 ','5 ','6 ','7 ','8 ']
random.shuffle(datas)
a8,b8,c8,a7,b7,c7,a6,b6=datas
    

board=f'''
| {a1} |  =  | {b1} |  =  | {c1} |
| {a2} |  =  | {b2} |  =  | {c2} |
| {a3} |  =  | {b3} |  =  | {c3} |
| {a4} |  =  | {b4} |  =  | {c4} |
| {a5} |  =  | {b5} |  =  | {c5} |
| {a6} |  =  | {b6} |  =  | {c6} |
| {a7} |  =  | {b7} |  =  | {c7} |
| {a8} |  =  | {b8} |  =  | {c8} |


 a          b          c
'''
print(board)


while True:
    #pilih number
    pilihroomawal=['a','b','c']
    room1=input('pilih yang mau dipindahkan = ')

    piliroomtujuan=['a','b','c']
    room2=input('pilih room untuk ditaro = ')
    


    if room1=='a':
        if a1!='a1':
            if room2=='b':
                if b8=='b8':
                    b8=a1
                    a1='a1'
                elif b7=='b7':
                    b7=a1
                    a1='a1'
                elif b6=='b6':
                    b6=a1
                    a1='a1'
                elif b5=='b5':
                    b5=a1
                    a1='a1'
                elif b4=='b4':
                    b4=a1
                    a1='a1'
                elif b3=='b3':
                    b3=a1
                    a1='a1'
                elif b2=='b2':
                    b2=a1
                    a1='a1'
                elif b1=='b1':
                    b1=a1
                    a1='a1'

            elif room2=='c':
                if c8=='c8':
                    c8=a1
                    a1='a1'
                elif c7=='c7':
                    c7=a1
                    a1='a1'
                elif c6=='c6':
                    c6=a1
                    a1='a1'
                elif c5=='c5':
                    c5=a1
                    a1='a1'
                elif c4=='c4':
                    c4=a1
                    a1='a1'
                elif c3=='c3':
                    c3=a1
                    a1='a1'
                elif c2=='c2':
                    c2=a1
                    a1='a1'
                elif c1=='c1':
                    c1=a1
                    a1='a1'


        elif a2!='a2':
            if room2=='b':
                if b8=='b8':
                    b8=a2
                    a2='a2'
                elif b7=='b7':
                    b7=a2
                    a2='a2'
                elif b6=='b6':
                    b6=a2
                    a2='a2'
                elif b5=='b5':
                    b5=a2
                    a2='a2'
                elif b4=='b4':
                    b4=a2
                    a2='a2'
                elif b3=='b3':
                    b3=a2
                    a2='a2'
                elif b2=='b2':
                    b2=a2
                    a2='a2'
                elif b1=='b1':
                    b1=a2
                    a2='a2'

            elif room2=='c':
                if c8=='c8':
                    c8=a2
                    a2='a2'
                elif c7=='c7':
                    c7=a2
                    a2='a2'
                elif c6=='c6':
                    c6=a2
                    a2='a2'
                elif c5=='c5':
                    c5=a2
                    a2='a2'
                elif c4=='c4':
                    c4=a2
                    a2='a2'
                elif c3=='c3':
                    c3=a2
                    a2='a2'
                elif c2=='c2':
                    c2=a2
                    a2='a2'
                elif c1=='c1':
                    c2=a2
                    a2='a2'

        elif a3!='a3':
            if room2=='b':
                if b8=='b8':
                    b8=a3
                    a3='a3'
                elif b7=='b7':
                    b7=a3
                    a3='a3'
                elif b6=='b6':
                    b6=a3
                    a3='a3'
                elif b5=='b5':
                    b5=a3
                    a3='a3'
                elif b4=='b4':
                    b4=a3
                    a3='a3'
                elif b3=='b3':
                    b3=a3
                    a3='a3'
                elif b2=='b2':
                    b2=a3
                    a3='a3'
                elif b1=='b1':
                    b2=a3
                    a3='a3'
            elif room2=='c':
                if c8=='c8':
                    c8=a3
                    a3='a3'
                elif c7=='c7':
                    c7=a3
                    a3='a3'
                elif c6=='c6':
                    c6=a3
                    a3='a3'
                elif c5=='c5':
                    c5=a3
                    a3='a3'
                elif c4=='c4':
                    c4=a3
                    a3='a3'
                elif c3=='c3':
                    c3=a3
                    a3='a3'
                elif c2=='c2':
                    c2=a3
                    a3='a3'
                elif c1=='c1':
                    c2=a3
                    a3='a3'
        elif a4!='a4':
            if room2=='b':
                if b8=='b8':
                    b8=a4
                    a4='a4'
                elif b7=='b7':
                    b7=a4
                    a4='a4'
                elif b6=='b6':
                    b6=a4
                    a4='a4'
                elif b5=='b5':
                    b5=a4
                    a4='a4'
                elif b4=='b4':
                    b4=a4
                    a4='a4'
                elif b3=='b3':
                    b3=a4
                    a4='a4'
                elif b2=='b2':
                    b2=a4
                    a4='a4'
                elif b1=='b1':
                    b2=a4
                    a4='a4'
            elif room2=='c':
                if c8=='c8':
                    c8=a4
                    a4='a4'
                elif c7=='c7':
                    c7=a4
                    a4='a4'
                elif c6=='c6':
                    c6=a4
                    a4='a4'
                elif c5=='c5':
                    c5=a4
                    a4='a4'
                elif c4=='c4':
                    c4=a4
                    a4='a4'
                elif c3=='c3':
                    c3=a4
                    a4='a4'
                elif c2=='c2':
                    c2=a4
                    a4='a4'
                elif c1=='c1':
                    c2=a4
                    a4='a4'
        elif a5!='a5':
            if room2=='b':
                if b8=='b8':
                    b8=a5
                    a5='a5'
                elif b7=='b7':
                    b7=a5
                    a5='a5'
                elif b6=='b6':
                    b6=a5
                    a5='a5'
                elif b5=='b5':
                    b5=a5
                    a5='a5'
                elif b4=='b4':
                    b4=a5
                    a5='a5'
                elif b3=='b3':
                    b3=a5
                    a5='a5'
                elif b2=='b2':
                    b2=a5
                    a5='a5'
                elif b1=='b1':
                    b2=a5
                    a5='a5'
            elif room2=='c':
                if c8=='c8':
                    c8=a5
                    a5='a5'
                elif c7=='c7':
                    c7=a5
                    a5='a5'
                elif c6=='c6':
                    c6=a5
                    a5='a5'
                elif c5=='c5':
                    c5=a5
                    a5='a5'
                elif c4=='c4':
                    c4=a5
                    a5='a5'
                elif c3=='c3':
                    c3=a5
                    a5='a5'
                elif c2=='c2':
                    c2=a5
                    a5='a5'
                elif c1=='c1':
                    c2=a5
                    a5='a5'
        elif a6!='a6':
            if room2=='b':
                if b8=='b8':
                    b8=a6
                    a6='a6'
                elif b7=='b7':
                    b7=a6
                    a6='a6'
                elif b6=='b6':
                    b6=a6
                    a6='a6'
                elif b5=='b5':
                    b5=a6
                    a6='a6'
                elif b4=='b4':
                    b4=a6
                    a6='a6'
                elif b3=='b3':
                    b3=a6
                    a6='a6'
                elif b2=='b2':
                    b2=a6
                    a6='a6'
                elif b1=='b1':
                    b1=a6
                    a6='a6'
            elif room2=='c':
                if c8=='c8':
                    c8=a6
                    a6='a6'
                elif c7=='c7':
                    c7=a6
                    a6='a6'
                elif c6=='c6':
                    c6=a6
                    a6='a6'
                elif c5=='c5':
                    c5=a6
                    a6='a6'
                elif c4=='c4':
                    c4=a6
                    a6='a6'
                elif c3=='c3':
                    c3=a6
                    a6='a6'
                elif c2=='c2':
                    c2=a6
                    a6='a6'
                elif c1=='c1':
                    c1=a6
                    a6='a6'
        elif a7!='a7':
            if room2=='b':
                if b8=='b8':
                    b8=a7
                    a7='a7'
                elif b7=='b7':
                    b7=a7
                    a7='a7'
                elif b6=='b6':
                    b6=a7
                    a7='a7'
                elif b5=='b5':
                    b5=a7
                    a7='a7'
                elif b4=='b4':
                    b4=a7
                    a7='a7'
                elif b3=='b3':
                    b3=a7
                    a7='a7'
                elif b2=='b2':
                    b2=a7
                    a7='a7'
                elif b1=='b1':
                    b1=a7
                    a7='a7'
            elif room2=='c':
                if c8=='c8':
                    c8=a7
                    a7='a7'
                elif c7=='c7':
                    c7=a7
                    a7='a7'
                elif c6=='c6':
                    c6=a7
                    a7='a7'
                elif c5=='c5':
                    c5=a7
                    a7='a7'
                elif c4=='c4':
                    c4=a7
                    a7='a7'
                elif c3=='c3':
                    c3=a7
                    a7='a7'
                elif c2=='c2':
                    c2=a7
                    a7='a7'
                elif c1=='c1':
                    c1=a7
                    a7='a7'
        elif a8!='a8':
            if room2=='b':
                if b8=='b8':
                    b8=a8
                    a8='a8'
                elif b7=='b7':
                    b7=a8
                    a8='a8'
                elif b6=='b6':
                    b6=a8
                    a8='a8'
                elif b5=='b5':
                    b5=a8
                    a8='a8'
                elif b4=='b4':
                    b4=a8
                    a8='a8'
                elif b3=='b3':
                    b3=a8
                    a8='a8'
                elif b2=='b2':
                    b2=a8
                    a8='a8'
                elif b1=='b1':
                    b1=a8
                    a8='a8'
            elif room2=='c':
                if c8=='c8':
                    c8=a8
                    a8='a8'
                elif c7=='c7':
                    c7=a8
                    a8='a8'
                elif c6=='c6':
                    c6=a8
                    a8='a8'
                elif c5=='c5':
                    c5=a8
                    a8='a8'
                elif c4=='c4':
                    c4=a8
                    a8='a8'
                elif c3=='c3':
                    c3=a8
                    a8='a8'
                elif c2=='c2':
                    c2=a8
                    a8='a8'
                elif c1=='c1':
                    c1=a8
                    a8='a8'

    if room1=='b':
        if b1!='b1':
            if room2=='a':
                if a8=='a8':
                    a8=b1
                    b1='b1'
                elif a7=='a7':
                    a7=b1
                    b1='b1'
                elif a6=='a6':
                    a6=b1
                    b1='b1'
                elif a5=='a5':
                    a5=b1
                    b1='b1'
                elif a4=='a4':
                    a4=b1
                    b1='b1'
                elif a3=='a3':
                    a3=b1
                    b1='b1'
                elif a2=='a2':
                    a2=b1
                    b1='b1'
                elif b1=='b1':
                    b1=b1
                    b1='b1'

            elif room2=='c':
                if c8=='c8':
                    c8=b1
                    b1='b1'
                elif c7=='c7':
                    c7=b1
                    b1='b1'
                elif c6=='c6':
                    c6=b1
                    b1='b1'
                elif c5=='c5':
                    c5=b1
                    b1='b1'
                elif c4=='c4':
                    c4=b1
                    b1='b1'
                elif c3=='c3':
                    c3=b1
                    b1='b1'
                elif c2=='c2':
                    c2=b1
                    b1='b1'
                elif c1=='c1':
                    c1=b1
                    b1='b1'


        elif b2!='b2':
            if room2=='a':
                if a8=='a8':
                    a8=b2
                    b2='b2'
                elif a7=='a7':
                    a7=b2
                    b2='b2'
                elif a6=='a6':
                    a6=b2
                    b2='b2'
                elif a5=='a5':
                    a5=b2
                    b2='b2'
                elif a4=='a4':
                    a4=b2
                    b2='b2'
                elif a3=='a3':
                    a3=b2
                    b2='b2'
                elif b2=='b2':
                    a2=b2
                    b2='b2'
                elif a1=='a1':
                    a1=b2
                    b2='b2'

            elif room2=='c':
                if c8=='c8':
                    c8=b2
                    b2='b2'
                elif c7=='c7':
                    c7=b2
                    b2='b2'
                elif c6=='c6':
                    c6=b2
                    b2='b2'
                elif c5=='c5':
                    c5=b2
                    b2='b2'
                elif c4=='c4':
                    c4=b2
                    b2='b2'
                elif c3=='c3':
                    c3=b2
                    b2='b2'
                elif c2=='c2':
                    c2=b2
                    b2='b2'
                elif c1=='c1':
                    c2=b2
                    b2='b2'

        elif b3!='b3':
            if room2=='a':
                if a8=='a8':
                    a8=b3
                    b3='b3'
                elif a7=='a7':
                    a7=b3
                    b3='b3'
                elif a6=='a6':
                    a6=b3
                    b3='b3'
                elif a5=='a5':
                    a5=b3
                    b3='b3'
                elif a4=='a4':
                    a4=b3
                    b3='b3'
                elif b3=='b3':
                    a3=b3
                    b3='b3'
                elif a2=='a2':
                    a2=b3
                    b3='b3'
                elif a1=='a1':
                    a1=b3
                    b3='b3'
            elif room2=='c':
                if c8=='c8':
                    c8=b3
                    b3='b3'
                elif c7=='c7':
                    c7=b3
                    b3='b3'
                elif c6=='c6':
                    c6=b3
                    b3='b3'
                elif c5=='c5':
                    c5=b3
                    b3='b3'
                elif c4=='c4':
                    c4=b3
                    b3='b3'
                elif c3=='c3':
                    c3=b3
                    b3='b3'
                elif c2=='c2':
                    c2=b3
                    b3='b3'
                elif c1=='c1':
                    c2=b3
                    b3='b3'
        elif b4!='b4':
            if room2=='a':
                if a8=='a8':
                    a8=b4
                    b4='b4'
                elif a7=='a7':
                    a7=b4
                    b4='b4'
                elif a6=='a6':
                    a6=b4
                    b4='b4'
                elif a5=='a5':
                    a5=b4
                    b4='b4'
                elif b4=='b4':
                    a4=b4
                    b4='b4'
                elif a3=='a3':
                    a3=b4
                    b4='b4'
                elif a2=='a2':
                    a2=b4
                    b4='b4'
                elif a1=='a1':
                    a2=b4
                    b4='b4'
            elif room2=='c':
                if c8=='c8':
                    c8=b4
                    b4='b4'
                elif c7=='c7':
                    c7=b4
                    b4='b4'
                elif c6=='c6':
                    c6=b4
                    b4='b4'
                elif c5=='c5':
                    c5=b4
                    b4='b4'
                elif c4=='c4':
                    c4=b4
                    b4='b4'
                elif c3=='c3':
                    c3=b4
                    b4='b4'
                elif c2=='c2':
                    c2=b4
                    b4='b4'
                elif c1=='c1':
                    c2=b4
                    b4='b4'
        elif b5!='b5':
            if room2=='a':
                if a8=='a8':
                    a8=b5
                    b5='b5'
                elif a7=='a7':
                    a7=b5
                    b5='b5'
                elif a6=='a6':
                    a6=b5
                    b5='b5'
                elif b5=='b5':
                    a5=b5
                    b5='b5'
                elif a4=='a4':
                    a4=b5
                    b5='b5'
                elif a3=='a3':
                    a3=b5
                    b5='b5'
                elif a2=='a2':
                    a2=b5
                    b5='b5'
                elif a1=='a1':
                    a2=b5
                    b5='b5'
            elif room2=='c':
                if c8=='c8':
                    c8=b5
                    b5='b5'
                elif c7=='c7':
                    c7=b5
                    b5='b5'
                elif c6=='c6':
                    c6=b5
                    b5='b5'
                elif c5=='c5':
                    c5=b5
                    b5='b5'
                elif c4=='c4':
                    c4=b5
                    b5='b5'
                elif c3=='c3':
                    c3=b5
                    b5='b5'
                elif c2=='c2':
                    c2=b5
                    b5='b5'
                elif c1=='c1':
                    c2=b5
                    b5='b5'
        elif b6!='b6':
            if room2=='a':
                if a8=='a8':
                    a8=b6
                    b6='b6'
                elif a7=='a7':
                    a7=b6
                    b6='b6'
                elif a6=='a6':
                    a6=b6
                    b6='b6'
                elif a5=='a5':
                    a5=b6
                    b6='b6'
                elif a4=='a4':
                    a4=b6
                    b6='b6'
                elif a3=='a3':
                    a3=b6
                    b6='b6'
                elif a2=='a2':
                    a2=b6
                    b6='b6'
                elif a1=='a1':
                    a1=b6
                    b6='b6'
            elif room2=='c':
                if c8=='c8':
                    c8=b6
                    b6='b6'
                elif c7=='c7':
                    c7=b6
                    b6='b6'
                elif c6=='c6':
                    c6=b6
                    b6='b6'
                elif c5=='c5':
                    c5=b6
                    b6='b6'
                elif c4=='c4':
                    c4=b6
                    b6='b6'
                elif c3=='c3':
                    c3=b6
                    b6='b6'
                elif c2=='c2':
                    c2=b6
                    b6='b6'
                elif c1=='c1':
                    c1=b6
                    b6='b6'
        elif b7!='b7':
            if room2=='a':
                if a8=='a8':
                    a8=b7
                    b7='b7'
                elif a7=='a7':
                    a7=b7
                    b7='b7'
                elif a6=='a6':
                    a6=b7
                    b7='b7'
                elif a5=='a5':
                    a5=b7
                    b7='b7'
                elif a4=='a4':
                    a4=b7
                    b7='b7'
                elif a3=='a3':
                    a3=b7
                    b7='b7'
                elif a2=='a2':
                    a2=b7
                    b7='b7'
                elif a1=='a1':
                    a1=b7
                    b7='b7'
            elif room2=='c':
                if c8=='c8':
                    c8=b7
                    b7='b7'
                elif c7=='c7':
                    c7=b7
                    b7='b7'
                elif c6=='c6':
                    c6=b7
                    b7='b7'
                elif c5=='c5':
                    c5=b7
                    b7='b7'
                elif c4=='c4':
                    c4=b7
                    b7='b7'
                elif c3=='c3':
                    c3=b7
                    b7='b7'
                elif c2=='c2':
                    c2=b7
                    b7='b7'
                elif c1=='c1':
                    c1=b7
                    b7='b7'
        elif b8!='b8':
            if room2=='a':
                if a8=='a8':
                    a8=b8
                    b8='b8'
                elif a7=='a7':
                    a7=b8
                    b8='b8'
                elif a6=='a6':
                    a6=b8
                    b8='b8'
                elif a5=='a5':
                    a5=b8
                    b8='b8'
                elif a4=='a4':
                    a4=b8
                    b8='b8'
                elif a3=='a3':
                    a3=b8
                    b8='b8'
                elif a2=='a2':
                    a2=b8
                    b8='b8'
                elif a1=='a1':
                    a1=b8
                    b8='b8'
            elif room2=='c':
                if c8=='c8':
                    c8=b8
                    b8='b8'
                elif c7=='c7':
                    c7=b8
                    b8='b8'
                elif c6=='c6':
                    c6=b8
                    b8='b8'
                elif c5=='c5':
                    c5=b8
                    b8='b8'
                elif c4=='c4':
                    c4=b8
                    b8='b8'
                elif c3=='c3':
                    c3=b8
                    b8='b8'
                elif c2=='c2':
                    c2=b8
                    b8='b8'
                elif c1=='c1':
                    c1=b8
                    b8='b8'
          
    if room1=='c':
        if c1!='c1':
            if room2=='a':
                if a8=='a8':
                    a8=c1
                    c1='c1'
                elif a7=='a7':
                    a7=c1
                    c1='c1'
                elif a6=='a6':
                    a6=c1
                    c1='c1'
                elif a5=='a5':
                    a5=c1
                    c1='c1'
                elif a4=='a4':
                    a4=c1
                    c1='c1'
                elif a3=='a3':
                    a3=c1
                    c1='c1'
                elif a2=='a2':
                    a2=c1
                    c1='c1'
                elif a1=='a1':
                    a1=c1
                    c1='c1'

            elif room2=='b':
                if b8=='b8':
                    b8=c1
                    c1='c1'
                elif b7=='b7':
                    b7=c1
                    c1='c1'
                elif b6=='b6':
                    b6=c1
                    c1='c1'
                elif b5=='b5':
                    b5=c1
                    c1='c1'
                elif b4=='b4':
                    b4=c1
                    c1='c1'
                elif b3=='b3':
                    b3=c1
                    c1='c1'
                elif b2=='b2':
                    b2=c1
                    c1='c1'
                elif c1=='c1':
                    b1=c1
                    c1='c1'


        elif c2!='c2':
            if room2=='a':
                if a8=='a8':
                    a8=c2
                    c2='c2'
                elif a7=='a7':
                    a7=c2
                    c2='c2'
                elif a6=='a6':
                    a6=c2
                    c2='c2'
                elif a5=='a5':
                    a5=c2
                    c2='c2'
                elif a4=='a4':
                    a4=c2
                    c2='c2'
                elif a3=='a3':
                    a3=c2
                    c2='c2'
                elif a2=='a2':
                    a2=c2
                    c2='c2'
                elif a1=='a1':
                    a1=c2
                    c2='c2'

            elif room2=='b':
                if b8=='b8':
                    b8=c2
                    c2='c2'
                elif b7=='b7':
                    b7=c2
                    c2='c2'
                elif b6=='b6':
                    b6=c2
                    c2='c2'
                elif b5=='b5':
                    b5=c2
                    c2='c2'
                elif b4=='b4':
                    b4=c2
                    c2='c2'
                elif b3=='b3':
                    b3=c2
                    c2='c2'
                elif c2=='c2':
                    b2=c2
                    c2='c2'
                elif b1=='b1':
                    b1=c2
                    c2='c2'

        elif c3!='c3':
            if room2=='a':
                if a8=='a8':
                    a8=c3
                    c3='c3'
                elif a7=='a7':
                    a7=c3
                    c3='c3'
                elif a6=='a6':
                    a6=c3
                    c3='c3'
                elif a5=='a5':
                    a5=c3
                    c3='c3'
                elif a4=='a4':
                    a4=c3
                    c3='c3'
                elif a3=='a3':
                    c3=c3
                    c3='c3'
                elif a2=='a2':
                    a2=c3
                    c3='c3'
                elif a1=='a1':
                    a1=c3
                    c3='c3'
            elif room2=='b':
                if b8=='b8':
                    b8=c3
                    c3='c3'
                elif b7=='b7':
                    b7=c3
                    c3='c3'
                elif b6=='b6':
                    b6=c3
                    c3='c3'
                elif b5=='b5':
                    b5=c3
                    c3='c3'
                elif b4=='b4':
                    b4=c3
                    c3='c3'
                elif c3=='c3':
                    b3=c3
                    c3='c3'
                elif b2=='b2':
                    b2=c3
                    c3='c3'
                elif b1=='b1':
                    b2=c3
                    c3='c3'
        elif c4!='c4':
            if room2=='a':
                if a8=='a8':
                    a8=c4
                    c4='c4'
                elif a7=='a7':
                    a7=c4
                    c4='c4'
                elif a6=='a6':
                    a6=c4
                    c4='c4'
                elif a5=='a5':
                    a5=c4
                    c4='c4'
                elif a4=='a4':
                    a4=c4
                    c4='c4'
                elif a3=='a3':
                    a3=c4
                    c4='c4'
                elif a2=='a2':
                    a2=c4
                    c4='c4'
                elif a1=='a1':
                    a2=c4
                    c4='c4'
            elif room2=='b':
                if b8=='b8':
                    b8=c4
                    c4='c4'
                elif b7=='b7':
                    b7=c4
                    c4='c4'
                elif b6=='b6':
                    b6=c4
                    c4='c4'
                elif b5=='b5':
                    b5=c4
                    c4='c4'
                elif c4=='c4':
                    c4=c4
                    c4='c4'
                elif b3=='b3':
                    b3=c4
                    c4='c4'
                elif b2=='b2':
                    b2=c4
                    c4='c4'
                elif b1=='b1':
                    b2=c4
                    c4='c4'
        elif c5!='c5':
            if room2=='a':
                if a8=='a8':
                    a8=c5
                    c5='c5'
                elif a7=='a7':
                    a7=c5
                    c5='c5'
                elif a6=='a6':
                    a6=c5
                    c5='c5'
                elif a5=='a5':
                    a5=c5
                    c5='c5'
                elif a4=='a4':
                    a4=c5
                    c5='c5'
                elif a3=='a3':
                    a3=c5
                    c5='c5'
                elif a2=='a2':
                    a2=c5
                    c5='c5'
                elif a1=='a1':
                    a2=c5
                    c5='c5'
            elif room2=='b':
                if b8=='b8':
                    b8=c5
                    c5='c5'
                elif b7=='b7':
                    b7=c5
                    c5='c5'
                elif b6=='b6':
                    b6=c5
                    c5='c5'
                elif c5=='c5':
                    b5=c5
                    c5='c5'
                elif b4=='b4':
                    b4=c5
                    c5='c5'
                elif b3=='b3':
                    b3=c5
                    c5='c5'
                elif b2=='b2':
                    b2=c5
                    c5='c5'
                elif b1=='b1':
                    b2=c5
                    c5='c5'
        elif c6!='c6':
            if room2=='a':
                if a8=='a8':
                    a8=c6
                    c6='c6'
                elif a7=='a7':
                    a7=c6
                    c6='c6'
                elif a6=='a6':
                    a6=c6
                    c6='c6'
                elif a5=='a5':
                    a5=c6
                    c6='c6'
                elif a4=='a4':
                    a4=c6
                    c6='c6'
                elif a3=='a3':
                    a3=c6
                    c6='c6'
                elif a2=='a2':
                    a2=c6
                    c6='c6'
                elif a1=='a1':
                    a1=c6
                    c6='c6'
            elif room2=='b':
                if b8=='b8':
                    b8=c6
                    c6='c6'
                elif b7=='b7':
                    b7=c6
                    c6='c6'
                elif c6=='c6':
                    b6=c6
                    c6='c6'
                elif b5=='b5':
                    b5=c6
                    c6='c6'
                elif b4=='b4':
                    b4=c6
                    c6='c6'
                elif b3=='b3':
                    b3=c6
                    c6='c6'
                elif b2=='b2':
                    b2=c6
                    c6='c6'
                elif b1=='b1':
                    b1=c6
                    c6='c6'
        elif c7!='c7':
            if room2=='a':
                if a8=='a8':
                    a8=c7
                    c7='c7'
                elif a7=='a7':
                    a7=c7
                    c7='c7'
                elif a6=='a6':
                    a6=c7
                    c7='c7'
                elif a5=='a5':
                    a5=c7
                    c7='c7'
                elif a4=='a4':
                    a4=c7
                    c7='c7'
                elif a3=='a3':
                    a3=c7
                    c7='c7'
                elif a2=='a2':
                    a2=c7
                    c7='c7'
                elif a1=='a1':
                    a1=c7
                    c7='c7'
            elif room2=='b':
                if b8=='b8':
                    b8=c7
                    c7='c7'
                elif c7=='c7':
                    b7=c7
                    c7='c7'
                elif b6=='b6':
                    b6=c7
                    c7='c7'
                elif b5=='b5':
                    b5=c7
                    c7='c7'
                elif b4=='b4':
                    b4=c7
                    c7='c7'
                elif b3=='b3':
                    b3=c7
                    c7='c7'
                elif b2=='b2':
                    b2=c7
                    c7='c7'
                elif b1=='b1':
                    b1=c7
                    c7='c7'
        elif c8!='c8':
            if room2=='a':
                if a8=='a8':
                    a8=c8
                    c8='c8'
                elif a7=='a7':
                    a7=c8
                    c8='c8'
                elif a6=='a6':
                    a6=c8
                    c8='c8'
                elif a5=='a5':
                    a5=c8
                    c8='c8'
                elif a4=='a4':
                    a4=c8
                    c8='c8'
                elif a3=='a3':
                    a3=c8
                    c8='c8'
                elif a2=='a2':
                    a2=c8
                    c8='c8'
                elif a1=='a1':
                    a1=c8
                    c8='c8'
            elif room2=='b':
                if b8=='b8':
                    b8=c8
                    c8='c8'
                elif b7=='b7':
                    b7=c8
                    c8='c8'
                elif b6=='b6':
                    b6=c8
                    c8='c8'
                elif b5=='b5':
                    b5=c8
                    c8='c8'
                elif b4=='b4':
                    b4=c8
                    c8='c8'
                elif b3=='b3':
                    b3=c8
                    c8='c8'
                elif b2=='b2':
                    b2=c8
                    c8='c8'
                elif b1=='b1':
                    b1=c8
                    c8='c8'
    board=f'''
| {a1} |  =  | {b1} |  =  | {c1} |
| {a2} |  =  | {b2} |  =  | {c2} |
| {a3} |  =  | {b3} |  =  | {c3} |
| {a4} |  =  | {b4} |  =  | {c4} |
| {a5} |  =  | {b5} |  =  | {c5} |
| {a6} |  =  | {b6} |  =  | {c6} |
| {a7} |  =  | {b7} |  =  | {c7} |
| {a8} |  =  | {b8} |  =  | {c8} |
    
    
 a          b          c
    '''
    print(board)
    if a1=='1 ' and a2=='2 ' and a3=='3 ' and a4=='4 ' and a5=='5 ' and a6=='6 ' and a7=='7 ' and a8=='8 ':
        print('MENANG')
    if b1=='1 ' and b2=='2 ' and b3=='3 ' and b4=='4 ' and b5=='5 ' and b6=='6 ' and b7=='7 ' and b8=='8 ':
        print('MENANG')
    if c1=='1 ' and c2=='2 ' and c3=='3 ' and c4=='4 ' and c5=='5 ' and c6=='6 ' and c7=='7 ' and c8=='8 ':
        print('MENANG')
    
    

