from pyplasm import *

#FIRSTFLOORS

verts = [[0,0],[10,0],[0,10],[10,10]]
cells = [[1,2,3,4]]
pols = None
firtsfloors = MKPOL([verts, cells, pols])
firtsfloors = PROD([firtsfloors, Q(60)])

verts = [[20,20],[20,30],[30,20],[30,30]]
cells = [[1,2,3,4]]
pols = None
firtsfloors2 = MKPOL([verts, cells, pols])
firtsfloors2 = PROD([firtsfloors2, Q(60)])

#SECONDFLOORS

verts = [[20,0],[30,0],[20,10],[30,10]]
cells = [[1,2,3,4]]
pols = None
secondfloors = MKPOL([verts, cells, pols])
secondfloors = PROD([secondfloors, Q(90)])

verts = [[0,20],[0,30],[10,20],[10,30]]
cells = [[1,2,3,4]]
pols = None
secondfloors2 = MKPOL([verts, cells, pols])
secondfloors2 = PROD([secondfloors2, Q(90)])

#THREEFLOORS

verts = [[10,0],[20,0],[10,10],[20,10]]
cells = [[1,2,3,4]]
pols = None
threefloors = MKPOL([verts, cells, pols])
threefloors = PROD([threefloors, Q(120)])

verts = [[20,10],[30,10],[20,20],[30,20]]
cells = [[1,2,3,4]]
pols = None
threefloors2 = MKPOL([verts, cells, pols])
threefloors2 = PROD([threefloors2, Q(120)])

verts = [[10,20],[20,20],[10,30],[20,30]]
cells = [[1,2,3,4]]
pols = None
threefloors3 = MKPOL([verts, cells, pols])
threefloors3 = PROD([threefloors3, Q(120)])

#FOURFLOORS

verts = [[0,10],[0,20],[20,10],[20,20]]
cells = [[1,2,3,4]]
pols = None
fourfloors = MKPOL([verts, cells, pols])
fourfloors = PROD([fourfloors, Q(150)])

#INTERRUZIONI 

verts = [[0,0,35],[0,0,41],[30,0,35],[30,0,41]]
cells = [[1,2,3,4]]
pols = None
inter = MKPOL([verts, cells, pols])

verts = [[0,0,35],[0,0,41],[0,30,35],[0,30,41]]
cells = [[1,2,3,4]]
pols = None
inter2 = MKPOL([verts, cells, pols])

verts = [[30,0,35],[30,0,41],[30,30,35],[30,30,41]]
cells = [[1,2,3,4]]
pols = None
inter3 = MKPOL([verts, cells, pols])

verts = [[30,30,35],[30,30,41],[0,30,35],[0,30,41]]
cells = [[1,2,3,4]]
pols = None
inter4 = MKPOL([verts, cells, pols])

verts = [[10,0,86],[10,0,90],[30,0,86],[30,0,90]]
cells = [[1,2,3,4]]
pols = None
inter11 = MKPOL([verts, cells, pols])

verts = [[0,10,86],[0,10,90],[0,30,86],[0,30,90]]
cells = [[1,2,3,4]]
pols = None
inter12 = MKPOL([verts, cells, pols])

verts = [[30,0,86],[30,0,90],[30,20,86],[30,20,90]]
cells = [[1,2,3,4]]
pols = None
inter13 = MKPOL([verts, cells, pols])

verts = [[20,30,86],[20,30,90],[0,30,86],[0,30,90]]
cells = [[1,2,3,4]]
pols = None
inter14 = MKPOL([verts, cells, pols])

verts = [[30,20,86],[30,20,90],[20,20,86],[20,20,90]]
cells = [[1,2,3,4]]
pols = None
inter15 = MKPOL([verts, cells, pols])

verts = [[20,20,86],[20,20,90],[20,30,86],[20,30,90]]
cells = [[1,2,3,4]]
pols = None
inter16 = MKPOL([verts, cells, pols])

verts = [[10,0,86],[10,0,90],[10,10,86],[10,10,90]]
cells = [[1,2,3,4]]
pols = None
inter17 = MKPOL([verts, cells, pols])


verts = [[0,10,86],[0,10,90],[10,10,86],[10,10,90]]
cells = [[1,2,3,4]]
pols = None
inter18 = MKPOL([verts, cells, pols])

verts = [[10,0,116],[10,0,120],[20,0,116],[20,0,120]]
cells = [[1,2,3,4]]
pols = None
inter19 = MKPOL([verts, cells, pols])

verts = [[20,0,116],[20,0,120],[20,10,116],[20,10,120]]
cells = [[1,2,3,4]]
pols = None
inter20 = MKPOL([verts, cells, pols])

