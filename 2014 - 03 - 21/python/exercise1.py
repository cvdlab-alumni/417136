from pyplasm import *

#USATA UNA SCALA DI 1:5 RISPETTO AL MODELLO IL 3D

#PIANOTERRA

verts = [[0,0],[30,0],[30,30],[0,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors7 = MKPOL([verts, cells, pols])
firtsfloorscolor7 = COLOR(GRAY)(firtsfloors7)

pianoterra = STRUCT([firtsfloorscolor7])


#PRIMOPIANO

verts = [[0,0],[10,0],[0,10],[10,10]]
cells = [[1,2,3,4]]
pols = None
firtsfloors = MKPOL([verts, cells, pols])
firtsfloorscolor = COLOR(BLUE)(firtsfloors)

verts = [[20,20],[30,20],[30,30],[20,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors2 = MKPOL([verts, cells, pols])
firtsfloorscolor2 = COLOR(BLUE)(firtsfloors2)

verts = [[0,0],[30,0],[30,30],[0,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors9 = MKPOL([verts, cells, pols])
firtsfloorscolor9 = COLOR(GRAY)(firtsfloors9)

primopiano = STRUCT([firtsfloorscolor,firtsfloorscolor2,firtsfloorscolor9])
#VIEW(primopiano)

#SECONDPIANO

verts = [[20,0],[30,0],[20,10],[30,10]]
cells = [[1,2,3,4]]
pols = None
secondfloors3 = MKPOL([verts, cells, pols])
secondfloorscolor3 = COLOR(GREEN)(secondfloors3)

verts = [[0,20],[0,30],[10,20],[10,30]]
cells = [[1,2,3,4]]
pols = None
secondfloors4 = MKPOL([verts, cells, pols])
secondfloorscolor4 = COLOR(GREEN)(secondfloors4)

verts = [[0,0],[30,0],[30,30],[0,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors10 = MKPOL([verts, cells, pols])
firtsfloorscolor10 = COLOR(GRAY)(firtsfloors10)

secondopiano = STRUCT([secondfloorscolor3,secondfloorscolor4,firtsfloorscolor10])
#VIEW(secondopiano)

#TERZOPIANO

verts = [[10,0],[20,0],[10,10],[20,10]]
cells = [[1,2,3,4]]
pols = None
threefloors5 = MKPOL([verts, cells, pols])
threefloorscolor5 = COLOR(YELLOW)(threefloors5)

verts = [[20,10],[30,10],[20,20],[30,20]]
cells = [[1,2,3,4]]
pols = None
threefloors6 = MKPOL([verts, cells, pols])
threefloorscolor6 = COLOR(YELLOW)(threefloors6)

verts = [[10,20],[20,20],[20,30],[10,30]]
cells = [[1,2,3,4]]
pols = None
threefloors7 = MKPOL([verts, cells, pols])
threefloorscolor7 = COLOR(YELLOW)(threefloors7)

verts = [[0,0],[30,0],[30,30],[0,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors11 = MKPOL([verts, cells, pols])
firtsfloorscolor11 = COLOR(GRAY)(firtsfloors11)



terzopiano = STRUCT([threefloorscolor5,threefloorscolor6,threefloorscolor7,firtsfloorscolor11])

#QUARTOPIANO

verts = [[0,10],[20,10],[20,20],[0,20]]
cells = [[1,2,3,4]]
pols = None
fourfloors8 = MKPOL([verts, cells, pols])
fourfloorscolor8 = COLOR(RED)(fourfloors8)

verts = [[0,0],[30,0],[30,30],[0,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors12 = MKPOL([verts, cells, pols])
firtsfloorscolor12 = COLOR(GRAY)(firtsfloors12)
quartopiano = STRUCT([fourfloorscolor8,firtsfloorscolor12])





strutturafinale20D = STRUCT([primopiano,secondopiano,terzopiano,quartopiano,pianoterra])
VIEW(strutturafinale20D)

primopianotrasl = T(3)(30)(primopiano)
secondopianotrasl = T(3)(45)(secondopiano)
terzopianotrasl = T(3)(60)(terzopiano)
quartopianotrasl = T(3)(75)(quartopiano)

strutturaedificio = STRUCT([pianoterra,primopianotrasl,secondopianotrasl,terzopianotrasl,quartopianotrasl])
VIEW(strutturaedificio)



