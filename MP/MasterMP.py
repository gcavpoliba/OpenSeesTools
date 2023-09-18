############### PLEASE READ THE DISCLAIMER AND THE DESCRIPTION IN THE GITHUB PAGE #############

py = open("cubotto_exe.py","w")
py.write('import os\n\
import openseespy.opensees as ops\n\
import numpy as nup\n\
ops.wipe()\n\
import math as mm\n\
import time as tt\n')
py.close()
#####################################
######################################### NUMERO PROCESSORI 8 ncuts riga 258 ####################################
import os
import math as mm
import time as tt
import openseespy.opensees as ops
import gmsh2opensees as g2o
import numpy as nup
import gmsh


gmsh.initialize()
meshfilename = str(input("insert the name of the mesh file: Cubo_new.msh: "))
gmsh.open(meshfilename)

import openSToolsMP as ot

###### START ########
ops.wipe()

py = open("cubotto_exe.py","a")
py.write('pid = ops.getPID()\n\
np = ops.getNP()\n\
ops.barrier()\n')
py.close()


py = open("cubotto_exe.py","a")
py.write('ops.model("basicBuilder","-ndm",3,"-ndf",4)\n')
py.close()

ops.model("basicBuilder","-ndm",3,"-ndf",4)



matTag =  1
E = 210e9 #Pa
nd = 3 #dimension
nu = 0.3
rho = 7300. # kg/m3
friction = 31.0         #friction angle
phaseTransform = 26.0   #phase transformation angle
G1 = 9.e4
B1 = 22.e4
gamma =    0.600      # Newmark integration parameter
dT =   0.01           # time step for analysis, does not have to be the same as accDt.
numSteps= 2500       # number of time steps
rhoS  =1.80          # saturated mass density
rhoF  =1.00          # fluid mass density
Bfluid =2.2e6        # fluid shear modulus
fluid1 =1            # fluid material tag
solid1 =10           # solid material tag
perm   =1.e-5    #permeability (m/s)
accGravity =9.81  #acceleration of gravity
perm1   =[perm/accGravity/rhoF]    # actual value used in computation
accMul = 2                    # acceleration multiplier
pi = 3.1415926535
inclination = 0
massProportionalDamping   =0.0
InitStiffnessProportionalDamping =0.003
gravityX =[accGravity*nup.sin(inclination/180.0*pi)] # gravity acceleration in X direction
gravityY =0.0                                        # gravity acceleration in Y direction
gravityZ =[accGravity*nup.cos(inclination/180.0*pi)]  # gravity acceleration in Z direction

ops.nDMaterial('PressureDependMultiYield02', 1, 3, rhoS, G1, B1, friction, 2.5, 80, 0.5, phaseTransform, 0.067, 0.23, 0.06, 0.27)

py = open("cubotto_exe.py","a")
py.write(f"ops.nDMaterial('PressureDependMultiYield02',1, 3, {rhoS}, {G1}, {B1}, {friction}, 2.5, 80, 0.5, {phaseTransform}, 0.067, 0.23, 0.06, 0.27)\n")
py.close()


ot.mDefine()

ot.boundNodesPid0()


#X
print('vincolo sulle facce a perpendicolare X')
ot.mFix()
#Y
print('vincolo sulle facce a perpendicolare Y')
ot.mFix()
#DOWN
print('vincolo sulle facce di base')
ot.mFix()
#TOP
print('vincolo sulle facce in superficie')
ot.mFix()

ot.mGenFem20()
[colArea,dashpotCoeff,nodo_mesh]=ot.mDash()
ot.mNodeInfoTxt()
nodeList=ot.mRec()


motionDT = 0.005
recDT = 10*motionDT


py = open("cubotto_exe.py", "a")
py.write(f'motionDT = {motionDT}\n\
recDT = 10*{motionDT}\n')
py.close()


motionSteps = 2500

py = open("cubotto_exe.py", "a")
py.write(f'motionSteps = {motionSteps}\n')
py.close()