verts = [[20,10,116],[20,10,120],[30,10,116],[30,10,120]]
cells = [[1,2,3,4]]
pols = None
inter21 = MKPOL([verts, cells, pols])

verts = [[30,10,116],[30,10,120],[30,20,116],[30,20,120]]
cells = [[1,2,3,4]]
pols = None
inter22 = MKPOL([verts, cells, pols])

verts = [[20,30,116],[20,30,120],[10,30,116],[10,30,120]]
cells = [[1,2,3,4]]
pols = None
inter23 = MKPOL([verts, cells, pols])

verts = [[10,30,116],[10,30,120],[10,20,116],[10,20,120]]
cells = [[1,2,3,4]]
pols = None
inter24 = MKPOL([verts, cells, pols])

verts = [[10,20,116],[10,20,120],[0,20,116],[0,20,120]]
cells = [[1,2,3,4]]
pols = None
inter25 = MKPOL([verts, cells, pols])

verts = [[0,20,116],[0,20,120],[0,10,116],[0,10,120]]
cells = [[1,2,3,4]]
pols = None
inter26 = MKPOL([verts, cells, pols])

verts = [[30,20,116],[30,20,120],[20,20,116],[20,20,120]]
cells = [[1,2,3,4]]
pols = None
inter27 = MKPOL([verts, cells, pols])

verts = [[20,20,116],[20,20,120],[20,30,116],[20,30,120]]
cells = [[1,2,3,4]]
pols = None
inter28 = MKPOL([verts, cells, pols])

verts = [[10,0,116],[10,0,120],[10,10,116],[10,10,120]]
cells = [[1,2,3,4]]
pols = None
inter29 = MKPOL([verts, cells, pols])


verts = [[0,10,116],[0,10,120],[10,10,116],[10,10,120]]
cells = [[1,2,3,4]]
pols = None
inter30 = MKPOL([verts, cells, pols])



intesub1 = STRUCT([inter27,inter28,inter29,inter30,inter19,inter20,inter21,inter22,inter23,inter24,inter25,inter26])


verts = [[0,10,144],[0,10,150],[20,10,144],[20,10,150]]
cells = [[1,2,3,4]]
pols = None
inter31 = MKPOL([verts, cells, pols])

verts = [[20,10,144],[20,10,150],[20,20,144],[20,20,150]]
cells = [[1,2,3,4]]
pols = None
inter32 = MKPOL([verts, cells, pols])

verts = [[20,20,144],[20,20,150],[0,20,144],[0,20,150]]
cells = [[1,2,3,4]]
pols = None
inter33 = MKPOL([verts, cells, pols])

verts = [[0,20,144],[0,20,150],[0,10,144],[0,10,150]]
cells = [[1,2,3,4]]
pols = None
inter34 = MKPOL([verts, cells, pols])

intesub2 = STRUCT([inter31,inter32,inter33,inter34])

#ANTENNE
cone = CONE([0.5,15])(35)
conetrl = T([1,2,3])([6,14,150])(cone)
cone1 = CONE([0.5,15])(35)
conetrl1 = T([1,2,3])([14,14,150])(cone1)

#FINESTRE
#1facciata1
verts = [[1,0,2],[3,0,2],[1,0,5],[3,0,5]]
cells = [[1,2,3,4]]
pols = None
finestra = MKPOL([verts, cells, pols])
colorfinestra = COLOR(CYAN)(finestra)

pair_x = [T(1)(3), colorfinestra]
windows = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows]
windowsfinal = STRUCT(NN(6)(pair_z))
#2facciata1
verts = [[30,1,2],[30,3,2],[30,1,5],[30,3,5]]
cells = [[1,2,3,4]]
pols = None
finestra2 = MKPOL([verts, cells, pols])
colorfinestra2 = COLOR(CYAN)(finestra2)

pair_x = [T(2)(3), colorfinestra2]
windows2 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows2]
windowsfinal2 = STRUCT(NN(6)(pair_z))

#3facciata1
verts = [[27,30,2],[29,30,2],[27,30,5],[29,30,5]]
cells = [[1,2,3,4]]
pols = None
finestra3 = MKPOL([verts, cells, pols])
colorfinestra3 = COLOR(CYAN)(finestra3)

pair_x = [T(1)(-3), colorfinestra3]
windows3 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows3]
windowsfinal3 = STRUCT(NN(6)(pair_z))

#4facciata1
verts = [0,29,2],[0,27,2],[0,29,5],[0,27,5]
cells = [[1,2,3,4]]
pols = None
finestra4 = MKPOL([verts, cells, pols])
colorfinestra4 = COLOR(CYAN)(finestra4)

