def Unknown(x,y):
    if x < y:
      print(x+y)
      return (Unknown(x+1,y)*2)
    else:
       if x == y:
          return 1
       else:
          print(x+y)
          return (Unknown(x-1,y)//2) 



# print("The params value are 10 and 15")
# x = Unknown(10,15)
# print(f"return value {x}" )
# print("The params value are 10 and 10")
# x = Unknown(10,10)
# print(f"return value {x}" )

# print("The params value are 15 and 10")
# x = Unknown(15,10)
# print(f"return value {x}" )


def iterativeUnknown(x,y):
   while x < y :
      print(x+y)
      x += 1
      

def Unknown_iterative(x: int, y: int) -> int:
    result = 1 
    
    while x != y:
        print(x + y)  
        
        if x < y:
            x += 1
            result *= 2  
        else:
            x -= 1
            result //= 2  
    
    return result

# x = "15" 
# name = "Mubashir"
# Gender = "M"

# # print(x + " " + name + " " + Gender)
# print(f"{x} {name} {Gender}")


x = Unknown_iterative(10,15)