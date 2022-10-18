docs="""Pronet CPU simulator commands

cache-clear : clears the cache memory
cache-info : info about caches
cache-show : shows cache contents
exit : exit CPU simulator
alu-info : info about alu
main-mem-info : info about main mem storage
add : num1 and num2 will be asked, to add 2 numbers
sub : num1 and num2 will be asked, to subtract 2 numbers
mult : num1 and num2 will be asked, to multiply 2 numbers
div : num1 and num2 will be asked, to divide 2 numbers
mod : num1 and num2 will be asked, to perform modulos 2 numbers
read-mem : pwd will be asked, to read from main memory
write-mem : pwd and content will be asked, to write to main memory
read-mem : pwd will be asked, to read from main memory
"""
cache=[]
main_mem={}
class arithmetic_logic_unit:
  def __init__(self,name):
    self.name=name
  def __repr__(self):
    return self.name
  def add(self,a,b):
    a,b=int(a),int(b)
    cache.append(a+b)
  def sub(self,a,b):
    a,b=int(a),int(b)
    cache.append(a-b)
  def mult(self,a,b):
    a,b=int(a),int(b)
    cache.append(a*b)
  def div(self,a,b):
    a,b=int(a),int(b)
    cache.append(a/b)
  def mod(self,a,b):
    a,b=int(a),int(b)
    cache.append(a%b)
  def alu_info(self):
    print("Does all Arithemtic and Logic computations for CPU")

class main_memory_unit:
  def __init__(self,name):
    self.name=name
  def __repr__(self):
    return self.name
    
  def write(self,pwd,content):
    main_mem[pwd]=content 
    print("Added",pwd,":",content,"to main memory")
  def read(self,pwd):
    print(main_mem[pwd])
  def remove(self,pwd):
    print("Deleted",pwd,":",main_mem[pwd],"from main memory")
    del main_mem[pwd]
  def main_mem_info(self):
    print("Main memory storage area")

    
class cache_unit:
  def __init__(self,name):
    self.name=name
  def __repr__(self):
    return self.name
  def cache_clear(self):
    cache=[]
    print("Cache cleared, current info stored is",cache)
  def cache_show(self):
    print(cache)
  def cache_info(self):
    print("Cache storage for short processes")

comcache=cache_unit("CPU-MAIN-CACHE")
comem=main_memory_unit("CPU-MAIN-MEMORY")
comalu=arithmetic_logic_unit("CPU-MAIN-ALU")
while True:
  command=input(">>> ")
  if command=="cache-clear":
    comcache.cache_clear()
  elif command=="cache-info":
    comcache.cache_info()
  elif command=="docs":
    print(docs)
  elif command=="exit":
    print("Exiting CPU-Simulator")
    break
  elif command=="alu-info":
    comalu.alu_info()
  elif command=="main-mem-info":
    comem.main_mem_info()
  elif command=="add":
    num1=input(">>> num1:")
    num2=input(">>> num2:")
    comalu.add(num1,num2)
    print("ans:",cache[-1])
  elif command=="sub":
    num1=input(">>> num1:")
    num2=input(">>> num2:")
    comalu.sub(num1,num2)
    print("ans:",cache[-1])
  elif command=="mult":
    num1=input(">>> num1:")
    num2=input(">>> num2:")
    comalu.mult(num1,num2)
    print("ans:",cache[-1])
  elif command=="div":
    num1=input(">>> num1:")
    num2=input(">>> num2:")
    comalu.div(num1,num2)
    print("ans:",cache[-1])
  elif command=="mod":
    num1=input(">>> num1:")
    num2=input(">>> num2:")
    comalu.mod(num1,num2)
    print("ans:",cache[-1])
  elif command=="cache-show":
    comcache.cache_show()
  elif command=="read-mem":
    pwd=input("pwd: ")
    comem.read(pwd)
  elif command=="write-mem":
    pwd=input("pwd: ")
    content=input("content: ")
    comem.write(pwd, content)
  elif command=="remove-mem":
    pwd=input("pwd: ")
    comem.remove(pwd)
  else:
    print("Unknown command")