#---RAYLEIGH DAMPING PARAMETERS
# damping ratio
damp = 0.02
# lower frequency
omega1 = 2 * nup.pi * 0.2
# upper frequency
omega2 = 2 * nup.pi * 20
# damping coefficients
a0 = 2*damp*omega1*omega2/(omega1 + omega2)
a1 = 2*damp/(omega1 + omega2)
print(f"FATTORI DI SMORZAMENTO: a_0 = {a0};  a_1 = {a1}")

#---DETERMINE STABLE ANALYSIS TIME STEP USING CFL CONDITION
# maximum shear wave velocity (m/s)
vsMax = 250.0
# duration of ground motion (s)
duration = motionDT*motionSteps
# minimum element size
minSize = 2

# trial analysis time step
kTrial = minSize / (vsMax ** 0.5)
# define time step and number of steps for analysis
if motionDT <= kTrial:
    nSteps = motionSteps
    dT = motionDT
else:
    nSteps = int(mm.floor(duration / kTrial) + 1)
    dT = duration / nSteps

py = open("cubotto_exe.py", "a")
py.write(f'nSteps = {nSteps}\n\
dT = {dT}\n')
py.close()

##################################################################
gamma = 1.5
gamma1= 0.5

beta  = (1/4)*(gamma+0.5)**2
beta1 = 0.25

###################### ANALISI STAGE 0 ###########################
ot.mStage0(gamma1,beta1)



#################################################################

ops.updateMaterialStage('-material', 1, '-stage', 1)
ops.updateMaterialStage('-material', 2, '-stage', 1)


py = open("cubotto_exe.py", "a")
py.write("ops.updateMaterialStage('-material', 1, '-stage', 1)\n")
py.write("ops.updateMaterialStage('-material', 2, '-stage', 1)\n")
py.write("ops.domainChange()\n")
py.close()


#################### INSERIMENTO PERMEABILITA ##########################
ot.chPerm()

##################### TIME SERIES + PATTERN ############################

ops.reactions()
ops.timeSeries('Constant',1)
ops.pattern('Plain',1,1,'-fact',1.0)

py = open("cubotto_exe.py", "a")
py.write(f"ops.reactions()\n\
ops.timeSeries('Constant',1)\n\
ops.pattern('Plain',1,1,'-fact',1.0)\n")
py.close()


################### TIE NODES ##########################################

print('svincolo facce lungo x - movimento xy')
ot.App.subReacForce(ot.Model)


print('tie nodes facce a perpendicolare x')
ot.mTieNodes()


#############################################################
cFactor = colArea * dashpotCoeff

py = open("cubotto_exe.py", "a")
py.write(f"cFactor = {cFactor}\n")
py.close()

#############################################################
ops.model('basic', '-ndm', 3, '-ndf', 4)
##################### reset time and analysis ####################
ops.setTime(0.0)
ops.wipeAnalysis()
ops.remove('recorders')
######################## define velocity time history file
velocityFile = 'yerbaNSvelocity';
data_gm = nup.loadtxt('yerbaNSvelocity.out')
ops.timeSeries('Path', 2, '-dt', motionDT, '-filePath', velocityFile +'.out', '-factor', cFactor)
ops.pattern('Plain', 10, 2)
ops.load(nodo_mesh, 1.0,0.0, 0.0)

py = open("cubotto_exe.py", "a")
py.write(f"ops.model('basic', '-ndm', 3, '-ndf', 4)\n\
ops.setTime(0.0)\n\
ops.wipeAnalysis()\n\
ops.remove('recorders')\n\
velocityFile = 'yerbaNSvelocity'\n\
data_gm = nup.loadtxt('yerbaNSvelocity.out')\n\
ops.timeSeries('Path', 2, '-dt', {motionDT}, '-filePath', velocityFile +'.out', '-factor', {cFactor})\n\
ops.pattern('Plain', 10, 2)\n")
py.close()

