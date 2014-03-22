from pyplasm import *

verts = [[0,0],[30,0],[0,150],[30,150]]
cells = [[1,2,3,4]]
pols = None
primafacciata = MKPOL([verts, cells, pols])

verts = [[1,1,0],[3,1,0],[1,3,0],[3,3,0]]
cells = [[1,2,3,4]]
pols = None
finestra = MKPOL([verts, cells, pols])
colorfinestra = COLOR(CYAN)(finestra)

pair_x = [T(1)(3), colorfinestra]
windows = STRUCT(NN(8)(pair_x))
pair_z = [T(2)(5), windows]
windowsfinal = STRUCT(NN(29)(pair_z))


verts = [[30,0,0],[30,0,-30],[30,150,0],[30,150,-30]]
cells = [[1,2,3,4]]
pols = None
primafacciata1 = MKPOL([verts, cells, pols])

verts = [[30,1,-1],[30,1,-3],[30,3,-1],[30,3,-3]]
cells = [[1,2,3,4]]
pols = None
finestra1 = MKPOL([verts, cells, pols])
colorfinestra1 = COLOR(CYAN)(finestra1)

pair_x = [T(3)(-3), colorfinestra1]
windows1 = STRUCT(NN(8)(pair_x))
pair_z = [T(2)(5), windows1]
windowsfinal1 = STRUCT(NN(29)(pair_z))


verts = [[30,0,-30],[0,0,-30],[30,150,-30],[0,150,-30]]
cells = [[1,2,3,4]]
pols = None
primafacciata2 = MKPOL([verts, cells, pols])

verts = [[30,1,-30],[28,1,-30],[30,3,-30],[28,3,-30]]
cells = [[1,2,3,4]]
pols = None
finestra2 = MKPOL([verts, cells, pols])
colorfinestra2 = COLOR(CYAN)(finestra2)

pair_x = [T(1)(-3), colorfinestra2]
windows2 = STRUCT(NN(8)(pair_x))
pair_z = [T(2)(5), windows2]
windowsfinal2 = STRUCT(NN(29)(pair_z))

verts = [[0,0,-30],[0,0,0],[0,150,-30],[0,150,0]]
cells = [[1,2,3,4]]
pols = None
primafacciata3 = MKPOL([verts, cells, pols])

verts = [[0,1,-30],[0,3,-30],[0,1,-28],[0,3,-28]]
cells = [[1,2,3,4]]
pols = None
finestra3 = MKPOL([verts, cells, pols])
colorfinestra3 = COLOR(CYAN)(finestra3)

pair_x = [T(3)(3), colorfinestra3]
windows3 = STRUCT(NN(8)(pair_x))
pair_z = [T(2)(5), windows3]
windowsfinal3 = STRUCT(NN(29)(pair_z))

edificio = STRUCT([primafacciata,windows,windowsfinal,windows1,windowsfinal1,windows2,windowsfinal2,windows3,windowsfinal3,primafacciata1,primafacciata2,primafacciata3])
VIEW(edificio)

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






primopianotrasl = T(2)(60)(primopiano)

secondopianotrasl = T(2)(90)(secondopiano)
terzopianotrasl = T(2)(120)(terzopiano)
quartopianotrasl = T(2)(150)(quartopiano)

strutturaedificio = STRUCT([pianoterra,primopianotrasl,secondopianotrasl,terzopianotrasl,quartopianotrasl])
VIEW(strutturaedificio)





edificio1 = STRUCT([primafacciata,windows,windowsfinal,windows1,windowsfinal1,windows2,windowsfinal2,windows3,windowsfinal3,primafacciata1,primafacciata2,primafacciata3,strutturaedificio])
VIEW(edificio1)





