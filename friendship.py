from time import sleep as s
x,y="Friends","Forever"
friends=["hemanth","jay"]
for friend in friends :
  print('\/'*9+'\\'+friend+"\/"*10+'\...');s(.2)
  print("\n\t     "+x+"\t "+y),s(.2)
  print("\t"+x+y+"  "+x+y),s(.2)
  print("      "+(x+y)*2+x*1),s(.2)
  print(" "*4+(x+y)*2+x*1+y[:1]),s(.2)
  print(" "*5+x+"Happy"+x+"together"+x),s(.2)
  print("         "+x+y+friend+y+x[:11-len(friend)]),s(.2)
  print("\t"+(x+y)*2),s(.2)
  print("\t"+" "*2+x+y+x+y[:2]),s(.2)
  print("\t"+" "*4+x+y+x[:5]),s(.2)
  print("\t"+" "*7+x+y),s(.2)
  print("\t"+" "*10+x),s(.2)
  print("\t"+" "*13+"v\n"),s(.2)
  print("\t"+"Happy "+x+"together "+friend+"\n\n\n"),s(.5)