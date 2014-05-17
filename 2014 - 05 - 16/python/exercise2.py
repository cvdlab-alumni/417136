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
DRAW = COMP([VIEW,STRUCT,MKPOLS])




#MAIN MASTER:
master = assemblyDiagramInit([3,1,2])([[4,2.5,4.5],[12],[0.3,3]])
V_master,CV_master = master
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(CV_master)),CYAN,2)
#VIEW(hpc)

# MASTER TAGLIO 1:
master_primo_settore = assemblyDiagramInit([1,2,1])([[4],[6,6],[3]])
V_uno,CV_uno = master_primo_settore
hpc_primo_settore = SKEL_1(STRUCT(MKPOLS(master_primo_settore)))
hpc_primo_settore = cellNumbering (master_primo_settore,hpc_primo_settore)(range(len(CV_uno)),CYAN,2)
#VIEW(hpc_primo_settore)

#MASTER TAGLIO 2:
master_secondo_settore = assemblyDiagramInit([1,2,1])([[2.5],[9,3],[3]])
V_uno,CV_uno = master_secondo_settore
hpc_secondo_settore = SKEL_1(STRUCT(MKPOLS(master_secondo_settore)))
hpc_secondo_settore = cellNumbering (master_secondo_settore,hpc_secondo_settore)(range(len(CV_uno)),CYAN,2)
#VIEW(hpc_secondo_settore)



#MASTER TAGLIO 3:
master_terzo_settore = assemblyDiagramInit([1,3,1])([[4.5],[5.5,2.5,4],[3]])
V_uno,CV_uno = master_terzo_settore
hpc_terzo_settore = SKEL_1(STRUCT(MKPOLS(master_terzo_settore)))
hpc_terzo_settore = cellNumbering (master_terzo_settore,hpc_terzo_settore)(range(len(CV_uno)),CYAN,2)
#VIEW(hpc_terzo_settore)



toMerge_primo = 1
toMerge_secondo = 2
toMerge_terzo = 3

master = diagram2cell(master_primo_settore,master,toMerge_primo)
master = diagram2cell(master_secondo_settore,master,toMerge_secondo)
master = diagram2cell(master_terzo_settore,master,toMerge_terzo)

hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


#Camera da letto 1:
diagramCamera1 = assemblyDiagramInit([3,3,2])([[0.3,4,0.1],[0.3,6,0.1],[0.3,3]])
hpcCamera1 = SKEL_1(STRUCT(MKPOLS(diagramCamera1)))
VCamera1,CVCamera1 = diagramCamera1
hpcCamera1 = cellNumbering (diagramCamera1,hpcCamera1)(range(len(CVCamera1)),CYAN,2)
#VIEW(hpcCamera1)

toMerge = 15

