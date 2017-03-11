# for define the parameter we use ths pattern:
# par1[mass,x,y,r,v,a,f]
# par2[mass,x,v,r,v,a,f]
# w1[mass,x,y,r,v,a,f]
# w2[mass,x,y,v,r,a,f]
#and for par1,2 the r is zero
import numpy as np 


par1=[1,2,55,4,0,6,7]
par2=[1,18,56,2,5,6,7]
W1=[5,6,7,1,2,3,4]
W2=[3,4,2,6,7,1,2]

a=min(par1[2],par2[2],W1[2],W2[2])
print min(par1[2],par2[2],W1[2],W2[2])
if a==par1[2] or a==par2[2]:
    d=0
    #print par1
else :
  a=min(par1[2],par2[2],W1[2],W2[2])
  print a
  print ''
  print par1[2]-a
  par1[2]=par1[2]-a
  par2[2]=par2[2]-a
  W1[2]=W1[2]-a+W1[3]
  W2[2]=W2[2]-a+W2[3]
  
#yes...now one of the wheel must be on the ground
print par1
print par2
print W1
print W2

