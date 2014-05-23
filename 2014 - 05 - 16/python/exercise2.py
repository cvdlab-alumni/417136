from pyplasm import *
from scipy import *
from lar2psm import *
from simplexn import *
from larcc import *
from largrid import *
from mapper import *
from boolean import *
from sysml import *
from architectural import *
from splines import *

DRAW = COMP([VIEW,STRUCT,MKPOLS])

#Camera 1:
diagramCamera1 = assemblyDiagramInit([3,3,2])([[0.1,3,0.3],[0.3,3,0.1],[0.3,2.7]])
hpcCamera1 = SKEL_1(STRUCT(MKPOLS(diagramCamera1)))
VCamera1,CVCamera1 = diagramCamera1
hpcCamera1 = cellNumbering (diagramCamera1,hpcCamera1)(range(len(CVCamera1)),CYAN,2)
#VIEW(hpcCamera1)

toMerge = 3

doorCamera1 = assemblyDiagramInit([1,3,2])([[0.1],[1,1,1],[2.2,0.5]])
masterCamera1 = diagram2cell(doorCamera1,diagramCamera1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera1)))
hpc = cellNumbering (masterCamera1,hpc)(range(len(masterCamera1[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCamera1 = masterCamera1[0], [cell for k,cell in enumerate(masterCamera1[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera1)))
hpc = cellNumbering (masterCamera1,hpc)(range(len(masterCamera1[1])),CYAN,2)
#VIEW(hpc)

toMerge = 13

windowCamera1 = assemblyDiagramInit([1,5,3])([[0.3],[0.5,0.9,0.2,0.9,0.5],[1,1.4,0.3]])
masterCamera1 = diagram2cell(windowCamera1,masterCamera1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera1)))
hpc = cellNumbering (masterCamera1,hpc)(range(len(masterCamera1[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24,30]
masterCamera1 = masterCamera1[0], [cell for k,cell in enumerate(masterCamera1[1]) if not (k in toRemove)]
#DRAW(masterCamera1)

# Camera da letto 2:
diagramCamera2 = assemblyDiagramInit([3,3,2])([[0.3,3,0.1],[0.1,4,0.3],[0.3,2.7]])
hpcCamera2 = SKEL_1(STRUCT(MKPOLS(diagramCamera2)))
VCamera2,CVCamera2 = diagramCamera2
hpcCamera2 = cellNumbering (diagramCamera2,hpcCamera2)(range(len(CVCamera2)),CYAN,2)
#VIEW(hpcCamera2)

toMerge = 15

doorCamera2 = assemblyDiagramInit([1,3,2])([[0.1],[0.2,1,2.8],[2.2,0.5]])
masterCamera2 = diagram2cell(doorCamera2,diagramCamera2,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera2)))
hpc = cellNumbering (masterCamera2,hpc)(range(len(masterCamera2[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterCamera2 = masterCamera2[0], [cell for k,cell in enumerate(masterCamera2[1]) if not (k in toRemove)]
#DRAW(masterCamera2)

toMerge = 3

windowCamera2 = assemblyDiagramInit([1,5,3])([[0.3],[0.5,0.9,0.2,0.9,0.5],[1,1.4,0.3]])
masterCamera2 = diagram2cell(windowCamera2,masterCamera2,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera2)))
hpc = cellNumbering (masterCamera2,hpc)(range(len(masterCamera2[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24,30]
masterCamera2 = masterCamera2[0], [cell for k,cell in enumerate(masterCamera2[1]) if not (k in toRemove)]
#DRAW(masterCamera2)

#Cucina:
diagramCucina = assemblyDiagramInit([3,3,2])([[0.1,3,0.3],[0.1,3,0.3],[0.3,2.7]])
hpcCucina = SKEL_1(STRUCT(MKPOLS(diagramCucina)))
VCucina,CVCucina = diagramCucina
hpcDiagramCucina = cellNumbering (diagramCucina,hpcCucina)(range(len(CVCucina)),CYAN,2)
#VIEW(hpcDiagramCucina)

toMerge = 3

doorCucina = assemblyDiagramInit([1,3,2])([[0.1],[0.2,1,1.8],[2.2,0.5]])
masterCucina = diagram2cell(doorCucina,diagramCucina,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpc = cellNumbering (masterCucina,hpc)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemove)]
#DRAW(masterCucina)

toMerge = 9

windowCucina = assemblyDiagramInit([3,1,3])([[0.9,1.2,0.9],[0.3],[2,3.5,2]])
masterCucina = diagram2cell(windowCucina,masterCucina,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpc = cellNumbering (masterCucina,hpc)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemove)]
#DRAW(masterCucina)

#Salotto:
diagramSalotto = assemblyDiagramInit([3,3,2])([[0.3,3,0.1],[0.3,4,0.1],[0.3,2.7]])
hpcSalotto = SKEL_1(STRUCT(MKPOLS(diagramSalotto)))
VSalotto,CVSalotto = diagramSalotto
hpcDiagramSalotto = cellNumbering (diagramSalotto,hpcSalotto)(range(len(CVSalotto)),CYAN,2)
#VIEW(hpcDiagramSalotto)

toMerge = 15

doorSalotto = assemblyDiagramInit([1,3,2])([[0.1],[1.5,1,1.5],[2.2,0.5]])
masterSalotto = diagram2cell(doorSalotto,diagramSalotto,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterSalotto)))
hpc = cellNumbering (masterSalotto,hpc)(range(len(masterSalotto[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterSalotto = masterSalotto[0], [cell for k,cell in enumerate(masterSalotto[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(masterSalotto)))
hpc = cellNumbering (masterSalotto,hpc)(range(len(masterSalotto[1])),CYAN,2)
#VIEW(hpc)
#DRAW(masterSalotto)

toMerge = 3

windowSalotto = assemblyDiagramInit([1,5,3])([[0.3],[0.5,0.9,0.2,0.9,0.5],[1,1.4,0.3]])
masterSalotto = diagram2cell(windowSalotto,masterSalotto,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterSalotto)))
hpc = cellNumbering (masterSalotto,hpc)(range(len(masterSalotto[1])),CYAN,.2)
#VIEW(hpc)

toRemove = [24,30]
masterSalotto = masterSalotto[0], [cell for k,cell in enumerate(masterSalotto[1]) if not (k in toRemove)]
#DRAW(masterSalotto)

#Bagno
diagramBagno = assemblyDiagramInit([3,3,2])([[0.1,3,0.3],[0.1,2,0.1],[0.3,2.7]])
hpcBagno = SKEL_1(STRUCT(MKPOLS(diagramBagno)))
VBagno,CVBagno = diagramBagno
hpcDiagramBagno = cellNumbering (diagramBagno,hpcBagno)(range(len(CVBagno)),CYAN,2)
#VIEW(hpcDiagramBagno)

toMerge = 3

doorBagno = assemblyDiagramInit([1,3,2])([[0.1],[0.5,1,0.5],[2.2,0.5]])
masterBagno = diagram2cell(doorBagno,diagramBagno,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterBagno = masterBagno[0], [cell for k,cell in enumerate(masterBagno[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)
#DRAW(masterBagno)

toMerge = 13

windowBagno = assemblyDiagramInit([1,3,3])([[0.3],[0.6,0.8,0.6],[1,1.4,0.3]])
masterBagno = diagram2cell(windowBagno,masterBagno,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterBagno = masterBagno[0], [cell for k,cell in enumerate(masterBagno[1]) if not (k in toRemove)]
#DRAW(masterBagno)

#Corridoio:
diagramCorridoio = assemblyDiagramInit([3,3,2])([[0.1,3,0.1],[0.3,6.8,0.1],[0.3,2.7]])
hpcCorridoio = SKEL_1(STRUCT(MKPOLS(diagramCorridoio)))
VCorridoio,CVCorridoio = diagramCorridoio
hpcDiagramCorridoio = cellNumbering (diagramCorridoio,hpcCorridoio)(range(len(CVCorridoio)),CYAN,2)
#VIEW(hpcDiagramCorridoio)

toMerge = 7

doorCorridoio = assemblyDiagramInit([3,1,2])([[0.4,1.2,0.4],[0.3],[2.2,0.5]])
masterCorridoio = diagram2cell(doorCorridoio,diagramCorridoio,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCorridoio)))
hpc = cellNumbering (masterCorridoio,hpc)(range(len(masterCorridoio[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCorridoio = masterCorridoio[0], [cell for k,cell in enumerate(masterCorridoio[1]) if not (k in toRemove)]
#DRAW(masterCorridoio)

# Ripostiglio:
diagramRipostiglio = assemblyDiagramInit([3,3,2])([[0.1,2,0.1],[0.1,1.3,0.3],[0.3,2.7]])
hpcRipostiglio = SKEL_1(STRUCT(MKPOLS(diagramRipostiglio)))
VRipostiglio,CVRipostiglio = diagramRipostiglio
hpcDiagramRipostiglio = cellNumbering (diagramRipostiglio,hpcRipostiglio)(range(len(CVRipostiglio)),CYAN,2)
#VIEW(hpcDiagramRipostiglio)

toMerge = 7

doorRipostiglio = assemblyDiagramInit([3,1,2])([[0.5,1,0.5],[0.1],[2.2,0.5]])
masterRipostiglio = diagram2cell(doorRipostiglio,diagramRipostiglio,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterRipostiglio)))
hpc = cellNumbering (masterRipostiglio,hpc)(range(len(masterRipostiglio[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterRipostiglio = masterRipostiglio[0], [cell for k,cell in enumerate(masterRipostiglio[1]) if not (k in toRemove)]
#DRAW(masterRipostiglio)


#creo il master principale
master = assemblyDiagramInit([3,1,1])([[3,2,3],[8],[3]])
V_master,CV_master = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV_master)),CYAN,2)
#VIEW(hpc)

#TAGLIO salotto-camera2:
cut1 = assemblyDiagramInit([1,2,1])([[3],[4,4],[3]])
toMerge = 0
masterCut1 = diagram2cell(cut1,master,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCut1)))
hpc = cellNumbering (masterCut1,hpc)(range(len(masterCut1[1])),CYAN,2)
#VIEW(hpc)

#inserisco camera2
toMerge = 3
masterCamera2F = diagram2cell(masterCamera2,masterCut1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera2F)))
hpc = cellNumbering (masterCamera2F,hpc)(range(len(masterCamera2F[1])),CYAN,2)
#VIEW(hpc)

#inserisco salotto
toMerge = 2
masterSalottoF = diagram2cell(masterSalotto,masterCamera2F,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterSalottoF)))
hpc = cellNumbering (masterSalottoF,hpc)(range(len(masterSalottoF[1])),CYAN,2)
#VIEW(hpc)

#TAGLIO stanzino-corridoio:
cut1 = assemblyDiagramInit([1,2,1])([[2],[6.8,1.2],[3]])
toMerge = 0
masterCut1 = diagram2cell(cut1,masterSalottoF,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCut1)))
hpc = cellNumbering (masterCut1,hpc)(range(len(masterCut1[1])),CYAN,2)
#VIEW(hpc)

#inserisco stanzino
toMerge = 68
masterStanzinoF = diagram2cell(masterRipostiglio,masterCut1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterStanzinoF)))
hpc = cellNumbering (masterStanzinoF,hpc)(range(len(masterStanzinoF[1])),CYAN,2)
#VIEW(hpc)

#inserisco corridoio
toMerge = 67
masterCorridoioF = diagram2cell(masterCorridoio,masterStanzinoF,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCorridoioF)))
hpc = cellNumbering (masterCorridoioF,hpc)(range(len(masterCorridoioF[1])),CYAN,2)
#VIEW(hpc)

