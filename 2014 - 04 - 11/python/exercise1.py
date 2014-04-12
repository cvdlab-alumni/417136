from pyplasm import *
#BASE primi 9 piani
verts0 = [[3,3],[12,3],[3,12],[12,12]]
cells0 = [[1,2,3,4]]
pols0 = None
floor0 = MKPOL([verts0, cells0, pols0])
 

floor0Solid = PROD([floor0,Q(0.2)])
floor1Solid = T([3])([3])(floor0Solid)
floor2Solid = T([3])([6])(floor0Solid)
floor3Solid = T([3])([9])(floor0Solid)
floor4Solid = T([3])([12])(floor0Solid)
floor5Solid = T([3])([15])(floor0Solid)
floor6Solid = T([3])([18])(floor0Solid)
floor7Solid = T([3])([21])(floor0Solid)
floor8Solid = T([3])([24])(floor0Solid)
floor9Solid = T([3])([27])(floor0Solid)

#pareti primi 9 piani 
verts0PVert = [[5.95,3],[6.05,3],[5.95,12],[6.05,12]]
cells0PVert = [[1,2,3,4]]
pols0PVert = None
wall0P = MKPOL([verts0PVert, cells0PVert, pols0PVert])
wall0SolidVert = PROD([wall0P,Q(3)])
wall1SolidVert = T([3])([3])(wall0SolidVert)
wall2SolidVert = T([3])([6])(wall0SolidVert)
wall3SolidVert = T([3])([9])(wall0SolidVert)
wall4SolidVert = T([3])([12])(wall0SolidVert)
wall5SolidVert = T([3])([15])(wall0SolidVert)
wall6SolidVert = T([3])([18])(wall0SolidVert)
wall7SolidVert = T([3])([21])(wall0SolidVert)
wall8SolidVert = T([3])([24])(wall0SolidVert)

orzs0POrz = [[3,5.95],[3,6.05],[12,5.95],[12,6.05]]
cells0POrz = [[1,2,3,4]]
pols0POrz = None
wall0POrz = MKPOL([orzs0POrz, cells0POrz, pols0POrz])
wall0SolidOrz = PROD([wall0POrz,Q(3)])
wall1SolidOrz = T([3])([3])(wall0SolidOrz)
wall2SolidOrz = T([3])([6])(wall0SolidOrz)
wall3SolidOrz = T([3])([9])(wall0SolidOrz)
wall4SolidOrz = T([3])([12])(wall0SolidOrz)
wall5SolidOrz = T([3])([15])(wall0SolidOrz)
wall6SolidOrz = T([3])([18])(wall0SolidOrz)
wall7SolidOrz = T([3])([21])(wall0SolidOrz)
wall8SolidOrz = T([3])([24])(wall0SolidOrz)


semiwall0_2 = COLOR(GRAY)(STRUCT([wall0SolidOrz,wall1SolidOrz,wall2SolidOrz,wall3SolidOrz,wall4SolidOrz,wall5SolidOrz,wall6SolidOrz,wall7SolidOrz,wall8SolidOrz]))
semiwall1_2 = COLOR(GRAY)(T([2])([3])(semiwall0_2))
semiwall0_1 = COLOR(GRAY)(STRUCT([wall0SolidVert,wall1SolidVert,wall2SolidVert,wall3SolidVert,wall4SolidVert,wall5SolidVert,wall6SolidVert,wall7SolidVert,wall8SolidVert]))
semiwall1_1 = COLOR(GRAY)(T([1])([3])(semiwall0_1))

#PRIMO secondi 9 piani
verts1 = [[3,3],[9,3],[9,9],[3,9]]
cells1 = [[1,2,3,4]]
pols1 = None
floor10_1 = MKPOL([verts1, cells1, pols1])
verts1_1 = [[6,6],[12,6],[12,12],[6,12]]
cells1_1 = [[1,2,3,4]]
pols1_1 = None
floor10_2 = MKPOL([verts1_1, cells1_1, pols1_1])
floor10 = (STRUCT([floor10_2,floor10_1]))
floor10Solid = PROD([floor10,Q(0.2)])

floor10posOK = COLOR(RED)(T([3])([27.1])(floor10Solid))

floor11Solid = T([3])([3])(floor10posOK)
floor12Solid = T([3])([6])(floor10posOK)
floor13Solid = T([3])([9])(floor10posOK)
floor14Solid = T([3])([12])(floor10posOK)
floor15Solid = T([3])([15])(floor10posOK)
floor16Solid = T([3])([18])(floor10posOK)
floor17Solid = T([3])([21])(floor10posOK)
floor18Solid = T([3])([24])(floor10posOK)
floor19Solid = T([3])([27])(floor10posOK)


