from pyplasm import *


#primo blocco 
verts0PVert = [[3,3],[3.2,3],[3,12],[3.2,12]]
cells0PVert = [[1,2,3,4]]
pols0PVert = None
wall0P = MKPOL([verts0PVert, cells0PVert, pols0PVert])
wall0SolidVert = PROD([wall0P,Q(27)])
wall1SolidVert = T([1])([8.8])(wall0SolidVert)


orzs0POrz = [[3,3],[3,3.2],[12,3],[12,3.2]]
cells0POrz = [[1,2,3,4]]
pols0POrz = None
wall0POrz = MKPOL([orzs0POrz, cells0POrz, pols0POrz])
wall0SolidOrz = PROD([wall0POrz,Q(27)])
wall1SolidOrz = T([2])([8.8])(wall0SolidOrz)

verts1piano = [[3,3],[12,3],[3,12],[12,12]]
cells1piano = [[1,2,3,4]]
pols1piano = None
wall01piano= MKPOL([verts1piano, cells1piano, pols1piano])
wall0Solid1piano = PROD([wall01piano,Q(0.2)])
wall1Solid1piano = T([3])([27])(wall0Solid1piano)

verts111piano = [[3,3],[12,3],[3,12],[12,12]]
cells111piano = [[1,2,3,4]]
pols111piano = None
wall0111piano= MKPOL([verts111piano, cells111piano, pols111piano])
wall0Solid111piano = PROD([wall0111piano,Q(0.2)])



#finestre primo blocco

verts0Windows = [[3.3,3],[3.7,3],[3.3,3.2],[3.7,3.2]]
cells0Windows = [[1,2,3,4]]
pols0Windows = None
windows = MKPOL([verts0Windows, cells0Windows, pols0Windows])
windowsProd = PROD([windows,Q(0.6)])
windowsTrasl = T([3])([0.3])(windowsProd)
windowsColonne = STRUCT([windowsTrasl, T(1)(1)]*9)
windowsRighe = STRUCT([windowsColonne, T(3)(1)]*25)
windowsTrasl1 = T([2])([8.8])(windowsTrasl)
windowsColonne1 = STRUCT([windowsTrasl1, T(1)(1)]*9)
windowsRighe1 = STRUCT([windowsColonne1, T(3)(1)]*25)
###########
verts0Windows1 = [[3,3.3],[3,3.7],[3.2,3.3],[3.2,3.7]]
cells0Windows1 = [[1,2,3,4]]
pols0Windows1 = None
windows1 = MKPOL([verts0Windows1, cells0Windows1, pols0Windows1])
windowsProd1 = PROD([windows1,Q(0.6)])
windowsTrasl2 = T([3])([0.3])(windowsProd1)
windowsColonne2 = STRUCT([windowsTrasl2, T(2)(1)]*9)
windowsRighe2 = STRUCT([windowsColonne2, T(3)(1)]*25)
windowsTrasl3 = T([1])([8.8])(windowsTrasl2)
windowsColonne3 = STRUCT([windowsTrasl3, T(2)(1)]*9)
windowsRighe3 = STRUCT([windowsColonne3, T(3)(1)]*25)

#secondo blocco 
verts0PVert1 = [[3,3],[3.2,3],[3,9],[3.2,9]]
cells0PVert1 = [[1,2,3,4]]
pols0PVert1 = None
wall0P1 = MKPOL([verts0PVert1, cells0PVert1, pols0PVert1])
wall0SolidVert1 = PROD([wall0P1,Q(27)])
wall1SolidVert1OK = T([3])([27])(wall0SolidVert1)
wall1SolidVert1 = T([1,2])([8.8,3])(wall1SolidVert1OK)

orzs0POrz1 = [[3,3],[3,3.2],[9,3],[9,3.2]]
cells0POrz1 = [[1,2,3,4]]
pols0POrz1 = None
wall0POrz1 = MKPOL([orzs0POrz1, cells0POrz1, pols0POrz1])
wall0SolidOrz1 = PROD([wall0POrz1,Q(27)])
wall1SolidOrz1OK = T([3])([27])(wall0SolidOrz1)
wall1SolidOrz1 = T([1,2])([3,8.8])(wall1SolidOrz1OK)

