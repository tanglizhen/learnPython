li=[1,2,3]
li2=[elem*2 for elem in li]
print li
print li2
params={"tina":10,"david":20,"mary":30}
dic=params.items()
li3=["%s=%s" %(k,v) for k,v in dic]
print li3
print ";".join(li3)