#pareti SECONDI 9 piani 
verts0PVert1 = [[5.95,3],[6.05,3],[5.95,9],[6.05,9]]
cells0PVert1 = [[1,2,3,4]]
pols0PVert1 = None
wall0P1 = MKPOL([verts0PVert1, cells0PVert1, pols0PVert1])
wall0SolidVert1 = PROD([wall0P1,Q(3)])
wall0Ptrasl = T([3])([27.1])(wall0SolidVert1)
wall1Ptrasl = T([3])([3])(wall0Ptrasl)
wall2Ptrasl = T([3])([6])(wall0Ptrasl)
wall3Ptrasl = T([3])([9])(wall0Ptrasl)
wall4Ptrasl = T([3])([12])(wall0Ptrasl)
wall5Ptrasl = T([3])([15])(wall0Ptrasl)
wall6Ptrasl = T([3])([18])(wall0Ptrasl)
wall7Ptrasl = T([3])([21])(wall0Ptrasl)
wall8Ptrasl = T([3])([24])(wall0Ptrasl)

orzs0POrz1 = [[3,5.95],[3,6.05],[9,5.95],[9,6.05]]
cells0POrz1 = [[1,2,3,4]]
pols0POrz1 = None
wall0POrz1 = MKPOL([orzs0POrz1, cells0POrz1, pols0POrz1])
wall0SolidOrz1 = PROD([wall0POrz1,Q(3)])
wall0PtraslOrz = T([3])([27.1])(wall0SolidOrz1)
wall1PtraslOrz = T([3])([3])(wall0PtraslOrz)
wall2PtraslOrz = T([3])([6])(wall0PtraslOrz)
wall3PtraslOrz = T([3])([9])(wall0PtraslOrz)
wall4PtraslOrz = T([3])([12])(wall0PtraslOrz)
wall5PtraslOrz = T([3])([15])(wall0PtraslOrz)
wall6PtraslOrz = T([3])([18])(wall0PtraslOrz)
wall7PtraslOrz = T([3])([21])(wall0PtraslOrz)
wall8PtraslOrz = T([3])([24])(wall0PtraslOrz)

semiwall0_3 = COLOR(GRAY)(STRUCT([wall0Ptrasl,wall1Ptrasl,wall2Ptrasl,wall3Ptrasl,wall4Ptrasl,wall5Ptrasl,wall6Ptrasl,wall7Ptrasl,wall8Ptrasl]))
semiwall1_3 = COLOR(GRAY)(T([1,2])([3,3])(semiwall0_3))
semiwall0_4 = COLOR(GRAY)(STRUCT([wall0PtraslOrz,wall1PtraslOrz,wall2PtraslOrz,wall3PtraslOrz,wall4PtraslOrz,wall5PtraslOrz,wall6PtraslOrz,wall7PtraslOrz,wall8PtraslOrz]))
semiwall1_4 = COLOR(GRAY)(T([1,2])([3,3])(semiwall0_4))

#TERZO  6 piani
verts2 = [[6,3],[9,3],[6,12],[9,12]]
cells2 = [[1,2,3,4]]
pols2 = None
floor20_1 = MKPOL([verts2, cells2, pols2])
verts2_1 = [[3,6],[3,9],[12,6],[12,9]]
cells2_1 = [[1,2,3,4]]
pols2_1 = None
floor20_2 = MKPOL([verts2_1, cells2_1, pols2_1])
floor20 = (STRUCT([floor20_2,floor20_1]))
floor20Solid = PROD([floor20,Q(0.2)])

floor20posOK = T([3])([54.3])(floor20Solid)

floor21Solid = T([3])([3])(floor20posOK)
floor22Solid = T([3])([6])(floor20posOK)
floor23Solid = T([3])([9])(floor20posOK)
floor24Solid = T([3])([12])(floor20posOK)
floor25Solid = T([3])([15])(floor20posOK)
floor26Solid = T([3])([18])(floor20posOK)

#pareti TERZI 6 piani 
verts0PVert2 = [[5.95,6],[6.05,6],[5.95,9],[6.05,9]]
cells0PVert2 = [[1,2,3,4]]
pols0PVert2 = None
wall0P2 = MKPOL([verts0PVert2, cells0PVert2, pols0PVert2])
wall0SolidVert2 = PROD([wall0P2,Q(3)])
wall0Ptrasl2 = T([3])([54.3])(wall0SolidVert2)
wall1Ptrasl2 = T([3])([3])(wall0Ptrasl2)
wall2Ptrasl2 = T([3])([6])(wall0Ptrasl2)
wall3Ptrasl2 = T([3])([9])(wall0Ptrasl2)
wall4Ptrasl2 = T([3])([12])(wall0Ptrasl2)
wall5Ptrasl2 = T([3])([15])(wall0Ptrasl2)

