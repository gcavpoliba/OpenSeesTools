print('#######################################################################################################')
print('#######################################################################################################')
print('PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME ')
print('#######################################################################################################')
print('#######################################################################################################')
print('OPENSEES AUTOCOMP 1.1\nAUTHOR: GIANLUCA CAVALLO\nPOLITECNICO DI BARI')
print('YEAR: 2023')
print('EMAIL: gi.cav.2586@gmail.com')
print('Please, cite the author if use any part of this code')
print('#######################################################################################################')
print('#######################################################################################################')


print('THE AUTHOR IS NOT RESPONSABLE FOR ANY USE OF THE CODE, THE USER IS!')


print('#######################################################################################################')
print('################################ REMARKS AND TIPS     #################################################')
print('#######################################################################################################')
print('The file MASTER.py is only a rough example to test the code functionality and it will not lead to a result')
print('The file MASTER is connected to the tool module "openSTools.py"')
print('You have to execute the mfix function any times the number of the fixed surfaces, pay attention to the edges')
print('The same if you want remove the fixies')
print('You have to call with the string "Solid" the volume geoElement in the mesh')
print('Please contact me for some code bugs to correct')
print('#######################################################################################################')
print('#######################################################################################################')
print('ATTENTION PLEASE: REMEMBER TO ADD THE 20-8 UPELEMENT TO gmsh2opensees PACKET OR THIS CODE WILL NOT WORK')
print('#######################################################################################################')
print('#######################################################################################################')

print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')

import os
import openseespy.opensees as ops
import gmsh2opensees as g2o
import numpy as np
import gmsh
import math as mm
import time as tt
class Model(object):
    global nodo_mesh
    global PhysGr
    PhysGr = g2o.get_physical_groups_map(gmsh.model)
    print(g2o.get_physical_groups_map(gmsh.model))

    def __init__(self,uniqueVector = [],nomeEl=str()):
        self.uniqueVector = uniqueVector
        self.nomeEl = nomeEl
        print('Model activated')

    def setGeoElement(self,nomeEl):
        self.nomeEl = nomeEl
        print('setGeoElement: geometry element inserted')

    def getElementsVectors(self):
        elementTag=[]
        nodeTag=[]
        entities=[]
        entTag = []
        elementName=[]
        elementNnode=[]
        Tags = []
        LNT = 0
        TagPh = PhysGr[self.nomeEl][1]
        DimPh = PhysGr[self.nomeEl][0]
        if DimPh ==3:
            elementTag, nodeTag, elementName, elementNnode = g2o.get_elements_and_nodes_in_physical_group(self.nomeEl,gmsh.model)
            LNT = len(nodeTag)
            return (elementTag, nodeTag, elementName, elementNnode,LNT)
        else:
            entities = gmsh.model.getEntitiesForPhysicalGroup(DimPh, TagPh)
            Tags = gmsh.model.mesh.getElements(DimPh, entities[0])
            elementTag = Tags[1][0]
            nodeTag = Tags[2][0]
            entTag, elementTag, nodeTag = gmsh.model.mesh.getElements(DimPh, entities[0])
            return (elementTag, nodeTag)
    def setUniqueVector(self,uniqueVector):
        self.uniqueVector = uniqueVector

    def getUniqueVector(self):
        return self.uniqueVector

    def nodeNumCoordVector(self):
        opsVector = []
        collect = []
        coord_l=[]
        num = 0
        x=0
        y=0
        z=0
        j=0
        for j in self.uniqueVector:
            x = gmsh.model.mesh.getNode(int(j))[0][0]
            y = gmsh.model.mesh.getNode(int(j))[0][1]
            z = gmsh.model.mesh.getNode(int(j))[0][2]
            coord_l=[x,y,z]
            num = int(j)
            collect = [num,coord_l]
            opsVector.append(collect)
        return opsVector


    def listOfTagsij(self,l,ll):
        nodeTot = []
        nodeTotU = []
        self.l = l 
        self.ll = ll 
        for i in range(0, l):
            for j in range(0, ll):
                nodeTot.append(self.uniqueVector[i][j])
        nodeTotU=np.unique(np.array(nodeTot, dtype=int).reshape(-1))
        return nodeTotU

    def makeUnique(self):
        getUnique= np.unique(np.array(self.uniqueVector, dtype=int).reshape(-1))
        print('make Unique ok')
        return getUnique

    def nodeCornEdge(self,type):
        print('insert type = 8-nodi o 20-nodi')
        self.type = type
        j=0
        i=0
        k=0
        n = 0
        nodeNum = []
        nodeVecCorn = []
        nodeVecEdge = []
        mem = []
        elemento = str(type) 
        if elemento == '20-nodi':
            p = 1 
            l = int(len(self.uniqueVector[p]))
            for i in range(0, l):
                for j in range(0, 20):
                    nodeNum = self.uniqueVector[p][i][j]
                    mem.append(nodeNum)
                    if j == 7:
                        nodeVecCorn.append(mem)
                        mem = []
                    elif j == 19:
                        nodeVecEdge.append(mem)
                        mem = []
        else:
            len1 = len(self.uniqueVector[1][0])
            for i in range(0, len1):
                n = self.uniqueVector[1][0][i]
                mem.append(n)
                j = j + 1
                if j == 4:
                    nodeVecCorn.append(mem)
                    mem = []
                elif j == 8:
                    nodeVecEdge.append(mem)
                    j = 0
                    mem = []
        return (nodeVecCorn,nodeVecEdge)

    def sendOpsNodes(self,dim,ndf):
        self.dim = dim 
        self.ndf = ndf 
        ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
        l = len(self.uniqueVector)
        for i in range(0,l):
            coord = [self.uniqueVector[i][1][0],self.uniqueVector[i][1][1],self.uniqueVector[i][1][2]]
            ops.node(int(self.uniqueVector[i][0]),*coord)

    def sendOpsFixes(self,dim,ndf,x,y,z,p):
        self.dim = int(dim)
        self.ndf = int(ndf)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.p = int(p)
        if ndf == 4:
            ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
            l = len(self.uniqueVector)
            for i in range(0, l):
                ops.remove('sp', int(self.uniqueVector[i][0]))
                ops.fix(int(self.uniqueVector[i][0]), x, y, z, p)
        else:
            ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
            l = len(self.uniqueVector)
            for i in range(0, l):
                ops.remove('sp', int(self.uniqueVector[i][0]))
                ops.fix(int(self.uniqueVector[i][0]), x, y, z)
        