pair_x = [T(2)(-3), colorfinestra4]
windows4 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows4]
windowsfinal4 = STRUCT(NN(6)(pair_z))

#1facciata2
verts = [1,0,43],[3,0,43],[1,0,46],[3,0,46]
cells = [[1,2,3,4]]
pols = None
finestra5 = MKPOL([verts, cells, pols])
colorfinestra5 = COLOR(CYAN)(finestra5)

pair_x = [T(1)(3), colorfinestra5]
windows5 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows5]
windowsfinal5 = STRUCT(NN(3)(pair_z))

#1facciata2
verts = [10,0,61],[12,0,61],[10,0,64],[12,0,64]
cells = [[1,2,3,4]]
pols = None
finestra6 = MKPOL([verts, cells, pols])
colorfinestra6 = COLOR(CYAN)(finestra6)

pair_x = [T(1)(3), colorfinestra6]
windows6 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows6]
windowsfinal6 = STRUCT(NN(4)(pair_z))

#1facciata2

verts = [30,1,61],[30,3,61],[30,1,64],[30,3,64]
cells = [[1,2,3,4]]
pols = None
finestra7 = MKPOL([verts, cells, pols])
colorfinestra7 = COLOR(CYAN)(finestra7)

pair_x = [T(2)(3), colorfinestra7]
windows7 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows7]
windowsfinal7 = STRUCT(NN(4)(pair_z))

verts = [30,1,43],[30,3,43],[30,1,46],[30,3,46]
cells = [[1,2,3,4]]
pols = None
finestra8 = MKPOL([verts, cells, pols])
colorfinestra8 = COLOR(CYAN)(finestra8)

pair_x = [T(2)(3), colorfinestra8]
windows8 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows8]
windowsfinal8 = STRUCT(NN(3)(pair_z))

#1facciata2

verts = [20,30,61],[18,30,61],[20,30,64],[18,30,64]
cells = [[1,2,3,4]]
pols = None
finestra9 = MKPOL([verts, cells, pols])
colorfinestra9 = COLOR(CYAN)(finestra9)

pair_x = [T(1)(-3), colorfinestra9]
windows9 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows9]
windowsfinal9 = STRUCT(NN(4)(pair_z))

verts = [27,30,43],[29,30,43],[27,30,46],[29,30,46]
cells = [[1,2,3,4]]
pols = None
finestra10 = MKPOL([verts, cells, pols])
colorfinestra10 = COLOR(CYAN)(finestra10)

pair_x = [T(1)(-3), colorfinestra10]
windows10 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows10]
windowsfinal10 = STRUCT(NN(3)(pair_z))

#1facciata2

verts = [0,29,61],[0,27,61],[0,29,64],[0,27,64]
cells = [[1,2,3,4]]
pols = None
finestra12 = MKPOL([verts, cells, pols])
colorfinestra12 = COLOR(CYAN)(finestra12)

pair_x = [T(2)(-3), colorfinestra12]
windows12 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows12]
windowsfinal12 = STRUCT(NN(4)(pair_z))

verts = [0,29,43],[0,27,43],[0,29,46],[0,27,46]
cells = [[1,2,3,4]]
pols = None
finestra11 = MKPOL([verts, cells, pols])
colorfinestra11 = COLOR(CYAN)(finestra11)

pair_x = [T(2)(-3), colorfinestra11]
windows11 = STRUCT(NN(8)(pair_x))

pair_z = [T(3)(4.5), windows11]
windowsfinal11 = STRUCT(NN(3)(pair_z))

verts = [1,10,61],[3,10,61],[1,10,64],[3,10,64]
cells = [[1,2,3,4]]
pols = None
finestra13 = MKPOL([verts, cells, pols])
colorfinestra13 = COLOR(CYAN)(finestra13)

pair_x = [T(1)(3), colorfinestra13]
windows13 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows13]
windowsfinal13 = STRUCT(NN(4)(pair_z)) 

verts = [10,1,61],[10,3,61],[10,1,64],[10,3,64]
cells = [[1,2,3,4]]
pols = None
finestra14 = MKPOL([verts, cells, pols])
colorfinestra14 = COLOR(CYAN)(finestra14)

pair_x = [T(2)(3), colorfinestra14]
windows14 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows14]
windowsfinal14 = STRUCT(NN(4)(pair_z))

verts = [29,20,61],[27,20,61],[29,20,64],[27,20,64]
cells = [[1,2,3,4]]
pols = None
finestra15 = MKPOL([verts, cells, pols])
colorfinestra15 = COLOR(CYAN)(finestra15)

