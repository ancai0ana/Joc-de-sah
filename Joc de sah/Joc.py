"""hi"""
import random
from flask import Flask
from flask import request
from flask import render_template


class Pozitie:
    x=0
    y=0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

class Stare_posibila:
    stare_p=[]
    p=Pozitie(0,0)

app = Flask(__name__)


def initializeaza():
    stare=[]
    k=0
    for i in range(8):
        p=Pozitie(i,0)
        stare.insert(k,p)
        k=k+1
    return stare

starea_mea = initializeaza()
stare_op = initializeaza()
index=1

@app.route('/')
def my_form():
    for s in starea_mea:
        print s.x, s.y
    k = 0
    return render_template("interfata.html", starea_mea=starea_mea, stare_op=stare_op, eroare=False)

app.debug = True

@app.route('/', methods=['POST'])
def my_form_post():
    xi = request.form.get('xi', 0)
    yi = request.form.get('yi', 0)
    xf = request.form.get('xf', 0)
    yf = request.form.get('yf', 0)

    p = Pozitie(xi, yi)
    pf = Pozitie(xf, yf)
    global stare_op
    global starea_mea
    global index

    #verificam daca e o mutare Valida
    pos=stari_posibile(p, stare_op, starea_mea)

    gasit=False
    for s in pos:
        if (int(s.p.x)==int(pf.x) and int(s.p.y)==int(pf.y)):
            gasit=True
    if gasit==False:
        pos = stari_posibile(p, stare_op, starea_mea)
        print "nu se poate"
        return render_template("interfata.html", starea_mea=starea_mea, stare_op=stare_op, eroare=True)

    r = Pozitie(pf.x, 7 -int(pf.y))

    starea_mea = modifica_stare(r, starea_mea)

    stemp=list(stare_op)

    stare_f = list(stare_op)
    stare_f2 = []
    k = 0

    for sf in stare_f:
        if (int(p.get_x()) == int(sf.get_x()) and int(p.get_y()) == int(sf.get_y())):
            stare_f2.insert(k, pf)
        else:
            stare_f2.insert(k, sf)
        k = k + 1

    stare_op = list(stare_f2)

    print "AI MUTAT"

    if (stare_finala(stare_op)):
        print "AI CASTIGAT"
        return render_template("castig.html", winner="YOU WIN")
    w = strategie(starea_mea, stare_op, index)
    index=index+1
    if (stare_finala(w.stare_p)):
        print "robo win"
        return render_template("castig.html", winner="ROBO WINS")
        starea_mea = w.stare_p;
    else:
        if (len(w.stare_p)==0):
            return render_template("castig.html", winner="YOU WIN")
        starea_mea = muta(w.stare_p[0], w.stare_p[1], starea_mea)
        r=Pozitie(w.stare_p[1].x, 7-int(w.stare_p[1].y))
        stare_op = modifica_stare(r, stare_op)

    return render_template("interfata.html", starea_mea=starea_mea, stare_op=stare_op, eroare=False)


def search_poz (poz, stare):
    for p in stare:
        if (int(p.x) == int(poz.x) and int(p.y)==int(poz.y)):
            return True;
    return False;

def pozitie_valida(poz):
    return (poz.x>=0 and poz.x<=7 and poz.y<=7 and poz.y>=0);