#TAGLIO cucina-bagno-camera1:
cut1 = assemblyDiagramInit([1,3,1])([[3],[3,2,3],[3]])
toMerge = 0
masterCut1 = diagram2cell(cut1,masterCorridoioF,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCut1)))
hpc = cellNumbering (masterCut1,hpc)(range(len(masterCut1[1])),CYAN,2)
#VIEW(hpc)

#inserisco cucina
toMerge = 110
masterCucinaF = diagram2cell(masterCucina,masterCut1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucinaF)))
hpc = cellNumbering (masterCucinaF,hpc)(range(len(masterCucinaF[1])),CYAN,2)
#VIEW(hpc)

#inserisco bagno
toMerge = 109
masterBagnoF = diagram2cell(masterBagno,masterCucinaF,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagnoF)))
hpc = cellNumbering (masterBagnoF,hpc)(range(len(masterBagnoF[1])),CYAN,2)
#VIEW(hpc)

#inserisco camera 1
toMerge = 108
masterCamera1F = diagram2cell(masterCamera1,masterBagnoF,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera1F)))
hpc = cellNumbering (masterCamera1F,hpc)(range(len(masterCamera1F[1])),CYAN,.5)
#VIEW(hpc)


toRemove = [90,96,100,114,173,42]
master = masterCamera1F[0], [cell for k,cell in enumerate(masterCamera1F[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#DRAW(master)
#VIEW(hpc)

CREA_MODELLO = COMP([STRUCT,MKPOLS])
modelloPiano = CREA_MODELLO(master)

#porte

door = COLOR([0.8,0.4666666,0.13333333])(CUBOID([0.06,1,2.2]))

primoPezzoManiglia = T([1,2,3])([0.08,0.9,1])(CUBOID([0.03,0.1,0.03]))
secondoPezzoManiglia = T([1,2,3])([-0.03,0.9,1])(CUBOID([0.03,0.1,0.03]))
maniglia = STRUCT([primoPezzoManiglia,secondoPezzoManiglia])
maniglia = COLOR([0.8,0.4,0])(maniglia)

doorG = STRUCT([door,maniglia])
doorSalottoCop = T([1,2,3])([2.92,1.55,0.3])(doorG)
doorCamera2Cop = T([1,2,3])([2.92,4.20,0.3])(doorG)
doorCamera1Cop = T([1,2,3])([5,1.03,0.3])(doorG)
doorBagnoCop = T([1,2,3])([5,3.47,0.3])(doorG)
doorCucinaCop = T([1,2,3])([5,5.15,0.3])(doorG)
doorStanzinoCop = R([1,2])(-PI/2)(doorG)
doorStanzinoCop = T([1,2,3])([3.47,6.86,0.3])(doorStanzinoCop)

doorEntrata = COLOR([0.4823,0.1058,0.007843])(CUBOID([0.09,1.3,2.2]))

primoPezzoManiglia = T([1,2,3])([0.08,0.9,1])(CUBOID([0.03,0.1,0.03]))
secondoPezzoManiglia = T([1,2,3])([-0.03,0.9,1])(CUBOID([0.03,0.1,0.03]))
maniglia = STRUCT([primoPezzoManiglia,secondoPezzoManiglia])
maniglia = COLOR([0.8,0.4,0])(maniglia)

doorEntrata1 = STRUCT([doorEntrata,maniglia])
doorEntrataCop = R([1,2])(-PI/2)(doorEntrata1)
doorEntrataCop = T([1,2,3])([3.43,0.1,0.3])(doorEntrataCop)


windows = COLOR([0.5882,0.87058,0.819607])(CUBOID([0.1,7.5,1.9]))
windowsm = COLOR([0.5882,0.87058,0.819607])(CUBOID([0.1,1.3,1.9]))



windows1 = T([1,2,3])([0,0,1])(windows)
windows2 = T([1,2,3])([7.9,0,1])(windows)
windows3 = R([1,2])(-PI/2)(windowsm)

windows3 = T([1,2,3])([5.85,7.98,1])(windows3)



#VIEW(STRUCT([modelloPiano,doorSalottoCop,doorCamera2Cop,doorCamera1Cop,doorBagnoCop,doorCucinaCop,doorStanzinoCop,doorEntrataCop,windows1,windows2,windows3]))


#ES 2

prepPal = STRUCT([modelloPiano,doorSalottoCop,doorCamera2Cop,doorCamera1Cop,doorBagnoCop,doorCucinaCop,doorStanzinoCop,doorEntrataCop,windows1,windows2,windows3])
prepPal = T([1,2])([8,8])(R([1,2])(PI)(prepPal))
prepPal1 = T(1)(8)(T(2)(20)(R([1,2])(PI)(prepPal)))
modelBase = STRUCT([prepPal,prepPal1])
#VIEW(modelBase)


strutPalazzo = STRUCT([modelBase,T(3)(3)]*6)
#VIEW(strutPalazzo)



#FUNZIONE GENERA SCALA#
def spiralscala(thickness=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
    V,CV = larSolidHelicoid(thickness,R,r,pitch,nturns,steps)()
    W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
        for k,v in enumerate(V[:-4]) if k%4==0])
    for k,w in enumerate(W[:-12]):
        if k%6==0: W[k+1][2]=W[k+10][2]; W[k+3][2]=W[k+11][2]
    nsteps = len(W)/12
    CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*35])
            for k in range(nsteps)]
    return W,CW



