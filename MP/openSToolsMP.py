############### PLEASE READ THE DISCLAIMER AND THE DESCRIPTION IN THE GITHUB PAGE #############


py = open("cubotto_exe.py","w")
py.write('import os\n\
import openseespy.opensees as ops\n\
import numpy as nup\n\
ops.wipe()\n\
import math as mm\n\
import time as tt\n')
py.close()

import os
import openseespy.opensees as ops
import gmsh2opensees as g2o
import numpy as nup
import gmsh
import math as mm
import time as tt


def trova_nodo(dicto,value):
    output = []
    for nproc, subdict in dicto.items():
        if subdict == {}:
            break
        else:
            for el_num,nod_list in subdict.items():
                if value in nod_list:
                    output.append(nproc)
    output = nup.unique(nup.array(output,dtype = int))
    return output



def trova_elemento(dicto,value):
    for nproc, subdict in dicto.items():
        for el_num,nod_list in subdict.items():
            if value == el_num:
                return nproc

nop = int(input('inserire il numero dei processori; '))

class Model(object):
    global nodo_mesh
    global PhysGr
    global nop
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
    
    def mDict(self): 
        global proc_dict
        
        tag_nodi = gmsh.model.mesh.getNodes()[0]
        numero_nodi = len(tag_nodi)
        print(f'numero dei nodi:  {numero_nodi}')
        
        tag_el = gmsh.model.mesh.getElements()[1][2]
        numero_el = len(tag_el)
        print(f'numero di elementi: {numero_el}')
        
        
        numero_el_np = 0
        if numero_el%nop==0:
            numero_el_np = int(numero_el/nop)
        else:
            numero_el_np = int(numero_el/nop) + 1
        
        print(f'il numero di el per np è: {numero_el_np}')
        
        proc_dict = {}
        for i in range(nop):
            proc_dict[i] = 0
        
        m = Model()
        m.setGeoElement('Solid')
        elementTag, nodeTag, elementName, elementNnode,LNT  = m.getElementsVectors()
        eleNode={}
        eleNode = dict(zip(elementTag,nodeTag))
        
        i = 0
        j = 0 
        k = 0 
        jj = 0
        proc_list = {}
        while i < nop:
            proc_dict[i] = {}
            while j < numero_el:
                jj = tag_el[j]
                if k < numero_el_np:
                    proc_dict[i][jj] = eleNode[jj]
                    k = k + 1
                    j = j + 1
                else:  
                    k = 0
                    break
            i = i + 1
        return proc_dict    
    
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
        nodeTotU=nup.unique(nup.array(nodeTot, dtype=int).reshape(-1))
        return nodeTotU

    def makeUnique(self):
        getUnique= nup.unique(nup.array(self.uniqueVector, dtype=int).reshape(-1))
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
        m = Model()
        proc_dict = m.mDict()
        ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
        ###################################
        
        py = open("cubotto_exe.py","a")
        py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
        py.close()
        
        ###################################
        l = len(self.uniqueVector)
        for i in range(0,l):
            coord = [self.uniqueVector[i][1][0],self.uniqueVector[i][1][1],self.uniqueVector[i][1][2]]
            ops.node(int(self.uniqueVector[i][0]),*coord)
            ###################################
            procId = trova_nodo(proc_dict,self.uniqueVector[i][0])
            for proc in procId:
                py = open("cubotto_exe.py","a")
                py.write(f'if pid == {proc}:\n')
                py.close()
                
                py = open("cubotto_exe.py","a")
                py.write(f"    ops.node({int(self.uniqueVector[i][0])}, {coord[0]}, {coord[1]}, {coord[2]})\n")
                py.close()
            ###################################

    def sendOpsFixes(self,dim,ndf,x,y,z,p):
        self.dim = int(dim)
        self.ndf = int(ndf)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
        self.p = int(p)
        m = Model()
        proc_dict = m.mDict()
        if ndf == 4:
            ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
            ################################### 
            
            py = open("cubotto_exe.py","a")
            py.write(f'    ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
            py.close()
            
            ###################################
            l = len(self.uniqueVector)
            for i in range(0, l):
                ###################################
                procId = trova_nodo(proc_dict,self.uniqueVector[i][0])
                for proc in procId:
                
                    py = open("cubotto_exe.py","a")
                    py.write(f'if pid == {proc}:\n')
                    py.close()
                    
                    py = open("cubotto_exe.py", "a")
                    py.write(f'    ops.remove("sp", {int(self.uniqueVector[i][0])})\n\
    ops.fix({int(self.uniqueVector[i][0])}, {x}, {y}, {z},{p})\n')
                    py.close()
                ###################################

                ops.remove('sp', int(self.uniqueVector[i][0]))
                ops.fix(int(self.uniqueVector[i][0]), x, y, z, p)
                
        else:
            ops.model("basicBuilder", "-ndm", dim, "-ndf", ndf)
            ################################### 
            
            py = open("cubotto_exe.py","a")
            py.write(f'ops.model("basicBuilder","-ndm",{dim},"-ndf",{ndf})\n')
            py.close()
            
            ###################################
            l = len(self.uniqueVector)
            for i in range(0, l):
                ops.remove('sp', int(self.uniqueVector[i][0]))
                ops.fix(int(self.uniqueVector[i][0]), x, y, z)
                ###################################
                procId = trova_nodo(proc_dict,self.uniqueVector[i][0])
                for proc in procId:
                    
                    py = open("cubotto_exe.py","a")
                    py.write(f'if pid == {proc}:\n')
                    py.close()
                    
                    py = open("cubotto_exe.py", "a")
                    py.write(f'    ops.remove("sp", {int(self.uniqueVector[i][0])})\n\
    ops.fix({int(self.uniqueVector[i][0])}, {x}, {y}, {z})\n')
                    py.close()
                ###################################
        

class App(Model):
    ops.reactions()
    
    def __init__(self):
        Model.__init__(self)

    def subReacForce(self):
        print(g2o.get_physical_groups_map(gmsh.model))
        m = Model()
        proc_dict = m.mDict()
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
            ops.load(int(i[0]), mem[0],mem[1],mem[2],0.0)
            ops.remove('sp',int(i[0]))
            
            procId = trova_nodo(proc_dict,int(i[0]))
            for proc in procId:
                
                py = open("cubotto_exe.py", "a")
                py.write(f'if pid == {proc}:\n')
                py.write(f"    ops.load({int(i[0])}, {mem[0]},{mem[1]},{mem[2]},0.0)\n    ops.remove('sp',{int(i[0])})\n")
                py.close()

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
            ops.load(int(i[0]), mem[0],mem[1],mem[2])  
            ops.remove('sp',int(i[0]))
            
            procId = trova_nodo(proc_dict,int(i[0]))
            for proc in procId:
                py = open("cubotto_exe.py", "a")
                py.write(f'if pid == {proc}:\n')
                py.write(f"    ops.load({int(i[0])}, {mem[0]},{mem[1]},{mem[2]})\n    ops.remove('sp',{int(i[0])})\n")
                py.close()
            

def mDefine():
        m = Model()
        proc_dict = m.mDict()
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

def mgetFixedCoord():
        f = ops.getFixedNodes()
        coordTag=[]
        fixedCoord=[]
        Dofs=[]
        for i in f:
            coordTag.append(i)
            coordFixNode = ops.nodeCoord(i)
            fixedCoord.append(coordFixNode)
            g = ops.getFixedDOFs(i)
            Dofs.append(g)
        return [coordTag,fixedCoord,Dofs]

def mFix():
    print(g2o.get_physical_groups_map(gmsh.model))
    m = Model()  
    fixed = mgetFixedCoord()
    type_el = str(input('inserisci l elemento geo da vincolare: '))
    print('inserire 1 per vincolo on 0 per vincolo off')

    DofL = []
    x = int(input('x: 1 0n - 0 off: '))
    f_x = 0
    if x == 1:
        f_x = 1
        DofL.append(f_x)
    else:
        f_x = 0
        
    y = int(input('y: 1 0n - 0 off: '))
    f_y = 0
    if y == 1:
        f_y = 2
        DofL.append(f_y)
    else:
        f_y = 0
        
    z = int(input('z: 1 0n - 0 off: '))
    f_z = 0
    if z == 1:
        f_z = 3
        DofL.append(f_z)
    else:
        f_z = 0
        
    p = int(input('p: 1 0n - 0 off: '))
    f_p = 0
    if p == 1:
        f_p = 4
        DofL.append(f_p)
    else:
        f_p = 0
    #Vettore dof Locale ok

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
    ff = []

    for i in f:
        flag=0
        mem=[]
        if fixed ==[[],[],[]]:
            ff.append(i)
            continue
        for j in fixed[1]:
            if flag == 1:
                break
            if i[1] == j:
                for k in fixed[2]:
                  if flag == 1:
                     break
                  for kk in k:
                      if flag == 1:
                          break
                      for l in DofL:
                        if kk == l:
                            flag=1
                            break
        if flag == 0:
            ff.append(i)


    m.setUniqueVector(ff)
    dim = 3
    ndf = 4
    m.sendOpsFixes(dim,ndf,x,y,z,p)
    
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
    ff = []

    for i in f:
        flag=0
        mem=[]
        if fixed ==[[],[],[]]:
            ff.append(i)
            continue
        for j in fixed[1]:
            if flag == 1:
                break
            if i[1] == j:
                for k in fixed[2]:
                  if flag == 1:
                     break
                  for kk in k:
                      if flag == 1:
                          break
                      for l in DofL:
                        if kk == l:
                            flag=1
                            break
        if flag == 0:
            ff.append(i)


    m.setUniqueVector(ff)
    dim = 3
    ndf = 3
    m.sendOpsFixes(dim,ndf,x,y,z,p)



def mRec():
    print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')
    global nodeList

    m = Model()
    proc_dict = m.mDict()
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
    nup.savetxt('nodeInfo.txt', e)
    #############################################
    load_nodeList = nup.loadtxt('nodeInfo.txt')
    nodeList = []

    for i in range(len(load_nodeList)):
        nodeList.append(int(load_nodeList[i]))

    m.setUniqueVector(eleTag)
    max_value = nup.max(eleTag)
    min_value = nup.min(eleTag)
    print(f'min_value = {min_value}, max_value = {max_value}')
    ops.recorder('Node', '-file', 'Gdisplacement.out', '-time', '-node', *nodeList, '-dof', 1, 2, 3, 'disp')
    ops.recorder('Node', '-file', 'Gacceleration.out', '-time', '-node', *nodeList, '-dof', 1, 2, 3, 'accel')
    ops.recorder('Node', '-file', 'GporePressure.out', '-time', '-node', *nodeList, '-dof', 4, 'vel')
    #################################################
    for nproc, subdict in proc_dict.items():
        if subdict == {}:
            break
        else:
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {nproc}:\n')
            py.close()
            for el_num,nod_list in subdict.items():
                max_val = int(nup.max(nod_list))
                min_val = int(nup.min(nod_list))
                py = open("cubotto_exe.py", "a")
                py.write(f"    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',{min_val}, {max_val},'-dof', 1, 2, 3, 'disp')\n\
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',{min_val}, {max_val},'-dof', 1, 2, 3, 'accel')\n\
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',{min_val}, {max_val},'-dof', 4, 'vel')\n")
                py.close()
    #################################################
    ops.recorder('Element', '-file', 'Gstress.out', '-time', '-eleRange', 211, 355, 'material', '1', 'stress')
    ops.recorder('Element', '-file', 'Ggauss.out', '-time', '-eleRange', 211, 355, 'material', '1', 'gausspoint')
    ops.recorder('Element', '-file', 'Gstrain.out', '-time', '-eleRange', 211, 355, 'material', '1', 'strain')
    #################################################
    for nproc, subdict in proc_dict.items():
        if subdict == {}:
            break
        else:
            el_n_list=[]
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {nproc}:\n')
            py.close()
            for el_num,nod_list in subdict.items():
                el_n_list.append(el_num)
            max_val = int(nup.max(el_n_list))
            min_val = int(nup.min(el_n_list))
            py = open("cubotto_exe.py", "a")
            py.write(f"    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', {min_val},{max_val},'material','1','stress')\n\
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', {min_val},{max_val},'material','1','gausspoint')\n\
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', {min_val},{max_val},'material','1','strain')\n")
            py.close()
        #################################################
    return nodeList

def mGenFem20():
    m = Model()
    proc_dict = m.mDict()
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
        #################################################
        procId = trova_elemento(proc_dict,elem)    
        py = open("cubotto_exe.py", "a")
        py.write(f'if pid == {procId}:\n')
        py.write(f"    ops.element('20_8_BrickUP',{elem},{nodo1}, {nodo2}, {nodo3}, {nodo4}, {nodo5}, {nodo6}, {nodo7}, {nodo8}, {nodo9},{nodo10}, {nodo11}, {nodo12}, {nodo13}, {nodo14}, {nodo15}, {nodo16}, {nodo17}, {nodo18},{nodo19}, {nodo20}, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)\n")
        py.close()


def mDash():
        m = Model()
        proc_dict = m.mDict()
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
        max_value = nup.max(cc)
        min_value = nup.min(cc)
        dashFree = int(max_value + 1)
        
        print(f'dashFree = {dashFree}')
        
        dashFix = int(max_value + 2)
        print(f'dashFix = {dashFix}')
        
        x = float(input('insert x coord of dashpot in format 0.0'))
        y = float(input('insert y coord of dashpot in format 0.0')) 
        z = float(input('insert z coord of dashpot in format 0.0'))
        ops.node(dashFree,x,y,z)
        #################################################
        #################################################
        ops.node(dashFix,x,y,z)
        #################################################
        #################################################
        
        ops.fix(dashFix,1,1,1)
        
        #################################################
        #################################################
        
        f_x = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir x'))
        f_y = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir y'))
        f_z = int(input('Free node - insert 1 to constrain on - 0 to constrain off on dir z'))
        
        ops.fix(int(dashFree),f_x,f_y,f_z)
        
        #################################################
        #################################################
        
        nodo_mesh = int(input('write the mesh node tag who want to assigned dashpot'))
        
        ops.equalDOF(int(nodo_mesh), int(dashFree),1)
        
        #################################################
        procId = trova_nodo(proc_dict,int(nodo_mesh))
        for proc in procId:
            
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {proc}:\n')
        
        
        py = open("cubotto_exe.py", "a")
        py.write(f'    ops.node({dashFree},{x},{y},{z})\n')
        py.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f'    ops.node({dashFix},{x},{y},{z})\n')
        py.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f'    ops.fix({dashFix},1,1,1)\n')
        py.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f'    ops.fix({dashFree},{f_x},{f_y},{f_z})\n')
        py.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f'    ops.equalDOF(int({nodo_mesh}), int({dashFree}),1)\n')
        py.close()
        #################################################
        
        colArea =   float(input('conn. area of dashpot'))
        rockVS =    float(input('Bedrock VS'))
        rockDen  =  float(input('Bedrock density'))
        dashpotCoeff = rockVS*rockDen*colArea
        tag = int(input('insert uniaxialMaterial tag (> n. geo-material)'))
        alpha = 1 
        ops.uniaxialMaterial('Viscous',tag,dashpotCoeff, alpha)
        #################################################
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.uniaxialMaterial('Viscous',{tag},{dashpotCoeff}, {alpha})\n")
        py.close()
        #################################################
        m.setUniqueVector(eleTag)
        max_tag = nup.max(eleTag)
        var_dir = int(input('dof of dashpot -dir: 1 along x, 2 along xy, 3 along y'))
        if var_dir == 1:
            dir = [1]
        elif var_dir == 2:
            dir = [1,2]
        elif var_dir == 3:
            dir = [2]
        ops.element('zeroLength', int(max_tag+1), int(dashFix), int(dashFree), '-mat', tag, '-dir', *dir)
        #################################################
        py = open("cubotto_exe.py", "a")
        py.write(f'    dir = {dir}\n')
        py.write(f"    ops.element('zeroLength', {int(max_tag+1)}, {int(dashFix)}, {int(dashFree)}, '-mat', {tag}, '-dir', *dir)\n")
        py.close()
        #################################################
        return [colArea,dashpotCoeff,nodo_mesh]
    
        
        

