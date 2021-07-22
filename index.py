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
  print(" [+] 2. Akses root termux ( ubuntu )")
  print(" [~] ")
  print(" [+] 3. Akses root termux ( debian )")
  print(" [~] ")

b()
login()
b()
menu()
ins()
jalan("  Pilih tools terlebih dahulu!  ".center(22))
pil = input("Pilih (1-3): ")
if pil == 1:
  b()
  print(" [•] ~~~~~~~~~~~~~~~~~ ")
  print(" Keluar Dari Tool!")
  time.sleep(5)
elif pil == 2:
  os.system("pkg upgrade && pkg update && pkg install git && pkg install curl && pkg install bash")
  os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu.sh | bash")
elif pil == 3:
  os.system("pkg upgrade && pkg update && pkg install git && pkg install curl && pkg install bash")
  os.system("curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Debian/debian.sh | bash")
