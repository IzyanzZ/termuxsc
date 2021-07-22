import os,sys,time

x = 'Username'
y = 'Password'

def b():
  os.system("clear")

def login():
  b()
  user = input("Username 》 ")
  passw = input("Password 》 ")
  if user == x and passw == y:
    print("Login Succes!")
    time.sleep(2)
    sys.exit

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
  print(" [+] 1. Keluar 🚪")
  print(" [~] ")
  print(" [+] 2. More Tools (etc)")

b()
login()
b()
menu()
ins()
jalan("  Pilih tools terlebih dahulu!  ".center(22))
pil = input("Pilih (1/2): ")
if pil == 1:
  b()
  print(" [•] ~~~~~~~~~~~~~~~~~ ")
  print(" Keluar Dari Tool!")
  time.sleep(5)
elif pil == 2:
  os.system("pkg install git")
  os.system("git clone")
