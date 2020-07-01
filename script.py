def ground(weight):
   if weight <=2.0:
     return weight*1.5+20.0
   elif weight >2.0 and weight <=6.0:
     return weight*3.0+20
   elif weight >6.0 and weight <=10.0:
     return weight*4.0+20
   else: return weight*4.75+20

def drone(weight):
   if weight <=2.0:
     return weight*4.5
   elif weight >2.0 and weight <=6.0:
     return  weight*9.0
   elif weight >6.0 and weight <=10.0:
     return weight*12.0
   else: return weight*14.25
   

def cheapo(weight):
   if drone(weight) < ground(weight) and drone(weight)<125:
     return "drone",drone(weight)
   elif ground(weight)< 125:
     return "ground non-premium",ground(weight)
   else: return "premium shipping 125"

cheapo(4.8)