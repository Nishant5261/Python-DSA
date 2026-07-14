from math import gcd,lcm
class Frac:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def sim(self,n=1, d=1):
        if n==1 and d==1:
            tnum=self.num
            tden=self.den
            com=gcd(tnum,tden)
            self.num=int(tnum/com)
            self.den=int(tden/com)
        else:
            com=gcd(n,d)
            return int(n/com), int(d/com)
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    def __add__(self,other):
        temp_den=self.den*other.den
        temp_num=self.num*other.den+other.num*self.den
        temp_num,temp_den=self.sim(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)
    def __sub__(self,other):
        temp_den=self.den*other.den
        temp_num=self.num*other.den-other.num*self.den
        temp_num,temp_den=self.sim(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)
    def __mul__(self,other):
        temp_den=self.den*other.den
        temp_num=self.num*other.num
        temp_num,temp_den=self.sim(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)
    def __truediv__(self,other):
        temp_den=self.den*other.num
        temp_num=self.num*other.den
        temp_num,temp_den=self.sim(temp_num,temp_den)
        return "{}/{}".format(temp_num,temp_den)
    def __eq__(self,other):
        self.sim()
        other.sim()
        if (self.num == other.num) and (self.den == other.den):
            return True
        else : return False
    def __ne__(self,other):
        self.sim()
        other.sim()
        if (self.num == other.num) and (self.den == other.den):
            return False
        else : return True
    def __lt__(self,other):
        self.sim()
        other.sim()
        if self.den==other.den:
            if self.num<other.den: return True
            else : return False
        else:
            mul=lcm(self.den,other.den)
            f1=int(mul/self.den)
            f2=int(mul/other.den)
            if self.num*f1< other.num*f2 : return True
            else : return False
    def __rt__(self,other):
        self.sim()
        other.sim()
        if self.den==other.den:
            if self.num > other.den: return True
            else : return False
        else:
            mul=lcm(self.den,other.den)
            f1=int(mul/self.den)
            f2=int(mul/other.den)
            if self.num*f1 > other.num*f2 : return True
            else : return False
    def __le__(self,other):
        self.sim()
        other.sim()
        if self.den==other.den:
            if self.num <= other.den: return True
            else : return False
        else:
            mul=lcm(self.den,other.den)
            f1=int(mul/self.den)
            f2=int(mul/other.den)
            if self.num*f1 <= other.num*f2 : return True
            else : return False
    def __re__(self,other):
        self.sim()
        other.sim()
        if self.den==other.den:
            if self.num >= other.den: return True
            else : return False
        else:
            mul=lcm(self.den,other.den)
            f1=int(mul/self.den)
            f2=int(mul/other.den)
            if self.num*f1 >= other.num*f2 : return True
            else : return False
        
        
    
    
        
    
        