verts0PVert12 = [[6,9],[6.2,9],[6,12],[6.2,12]]
cells0PVert12 = [[1,2,3,4]]
pols0PVert12 = None
wall0P12 = MKPOL([verts0PVert12, cells0PVert12, pols0PVert12])
wall0SolidVert2 = PROD([wall0P12,Q(27)])
wall1SolidVert2OK = T([3])([27])(wall0SolidVert2)
wall1SolidVert2 = T([1,2])([2.8,-6])(wall1SolidVert2OK)

orzs0POrz12 = [[3,9],[3,8.8],[6,9],[6,8.8]]
cells0POrz12 = [[1,2,3,4]]
pols0POrz12 = None
wall0POrz12 = MKPOL([orzs0POrz12, cells0POrz12, pols0POrz12])
wall0SolidOrz12 = PROD([wall0POrz12,Q(27)])
wall1SolidOrz2OK = T([3])([27])(wall0SolidOrz12)
wall1SolidOrz2 = T([1,2])([6,-2.8])(wall1SolidOrz2OK)

verts2piano = [[3,3],[9,3],[3,9],[9,9]]
cells2piano = [[1,2,3,4]]
pols2piano = None
wall02piano= MKPOL([verts2piano, cells2piano, pols2piano])
wall0Solid2piano = PROD([wall02piano,Q(0.2)])
wall1Solid2piano = T([3])([54])(wall0Solid2piano)

verts22piano = [[6,6],[12,6],[12,12],[6,12]]
cells22piano = [[1,2,3,4]]
pols22piano = None
wall022piano= MKPOL([verts22piano, cells22piano, pols22piano])
wall0Solid22piano = PROD([wall022piano,Q(0.2)])
wall1Solid22piano = T([3])([54])(wall0Solid22piano)

#finestre secondo blocco

verts0Windows4 = [[3.3,3],[3.7,3],[3.3,3.2],[3.7,3.2]]
cells0Windows4 = [[1,2,3,4]]
pols0Windows4 = None
windows4 = MKPOL([verts0Windows4, cells0Windows4, pols0Windows4])
windowsProd4 = PROD([windows4,Q(0.6)])
windowsTrasl4 = T([3])([27.3])(windowsProd4)
windowsColonne4 = STRUCT([windowsTrasl4, T(1)(1)]*6)
windowsRighe4 = STRUCT([windowsColonne4, T(3)(1)]*25)
windowsTrasl5 = T([1,2])([3,8.8])(windowsTrasl4)
windowsColonne5 = STRUCT([windowsTrasl5, T(1)(1)]*6)
windowsRighe5 = STRUCT([windowsColonne5, T(3)(1)]*25)
windowsTrasl51 = T([2])([5.8])(windowsTrasl4)
windowsColonne51 = STRUCT([windowsTrasl51, T(1)(1)]*3)
windowsRighe51 = STRUCT([windowsColonne51, T(3)(1)]*25)
windowsTrasl52 = T([1,2])([6,3])(windowsTrasl4)
windowsColonne52 = STRUCT([windowsTrasl52, T(1)(1)]*3)
windowsRighe52 = STRUCT([windowsColonne52, T(3)(1)]*25)
windowsA = STRUCT([windowsColonne4,windowsColonne5,windowsRighe5,windowsRighe4,windowsColonne51,windowsRighe51,windowsColonne52,windowsRighe52])
###########
verts0Windows6 = [[3,3.3],[3,3.7],[3.2,3.3],[3.2,3.7]]
cells0Windows6 = [[1,2,3,4]]
pols0Windows6 = None
windows6 = MKPOL([verts0Windows6, cells0Windows6, pols0Windows6])
windowsProd6 = PROD([windows6,Q(0.6)])
windowsTrasl6 = T([3])([27.3])(windowsProd6)
windowsColonne6 = STRUCT([windowsTrasl6, T(2)(1)]*6)
windowsRighe6 = STRUCT([windowsColonne6, T(3)(1)]*25)
windowsTrasl7 = T([1,2])([8.8,3])(windowsTrasl6)
windowsColonne7 = STRUCT([windowsTrasl7, T(2)(1)]*6)
windowsRighe7 = STRUCT([windowsColonne7, T(3)(1)]*25)
windowsTrasl71 = T([1])([5.8])(windowsTrasl6)
windowsColonne71 = STRUCT([windowsTrasl71, T(2)(1)]*3)
windowsRighe71 = STRUCT([windowsColonne71, T(3)(1)]*25)
windowsTrasl72 = T([1,2])([3,6])(windowsTrasl6)
windowsColonne72 = STRUCT([windowsTrasl72, T(2)(1)]*3)
windowsRighe72 = STRUCT([windowsColonne72, T(3)(1)]*25)
windowsB = STRUCT([windowsColonne6,windowsRighe6,windowsRighe7,windowsRighe7,windowsColonne71,windowsRighe71,windowsRighe72,windowsColonne72])

