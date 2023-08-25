#######################################################################################################
#######################################################################################################
PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME PLEASE READE ME 
#######################################################################################################
#######################################################################################################
 
OPENSEES AUTOCOMP 1.1 
AUTHOR: GIANLUCA CAVALLO\nPOLITECNICO DI BARI
YEAR: 2023
EMAIL: gi.cav.2586@gmail.com
Please, cite the author if use any part of this code
 
#######################################################################################################
#######################################################################################################
 
 
THE AUTHOR IS NOT RESPONSABLE FOR ANY USE OF THE CODE, THE USER IS!
 
 
#######################################################################################################
################################ REMARKS AND TIPS     #################################################
#######################################################################################################
 
                 THIS IS AN ALPHA VERSION - CONSIDER THAT IN YOUR COMMENTS
 
The milestone codes followed are those in the opensees and openseespy documentation on 2d and 3d shaked columns
The file MASTER.py is only a rough example to test the code functionality and it will not lead to a result
The file MASTER is connected to the tool module "openSTools.py"
You have to execute the mfix function any times the number of the fixed surfaces, pay attention to the edges
The same if you want remove the fixies
Please contact me for some code bugs to correct
You have to install by pip: openseespy opensees gmsh gmsh2opensees numpy scipy time math os
Whit this code you could perform easily the analysis with every mesh you build with gmsh and 20-8 node up element
you should take care in the geo_material choice
Have fun
 
#######################################################################################################
#######################################################################################################
 
ATTENTION PLEASE: REMEMBER TO ADD THE 20-8 UPELEMENT TO gmsh2opensees PACKET OR THIS CODE WILL NOT WORK
 
#######################################################################################################
#######################################################################################################
 