class App(Model):
    ops.reactions()
    def __init__(self):
        Model.__init__(self)

    def subReacForce(self):
        print(g2o.get_physical_groups_map(gmsh.model))
        m = Model()
        type_el = str(input('what geoElement do you want to unconstrain'))
        b = m.setGeoElement(type_el)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 4
        reacV1={}
        mem = 0
        for i in f:
            mem = ops.nodeReaction(int(i[0]), -1) 

            reacV1[int(i[0])] = mem
            ops.load(int(i[0]), mem[0],0.0,0.0,0.0)  
            ops.remove('sp',int(i[0]),1)
        #########################
      
        print('\nEdge\n')
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l=len(c[1])
        ll=len(c[1][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 3
        reacV2={}
        mem = 0
        for i in f:
            mem = ops.nodeReaction(int(i[0]), -1) 

            reacV2[int(i[0])] = mem
            ops.load(int(i[0]), mem[0],0.0,0.0)  
            ops.remove('sp',int(i[0]),1)
        

def mDefine():
        m = Model()
        b = m.setGeoElement('Solid')
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('20-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 4
        m.sendOpsNodes(dim,ndf)
        ##
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l=len(c[1])
        ll=len(c[1][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()
        m.setUniqueVector(f)
        dim = 3
        ndf = 3
        m.sendOpsNodes(dim,ndf)

def mFix():
    print(g2o.get_physical_groups_map(gmsh.model))
    m = Model()
    type_el = str(input('insert the geoElement to constarin'))
    print('insert 1 constrain on 0 to constrain off')
    x = int(input('x: 1 0n - 0 off'))
    y = int(input('y: 1 0n - 0 off'))
    z = int(input('z: 1 0n - 0 off'))
    p = int(input('p: 1 0n - 0 off'))
    b = m.setGeoElement(type_el)
    bb = m.getElementsVectors()
    m.setUniqueVector(bb)
    c = m.nodeCornEdge('8-nodi')
    m.setUniqueVector(c[0])
    print(len(c[0]))
    print(len(c[0][0]))
    l = len(c[0])
    ll = len(c[0][0])
    d = m.listOfTagsij(l,ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    f = m.nodeNumCoordVector()
    m.setUniqueVector(f)
    dim = 3
    ndf = 4
    m.sendOpsFixes(dim,ndf,x,y,z,p)
    m.setUniqueVector(c[1])
    print(len(c[1]))
    print(len(c[1][0]))
    l=len(c[1])
    ll=len(c[1][0])
    d = m.listOfTagsij(l,ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    f = m.nodeNumCoordVector()
    m.setUniqueVector(f)
    dim = 3
    ndf = 3
    m.sendOpsFixes(dim,ndf,x,y,z,p)


def mRec():
    print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')
    global nodeList
    # Selezione dei nodi di cui effettuare il record dei risultati - spostamenti - accelerazioni
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    m.setUniqueVector(eleNodes)
    l = len(eleNodes)
    ll = len(eleNodes[0])
    d = m.listOfTagsij(l, ll)
    m.setUniqueVector(d)
    e = m.makeUnique()
    np.savetxt('nodeInfo.txt', e)
    #############################################
    load_nodeList = np.loadtxt('nodeInfo.txt')
    nodeList = []

    for i in range(len(load_nodeList)):
        nodeList.append(int(load_nodeList[i]))

    m.setUniqueVector(eleTag)
    max_value = np.max(eleTag)
    min_value = np.min(eleTag)
    print(f'min_value = {min_value}, max_value = {max_value}')
    ops.recorder('Node', '-file', 'Gdisplacement.out', '-time', '-node', *nodeList, '-dof', 1, 2, 3, 'disp')
    ops.recorder('Node', '-file', 'Gacceleration.out', '-time', '-node', *nodeList, '-dof', 1, 2, 3, 'accel')
    ops.recorder('Node', '-file', 'GporePressure.out', '-time', '-node', *nodeList, '-dof', 4, 'vel')

    ops.recorder('Element', '-file', 'Gstress.out', '-time', '-eleRange', 211, 355, 'material', '1', 'stress')
    ops.recorder('Element', '-file', 'Ggauss.out', '-time', '-eleRange', 211, 355, 'material', '1', 'gausspoint')
    ops.recorder('Element', '-file', 'Gstrain.out', '-time', '-eleRange', 211, 355, 'material', '1', 'strain')
    return nodeList

def mGenFem20():
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    LET = len(bb[0])
    for i in range(0,LET):
        elem = int(eleTag[i])
        nodo1 = int(eleNodes[i][4])
        nodo2 = int(eleNodes[i][5])
        nodo3 = int(eleNodes[i][1])
        nodo4 = int(eleNodes[i][0])
        nodo5 = int(eleNodes[i][7])
        nodo6 = int(eleNodes[i][6])
        nodo7 = int(eleNodes[i][2])
        nodo8 = int(eleNodes[i][3])
        nodo9 = int(eleNodes[i][16])
        nodo10 = int(eleNodes[i][12])
        nodo11 = int(eleNodes[i][8])
        nodo12 = int(eleNodes[i][10])
        nodo13 = int(eleNodes[i][19])
        nodo14 = int(eleNodes[i][14])
        nodo15 = int(eleNodes[i][13])
        nodo16 = int(eleNodes[i][15])
        nodo17 = int(eleNodes[i][17])
        nodo18 = int(eleNodes[i][18])
        nodo19 = int(eleNodes[i][11])
        nodo20 = int(eleNodes[i][9])
        nodes_l = [nodo1,nodo2,nodo3,nodo4,nodo5,nodo6,nodo7,nodo8,nodo9, nodo10, nodo11,nodo12, nodo13, nodo14,nodo15,nodo16, nodo17,nodo18, nodo19, nodo20]
        ops.element('20_8_BrickUP',elem,*nodes_l, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-20)


def mDash():
        m = Model()
        b = m.setGeoElement('Solid')
        bb = m.getElementsVectors()
        eleNodes = bb[1]
        eleTag = bb[0]
        m.setUniqueVector(eleNodes)
        l = len(bb[1])
        ll=len(bb[1][0])
        c = m.listOfTagsij(l,ll)
        m.setUniqueVector(c)
        cc = m.makeUnique()
        max_value = np.max(cc)
        min_value = np.min(cc)
        dashFree = int(max_value + 1)
        print(f'dashFree = {dashFree}')
        dashFix = int(max_value + 2)
        print(f'dashFix = {dashFix}')
        x = float(input('insert x coord of dashpot in format 0.0'))
        y = float(input('insert y coord of dashpot in format 0.0')) 
        z = float(input('insert z coord of dashpot in format 0.0'))
        ops.node(dashFree,x,y,z)
        ops.node(dashFix,x,y,z)
        ops.fix(dashFix,1,1,1)
        f_x = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir x'))
        f_y = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir y'))
        f_z = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir z'))
        ops.fix(int(dashFree),f_x,f_y,f_z)
        nodo_mesh = int(input('write the mesh node tag who want to assigned dashpot'))
        ops.equalDOF(int(nodo_mesh), int(dashFree),1)
        colArea =   float(input('conn. area of dashpot'))
        rockVS =    float(input('Bedrock VS'))
        rockDen  =  float(input('Bedrock density'))
        dashpotCoeff = rockVS*rockDen*colArea
        tag = int(input('insert uniaxialMaterial tag (> n. geo-material)'))
        alpha = 1 
        ops.uniaxialMaterial('Viscous',tag,dashpotCoeff, alpha)
        m.setUniqueVector(eleTag)
        max_tag = np.max(eleTag)
        var_dir = int(input('dof of dashpot -dir: 1 along x, 2 along xy, 3 along y'))
        if var_dir == 1:
            dir = [1]
        elif var_dir == 2:
            dir = [1,2]
        elif var_dir == 3:
            dir = [2]
        ops.element('zeroLength', int(max_tag+1), int(dashFix), int(dashFree), '-mat', tag, '-dir', *dir)
        return [colArea,dashpotCoeff,nodo_mesh]

def floatingNodes():
    connectedNodes = []
    for ele in ops.getEleTags():
        for nd in ops.eleNodes(ele):
            connectedNodes.append(nd)

    definedNodes = ops.getNodeTags()

    return list(set(connectedNodes) ^ set(definedNodes))


def chPerm():
    permh = float(input('insert h permeability'))
    permv = float(input('insert v permeability'))
    eleTags = []
    getParamTags = []

    for i in ops.getParamTags():
        getParamTags.append(i)

    LT = len(getParamTags)
    if getParamTags == []:
        tag = 1
    else:
        tag = int(getParamTags[LT - 1]) + 1

    for i in ops.getEleTags():
        eleTags.append(int(i))

    LT2 = len(eleTags)
    for j in range(0, LT2 - 1):
        i = eleTags[j]
        ops.parameter(int(tag), 'element', i, 'hPerm')
        ops.parameter(int(tag + 1), 'element', i, 'vPerm')

        ops.updateParameter(int(tag), permh)
        ops.updateParameter(int(tag + 1), permv)
        tag = tag + 2

def mTieNodes():
        m = Model()
        type_el_master1 = str(input('insert master plane geoElement'))
        b = m.setGeoElement(type_el_master1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()

        type_el_slave1 = str(input('insert slabe plane geoElement'))
        b = m.setGeoElement(type_el_slave1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0])
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        g = m.nodeNumCoordVector()
        i = 0
        j = 0
        k = 0
        DOF = [1, 2]
        eqDofDic = {}
        for i in f:
            for j in g:
                z_master = i[1][2]
                z_slave = j[1][2]
                if z_master == z_slave:
                    eqDofDic[i[0]] = j[0]
                    ops.equalDOF(int(i[0]), int(j[0]), *DOF)

        b = m.setGeoElement(type_el_master1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l=len(c[1])
        ll=len(c[1][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()

        b = m.setGeoElement(type_el_slave1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[1])
        print(len(c[1]))
        print(len(c[1][0]))
        l = len(c[1])
        ll = len(c[1][0])
        d = m.listOfTagsij(l, ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        g = m.nodeNumCoordVector()
        i = 0
        j = 0
        k = 0
        DOF = [1, 2]
        eqDofDic = {}
        for i in f:
            for j in g:
                z_master = i[1][2]
                z_slave = j[1][2]
                if z_master == z_slave:
                    eqDofDic[i[0]] = j[0]
                    ops.equalDOF(int(i[0]), int(j[0]), *DOF)

def mStage0(gamma1,beta1):
    ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)

    ops.updateMaterialStage('-material', 1, '-stage', 0)
    ops.updateMaterialStage('-material', 2, '-stage', 0)

    ##################################################### COSTRAINTS #################################################
    ops.constraints('Penalty', 1.e18, 1.e18)

    ##################################################### TEST #######################################################
    ops.test('NormDispIncr', 1.0e-6, 500, 1)

    ##################################################### ALGORITHMS #################################################
    ops.algorithm('KrylovNewton')

    ##################################################### NUMBERER ###################################################

    ops.numberer('Plain')

    ##################################################### SYSTEM #####################################################

    ops.system('ProfileSPD')

    ##################################################### INTEGRATOR #################################################
    ops.integrator('Newmark', gamma1, beta1)

    ##################################################### ANALYSIS ###################################################
    ops.analysis('Transient')

    ##################################################### startT ###################################################
    startT = tt.time()

    ##################################################### ANALYZE ###################################################
    ops.analyze(1, 1)

def mRecDyn(recDT):
    print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')
    # record nodal displacment, acceleration, and porepressure
    ops.recorder('Node', '-file', 'displacement.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 1, 2, 3,'disp')
    ops.recorder('Node', '-file', 'acceleration.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 1, 2, 3,'accel')
    ops.recorder('Node', '-file', 'porePressure.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 4, 'vel')

    # record elemental stress and strain (files are names to reflect GiD gp numbering)
    ops.recorder('Element', '-file', 'stress.txt', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','stress')
    ops.recorder('Element', '-file', 'strain.txt', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','strain')
    ops.recorder('Element', '-file', 'strain.txt', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','plastic')

    ops.recorder('Element', '-file', 'stress.out', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','stress')
    ops.recorder('Element', '-file', 'strain.out', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','strain')
    ops.recorder('Element', '-file', 'plastic.out', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','plastic')