#terzo blocco 
verts0PVert2 = [[3,6],[3.2,6],[3,9],[3.2,9]]
cells0PVert2 = [[1,2,3,4]]
pols0PVert2 = None
wall0P2 = MKPOL([verts0PVert2, cells0PVert2, pols0PVert2])
wall0SolidVert22 = PROD([wall0P2,Q(15)])
wall1SolidVert3OK = T([3])([54])(wall0SolidVert22)
wall1SolidVert22 = T([1])([8.8])(wall1SolidVert3OK)
wall1SolidVert3 = T([1,2])([3,3])(wall1SolidVert3OK)
wall1SolidVert4 = T([1,2])([3,-3])(wall1SolidVert3OK)
wall1SolidVert5 = T([1,2])([5.8,3])(wall1SolidVert3OK)
wall1SolidVert6 = T([1,2])([5.8,-3])(wall1SolidVert3OK)

verts0PVert21 = [[6,3],[6,3.2],[9,3],[9,3.2]]
cells0PVert21 = [[1,2,3,4]]
pols0PVert21 = None
wall0P21 = MKPOL([verts0PVert21, cells0PVert21, pols0PVert21])
wall0SolidVert222 = PROD([wall0P21,Q(15)])
wall1SolidVert4OK = T([3])([54])(wall0SolidVert222)
wall1SolidVert222 = T([2])([8.8])(wall1SolidVert4OK)
wall1SolidVert32 = T([1,2])([-3,3])(wall1SolidVert4OK)
wall1SolidVert42 = T([1,2])([3,3])(wall1SolidVert4OK)
wall1SolidVert52 = T([2,1])([5.8,3])(wall1SolidVert4OK)
wall1SolidVert62 = T([2,1])([5.8,-3])(wall1SolidVert4OK)

verts33piano = [[3,6],[12,6],[3,9],[12,9]]
cells33piano = [[1,2,3,4]]
pols33piano = None
wall033piano= MKPOL([verts33piano, cells33piano, pols33piano])
wall0Solid33piano = PROD([wall033piano,Q(0.2)])
wall1Solid33piano = T([3])([69])(wall0Solid33piano)
verts333piano = [[6,3],[9,3],[6,12],[9,12]]
cells333piano = [[1,2,3,4]]
pols333piano = None
wall0333piano= MKPOL([verts333piano, cells333piano, pols333piano])
wall0Solid333piano = PROD([wall0333piano,Q(0.2)])
wall1Solid333piano = T([3])([69])(wall0Solid333piano)
wallG = STRUCT([wall1Solid33piano,wall1Solid333piano])

allwallA = STRUCT([wall1SolidVert3OK,wall1SolidVert22,wall1SolidVert3,wall1SolidVert4,wall1SolidVert5,wall1SolidVert6,wall1SolidVert4OK,wall1SolidVert222,wall1SolidVert32,wall1SolidVert42,wall1SolidVert52,wall1SolidVert62,wallG])

#finestre terzo blocco