scala = STRUCT(MKPOLS(spiralscala(0.2,1,0.5,0.1,2,15,18)))
scalaR = T([1,2])([6,10])(R([1,2])(PI)(scala))

#base
base = CUBOID([8,20,0.03])

trombaScale = T([1,2])([6,10])(CYLINDER([1.1,.03])(64))
baseplus = DIFFERENCE([base,trombaScale])

baseF = STRUCT([baseplus,T(3)(3)]*6)
baseFF = STRUCT([baseplus,T(3)(3)]*7)
copertura = T(3)(18)(base)

facciata = CUBOID([0.03,4,18])
facciata = T([1,2])([0,8])(facciata)
finestrone = CUBOID([0.03,1,2])
finestrone1 = CUBOID([0.03,1,2])

finestrone = T([1,2,3])([8,9.5,3.5])(finestrone)
finestrone = COLOR([0.5882,0.87058,0.819607])(STRUCT([finestrone,T([3])(3)]*5))
finestrone1 = T([1,2,3])([0,9.5,3.5])(finestrone1)
finestrone1 = COLOR([0.5882,0.87058,0.819607])(STRUCT([finestrone1,T([3])(3)]*5))

facciata1 = T([1,2])([8,0])(facciata)



doorBack = CUBOID([.01,0.8,1.3])
doorBack = COLOR([0.50196,0,0])(doorBack)
doorBack1 = T([1,2])([8.05,9])(doorBack)
doorBack2 = T([1,2])([8.05,10])(doorBack)

