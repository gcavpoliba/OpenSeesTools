print('#######################################################################################################')
print('#######################################################################################################')
print('PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME ')
print('#######################################################################################################')
print('#######################################################################################################')
print(' ')
print('OPENSEES AUTOCOMP 1.1 \nAUTHOR: GIANLUCA CAVALLO\nPOLITECNICO DI BARI')
print('YEAR: 2023')
print('EMAIL: gi.cav.2586@gmail.com')
print('Please, cite the author if use any part of this code')
print(' ')
print('#######################################################################################################')
print('#######################################################################################################')
print(' ')
print(' ')
print('THE AUTHOR IS NOT RESPONSABLE FOR ANY USE OF THE CODE, THE USER IS!')
print(' ')
print(' ')
print('#######################################################################################################')
print('################################ REMARKS AND TIPS     #################################################')
print('#######################################################################################################')
print(' ')
print('                 THIS IS AN ALPHA VERSION - CONSIDER THAT IN YOUR COMMENTS')
print(' ')
print('The milestone codes followed are those in the opensees and openseespy documentation on 2d and 3d shaked columns')
print('The file MASTER.py is only a rough example to test the code functionality and it will not lead to a result')
print('The file MASTER is connected to the tool module "openSTools.py"')
print('You have to execute the mfix function any times the number of the fixed surfaces, pay attention to the edges')
print('The same if you want remove the fixies')
print('Please contact me for some code bugs to correct')
print('You have to install by pip: openseespy opensees gmsh gmsh2opensees numpy scipy time math os')
print('Whit this code you could perform easily the analysis with every mesh you build with gmsh and 20-8 node up element')
print('you should take care in the geo_material choice')
print('Have fun')
print(' ')
print('#######################################################################################################')
print('#######################################################################################################')
print(' ')
print('ATTENTION PLEASE: REMEMBER TO ADD THE 20-8 UPELEMENT TO gmsh2opensees PACKET OR THIS CODE WILL NOT WORK')
print(' ')
print('#######################################################################################################')
print('#######################################################################################################')
print(' ')
print('#######################################################################################################')
print('############################## OK - LET S GO ##########################################################')
print('#######################################################################################################')
print(' ')
################ DEPENDENCIES: OPENSEES OPENSEESPY GMSH GMSH2OPENSEES##########################################
import os
import math as mm
import time as tt
import openseespy.opensees as ops

import gmsh2opensees as g2o
import numpy as np
import gmsh

gmsh.initialize()
print('a ready to use msh file is in the github repository if you need to test the code')
meshfilename = str(input("insert the name of the mesh file - i.e. Cubo_new.msh: "))
gmsh.open(meshfilename)
import openSTools as ot
ops.wipe()
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
gravityX =[accGravity*np.sin(inclination/180.0*pi)] # gravity acceleration in X direction
gravityY =0.0                                        # gravity acceleration in Y direction
gravityZ =[accGravity*np.cos(inclination/180.0*pi)]  # gravity acceleration in Z direction

ops.nDMaterial('PressureDependMultiYield02', 1, 3, rhoS, G1, B1, friction, 2.5, 80, 0.5, phaseTransform, 0.067, 0.23, 0.06, 0.27)

ot.mDefine()
ot.mFix()
ot.mGenFem20()
[colArea,dashpotCoeff,nodo_mesh]=ot.mDash()
nodeList=ot.mRec()

motionDT = 0.005
motionSteps = 2500

damp = 0.02
omega1 = 2 * np.pi * 0.2
omega2 = 2 * np.pi * 20
a0 = 2*damp*omega1*omega2/(omega1 + omega2)
a1 = 2*damp/(omega1 + omega2)
print(f"a_0 = {a0};  a_1 = {a1}")
vsMax = 250.0
duration = motionDT*motionSteps
minSize = 2
kTrial = minSize / (vsMax ** 0.5)
if motionDT <= kTrial:
    nSteps = motionSteps
    dT = motionDT
else:
    nSteps = int(mm.floor(duration / kTrial) + 1)
    dT = duration / nSteps
gamma = 1.5
gamma1=0.5
beta  = (1/4)*(gamma+0.5)**2
beta1 = 0.25
########################################################################
ot.mStage0(gamma1,beta1)
ops.updateMaterialStage('-material', 1, '-stage', 1)
ops.updateMaterialStage('-material', 2, '-stage', 1)
ot.chPerm()
ops.timeSeries('Constant',1)
ops.pattern('Plain',1,1,'-fact',1.0)
ops.reactions()
ot.App.subReacForce(ot.Model)
ot.mTieNodes()
ops.setTime(0.0)
ops.wipeAnalysis()
ops.remove('recorders')
recDT = 10*motionDT
ot.mRecDyn(recDT)
ops.model('basic', '-ndm', 3, '-ndf', 4)
colArea = 100
cFactor = colArea * dashpotCoeff
velocityFile = 'yerbaNSvelocity';
data_gm = np.loadtxt('yerbaNSvelocity.out')
ops.timeSeries('Path', 2, '-dt', motionDT, '-filePath', velocityFile +'.out', '-factor', cFactor)
ops.pattern('Plain', 10, 2)
ops.load(nodo_mesh, 1.0,0.0, 0.0)
print("Dynamic loading created...")
ops.constraints('Penalty', 1.0E16, 1.0E16)
ops.test('NormDispIncr', 1e-3, 100, 1)
ops.algorithm('KrylovNewton')
ops.numberer('RCM')
ops.system('ProfileSPD')
ops.integrator('Newmark', gamma, beta)
ops.rayleigh(a0, a1, 0.0, 0.0)
ops.analysis('Transient')
ok = ops.analyze(nSteps, dT)
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