verts0Windows9 = [[6.3,3],[6.7,3],[6.3,3.2],[6.7,3.2]]
cells0Windows9 = [[1,2,3,4]]
pols0Windows9 = None
windows9 = MKPOL([verts0Windows9, cells0Windows9, pols0Windows9])
windowsProd9 = PROD([windows9,Q(0.6)])
windowsTrasl9 = T([3])([54.3])(windowsProd9)
windowsColonne9 = STRUCT([windowsTrasl9, T(1)(1)]*3)
windowsRighe9 = STRUCT([windowsColonne9, T(3)(1)]*13)
windowsTrasl8 = T([1,2])([-3,3])(windowsTrasl9)
windowsColonne8 = STRUCT([windowsTrasl8, T(1)(1)]*3)
windowsRighe8 = STRUCT([windowsColonne8, T(3)(1)]*13)
windowsTrasl81 = T([2])([8.8])(windowsTrasl9)
windowsColonne81 = STRUCT([windowsTrasl81, T(1)(1)]*3)
windowsRighe81 = STRUCT([windowsColonne81, T(3)(1)]*13)
windowsTrasl82 = T([1,2])([3,3])(windowsTrasl9)
windowsColonne82 = STRUCT([windowsTrasl82, T(1)(1)]*3)
windowsRighe82 = STRUCT([windowsColonne82, T(3)(1)]*13)
windowsTrasl83 = T([1,2])([-3,5.8])(windowsTrasl9)
windowsColonne83 = STRUCT([windowsTrasl83, T(1)(1)]*3)
windowsRighe83 = STRUCT([windowsColonne83, T(3)(1)]*13)
windowsTrasl84 = T([1,2])([3,5.8])(windowsTrasl9)
windowsColonne84 = STRUCT([windowsTrasl84, T(1)(1)]*3)
windowsRighe84 = STRUCT([windowsColonne84, T(3)(1)]*13)
windowsJ = STRUCT([windowsColonne9,windowsColonne8,windowsRighe8,windowsRighe9,windowsColonne81,windowsRighe81,windowsColonne82,windowsRighe82,windowsColonne83,windowsRighe83,windowsColonne84,windowsRighe84])
###########
verts0Windows15 = [[3,6.3],[3,6.7],[3.2,6.3],[3.2,6.7]]
cells0Windows15 = [[1,2,3,4]]
pols0Windows15 = None
windows15 = MKPOL([verts0Windows15, cells0Windows15, pols0Windows15])
windowsProd15 = PROD([windows15,Q(0.6)])
windowsTrasl15 = T([3])([54.3])(windowsProd15)
windowsColonne15 = STRUCT([windowsTrasl15, T(2)(1)]*3)
windowsRighe15 = STRUCT([windowsColonne15, T(3)(1)]*13)
windowsTrasl16 = T([2,1])([-3,3])(windowsTrasl15)
windowsColonne16 = STRUCT([windowsTrasl16, T(2)(1)]*3)
windowsRighe16 = STRUCT([windowsColonne16, T(3)(1)]*13)
windowsTrasl161 = T([1])([8.8])(windowsTrasl15)
windowsColonne161 = STRUCT([windowsTrasl161, T(2)(1)]*3)
windowsRighe161 = STRUCT([windowsColonne161, T(3)(1)]*13)
windowsTrasl162 = T([2,1])([3,3])(windowsTrasl15)
windowsColonne162 = STRUCT([windowsTrasl162, T(2)(1)]*3)
windowsRighe162 = STRUCT([windowsColonne162, T(3)(1)]*13)
windowsTrasl163 = T([2,1])([-3,5.8])(windowsTrasl15)
windowsColonne163 = STRUCT([windowsTrasl163, T(2)(1)]*3)
windowsRighe163 = STRUCT([windowsColonne163, T(3)(1)]*13)
windowsTrasl164 = T([2,1])([3,5.8])(windowsTrasl15)
windowsColonne164 = STRUCT([windowsTrasl164, T(2)(1)]*3)
windowsRighe164 = STRUCT([windowsColonne164, T(3)(1)]*13)
windowsH = STRUCT([windowsColonne15,windowsColonne16,windowsRighe16,windowsRighe15,windowsColonne161,windowsRighe161,windowsColonne162,windowsRighe162,windowsColonne163,windowsRighe163,windowsColonne164,windowsRighe164])