def floatingNodes():
    connectedNodes = []
    for ele in ops.getEleTags():
        for nd in ops.eleNodes(ele):
            connectedNodes.append(nd)

    definedNodes = ops.getNodeTags()

    return list(set(connectedNodes) ^ set(definedNodes))


def chPerm():
    m = Model()
    proc_dict = m.mDict()
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
        #################################################
        procId = trova_elemento(proc_dict,i)    
        py = open("cubotto_exe.py", "a")
        py.write(f'if pid == {procId}:\n')
        py.write(f"    ops.parameter({int(tag)}, 'element', {i},'hPerm')\n")
        py.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.parameter({int(tag + 1)}, 'element', {i},'vPerm')\n")
        py.close()
        #################################################
        ops.updateParameter(int(tag), permh)
        ops.updateParameter(int(tag + 1), permv)
        #################################################
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.updateParameter({int(tag)},{permh})\n")
        py.close()
        
        py = open("cubotto_exe.py", "a")
        py.write(f"    ops.updateParameter({int(tag + 1)},{permv})\n")
        py.close()
        #################################################
        tag = tag + 2
        
        
def mTieNodes():
        m = Model()
        proc_dict = m.mDict()
        type_el_master1 = str(input('insert master plane geoElement'))
        b = m.setGeoElement(type_el_master1)
        bb = m.getElementsVectors()
        m.setUniqueVector(bb)
        c = m.nodeCornEdge('8-nodi')
        m.setUniqueVector(c[0]) ############ CORNER
        print(len(c[0]))
        print(len(c[0][0]))
        l = len(c[0])
        ll = len(c[0][0])
        d = m.listOfTagsij(l,ll)
        m.setUniqueVector(d)
        e = m.makeUnique()
        f = m.nodeNumCoordVector()

        type_el_slave1 = str(input('insert slave plane geoElement'))
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
                    #################################################
                    procId_i = trova_nodo(proc_dict,int(i[0]))
                    procId_j = trova_nodo(proc_dict,int(j[0]))
                    for proc_i in procId_i:
                           if proc_i in procId_j:
                                py = open("cubotto_exe.py", "a")
                                py.write(f'if pid == {proc_i}:\n')
                                py.write(f'    DOF = {DOF}\n')
                                py.write(f'    equalDOF({int(i[0])}, {int(j[0])}, *DOF)\n')
                                py.close()
                           else:
                                py = open("cubotto_exe.py", "a")
                                py.write(f'if pid == {proc_i}:\n') 
                                py.write(f'    DOF = {DOF}\n\
    x = gmsh.model.mesh.getNode({int(j[0])})[0][0]\n\
    y = gmsh.model.mesh.getNode({int(j[0])})[0][1]\n\
    z = gmsh.model.mesh.getNode({int(j[0])})[0][2]\n\
    coord_l=[x,y,z]\n')
                                py.write(f'    ops.node({int(j[0])},*coord_l)\n') 
                                py.write(f'    equalDOF({int(i[0])}, {int(j[0])}, *DOF)\n')
                                py.close()
                                
           
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
                    #################################################
                    procId_i = trova_nodo(proc_dict,int(i[0]))
                    procId_j = trova_nodo(proc_dict,int(j[0]))
                    for proc_i in procId_i:
                           if proc_i in procId_j:
                                py = open("cubotto_exe.py", "a")
                                py.write(f'if pid == {proc_i}:\n')
                                py.write(f'    DOF = {DOF}\n')
                                py.write(f'    equalDOF({int(i[0])}, {int(j[0])}, *DOF)\n')
                                py.close()
                           else:
                                py = open("cubotto_exe.py", "a")
                                py.write(f'if pid == {proc_i}:\n') 
                                py.write(f'    DOF = {DOF}\n\
    x = gmsh.model.mesh.getNode({int(j[0])})[0][0]\n\
    y = gmsh.model.mesh.getNode({int(j[0])})[0][1]\n\
    z = gmsh.model.mesh.getNode({int(j[0])})[0][2]\n\
    coord_l=[x,y,z]\n')
                                py.write(f'    ops.node({int(j[0])},*coord_l)\n') 
                                py.write(f'    equalDOF({int(i[0])}, {int(j[0])}, *DOF)\n')
                                py.close()
                    #################################################