#balconi

balconi = CUBOID([1,3,0.1])
murettoLat = CUBOID([1,0.1,1])
murettoLat1 = T(2)(2.9)(murettoLat)
staccionata = CYLINDER([0.05,0.8])(64)
staccionata = T([1,2,3])([0.95,0.3,0.1])(staccionata)
staccionata = STRUCT([staccionata,T(2)(0.3)]*9)
murettoalto = CUBOID([0.10,3,0.1])
murettoalto = T([1,3])([0.90,0.9])(murettoalto)
balcone = STRUCT([balconi,murettoLat,murettoLat1,murettoalto,COLOR(BLACK)(staccionata)])
balcone1 = T([1,2,3])([8,0.6,3.5])(balcone)
balcone2 = T([1,2,3])([8,12.07,3.5])(balcone)
balcone3 = STRUCT([balcone1,balcone2])
structBalconi = STRUCT([balcone3,T(3)(3)]*5)
structBalconi1 = R([1,2])(PI)(structBalconi)
structBalconi1 = T(1)(8)(structBalconi1)
structBalconi1 = T(2)(20)(structBalconi1)





VIEW(STRUCT([base,baseF,strutPalazzo,scalaR,facciata]))


VIEW(STRUCT([base,baseFF,strutPalazzo,scalaR,facciata,facciata1,doorBack1,doorBack2,copertura,finestrone,finestrone1,structBalconi,structBalconi1]))