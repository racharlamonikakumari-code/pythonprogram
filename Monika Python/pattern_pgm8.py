""" wap pattern program=
4
4 3
4 3 2
4 3 2 1"""
for i in range(4,0,-1):
  for j in range (4,i-1,-1): """ #row=-1 in i hence work on 1
    print(j,end="\t")
  print()