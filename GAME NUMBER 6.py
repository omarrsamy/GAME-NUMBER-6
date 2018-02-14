x=int(input("TOTAL :"))
Rx=int(x**(1/2))
FRx=float(Rx)

while(x>0):
  T=True
  try:
    playerA=int(input(" FIRST PLAYER : "))
  except:
    print(" Oops!!!! NUMBERS ONLY ")
    continue
  RplayerA=playerA**(1/2)
  while(T==True):
    if(FRx==RplayerA):
      T=False
    else:
      FRx-=1
    if(FRx==0 or playerA>x or 0>x):
      print(" WRONG!! Try Again with square numbers ")
      playerA=int(input("FIRST PLAYER: "))
      RplayerA=playerA**(1/2)
      FRx=float(Rx)
  x=x-playerA
  print(" REMAINING ",x)
  if(x==0):
    print(" **FIRST PLAYER WINS**")
    break
  A=True
  while(A==True):
    try:
      playerB=int(input(" SECOND PLAYER : "))
      A=False
    except:
      print(" Oops!!!! NUMBERS ONLY ")
      continue
  RplayerB=playerB**(1/2)
  T=True
  while(T==True):
    if(FRx==RplayerB):
      T=False
    else:
      FRx-=1
    if(FRx==0 or playerB>x or 0>x ):
      print(" WRONG!!! Try Again with square numbers ")
      playerB=int(input(" SECOND PLAYER : "))
      RplayerB=playerB**(1/2)
      FRx=Rx
  x=x-playerB
  print("REMAINING: ",x)
  if(x==0):
    print(" **SECOND PLAYER WINS**")