#quarto blocco 
verts0PVert99 = [[6,6],[6.2,6],[6,9],[6.2,9]]
cells0PVert99 = [[1,2,3,4]]
pols0PVert99 = None
wall0P99 = MKPOL([verts0PVert99, cells0PVert99, pols0PVert99])
wall0SolidVert99 = PROD([wall0P99,Q(15)])
wall1SolidVert99K = T([3])([69])(wall0SolidVert99)
wall1SolidVert61 = T([1])([5.8])(wall1SolidVert99K)

verts0PVert98 = [[6,6],[6,6.2],[12,6],[12,6.2]]
cells0PVert98 = [[1,2,3,4]]
pols0PVert98 = None
wall0P98 = MKPOL([verts0PVert98, cells0PVert98, pols0PVert98])
wall0SolidVert2222 = PROD([wall0P98,Q(15)])
wall1SolidVert98K = T([3])([69])(wall0SolidVert2222)
wall1SolidVert62 = T([2])([2.8])(wall1SolidVert98K)

allwallE = STRUCT([wall1SolidVert98K,wall1SolidVert99K,wall1SolidVert61,wall1SolidVert62])

verts4piano = [[6,6],[12,6],[12,9],[6,9]]
cells4piano = [[1,2,3,4]]
pols4piano = None
wall04piano= MKPOL([verts4piano, cells4piano, pols4piano])
wall0Solid4piano = PROD([wall04piano,Q(0.2)])
wall1Solid4piano = T([3])([84])(wall0Solid4piano)


#finestre quarto blocco

verts0Windows55 = [[6.3,6],[6.7,6],[6.3,6.2],[6.7,6.2]]
cells0Windows55 = [[1,2,3,4]]
pols0Windows55 = None
windows55 = MKPOL([verts0Windows55, cells0Windows55, pols0Windows55])
windowsProd55 = PROD([windows55,Q(0.6)])
windowsTrasl44 = T([3])([69.3])(windowsProd55)
windowsColonne55 = STRUCT([windowsTrasl44, T(1)(1)]*6)
windowsRighe55 = STRUCT([windowsColonne55, T(3)(1)]*13)
windowsTrasl98 = T([2])([2.8])(windowsTrasl44)
windowsColonne98 = STRUCT([windowsTrasl98, T(1)(1)]*6)
windowsRighe98 = STRUCT([windowsColonne98, T(3)(1)]*13)

windowsP = STRUCT([windowsColonne55,windowsRighe55,windowsColonne98,windowsRighe98])

verts0Windows77 = [[6,6.3],[6,6.7],[6.2,6.3],[6.2,6.7]]
cells0Windows77 = [[1,2,3,4]]
pols0Windows77 = None
windows77 = MKPOL([verts0Windows77, cells0Windows77, pols0Windows77])
windowsProd77 = PROD([windows77,Q(0.6)])
windowsTrasl77 = T([3])([69.3])(windowsProd77)
windowsColonne77 = STRUCT([windowsTrasl77, T(2)(1)]*3)
windowsRighe77 = STRUCT([windowsColonne77, T(3)(1)]*13)
windowsTrasl78 = T([1])([5.8])(windowsTrasl77)
windowsColonne78 = STRUCT([windowsTrasl78, T(2)(1)]*3)
windowsRighe78 = STRUCT([windowsColonne78, T(3)(1)]*13)

windowsPP = STRUCT([windowsColonne77,windowsRighe77,windowsColonne78,windowsRighe78])


opera = STRUCT([wall0SolidOrz,wall1SolidOrz,wall0SolidVert,wall1SolidVert,wall1SolidVert1OK,wall1SolidVert1,wall1SolidOrz1OK,wall1SolidOrz1,wall1SolidVert2OK,wall1SolidVert2,wall1SolidOrz2OK,wall1SolidOrz2,wall1Solid1piano,wall1Solid2piano,wall1Solid22piano,allwallA,wall0Solid111piano,allwallE,wall1Solid4piano])
opera1 = COLOR([0.38823335,0.592156,0.7098039])(DIFFERENCE([opera,windowsColonne,windowsRighe,windowsColonne1,windowsRighe1,windowsColonne3,windowsColonne2,windowsRighe3,windowsRighe2,windowsA,windowsB,windowsJ,windowsH,windowsP,windowsPP]))