orzs0POrz2 = [[6,5.95],[6,6.05],[9,5.95],[9,6.05]]
cells0POrz2 = [[1,2,3,4]]
pols0POrz2 = None
wall0POrz2 = MKPOL([orzs0POrz2, cells0POrz2, pols0POrz2])
wall0SolidOrz2 = PROD([wall0POrz2,Q(3)])
wall0PtraslOrz1 = T([3])([54.3])(wall0SolidOrz2)
wall1PtraslOrz1 = T([3])([3])(wall0PtraslOrz1)
wall2PtraslOrz1 = T([3])([6])(wall0PtraslOrz1)
wall3PtraslOrz1 = T([3])([9])(wall0PtraslOrz1)
wall4PtraslOrz1 = T([3])([12])(wall0PtraslOrz1)
wall5PtraslOrz1 = T([3])([15])(wall0PtraslOrz1)


semiwall0_5 = COLOR(GRAY)(STRUCT([wall0Ptrasl2,wall1Ptrasl2,wall2Ptrasl2,wall3Ptrasl2,wall4Ptrasl2,wall5Ptrasl2]))
semiwall1_5 = COLOR(GRAY)(T([1])([3])(semiwall0_5))
semiwall0_6 = COLOR(GRAY)(STRUCT([wall0PtraslOrz1,wall1PtraslOrz1,wall2PtraslOrz1,wall3PtraslOrz1,wall4PtraslOrz1,wall5PtraslOrz1]))
semiwall1_6 = COLOR(GRAY)(T([2])([3])(semiwall0_6))


#QUARTO  6 piani
verts3 = [[6,6],[12,6],[12,9],[6,9]]
cells3 = [[1,2,3,4]]
pols3 = None
floor27 = MKPOL([verts3, cells3, pols3])
floor27Solid = PROD([floor27,Q(0.2)])

floor27posOK = COLOR(RED)(T([3])([69.3])(floor27Solid))

floor28Solid = T([3])([3])(floor27posOK)
floor29Solid = T([3])([6])(floor27posOK)
floor30Solid = T([3])([9])(floor27posOK)
floor31Solid = T([3])([12])(floor27posOK)
floor32Solid = T([3])([15])(floor27posOK)
floor33Solid = T([3])([18])(floor27posOK)

#pareti TERZI 6 piani 
verts0PVert3 = [[8.95,6],[9.05,6],[8.95,9],[9.05,9]]
cells0PVert3 = [[1,2,3,4]]
pols0PVert3 = None
wall0P3 = MKPOL([verts0PVert3, cells0PVert3, pols0PVert3])
wall0SolidVert3 = PROD([wall0P3,Q(3)])
wall0Ptrasl3 = T([3])([69.5])(wall0SolidVert3)
wall1Ptrasl3 = T([3])([3])(wall0Ptrasl3)
wall2Ptrasl3 = T([3])([6])(wall0Ptrasl3)
wall3Ptrasl3 = T([3])([9])(wall0Ptrasl3)
wall4Ptrasl3 = T([3])([12])(wall0Ptrasl3)
wall5Ptrasl3 = T([3])([15])(wall0Ptrasl3)



semiwall0_7 = COLOR(GRAY)(STRUCT([wall0Ptrasl3,wall1Ptrasl3,wall2Ptrasl3,wall3Ptrasl3,wall4Ptrasl3,wall5Ptrasl3]))


allfloor = STRUCT([floor0Solid,floor1Solid,floor2Solid,floor3Solid,floor4Solid,floor5Solid,floor6Solid,floor7Solid,floor8Solid,floor9Solid,floor10posOK,floor11Solid,floor12Solid,floor13Solid,floor14Solid,floor15Solid,floor16Solid,floor17Solid,floor18Solid,floor19Solid,floor20posOK,floor21Solid,floor22Solid,floor23Solid,floor24Solid,floor25Solid,floor26Solid,floor27posOK,floor28Solid,floor29Solid,floor30Solid,floor31Solid,floor32Solid,floor33Solid])
piano = STRUCT([semiwall1_1,allfloor,semiwall0_1,semiwall0_2,semiwall1_2,semiwall1_3,semiwall0_3,semiwall0_4,semiwall1_4,semiwall0_5,semiwall1_5,semiwall0_6,semiwall1_6,semiwall0_7])
A = S([1,2,3])([0.6,0.6,0.6])(piano)

VIEW(A)