def stari_posibile (p, starea_mea, stare_oponent):
    stari = []
    index=0

    #verifica in fata -middle
    pozitie_m_op=Pozitie()
    pozitie_m_op.x=int(p.x);
    pozitie_m_op.y=7-(int(p.y)+1);
    pozitie_m_mine=Pozitie()
    pozitie_m_mine.x=int(p.x)
    pozitie_m_mine.y=int(p.y)+1
    if (search_poz(pozitie_m_op, stare_oponent)==False and search_poz(pozitie_m_mine, starea_mea)==False
        and pozitie_valida(pozitie_m_op) and pozitie_valida(pozitie_m_mine)):
        stare_middle=[];
        k=0
        for p2 in starea_mea:
            if (int(p.x) == int(p2.x) and int(p.y) == int(p2.y)):
                stare_middle.insert(k, pozitie_m_mine);
            else:
                stare_middle.insert(k, p2);
            k=k+1
        #memoram atat starea cat si muatrea facuta
        stare_pos=Stare_posibila()
        stare_pos.stare_p=stare_middle
        stare_pos.p=pozitie_m_mine
        stari.insert(index,stare_pos)
        index=index+1

    #verifica stanga diag - left
    pozitie_l_op=Pozitie()
    pozitie_l_op.x=int(p.x)+1;
    pozitie_l_op.y=7-(int(p.y)+1);
    pozitie_l_mine=Pozitie()
    pozitie_l_mine.x=int(p.x)+1;
    pozitie_l_mine.y=int(p.y)+1
    if (search_poz(pozitie_l_op, stare_oponent)==True and search_poz(pozitie_l_mine, starea_mea)==False
        and pozitie_valida(pozitie_l_op) and pozitie_valida(pozitie_l_mine)):
        stare_left = [];
        k = 0
        for p2 in starea_mea:
            if (int(p.x) == int(p2.x) and int(p.y) == int(p2.y)):
                stare_left.insert(k, pozitie_l_mine);
            else:
                stare_left.insert(k, p2);
            k = k + 1
        stare_pos = Stare_posibila()
        stare_pos.stare_p = stare_left
        stare_pos.p = pozitie_l_mine
        stari.insert(index, stare_pos)
        index = index + 1

    #verifica dreapta diag - right
    pozitie_r_op=Pozitie()
    pozitie_r_op.x=int(p.x)-1;
    pozitie_r_op.y=7-(int(p.y)+1);
    pozitie_r_mine=Pozitie()
    pozitie_r_mine.x=int(p.x)-1
    pozitie_r_mine.y=int(p.y)+1
    if (search_poz(pozitie_r_op, stare_oponent)==True and search_poz(pozitie_r_mine, starea_mea)==False
        and pozitie_valida(pozitie_r_op) and pozitie_valida(pozitie_r_mine)):
        stare_right = [];
        k = 0
        for p2 in starea_mea:
            if (int(p.x) == int(p2.x) and int(p.y) == int(p2.y)):
                stare_right.insert(k, pozitie_r_mine);
            else:
                stare_right.insert(k, p2);
            k = k + 1
        stare_pos = Stare_posibila()
        stare_pos.stare_p = stare_right
        stare_pos.p = pozitie_r_mine
        stari.insert(index, stare_pos)
        index = index + 1

    return stari

def calculeaza_cost(poz, starea_mea, stare_op):
    cost=0
    for p in starea_mea:
        count=p.y
        if (count!=8):
            while count!=0:
                cost=cost+count*10
                count=count-1
            if (int(p.x) == 0):
                cost = cost + 0
            elif (int(p.x) == 1):
                cost = cost + int(p.y)*1
            elif (int(p.x) == 2):
                cost = cost + int(p.y)*2
            elif (int(p.x) == 3):
                cost = cost + int(p.y)*3
            elif (int(p.x) == 4):
                cost = cost + int(p.y)*3
            elif (int(p.x) == 5):
                cost = cost + int(p.y)*2
            elif (int(p.x) == 6):
                cost = cost + int(p.y)*1
            else:
                cost = cost + 0
    pozitie_care_ma_poate_ataca=Pozitie()
    pozitie_care_ma_poate_ataca.x=poz.x-1
    pozitie_care_ma_poate_ataca.y=6-poz.y;
    pozitie_care_ma_poate_ataca2=Pozitie()
    pozitie_care_ma_poate_ataca2.x = poz.x + 1
    pozitie_care_ma_poate_ataca2.y = 6 - poz.y;
    if (search_poz(pozitie_care_ma_poate_ataca, stare_op) and pozitie_valida(pozitie_care_ma_poate_ataca)
        or search_poz(pozitie_care_ma_poate_ataca2, stare_op) and pozitie_valida(pozitie_care_ma_poate_ataca2)):
        count = poz.y
        while count != 0:
            cost = cost - count * 10
            count = count - 1
    print cost
    return cost