m = ot.Model()
proc_dict = m.mDict()
procId = ot.trova_nodo(proc_dict,int(nodo_mesh))
for proc in procId:
    
    py = open("cubotto_exe.py", "a")
    py.write(f'if pid == {proc}:\n')
    py.write(f'    ops.load({nodo_mesh}, 1.0,0.0, 0.0)\n')
    py.close()
            




ot.mRecDyn(recDT)

############################### ATTENZIONE NCUTS ######################################################
py = open("cubotto_exe.py", "a")
py.write(f"ops.barrier()\n\
ops.partition('-ncuts',8)\n\
ops.domainChange()\n")
py.close()


print("Dynamic loading created...")

ops.constraints('Penalty', 1.0E16, 1.0E16)
ops.test('NormDispIncr', 1e-3, 100, 1)
ops.algorithm('KrylovNewton')
ops.numberer('RCM')
ops.system('ProfileSPD')
ops.integrator('Newmark', gamma, beta)
ops.rayleigh(a0, a1, 0.0, 0.0)
ops.analysis('Transient')

py = open("cubotto_exe.py", "a")
py.write(f"ops.constraints('Penalty', 1.0E16, 1.0E16)\n\
ops.test('NormDispIncr', 1e-3, 100, 1)\n\
ops.algorithm('KrylovNewton')\n\
ops.numberer('ParallelRCM')\n\
ops.system('Mumps')\n\
ops.integrator('Newmark', {gamma}, {beta})\n\
ops.rayleigh({a0}, {a1}, 0.0, 0.0)\n\
ops.analysis('Transient')\n")
py.close()



py = open("cubotto_exe.py", "a")
py.write(f"ok = ops.analyze(nSteps, dT)\n\
if ok != 0:\n\
    print('did not converge, reducing time step')\n\
    curTime = ops.getTime()\n\
    mTime = curTime\n\
    print('curTime: ', curTime)\n\
    curStep = curTime / dT\n\
    print('curStep: ', curStep)\n\
    rStep = (nSteps - curStep) * 2.0\n\
    remStep = int((nSteps - curStep) * 2.0)\n\
    print('remStep: ', remStep)\n\
    dT = dT / 2.0\n\
    print('dT: ', dT)\n\
    ok = ops.analyze(remStep, dT)\n\
    # if analysis fails again, reduce timestep and continue with analysis\n\
    if ok != 0:\n\
        print('did not converge, reducing time step')\n\
        curTime = ops.getTime()\n\
        print('curTime: ', curTime)\n\
        curStep = (curTime - mTime) / dT\n\
        print('curStep: ', curStep)\n\
        remStep = int((rStep - curStep) * 2.0)\n\
        print('remStep: ', remStep)\n\
        dT = dT / 2.0\n\
        print('dT: ', dT)\n\
        ok = ops.analyze(remStep, dT)\n\
endT = tt.time()\n")
py.close() 


#perform analysis with timestep reduction loop
ok = ops.analyze(nSteps, dT)


#Per commentare e scommentare ctrl + 1 e ctrl + 4
#if analysis fails, reduce timestep and continue with analysis
if ok != 0:
     print("did not converge, reducing time step")
     curTime = ops.getTime()
     mTime = curTime
     print("curTime: ", curTime)
     curStep = curTime / dT
     print("curStep: ", curStep)
     rStep = (nSteps - curStep) * 2.0
     remStep = int((nSteps - curStep) * 2.0)
     print("remStep: ", remStep)
     dT = dT / 2.0
     print("dT: ", dT)

     ok = ops.analyze(remStep, dT)
    # if analysis fails again, reduce timestep and continue with analysis
     if ok != 0:
         print("did not converge, reducing time step")
         curTime = ops.getTime()
         print("curTime: ", curTime)
         curStep = (curTime - mTime) / dT
         print("curStep: ", curStep)
         remStep = int((rStep - curStep) * 2.0)
         print("remStep: ", remStep)
         dT = dT / 2.0
         print("dT: ", dT)

         ok = ops.analyze(remStep, dT)

        
       
        
       
endT = tt.time()
print("Finished with dynamic analysis...")
print("Analysis execution time: ", (endT - startT))
ops.wipe()