def mStage0(gamma1,beta1):
    
    
    
    ops.model("basicBuilder", "-ndm", 3, "-ndf", 4)
    

    ops.updateMaterialStage('-material', 1, '-stage', 0)
    ops.updateMaterialStage('-material', 2, '-stage', 0)

    py = open("cubotto_exe.py", "a")
    py.write('ops.model("basicBuilder","-ndm",3,"-ndf",4)\n')
    py.close()
    
    py = open("cubotto_exe.py", "a")
    py.write("ops.updateMaterialStage('-material', 1, '-stage', 0)\n")
    py.write("ops.updateMaterialStage('-material', 2, '-stage', 0)\n")
    py.close()


    ops.constraints('Penalty', 1.e18, 1.e18)
    ops.test('NormDispIncr', 1.0e-6, 500, 1)
    ops.algorithm('KrylovNewton')
    ops.numberer('Plain')
    ops.system('ProfileSPD')
    ops.integrator('Newmark', gamma1, beta1)
    ops.analysis('Transient')
    startT = tt.time()
    
    py = open("cubotto_exe.py", "a")
    py.write(f"ops.constraints('Penalty', 1.e18, 1.e18)\n\
ops.test('NormDispIncr', 1.0e-6, 500, 1)\n\
ops.algorithm('KrylovNewton')\n\
ops.numberer('Plain')\n\
ops.system('ProfileSPD')\n\
ops.integrator('Newmark', {gamma1}, {beta1})\n\
ops.analysis('Transient')\n\
startT = tt.time()\n\
ops.analyze(1,1)\n")
    py.close()
    
    ops.analyze(1, 1)

