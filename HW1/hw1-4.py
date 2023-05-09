level=1
atk=1
defence=1
power=1
weather_type=1
status=1
type_A=1
type_B=1
type_C=1
category=1
terrain=1
factor=1
damage=1

level = int(input("請輸入等級:"))
atk = int(input("請輸入攻擊力:"))
defence = int(input("請輸入防禦力:"))
power = int(input("請輸入招式力量:"))
weather_type = int(input("請輸入天氣:"))
status = int(input("請輸入異常狀態:"))
type_A = int(input("請輸入攻擊方寶可夢屬性:"))
type_B = int(input("請輸入守備方寶可夢屬性:"))
type_C = int(input("請輸入攻擊方招式屬性:"))
category = int(input("請輸入攻擊種類:"))
terrain = int(input("請輸入場地:"))

# 天氣與招式倍率
if weather_type==1:
  if type_C==0:
    factor=factor*0.5
  elif type_C==1:
    factor=factor*2
  else: 
    pass
elif weather_type==2:
  if type_C==0:
    factor=factor*2
  elif type_C==1:
    factor=factor*0.5
  else: 
    pass
else: 
  pass


# 攻擊屬性跟被攻擊型寶可夢傷害倍率
if type_C==0:
  if type_B==1 or type_B==4 or type_B==5:
    factor=factor*2
  elif type_B==0 or type_B==2 or type_B==7:
    factor=factor*0.5
  else:
    pass
elif type_C==1:
  if type_B==2:
    factor=factor*2
  elif type_B==0 or type_B==1 or type_B==4 or type_B==7:
    factor=factor*0.5
  else:
    pass
elif type_C==2:
  if type_B==0 or type_B==4 or type_B==5:
    factor=factor*2
  elif type_B==1 or type_B==2 or type_B==3 or type_B==7:
    factor=factor*0.5
  else:
    pass
elif type_C==3:
  if type_B==2:
    factor=factor*2
  elif type_B==4 or type_B==6:
    factor=factor*0.5
  else:
    pass
elif type_C==4:
  if type_B==1 or type_B==3:
    factor=factor*2
  elif type_B==5:
    factor=factor*0.5
  else:
    pass
elif type_C==5:
  if type_B==1 or type_B==4 or type_B==6:
    factor=factor*2
  elif type_B==3:
    factor=factor*0
  else:
    pass
elif type_C==6:
  if type_B==0 or type_B==3:
    factor=factor*2
  elif type_B==2 or type_B==6 or type_B==7:
    factor=factor*0.5
  elif type_B==5:
    factor=factor*0
  else:
    pass
elif type_C==7:
  if type_B==7:
    factor=factor*2
  else:
    pass

# 異常狀態與攻擊類型交互關係

if status==1:
  if category==0:
    factor=factor*0.5
elif status==2:
  if category==1:
    factor=factor*0.5

# 場地與傷害倍率
if terrain==1:
  if type_C==2:
    factor=factor*2
elif terrain==2:
  if type_C==6:
    factor=factor*2
elif terrain==3:
  if type_C==7:
    factor=factor*0.5

# 特殊狀況
if type_A==type_C:
  factor=factor*2

if weather_type==5:
  if type_A==4:
    defence=defence*2
  else:
    pass
elif weather_type==2:
  if type_A==5:
    defence=defence*0.5
  else :
    pass
elif weather_type==3:
  if type_A==2:
    atk=atk*0.5
  else :
    pass
elif weather_type==4:
  if type_A==3:
    atk=atk*2
  else :
    pass
else:
  pass

# 輸出
import math

damage = ((level*2+10)*atk*power/defence/250+2)*factor
print(factor)
if damage==0:
 damage=damage+1                     
print(damage)