########################################

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


semiwall0_2 = COLOR(RED)(STRUCT([wall0SolidOrz,wall1SolidOrz,wall2SolidOrz,wall3SolidOrz,wall4SolidOrz,wall5SolidOrz,wall6SolidOrz,wall7SolidOrz,wall8SolidOrz]))
semiwall1_2 = COLOR(RED)(T([2])([3])(semiwall0_2))
semiwall0_1 = COLOR(RED)(STRUCT([wall0SolidVert,wall1SolidVert,wall2SolidVert,wall3SolidVert,wall4SolidVert,wall5SolidVert,wall6SolidVert,wall7SolidVert,wall8SolidVert]))
semiwall1_1 = COLOR(RED)(T([1])([3])(semiwall0_1))

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

floor10posOK = T([3])([27.1])(floor10Solid)

floor11Solid = T([3])([3])(floor10posOK)
floor12Solid = T([3])([6])(floor10posOK)
floor13Solid = T([3])([9])(floor10posOK)
floor14Solid = T([3])([12])(floor10posOK)
floor15Solid = T([3])([15])(floor10posOK)
floor16Solid = T([3])([18])(floor10posOK)
floor17Solid = T([3])([21])(floor10posOK)
floor18Solid = T([3])([24])(floor10posOK)


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

semiwall0_3 = COLOR(RED)(STRUCT([wall0Ptrasl,wall1Ptrasl,wall2Ptrasl,wall3Ptrasl,wall4Ptrasl,wall5Ptrasl,wall6Ptrasl,wall7Ptrasl,wall8Ptrasl]))
semiwall1_3 = COLOR(RED)(T([1,2])([3,3])(semiwall0_3))
semiwall0_4 = COLOR(RED)(STRUCT([wall0PtraslOrz,wall1PtraslOrz,wall2PtraslOrz,wall3PtraslOrz,wall4PtraslOrz,wall5PtraslOrz,wall6PtraslOrz,wall7PtraslOrz,wall8PtraslOrz]))
semiwall1_4 = COLOR(RED)(T([1,2])([3,3])(semiwall0_4))

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


semiwall0_5 = COLOR(RED)(STRUCT([wall0Ptrasl2,wall1Ptrasl2,wall2Ptrasl2,wall3Ptrasl2,wall4Ptrasl2]))
semiwall1_5 = COLOR(RED)(T([1])([3])(semiwall0_5))
semiwall0_6 = COLOR(RED)(STRUCT([wall0PtraslOrz1,wall1PtraslOrz1,wall2PtraslOrz1,wall3PtraslOrz1,wall4PtraslOrz1]))
semiwall1_6 = COLOR(RED)(T([2])([3])(semiwall0_6))


#QUARTO  6 piani
verts3 = [[6,6],[12,6],[12,9],[6,9]]
cells3 = [[1,2,3,4]]
pols3 = None
floor27 = MKPOL([verts3, cells3, pols3])
floor27Solid = PROD([floor27,Q(0.2)])

floor27posOK = T([3])([69.3])(floor27Solid)

floor28Solid = T([3])([3])(floor27posOK)
floor29Solid = T([3])([6])(floor27posOK)
floor30Solid = T([3])([9])(floor27posOK)
floor31Solid = T([3])([12])(floor27posOK)

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
wall4Ptrasl3 = T([3])([11])(wall0Ptrasl3)



semiwall0_7 = COLOR(RED)(STRUCT([wall0Ptrasl3,wall1Ptrasl3,wall2Ptrasl3,wall3Ptrasl3,wall4Ptrasl3]))