pair_x = [T(1)(-3), colorfinestra15]
windows15 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows15]
windowsfinal15 = STRUCT(NN(4)(pair_z))

verts = [20,29,61],[20,27,61],[20,29,64],[20,27,64]
cells = [[1,2,3,4]]
pols = None
finestra16 = MKPOL([verts, cells, pols])
colorfinestra16 = COLOR(CYAN)(finestra16)

pair_x = [T(2)(-3), colorfinestra16]
windows16 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows16]
windowsfinal16 = STRUCT(NN(4)(pair_z))
#3piano
verts = [1,10,91],[3,10,91],[1,10,94],[3,10,94]
cells = [[1,2,3,4]]
pols = None
finestra17 = MKPOL([verts, cells, pols])
colorfinestra17 = COLOR(CYAN)(finestra17)

pair_x = [T(1)(3), colorfinestra17]
windows17 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows17]
windowsfinal17 = STRUCT(NN(4)(pair_z)) 

verts = [10,1,91],[10,3,91],[10,1,94],[10,3,94]
cells = [[1,2,3,4]]
pols = None
finestra18 = MKPOL([verts, cells, pols])
colorfinestra18 = COLOR(CYAN)(finestra18)

pair_x = [T(2)(3), colorfinestra18]
windows18 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows18]
windowsfinal18 = STRUCT(NN(4)(pair_z))

verts = [10,0,91],[12,0,91],[10,0,94],[12,0,94]
cells = [[1,2,3,4]]
pols = None
finestra19 = MKPOL([verts, cells, pols])
colorfinestra19 = COLOR(CYAN)(finestra19)

pair_x = [T(1)(3), colorfinestra19]
windows19 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows19]
windowsfinal19 = STRUCT(NN(4)(pair_z))

verts = [20,1,91],[20,3,91],[20,1,94],[20,3,94]
cells = [[1,2,3,4]]
pols = None
finestra20 = MKPOL([verts, cells, pols])
colorfinestra20 = COLOR(CYAN)(finestra20)

pair_x = [T(2)(3), colorfinestra20]
windows20 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows20]
windowsfinal20 = STRUCT(NN(4)(pair_z))

verts = [20,10,91],[22,10,91],[20,10,94],[22,10,94]
cells = [[1,2,3,4]]
pols = None
finestra21 = MKPOL([verts, cells, pols])
colorfinestra21 = COLOR(CYAN)(finestra21)

pair_x = [T(1)(3), colorfinestra21]
windows21 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows21]
windowsfinal21 = STRUCT(NN(4)(pair_z))

verts = [30,10,91],[30,12,91],[30,10,94],[30,12,94]
cells = [[1,2,3,4]]
pols = None
finestra22 = MKPOL([verts, cells, pols])
colorfinestra22 = COLOR(CYAN)(finestra22)

pair_x = [T(2)(3), colorfinestra22]
windows22 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows22]
windowsfinal22 = STRUCT(NN(4)(pair_z))

verts = [29,20,91],[27,20,91],[29,20,94],[27,20,94]
cells = [[1,2,3,4]]
pols = None
finestra23 = MKPOL([verts, cells, pols])
colorfinestra23 = COLOR(CYAN)(finestra23)

pair_x = [T(1)(-3), colorfinestra23]
windows23 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows23]
windowsfinal23 = STRUCT(NN(4)(pair_z))

verts = [20,29,91],[20,27,91],[20,29,94],[20,27,94]
cells = [[1,2,3,4]]
pols = None
finestra24 = MKPOL([verts, cells, pols])
colorfinestra24 = COLOR(CYAN)(finestra24)

pair_x = [T(2)(-3), colorfinestra24]
windows24 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows24]
windowsfinal24 = STRUCT(NN(4)(pair_z))

verts = [20,30,91],[18,30,91],[20,30,94],[18,30,94]
cells = [[1,2,3,4]]
pols = None
finestra25 = MKPOL([verts, cells, pols])
colorfinestra25 = COLOR(CYAN)(finestra25)

pair_x = [T(1)(-3), colorfinestra25]
windows25 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows25]
windowsfinal25 = STRUCT(NN(4)(pair_z))

verts = [10,29,91],[10,27,91],[10,29,94],[10,27,94]
cells = [[1,2,3,4]]
pols = None
finestra26 = MKPOL([verts, cells, pols])
colorfinestra26 = COLOR(CYAN)(finestra26)

pair_x = [T(2)(-3), colorfinestra26]
windows26 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows26]
windowsfinal26 = STRUCT(NN(4)(pair_z))

