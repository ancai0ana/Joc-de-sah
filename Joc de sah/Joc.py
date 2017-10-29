"""hi"""

class Pozitie:
    x=0
    y=0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Stare_posibila:
    stare_p=[]
    p=Pozitie(0,0)

def search_poz (poz, stare):
    for p in stare:
        if (p.x == poz.x and p.y==poz.y):
            return True;
    return False;

def pozitie_valida(poz):
    return (poz.x>=0 and poz.x<=7 and poz.y<=7 and poz.y>=0);

def stari_posibile (p, starea_mea, stare_oponent):
    stari = []
    index=0

    #verifica in fata -middle
    pozitie_m_op=Pozitie()
    pozitie_m_op.x=p.x;
    pozitie_m_op.y=7-(p.y+1);
    pozitie_m_mine=Pozitie()
    pozitie_m_mine.x=p.x
    pozitie_m_mine.y=p.y+1
    if (search_poz(pozitie_m_op, stare_oponent)==False and pozitie_valida(pozitie_m_op) and pozitie_valida(pozitie_m_mine)):
        stare_middle=[];
        k=0
        for p2 in starea_mea:
            if (p.x == p2.x and p.y == p2.y):
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
    pozitie_l_op.x=p.x+1;
    pozitie_l_op.y=7-(p.y+1);
    pozitie_l_mine=Pozitie()
    pozitie_l_mine.x=p.x+1;
    pozitie_l_mine.y=p.y+1
    if (search_poz(pozitie_l_op, stare_oponent) and pozitie_valida(pozitie_l_op) and pozitie_valida(pozitie_l_mine)):
        stare_left = [];
        k = 0
        for p2 in starea_mea:
            if (p.x == p2.x and p.y == p2.y):
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
    pozitie_r_op.x=p.x-1;
    pozitie_r_op.y=7-(p.y+1);
    pozitie_r_mine=Pozitie()
    pozitie_r_op.x=p.x-1
    pozitie_r_op.y=p.y+1
    if (search_poz(pozitie_r_op, stare_oponent)==True and pozitie_valida(pozitie_r_op) and pozitie_valida(pozitie_r_mine)):
        stare_right = [];
        k = 0
        for p2 in starea_mea:
            if (p.x == p2.x and p.y == p2.y):
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
        while count!=0:
            cost=cost+count*10
            count=count-1
    pozitie_care_ma_poate_ataca=Pozitie()
    pozitie_care_ma_poate_ataca.x=poz.x+1
    pozitie_care_ma_poate_ataca.y=6-poz.y;
    if (search_poz(pozitie_care_ma_poate_ataca, stare_op) and pozitie_valida(pozitie_care_ma_poate_ataca)):
        count = poz.y
        while count != 0:
            cost = cost - count * 10
            count = count - 1
    return cost

def cost_op(stare):
    cost=0
    for p in starea_mea:
        count=p.y
        while count!=0:
            cost=cost+count*10
            count=count-1
    return cost

#functie returneaza starea oponentului daca noi am facut o anumita mutare (vf daca am elminat o piesa pt oponent)
def modifica_stare(pozitie, stare):
    stare_op=[]
    k=0
    for p in stare:
        if (p.x==pozitie.x and p.y==7-pozitie.y):
            p2=Pozitie(p.x,0)
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


#presupunem ca userul face doar mutari valide
def muta(pozitie_initiala, pozitie_finala, stare):
    stare_f=[]
    k=0
    for p in stare:
        if (p.x==pozitie_initiala.x and p.y==pozitie_initiala.y):
            stare_f.insert(k, pozitie_finala)
        else:
            stare_f.insert(k, p)
        k=k+1
    return stare_f




def main():
    k=0
    starea_mea=[]
    stare_op=[]
    '''
    for i in range(8):
        p=Pozitie();
        p.x=i;
        p.y=0;
        starea_mea.insert(k, p);
        stare_op.insert(k,p);
        k=k+1
    '''
    k=0
    o1=Pozitie()
    stare_op.insert(k,o1)
    k=k+1
    o2=Pozitie(1,0)
    stare_op.insert(k, o2)
    k = k + 1
    o3=Pozitie(2,0)
    stare_op.insert(k, o3)
    k = k + 1
    o4=Pozitie(3,5)
    stare_op.insert(k, o4)
    k = k + 1
    o5=Pozitie(4,0)
    stare_op.insert(k, o5)
    k = k + 1
    o6=Pozitie(5,2)
    stare_op.insert(k, o6)
    k = k + 1
    o7=Pozitie(6,3)
    stare_op.insert(k, o7)
    k = k + 1
    o8=Pozitie(7,0)
    stare_op.insert(k, o8)
    k = k + 1

    k2=0
    m1=Pozitie()
    starea_mea.insert(k2, m1)
    k2=k2+1
    m2=Pozitie(1,0)
    starea_mea.insert(k2, m2)
    k2 = k2 + 1
    m3=Pozitie(2,0)
    starea_mea.insert(k2, m3)
    k2 = k2 + 1
    m4=Pozitie(3,1)
    starea_mea.insert(k2, m4)
    k2 = k2 + 1
    m5=Pozitie(4,3)
    starea_mea.insert(k2, m5)
    k2 = k2 + 1
    m6=Pozitie(5,3)
    starea_mea.insert(k2, m6)
    k2 = k2 + 1
    m7=Pozitie(6,0)
    starea_mea.insert(k2, m7)
    k2 = k2 + 1
    m8=Pozitie(7,0)
    starea_mea.insert(k2, m8)
    k2 = k2 + 1



    n=Pozitie(5,3)

    print calculeaza_cost(n, starea_mea, stare_op);
    stari=stari_posibile(n, starea_mea, stare_op);
    for s in stari:
        for p in s.stare_p:
            print p.x, p.y
        c=modifica_stare(s.p, stare_op)
        print "st"
        for p in c:
            print p.x, p.y
        print calculeaza_cost(s.p, s.stare_p, stare_op);


if __name__ == "__main__":
     main()






