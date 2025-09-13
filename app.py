# print("crt","rete","rtilibf","khan", sep='-', end="")
# print("typing","master",sep="-")
# cel=int(input("enter a mo"))
# f=(9/5*cel)+32
# print(f)
# import math
# x=int(input("enter two no"))
# X=int(input("ente no"))
# y=int(input("ente no"))
# Y=int(input("ente no"))
# formula=math.sqrt((x-y)**2+(X-Y)**2)
# print(formula)

import logging
#logging setting

logging.basicConfig(
    #filename='app.log',
    #filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging .StreamHandler()
    ]
    #force=True

)
#get logger is used to call module
logger=logging.getLogger("ArthematicApp")
def add(a,b):
    result=a+b
    logger.debug(f"Adding {a}+{b}={result}")
    return result


def subs(a,b):
    result=a-b
    logger.debug(f"substract {a}-{b}={result}")
    return result


def mul(a,b):
    result=a*b
    logger.debug(f"multiply {a}*{b}={result}")
    return result


def div(a,b):
    try:
        result=a/b
        logger.debug(f"dividing {a}/{b}={result}")
        return result
    except ZeroDivisionError:
        logger.error("divison by zero error")
        return None
    
add(10,5)  
subs(10,6)  
mul(10,6)
div(20,10)

print("hello world")
print("hello world")
print("hello world")
    