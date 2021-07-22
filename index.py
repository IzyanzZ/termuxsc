import os,sys,time

x = 'Username'
y = 'Password'

def mtk():
  print("[1] Pertambahan\n[2] Pengurangan\n[3] Perkalian\n[4] Pembagian")
  a = input("Pilih (1-4): ")
  if a == 1:
    ang = input("Angka 1: ")
    ang2 = input("Angka 2: ")
    total = ang + ang2
    print("Hasil Pertambahan Tadi Adalah", total )
    os.system("index.py")
    time.sleep(3)
  if a == 2:
    anng = input("Angka 1: ")
    anng2 = input("Angka 2: ")
    total = anng - anng2
    print("Hasil Pengurangan Tadi Adalah", total )
    os.system("index.py")
    time.sleep(3)
  if a == 3:
    annng = input("Angka 1: ")
    annng2 = input("Angka 2: ")
    total = annng * annng2
    print("Hasil Perkalian Tadi Adalah", total )
    os.system("index.py")
    time.sleep(3)
  if a == 1:
    annnng = input("Angka 1: ")
    annnng2 = input("Angka 2: ")
    total = annnng + annnng2
    print("Hasil Pembagian Tadi Adalah", total )
    os.system("index.py")
    time.sleep(3)

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
  print(" [+] 1. Kalkulator")
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
  mtk()