def mRecDyn(recDT):
    m = Model()
    proc_dict = m.mDict()
    print('The code is under developement, please remeber to change the 3d recorder element range in mRec functions')
    ops.recorder('Node', '-file', 'displacement.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 1, 2, 3,'disp')
    ops.recorder('Node', '-file', 'acceleration.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 1, 2, 3,'accel')
    ops.recorder('Node', '-file', 'porePressure.out', '-time', '-dT', recDT, '-node', *nodeList, '-dof', 4, 'vel')
    
    
    

    ops.recorder('Element', '-file', 'stress.txt', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','stress')
    ops.recorder('Element', '-file', 'strain.txt', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','strain')
    ops.recorder('Element', '-file', 'strain.txt', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','plastic')

    ops.recorder('Element', '-file', 'stress.out', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','stress')
    ops.recorder('Element', '-file', 'strain.out', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','strain')
    ops.recorder('Element', '-file', 'plastic.out', '-time', '-dT', recDT, '-eleRange', 211, 335, 'material', '1','plastic')
   

    for nproc, subdict in proc_dict.items():
        if subdict == {}:
            break
        else:
            el_n_list=[]
            py = open("cubotto_exe.py", "a")
            py.write(f'if pid == {nproc}:\n')
            py.close()
            for el_num,nod_list in subdict.items():
                el_n_list.append(el_num)
                max_val = int(nup.max(nod_list))
                min_val = int(nup.min(nod_list))
                py = open("cubotto_exe.py", "a")
                py.write(f"    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',{min_val},{max_val},'-dof', 1, 2,3, 'disp')\n\
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',{min_val},{max_val},'-dof', 1, 2,3, 'accel')\n\
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',{min_val},{max_val},'-dof', 4, 'vel')\n")
                py.close()
            max_val = int(nup.max(el_n_list))
            min_val = int(nup.min(el_n_list))
            py = open("cubotto_exe.py", "a")
            py.write(f"    ops.recorder('Element','-file','stress.out','-time','-eleRange', {min_val},{max_val},'material','1','stress')\n\
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', {min_val},{max_val},'material','1','gausspoint')\n\
    ops.recorder('Element','-file','strain.out','-time','-eleRange', {min_val},{max_val},'material','1','strain')\n")
            py.close()


def mExportPVD():
    m = Model()
    filename = 'exportPVDfile'
    if not os.path.exists(filename):
        os.makedirs(filename)
    ops.recorder('PVD', filename, 'disp', 'gausspoint', 'stress')


def mNodeInfoTxt():
    global nodeList
   
    m = Model()
    print('Attenzione chiamare con Solid l elemento di volume')
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
    nup.savetxt('nodeInfo.txt', e)

def mNodeInfoCornerDat():
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
    n = open("nodeInfoCorner.dat","w")
    for i in f:
        xCoord =  i[1][0]
        yCoord =  i[1][1]
        zCoord =  i[1][2]
        n.write(f"{i[0]} {xCoord}    {yCoord}    {zCoord}\n")
    n.close()
    

def mNodeInfoDat():
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    m.setUniqueVector(bb[1])
    c = m.makeUnique()
    m.setUniqueVector(c)
    d=m.nodeNumCoordVector()
    n=open("nodeInfo.dat","w")
    for i in d:
     xCoord =  i[1][0]
     yCoord =  i[1][1]
     zCoord =  i[1][2]
     n.write(f"{i[0]} {xCoord}    {yCoord}    {zCoord}\n")
    n.close()


def mGIDfile():
    m = Model()
    b = m.setGeoElement('Solid')
    bb = m.getElementsVectors()
    eleNodes = bb[1]
    eleTag = bb[0]
    LET = len(bb[0])
    print(LET)
    
    mesh=open("mesh4GID.msh","w")
    element=open("element4GID.dat","w")
    mesh.write("MESH dimension 3 ElemType Hexahedra Nnode 20\n") 
    mesh.write("Coordinates\n")
    mesh.write("#node_number   coord_x   coord_y   coord_z\n")
    m.setUniqueVector(bb[1])
    c = m.makeUnique()
    m.setUniqueVector(c)
    d=m.nodeNumCoordVector()
    for i in d:
         xCoord =  i[1][0]
         yCoord =  i[1][1]
         zCoord =  i[1][2]
    mesh.write(f"{i[0]} {xCoord}    {yCoord}    {zCoord}\n")
    mesh.write("end coordinates\n")
    mesh.write("Elements\n")
        
    mesh.write("# element   nodo1  nodo2   nodo3   nodo4   nodo5   nodo6   nodo7   nodo8   nodo9   nodo10   nodo11   nodo12   nodo13   nodo14   nodo15   nodo16   nodo17   nodo18   nodo19   nodo20\n")
    
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
            mesh.write(f"{elem} {nodo1} {nodo2} {nodo3} {nodo4} {nodo5} {nodo6} {nodo7} {nodo8} {nodo9} {nodo10} {nodo11} {nodo12} {nodo17} {nodo18} {nodo19} {nodo20} {nodo13} {nodo14} {nodo15} {nodo16} \n")
            element.write(f"{elem} {nodo1} {nodo2} {nodo3} {nodo4} {nodo5} {nodo6} {nodo7} {nodo8} {nodo9} {nodo10} {nodo11} {nodo12} {nodo17} {nodo18} {nodo19} {nodo20} {nodo13} {nodo14} {nodo15} {nodo16}\n")
    mesh.write("end elements")
    
    element.close()
    mesh.close()
