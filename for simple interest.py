# Programa Python3 para encontrar um interesse simples
# para determinado valor principal, tempo e
# Taxa de interesse. 
  
  
def simple_interest(p,t,r): 
    print('O principal é', p) 
    print('O período é', t) 
    print('A taxa de juros é',r) 
      
    si = (p * t * r)/100
      
    print('O interesse simples é', si) 
    return si 
      
# Driver code 
simple_interest(8, 6, 8) 