verts = [10,20,91],[12,20,91],[10,20,94],[12,20,94]
cells = [[1,2,3,4]]
pols = None
finestra27 = MKPOL([verts, cells, pols])
colorfinestra27 = COLOR(CYAN)(finestra27)

pair_x = [T(1)(-3), colorfinestra27]
windows27 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows27]
windowsfinal27 = STRUCT(NN(4)(pair_z))

verts = [0,19,91],[0,17,91],[0,19,94],[0,17,94]
cells = [[1,2,3,4]]
pols = None
finestra28 = MKPOL([verts, cells, pols])
colorfinestra28 = COLOR(CYAN)(finestra28)

pair_x = [T(2)(-3), colorfinestra28]
windows28 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows28]
windowsfinal28 = STRUCT(NN(4)(pair_z))
#4piano
verts = [1,10,121],[3,10,121],[1,10,124],[3,10,124]
cells = [[1,2,3,4]]
pols = None
finestra29 = MKPOL([verts, cells, pols])
colorfinestra29 = COLOR(CYAN)(finestra29)

pair_x = [T(1)(3), colorfinestra29]
windows29 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows29]
windowsfinal29 = STRUCT(NN(4)(pair_z)) 

verts = [20,10,121],[20,12,121],[20,10,124],[20,12,124]
cells = [[1,2,3,4]]
pols = None
finestra30 = MKPOL([verts, cells, pols])
colorfinestra30 = COLOR(CYAN)(finestra30)

pair_x = [T(2)(3), colorfinestra30]
windows30 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows30]
windowsfinal30 = STRUCT(NN(4)(pair_z)) 

verts = [20,20,121],[18,20,121],[20,20,124],[18,20,124]
cells = [[1,2,3,4]]
pols = None
finestra31 = MKPOL([verts, cells, pols])
colorfinestra31 = COLOR(CYAN)(finestra31)

pair_x = [T(1)(-3), colorfinestra31]
windows31 = STRUCT(NN(5)(pair_x))

pair_z = [T(3)(4.5), windows31]
windowsfinal31 = STRUCT(NN(4)(pair_z)) 

verts = [0,20,121],[0,18,121],[0,20,124],[0,18,124]
cells = [[1,2,3,4]]
pols = None
finestra32 = MKPOL([verts, cells, pols])
colorfinestra32 = COLOR(CYAN)(finestra32)

pair_x = [T(2)(-3), colorfinestra32]
windows32 = STRUCT(NN(2)(pair_x))

pair_z = [T(3)(4.5), windows32]
windowsfinal32 = STRUCT(NN(4)(pair_z)) 




prova = STRUCT([COLOR(BROWN)(firtsfloors), COLOR(BROWN)(firtsfloors2),COLOR(BROWN)(secondfloors),COLOR(BROWN)(secondfloors2),COLOR(BROWN)(threefloors),COLOR(BROWN)(threefloors2),COLOR(BROWN)(threefloors3),COLOR(BROWN)(fourfloors),COLOR(BLACK)(inter),COLOR(BLACK)(inter2),COLOR(BLACK)(inter3),COLOR(BLACK)(inter4),COLOR(RED)(inter11),COLOR(RED)(inter12),COLOR(RED)(inter13),COLOR(RED)(inter14),COLOR(RED)(inter15),COLOR(RED)(inter16),COLOR(RED)(inter17),COLOR(RED)(inter18),COLOR(RED)(intesub1),COLOR(BLACK)(intesub2),COLOR(RED)(conetrl),COLOR(RED)(conetrl1),windows,windowsfinal,windows2,windowsfinal2,windows3,windowsfinal3,windows4,windowsfinal4,windows5,windowsfinal5,windows6,windowsfinal6,windows7,windowsfinal7,windows8,windowsfinal8,windows9,windowsfinal9,windows10,windowsfinal10,windows12,windowsfinal12,windows11,windowsfinal11,windows13,windowsfinal13,windows14,windowsfinal14,windows15,windowsfinal15,windows16,windowsfinal16,windows17,windowsfinal17,windows18,windowsfinal18,windows19,windowsfinal19,windows20,windowsfinal20,windows21,windowsfinal21,windows22,windowsfinal22,windows23,windowsfinal23,windows24,windowsfinal24,windows25,windowsfinal25,windows26,windowsfinal26,windows27,windowsfinal27,windows28,windowsfinal28,windows29,windowsfinal29,windows30,windowsfinal30,windows31,windowsfinal31,windows32,windowsfinal32])
VIEW(SKELETON(1)(prova))
VIEW(prova)
