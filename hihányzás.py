lista=[]
segédLista=[]
segedListaint=[]
with open("hianyzasok.txt","r",encoding="utf-8")as fin:
    for sor in fin:
        segedListastring=sor.strip().split(",")
        for szamString in segedListastring:
            segedListaint.append(int(szamString))
        lista.append(segedListaint)
        segedListaint=[]
            
            
            
            
print(lista)