def cost_op(stare):
    cost=0
    for p in stare:
        count=int(p.y)
        if (count!=8):
            while count!=0:
                cost=cost+count*10
                count=count-1
        if (int(p.x)==0):
            cost=cost+0
        elif (int(p.x)==1):
            cost=cost+int(p.y)*1
        elif (int(p.x)==2):
            cost=cost+int(p.y)*2
        elif (int(p.x)==3):
            cost=cost+int(p.y)*3
        elif (int(p.x)==4):
            cost=cost+int(p.y)*3
        elif (int(p.x)==5):
            cost=cost+int(p.y)*2
        elif (int(p.x)==6):
            cost=cost+int(p.y)*1
        else:
            cost=cost+int(p.y)*0
    print cost
    return cost

#functie returneaza starea oponentului daca noi am facut o anumita mutare (vf daca am elminat o piesa pt oponent)
def modifica_stare(pozitie, stare):
    stare_op=[]
    k=0
    for p in stare:
        if (int(p.x)==int(pozitie.x) and int(p.y)==int(pozitie.y)):
            p2=Pozitie(8,8)
            stare_op.insert(k, p2)
        else:
            stare_op.insert(k, p)
        k=k+1
    return stare_op

def stare_finala(stare):
    for p in stare:
        if (p.y==7):
            return True
    return False


#userul face doar mutari valide
def muta(pozitie_initiala, pozitie_finala, stare):
    stare_f=list(stare)
    stare_f2=[]
    k=0
    c=pozitie_initiala.get_x()
    d=pozitie_initiala.get_y()
    for p in stare_f:
        if (int(p.get_x())==c and int(p.get_y())==d):
            stare_f2.insert(k, pozitie_finala)
        else:
            stare_f2.insert(k, p)
        k=k+1

    return stare_f2

def strategie(starea_mea, stare_op, index):
    diffMax=-5000
    stare_aleasa=Stare_posibila()
    stari=[]
    k=0
    count_random=0 #daca nu gasim dupa 100 de cautari inseamna ca nu mai avem mutari posibile
    if (index % 3 == 0):
        while (len(stari)==0 and count_random<100):
            i = random.randint(0, len(starea_mea)-1)
            stari=stari_posibile(starea_mea[i], starea_mea, stare_op)
            count_random=count_random+1
        j=random.randint(0, len(stari)-1)
        if (stare_finala(stari[j].stare_p)):
            return stari[j]
        stare_aleasa.stare_p.insert(k, starea_mea[i])
        k = k + 1
        stare_aleasa.stare_p.insert(k, stari[j].p)
        return stare_aleasa
    for p in starea_mea:
        stari=stari_posibile(p, starea_mea, stare_op)

        print "DIFF"
        for s in stari:
            if (stare_finala(s.stare_p)):
                return s
            c1=calculeaza_cost(s.p, s.stare_p, stare_op)
            temp=list(stare_op)
            r=Pozitie()
            r.x=s.p.x
            r.y=7-int(s.p.y)
            st=modifica_stare(r, temp)
            c2=cost_op(st)
            diff=c1-c2
            print diff
            if (diff>diffMax):
                diffMax=diff
                k=0
                stare_aleasa.stare_p.insert(k, p)
                k=k+1
                stare_aleasa.stare_p.insert(k, s.p)
    return stare_aleasa

def print_matrice(starea_mea, stare_op):
    A = [['o' for x in range(8)] for y in range(8)]
    for p in starea_mea:
        A[int(p.y)][int(p.x)]='B'
    for p in stare_op:
        A[7-int(p.y)][int(p.x)]='W'
    for i in range(8):
        for j in range(8):
            print '{:4}'.format(A[i][j]),
        print
    return True;

def main():
    app.run()


if __name__ == "__main__":
     main()

