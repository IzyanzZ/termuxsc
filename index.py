import os,sys,time

def b():
  os.system("clear")

def jalan(kata):
  for e in kata:
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.3)
def menu():
  print ("(===============+==============)")
  print ("(                              )")
  print ("(      Script By IzyanzZ,      )")
  print ("(                              )")
  print ("(===============+==============)")
  
def ins():
  print(" ")
  print(" [+] 1. Kalkulator")
  print(" [~] ")
  print(" [+] 2. More Tools (etc)")
  
b()
i = input ("Are you sure to use this tools? (Y/n)")
if i == n:
  print ("Keluar dsri tools!")
elif i == y:
  b()
  menu()
  ins()
  jalan("Pilih tools terlebih dahulu!".center(44))
