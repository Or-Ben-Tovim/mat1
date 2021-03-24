def power (a,b):
    result=1
    for i in range(int(b)):
        result=result*a
    return result

def factorial(b):
    result=1
    for i in range(1,int(b+1)):
        result=result*i
    return result

def exponent(x:float)-> float:
    try:
        result=0
        for i in range(70):
            result=result+(power(x,i)/factorial(i))
        return float(result)
    except:
        return float(0)

def Ln(x:float)-> float:
    try:
        if x<=0:
            return float(0)
        else:
            Yn=0
            result=x-1.0
            while((Yn-result)>0.001 or (result-Yn)>0.001):
                Yn=result
                result= result+ 2*((x-exponent(result))/(x+exponent(result)))
            return float(result)
    except:
        return float(0)

def XtimesY(x:float,y:float)-> float:
    try:    
        if(x>0):
            final=exponent(Ln(x)*y)
            return float('%0.6f' % final)
        else:
            return float(0)
    except:
        return float(0)
        
def sqrt(x:float,y:float)-> float:
    try:    
        if(y>0 and x!=0):
            x=1/x
            final=XtimesY(y,x)
            return float('%0.6f' % final)
        elif(x==0):
            return float(0)
        else:
            return float(0)
    except:
        return float(0)
        
def calculate(x:float) -> float:
    try:
        finalResult=exponent(x)*XtimesY(7,x)*(1/x)*sqrt(x,x)
        finalResult=float('%0.6f' % finalResult)
        return finalResult
    except:
        return float(0)