allfloor = STRUCT([floor1Solid,floor2Solid,floor3Solid,floor4Solid,floor5Solid,floor6Solid,floor7Solid,floor8Solid,floor10posOK,floor11Solid,floor12Solid,floor13Solid,floor14Solid,floor15Solid,floor16Solid,floor17Solid,floor18Solid,floor20posOK,floor21Solid,floor22Solid,floor23Solid,floor24Solid,floor27posOK,floor28Solid,floor29Solid,floor30Solid,floor31Solid])
piano = COLOR(RED)(STRUCT([semiwall1_1,semiwall0_1,semiwall0_2,semiwall1_2,semiwall1_3,semiwall0_3,semiwall0_4,semiwall1_4,semiwall0_5,semiwall1_5,semiwall0_6,semiwall1_6,semiwall0_7]))
A= COLOR([0.38823335,0.592156,0.7098039])(allfloor)

vertsAREA = [[-150,-130],[-150,130],[150,-130],[150,130]]
cellsAREA = [[1,2,3,4]]
polsAREA = None
wallAREA = MKPOL([vertsAREA, cellsAREA, polsAREA])
AREA = COLOR(GRAY)(wallAREA)

###FIUME
vertsFIUME = [[-150,-20],[150,-20],[-150,-30],[150,-30]]
cellsFIUME = [[1,2,3,4]]
polsFIUME = None
wallFIUME = MKPOL([vertsFIUME, cellsFIUME, polsFIUME])
wallSOLIDFIUME = PROD([wallFIUME,Q(0.1)])
fiume = COLOR(CYAN)(wallSOLIDFIUME)

##PONTI
vertsPONTE = [[-80,-15],[-75,-15],[-80,-130],[-75,-130]]
cellsPONTE = [[1,2,3,4]]
polsPONTE = None
wallPONTE = MKPOL([vertsPONTE, cellsPONTE, polsPONTE])
wallSOLIDPONTE = PROD([wallPONTE,Q(0.2)])
wallSOLIDPONTE1 = COLOR([0.250980,0.250980,0.250980])(wallSOLIDPONTE)
vertsSTRADA = [[-77.4,-16],[-77.6,-16],[-77.4,-17],[-77.6,-17]]
cellsSTRADA = [[1,2,3,4]]
polsSTRADA = None
wallSTRADA = MKPOL([vertsSTRADA, cellsSTRADA, polsSTRADA])
wallSOLIDSTRADA = PROD([wallSTRADA,Q(0.3)])
wallSOLIDSTRADAF = STRUCT([wallSOLIDSTRADA, T([2])([-2])]*57)
wallSOLIDSTRADAFINALY = STRUCT([wallSOLIDPONTE1,wallSOLIDSTRADAF])
wallSOLIDSTRADAF1 = T([1])([85])(wallSOLIDSTRADAFINALY)
wallSOLIDSTRADAF2 = T([1])([167])(wallSOLIDSTRADAFINALY)
PONTE = STRUCT([wallSOLIDSTRADAFINALY, wallSOLIDSTRADAF1,wallSOLIDSTRADAF2])

###PALAZZI

palazzo1 = CYLINDER([4,20])(6)
palazzo1TRA = COLOR([0.5019,0.5019,0.5019])(T([1,2])([50,15])(palazzo1))
palazzo12 = CYLINDER([4,35])(6)
palazzo12TRA = COLOR([0.5019,0.5019,0.5019])(T([1,2])([-40,35])(palazzo12))
palazzo13 = CYLINDER([4,50])(10)
palazzo13TRA = COLOR([0.5019,0.5019,0.5019])(T([1,2])([60,15])(palazzo13))
palazzo14 = CYLINDER([4,35])(10)
palazzo14TRA = COLOR([0.5019,0.5019,0.5019])(T([1,2])([-60,15])(palazzo14))
palazzo15 = COLOR([0.5019,0.5019,0.5019])(T([1,2])([-15,30])(CUBOID([7,5,33])))
STRUTTIRAPALAZZI = STRUCT([palazzo1TRA,palazzo12TRA,palazzo13TRA,palazzo14TRA,palazzo15])
STRUTTIRAPALAZZI1 = T([1,2])([20,30])(STRUTTIRAPALAZZI)
STRUTTIRAPALAZZI2 = T([1,2])([-20,60])(STRUTTIRAPALAZZI)
STRUTTIRAPALAZZI3 = STRUCT([STRUTTIRAPALAZZI,STRUTTIRAPALAZZI1,STRUTTIRAPALAZZI2])
STRUTTIRAPALAZZI4 = T([1,2])([5,-130])(STRUTTIRAPALAZZI3)