doorCamera1 = assemblyDiagramInit([1,3,2])([[0.1],[4,1,2],[2.2,0.5]])
masterCamera1 = diagram2cell(doorCamera1,diagramCamera1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera1)))
hpc = cellNumbering (masterCamera1,hpc)(range(len(masterCamera1[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterCamera1 = masterCamera1[0], [cell for k,cell in enumerate(masterCamera1[1]) if not (k in toRemove)]
#DRAW(masterCamera1)

toMerge = 3

windowCamera1 = assemblyDiagramInit([1,3,3])([[0.3],[2.5,1,2.5],[1.8,3.4,3.5]])
masterCamera1 = diagram2cell(windowCamera1,masterCamera1,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera1)))
hpc = cellNumbering (masterCamera1,hpc)(range(len(masterCamera1[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterCamera1 = masterCamera1[0], [cell for k,cell in enumerate(masterCamera1[1]) if not (k in toRemove)]
#DRAW(masterCamera1)





# Camera da letto 2:
diagramCamera2 = assemblyDiagramInit([3,3,2])([[0.3,4,0.1],[0.3,6,0.1],[0.3,3]])
hpcCamera2 = SKEL_1(STRUCT(MKPOLS(diagramCamera2)))
VCamera2,CVCamera2 = diagramCamera2
hpcCamera2 = cellNumbering (diagramCamera2,hpcCamera2)(range(len(CVCamera2)),CYAN,2)
#VIEW(hpcCamera2)

toMerge = 15

doorCamera2 = assemblyDiagramInit([1,3,2])([[0.1],[0.5,1,0.5],[2.2,0.5]])
masterCamera2 = diagram2cell(doorCamera2,diagramCamera2,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera2)))
hpc = cellNumbering (masterCamera2,hpc)(range(len(masterCamera2[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterCamera2 = masterCamera1[0], [cell for k,cell in enumerate(masterCamera2[1]) if not (k in toRemove)]
#DRAW(masterCamera2)

toMerge = 3

windowCamera2 = assemblyDiagramInit([1,3,3])([[0.3],[1.5,1,3.5],[1.8,3.4,3.5]])
masterCamera2 = diagram2cell(windowCamera2,masterCamera2,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera2)))
hpc = cellNumbering (masterCamera2,hpc)(range(len(masterCamera2[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterCamera2 = masterCamera2[0], [cell for k,cell in enumerate(masterCamera2[1]) if not (k in toRemove)]
#DRAW(masterCamera2)




#Cucina:
diagramCucina = assemblyDiagramInit([3,3,2])([[0.1,4.5,0.3],[0.1,4,0.3],[0.3,3]])
hpcCucina = SKEL_1(STRUCT(MKPOLS(diagramCucina)))
VCucina,CVCucina = diagramCucina
hpcDiagramCucina = cellNumbering (diagramCucina,hpcCucina)(range(len(CVCucina)),CYAN,2)
#VIEW(hpcDiagramCucina)

toMerge = 3

doorCucina = assemblyDiagramInit([1,3,2])([[0.1],[0,1,3],[2.2,0.5]])
masterCucina = diagram2cell(doorCucina,diagramCucina,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpc = cellNumbering (masterCucina,hpc)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemove)]
#DRAW(masterCucina)

toMerge = 9

windowCucina = assemblyDiagramInit([3,1,3])([[0.5,1,3],[0.3],[2,3.5,2]])
masterCucina = diagram2cell(windowCucina,masterCucina,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCucina)))
hpc = cellNumbering (masterCucina,hpc)(range(len(masterCucina[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterCucina = masterCucina[0], [cell for k,cell in enumerate(masterCucina[1]) if not (k in toRemove)]
#DRAW(masterCucina)


#Bagno
diagramBagno = assemblyDiagramInit([3,3,2])([[0.1,4.5,0.3],[0.1,2.5,0.1],[0.3,3]])
hpcBagno = SKEL_1(STRUCT(MKPOLS(diagramBagno)))
VBagno,CVBagno = diagramBagno
hpcDiagramBagno = cellNumbering (diagramBagno,hpcBagno)(range(len(CVBagno)),CYAN,2)
#VIEW(hpcDiagramBagno)

toMerge = 3

doorBagno = assemblyDiagramInit([1,3,2])([[0.1],[1,1,0.5],[2.2,0.5]])
masterBagno = diagram2cell(doorBagno,diagramBagno,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)

toMerge = 14

windowBagno = assemblyDiagramInit([1,3,3])([[0.3],[1,1,0.5],[1.8,3.7,2]])
masterBagno = diagram2cell(windowBagno,masterBagno,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterBagno)))
hpc = cellNumbering (masterBagno,hpc)(range(len(masterBagno[1])),CYAN,2)
#VIEW(hpc)

toRemove = [26,8,18]
masterBagno = masterBagno[0], [cell for k,cell in enumerate(masterBagno[1]) if not (k in toRemove)]
#DRAW(masterBagno)


#Camera da letto 3:
diagramCamera3 = assemblyDiagramInit([3,3,2])([[0.1,4.5,0.3],[0.3,5.5,0.1],[0.3,3]])
hpcCamera3 = SKEL_1(STRUCT(MKPOLS(diagramCamera3)))
VCamera3,CVCamera3 = diagramCamera3
hpcDiagramCamera3 = cellNumbering (diagramCamera3,hpcCamera3)(range(len(CVCamera3)),CYAN,2)
#VIEW(hpcDiagramCamera3)

toMerge = 3

doorCamera3 = assemblyDiagramInit([1,3,2])([[0.1],[3.5,1,1],[2.2,0.5]])
masterCamera3 = diagram2cell(doorCamera3,diagramCamera3,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera3)))
hpc = cellNumbering (masterCamera3,hpc)(range(len(masterCamera3[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCamera3 = masterCamera3[0], [cell for k,cell in enumerate(masterCamera3[1]) if not (k in toRemove)]
#DRAW(masterCamera3)

toMerge = 13

windowCamera3 = assemblyDiagramInit([1,3,3])([[0.3],[1.2,1.6,0.8],[2,3.5,2]])
masterCamera3 = diagram2cell(windowCamera3,masterCamera3,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCamera3)))
hpc = cellNumbering (masterCamera3,hpc)(range(len(masterCamera3[1])),CYAN,2)
#VIEW(hpc)

toRemove = [24]
masterCamera3 = masterCamera3[0], [cell for k,cell in enumerate(masterCamera3[1]) if not (k in toRemove)]
#DRAW(masterCamera3)




#Corridodio:
diagramCorridoio = assemblyDiagramInit([3,3,2])([[0.1,2.5,0.1],[0.3,8,0.1],[0.3,3]])
hpcCorridoio = SKEL_1(STRUCT(MKPOLS(diagramCorridoio)))
VCorridoio,CVCorridoio = diagramCorridoio
hpcDiagramCorridoio = cellNumbering (diagramCorridoio,hpcCorridoio)(range(len(CVCorridoio)),CYAN,2)
#VIEW(hpcDiagramCorridoio)

toMerge = 7

doorCorridoio = assemblyDiagramInit([3,1,2])([[1,1,0.5],[0.3],[2.2,0.5]])
masterCorridoio = diagram2cell(doorCorridoio,diagramCorridoio,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterCorridoio)))
hpc = cellNumbering (masterCorridoio,hpc)(range(len(masterCorridoio[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,8]
masterCorridoio = masterCorridoio[0], [cell for k,cell in enumerate(masterCorridoio[1]) if not (k in toRemove)]
#DRAW(masterCorridoio)

# Sgabuzzino:
diagramSgabuzzino = assemblyDiagramInit([3,3,2])([[0.1,2.5,0.1],[0.1,3,0.3],[0.3,3]])
hpcSgabuzzino = SKEL_1(STRUCT(MKPOLS(diagramCorridoio)))
VSgabuzzino,CVSgabuzzino = diagramSgabuzzino
hpcDiagramSgabuzzino = cellNumbering (diagramSgabuzzino,hpcSgabuzzino)(range(len(CVSgabuzzino)),CYAN,2)
#VIEW(hpcDiagramSgabuzzino)

toMerge = 11

doorSgabuzzino = assemblyDiagramInit([3,1,2])([[1,1,0.5],[0.1],[2.2,0.5]])
masterSgabuzzino = diagram2cell(doorSgabuzzino,diagramSgabuzzino,toMerge)
hpc = SKEL_1(STRUCT(MKPOLS(masterSgabuzzino)))
hpc = cellNumbering (masterSgabuzzino,hpc)(range(len(masterSgabuzzino[1])),CYAN,2)
#VIEW(hpc)

toRemove = [19,9]
masterSgabuzzino = masterSgabuzzino[0], [cell for k,cell in enumerate(masterSgabuzzino[1]) if not (k in toRemove)]
#DRAW(masterSgabuzzino)


# inserisco corridoio:

toMerge_corridoio = 5
master = diagram2cell(masterCorridoio,master,toMerge_corridoio)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)


#inserisco cucina:

toMerge_cucina = 8
master = diagram2cell(masterCucina,master,toMerge_cucina)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)


# inserisco bagno:

toMerge_bagno = 7
master = diagram2cell(masterBagno,master,toMerge_bagno)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)



# inserisco camera da letto 3:

toMerge_Camera3 = 6
master = diagram2cell(masterCamera3,master,toMerge_Camera3)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)

#inserisco sgabuzzino:

toMerge_Sgabuzzino = 5
master = diagram2cell(masterSgabuzzino,master,toMerge_Sgabuzzino)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#inserisco camera da letto 2:

toMerge_Camera2 = 4
master = diagram2cell(masterCamera2,master,toMerge_Camera2)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,2)
#VIEW(hpc)

#inserisco camera da letto 1:

toMerge_Camera1 = 3
master = diagram2cell(masterCamera3,master,toMerge_Camera1)
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
#VIEW(hpc)



# rimuovo eccessi:

toRemove = [93,16,189]
master = master[0], [cell for k,cell in enumerate(master[1]) if not (k in toRemove)]
hpc = SKEL_1(STRUCT(MKPOLS(master)))
hpc = cellNumbering (master,hpc)(range(len(master[1])),CYAN,.2)
DRAW(master)
VIEW(hpc)


#ES 2


appartamentoX = (STRUCT(MKPOLS(master)))
appartamentoY = T(1)(10.8)(T(2)(27)(R([1,2])(PI)(appartamentoX)))

piano = STRUCT([appartamentoX,appartamentoY])

palazzo = STRUCT([piano,T(3)(3)]*4)

#VIEW(palazzo)

def spiralStair(thickness=0.2,R=1.,r=0.5,riser=0.1,pitch=2.,nturns=2.,steps=18):
    V,CV = larSolidHelicoid(thickness,R,r,pitch,nturns,steps)()
    W = CAT([[V[k],V[k+1],V[k+2],V[k+3]]+[SUM([V[k+1],[0,0,-riser]]),SUM([V[k+3],[0,0,-riser]])]
        for k,v in enumerate(V[:-4]) if k%4==0])
    for k,w in enumerate(W[:-12]):
        if k%6==0: W[k+1][2]=W[k+10][2]; W[k+3][2]=W[k+11][2]
    nsteps = len(W)/12
    CW =[SUM([[0,1,2,3,6,8,10,11],[6*k]*8])
            for k in range(nsteps)]
    return W,CW

scala = STRUCT(MKPOLS(spiralStair(0.2,1,0.5,0.1,2,12.5,18)))
VIEW(STRUCT([palazzo, T(2)(13.5)(scala)]))