##STRADE
vertsSTRADE = [[-150,-15],[-150,-8],[150,-15],[150,-8]]
cellsSTRADE = [[1,2,3,4]]
polsSTRADE = None
walLSTRADE = MKPOL([vertsSTRADE, cellsSTRADE, polsSTRADE])
wallSOLIDSTRADE = PROD([walLSTRADE,Q(0.2)])
wallSOLIDSTRADE1 = COLOR([0.250980,0.250980,0.250980])(wallSOLIDSTRADE)
vertsSTRADA1 = [[-149,-11.4],[-149,-11.6],[-150,-11.4],[-150,-11.6]]
cellsSTRADA1 = [[1,2,3,4]]
polsSTRADA1 = None
wallSTRADA1 = MKPOL([vertsSTRADA1, cellsSTRADA1, polsSTRADA1])
wallSOLIDSTRADA1 = PROD([wallSTRADA1,Q(0.3)])
wallSOLIDSTRADAF11 = STRUCT([wallSOLIDSTRADA1, T([1])([2])]*150)
wallSOLIDSTRADAFINALY1 = STRUCT([wallSOLIDSTRADE1,wallSOLIDSTRADAF11])
wallSOLIDSTRADAFINALY22 = T(2)(37)(wallSOLIDSTRADAFINALY1)
wallSOLIDSTRADAFINALY23 = T(2)(95)(wallSOLIDSTRADAFINALY1)
wallSOLIDSTRADAFINALY24 = T(2)(-34)(wallSOLIDSTRADAFINALY1)
wallSOLIDSTRADAFINALY25 = T(2)(-95)(wallSOLIDSTRADAFINALY1)

vertsSTRADEW = [[130,-8],[137,-8],[130,130],[137,130]]
cellsSTRADEW = [[1,2,3,4]]
polsSTRADEW = None
walLSTRADEW = MKPOL([vertsSTRADEW, cellsSTRADEW, polsSTRADEW])
wallSOLIDSTRADEW = PROD([walLSTRADEW,Q(0.2)])
wallSOLIDSTRADE1W = COLOR([0.250980,0.250980,0.250980])(wallSOLIDSTRADEW)
vertsSTRADA1W = [[133.4,-8],[133.6,-8],[133.4,-7],[133.6,-7]]
cellsSTRADA1W = [[1,2,3,4]]
polsSTRADA1W = None
wallSTRADA1W = MKPOL([vertsSTRADA1W, cellsSTRADA1W, polsSTRADA1W])
wallSOLIDSTRADA1W = PROD([wallSTRADA1W,Q(0.3)])
wallSOLIDSTRADAF11W = STRUCT([wallSOLIDSTRADA1W, T([2])([2])]*69)
wallSOLIDSTRADAFINALY1W = STRUCT([wallSOLIDSTRADE1W,wallSOLIDSTRADAF11W])
wallSOLIDSTRADAFINALY2W = T(1)(-40)(wallSOLIDSTRADAFINALY1W)
wallSOLIDSTRADAFINALY3W = T(1)(-112)(wallSOLIDSTRADAFINALY1W)
wallSOLIDSTRADAFINALY4W = T(1)(-205)(wallSOLIDSTRADAFINALY1W)



STRUTTURAFINALE = STRUCT([piano,opera1,A,fiume,PONTE,AREA,STRUTTIRAPALAZZI,STRUTTIRAPALAZZI1,STRUTTIRAPALAZZI2,STRUTTIRAPALAZZI4,wallSOLIDSTRADE1,wallSOLIDSTRADAFINALY1,wallSOLIDSTRADAFINALY22,wallSOLIDSTRADAFINALY23,wallSOLIDSTRADAFINALY24,wallSOLIDSTRADAFINALY25,wallSOLIDSTRADAFINALY1W,wallSOLIDSTRADAFINALY2W,wallSOLIDSTRADAFINALY3W,wallSOLIDSTRADAFINALY4W])
VIEW(STRUTTURAFINALE)