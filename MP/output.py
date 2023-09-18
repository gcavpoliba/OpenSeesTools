import os
import openseespy.opensees as ops
import numpy as nup
ops.wipe()
import math as mm
import time as tt
pid = ops.getPID()
np = ops.getNP()
ops.barrier()
ops.model("basicBuilder","-ndm",3,"-ndf",4)
ops.nDMaterial('PressureDependMultiYield02',1, 3, 1.8, 90000.0, 220000.0, 31.0, 2.5, 80, 0.5, 26.0, 0.067, 0.23, 0.06, 0.27)
ops.model("basicBuilder","-ndm",3,"-ndf",4)
if pid == 1:
    ops.node(1, 0.0, 0.0, 10.0)
if pid == 6:
    ops.node(2, 0.0, 0.0, 0.0)
if pid == 2:
    ops.node(3, 0.0, 10.0, 10.0)
if pid == 7:
    ops.node(4, 0.0, 10.0, 0.0)
if pid == 1:
    ops.node(5, 10.0, 0.0, 10.0)
if pid == 6:
    ops.node(6, 10.0, 0.0, 0.0)
if pid == 2:
    ops.node(7, 10.0, 10.0, 10.0)
if pid == 7:
    ops.node(8, 10.0, 10.0, 0.0)
if pid == 5:
    ops.node(9, 0.0, 0.0, 2.0)
if pid == 6:
    ops.node(9, 0.0, 0.0, 2.0)
if pid == 3:
    ops.node(10, 0.0, 0.0, 4.0)
if pid == 5:
    ops.node(10, 0.0, 0.0, 4.0)
if pid == 2:
    ops.node(11, 0.0, 0.0, 6.0)
if pid == 3:
    ops.node(11, 0.0, 0.0, 6.0)
if pid == 1:
    ops.node(12, 0.0, 0.0, 8.0)
if pid == 2:
    ops.node(12, 0.0, 0.0, 8.0)
if pid == 1:
    ops.node(13, 0.0, 2.0, 10.0)
if pid == 1:
    ops.node(14, 0.0, 4.0, 10.0)
if pid == 1:
    ops.node(15, 0.0, 6.0, 10.0)
if pid == 1:
    ops.node(16, 0.0, 8.0, 10.0)
if pid == 2:
    ops.node(16, 0.0, 8.0, 10.0)
if pid == 6:
    ops.node(17, 0.0, 10.0, 2.0)
if pid == 7:
    ops.node(17, 0.0, 10.0, 2.0)
if pid == 4:
    ops.node(18, 0.0, 10.0, 4.0)
if pid == 6:
    ops.node(18, 0.0, 10.0, 4.0)
if pid == 3:
    ops.node(19, 0.0, 10.0, 6.0)
if pid == 4:
    ops.node(19, 0.0, 10.0, 6.0)
if pid == 2:
    ops.node(20, 0.0, 10.0, 8.0)
if pid == 3:
    ops.node(20, 0.0, 10.0, 8.0)
if pid == 6:
    ops.node(21, 0.0, 2.0, 0.0)
if pid == 6:
    ops.node(22, 0.0, 4.0, 0.0)
if pid == 7:
    ops.node(22, 0.0, 4.0, 0.0)
if pid == 7:
    ops.node(23, 0.0, 6.0, 0.0)
if pid == 7:
    ops.node(24, 0.0, 8.0, 0.0)
if pid == 5:
    ops.node(25, 10.0, 0.0, 2.0)
if pid == 6:
    ops.node(25, 10.0, 0.0, 2.0)
if pid == 4:
    ops.node(26, 10.0, 0.0, 4.0)
if pid == 5:
    ops.node(26, 10.0, 0.0, 4.0)
if pid == 2:
    ops.node(27, 10.0, 0.0, 6.0)
if pid == 4:
    ops.node(27, 10.0, 0.0, 6.0)
if pid == 1:
    ops.node(28, 10.0, 0.0, 8.0)
if pid == 2:
    ops.node(28, 10.0, 0.0, 8.0)
if pid == 1:
    ops.node(29, 10.0, 2.0, 10.0)
if pid == 1:
    ops.node(30, 10.0, 4.0, 10.0)
if pid == 1:
    ops.node(31, 10.0, 6.0, 10.0)
if pid == 2:
    ops.node(31, 10.0, 6.0, 10.0)
if pid == 2:
    ops.node(32, 10.0, 8.0, 10.0)
if pid == 6:
    ops.node(33, 10.0, 10.0, 2.0)
if pid == 7:
    ops.node(33, 10.0, 10.0, 2.0)
if pid == 5:
    ops.node(34, 10.0, 10.0, 4.0)
if pid == 6:
    ops.node(34, 10.0, 10.0, 4.0)
if pid == 3:
    ops.node(35, 10.0, 10.0, 6.0)
if pid == 5:
    ops.node(35, 10.0, 10.0, 6.0)
if pid == 2:
    ops.node(36, 10.0, 10.0, 8.0)
if pid == 3:
    ops.node(36, 10.0, 10.0, 8.0)
if pid == 6:
    ops.node(37, 10.0, 2.0, 0.0)
if pid == 7:
    ops.node(37, 10.0, 2.0, 0.0)
if pid == 7:
    ops.node(38, 10.0, 4.0, 0.0)
if pid == 7:
    ops.node(39, 10.0, 6.0, 0.0)
if pid == 7:
    ops.node(40, 10.0, 8.0, 0.0)
if pid == 6:
    ops.node(41, 2.0, 0.0, 0.0)
if pid == 6:
    ops.node(42, 4.0, 0.0, 0.0)
if pid == 6:
    ops.node(43, 6.0, 0.0, 0.0)
if pid == 6:
    ops.node(44, 8.0, 0.0, 0.0)
if pid == 1:
    ops.node(45, 2.0, 0.0, 10.0)
if pid == 1:
    ops.node(46, 4.0, 0.0, 10.0)
if pid == 1:
    ops.node(47, 6.0, 0.0, 10.0)
if pid == 1:
    ops.node(48, 8.0, 0.0, 10.0)
if pid == 7:
    ops.node(49, 2.0, 10.0, 0.0)
if pid == 7:
    ops.node(50, 4.0, 10.0, 0.0)
if pid == 7:
    ops.node(51, 6.0, 10.0, 0.0)
if pid == 7:
    ops.node(52, 8.0, 10.0, 0.0)
if pid == 2:
    ops.node(53, 2.0, 10.0, 10.0)
if pid == 2:
    ops.node(54, 4.0, 10.0, 10.0)
if pid == 2:
    ops.node(55, 6.0, 10.0, 10.0)
if pid == 2:
    ops.node(56, 8.0, 10.0, 10.0)
if pid == 5:
    ops.node(57, 0.0, 2.0, 2.0)
if pid == 6:
    ops.node(57, 0.0, 2.0, 2.0)
if pid == 5:
    ops.node(58, 0.0, 3.999999999999999, 2.0)
if pid == 6:
    ops.node(58, 0.0, 3.999999999999999, 2.0)
if pid == 7:
    ops.node(58, 0.0, 3.999999999999999, 2.0)
if pid == 5:
    ops.node(59, 0.0, 6.0, 2.0)
if pid == 6:
    ops.node(59, 0.0, 6.0, 2.0)
if pid == 7:
    ops.node(59, 0.0, 6.0, 2.0)
if pid == 6:
    ops.node(60, 0.0, 7.999999999999998, 2.0)
if pid == 7:
    ops.node(60, 0.0, 7.999999999999998, 2.0)
if pid == 3:
    ops.node(61, 0.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(61, 0.0, 2.0, 3.999999999999999)
if pid == 5:
    ops.node(61, 0.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(62, 0.0, 4.0, 4.0)
if pid == 5:
    ops.node(62, 0.0, 4.0, 4.0)
if pid == 4:
    ops.node(63, 0.0, 6.0, 4.0)
if pid == 5:
    ops.node(63, 0.0, 6.0, 4.0)
if pid == 6:
    ops.node(63, 0.0, 6.0, 4.0)
if pid == 4:
    ops.node(64, 0.0, 8.0, 4.0)
if pid == 6:
    ops.node(64, 0.0, 8.0, 4.0)
if pid == 2:
    ops.node(65, 0.0, 2.0, 6.0)
if pid == 3:
    ops.node(65, 0.0, 2.0, 6.0)
if pid == 4:
    ops.node(65, 0.0, 2.0, 6.0)
if pid == 2:
    ops.node(66, 0.0, 4.0, 6.0)
if pid == 4:
    ops.node(66, 0.0, 4.0, 6.0)
if pid == 2:
    ops.node(67, 0.0, 6.0, 6.0)
if pid == 3:
    ops.node(67, 0.0, 6.0, 6.0)
if pid == 4:
    ops.node(67, 0.0, 6.0, 6.0)
if pid == 3:
    ops.node(68, 0.0, 8.0, 6.0)
if pid == 4:
    ops.node(68, 0.0, 8.0, 6.0)
if pid == 1:
    ops.node(69, 0.0, 2.0, 7.999999999999998)
if pid == 2:
    ops.node(69, 0.0, 2.0, 7.999999999999998)
if pid == 1:
    ops.node(70, 0.0, 4.0, 8.0)
if pid == 2:
    ops.node(70, 0.0, 4.0, 8.0)
if pid == 1:
    ops.node(71, 0.0, 6.0, 8.0)
if pid == 2:
    ops.node(71, 0.0, 6.0, 8.0)
if pid == 3:
    ops.node(71, 0.0, 6.0, 8.0)
if pid == 1:
    ops.node(72, 0.0, 8.0, 8.0)
if pid == 2:
    ops.node(72, 0.0, 8.0, 8.0)
if pid == 3:
    ops.node(72, 0.0, 8.0, 8.0)
if pid == 1:
    ops.node(73, 10.0, 2.0, 7.999999999999998)
if pid == 2:
    ops.node(73, 10.0, 2.0, 7.999999999999998)
if pid == 1:
    ops.node(74, 10.0, 3.999999999999999, 8.0)
if pid == 2:
    ops.node(74, 10.0, 3.999999999999999, 8.0)
if pid == 3:
    ops.node(74, 10.0, 3.999999999999999, 8.0)
if pid == 1:
    ops.node(75, 10.0, 6.0, 8.0)
if pid == 2:
    ops.node(75, 10.0, 6.0, 8.0)
if pid == 3:
    ops.node(75, 10.0, 6.0, 8.0)
if pid == 2:
    ops.node(76, 10.0, 7.999999999999998, 8.0)
if pid == 3:
    ops.node(76, 10.0, 7.999999999999998, 8.0)
if pid == 2:
    ops.node(77, 10.0, 2.0, 6.0)
if pid == 4:
    ops.node(77, 10.0, 2.0, 6.0)
if pid == 2:
    ops.node(78, 10.0, 4.0, 6.0)
if pid == 3:
    ops.node(78, 10.0, 4.0, 6.0)
if pid == 4:
    ops.node(78, 10.0, 4.0, 6.0)
if pid == 3:
    ops.node(79, 10.0, 6.0, 6.0)
if pid == 4:
    ops.node(79, 10.0, 6.0, 6.0)
if pid == 3:
    ops.node(80, 10.0, 8.0, 6.0)
if pid == 4:
    ops.node(80, 10.0, 8.0, 6.0)
if pid == 5:
    ops.node(80, 10.0, 8.0, 6.0)
if pid == 4:
    ops.node(81, 10.0, 2.0, 3.999999999999999)
if pid == 5:
    ops.node(81, 10.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(82, 10.0, 4.0, 4.0)
if pid == 5:
    ops.node(82, 10.0, 4.0, 4.0)
if pid == 4:
    ops.node(83, 10.0, 6.0, 4.0)
if pid == 5:
    ops.node(83, 10.0, 6.0, 4.0)
if pid == 6:
    ops.node(83, 10.0, 6.0, 4.0)
if pid == 4:
    ops.node(84, 10.0, 8.0, 4.0)
if pid == 5:
    ops.node(84, 10.0, 8.0, 4.0)
if pid == 6:
    ops.node(84, 10.0, 8.0, 4.0)
if pid == 5:
    ops.node(85, 10.0, 2.0, 2.0)
if pid == 6:
    ops.node(85, 10.0, 2.0, 2.0)
if pid == 7:
    ops.node(85, 10.0, 2.0, 2.0)
if pid == 5:
    ops.node(86, 10.0, 4.0, 2.0)
if pid == 7:
    ops.node(86, 10.0, 4.0, 2.0)
if pid == 5:
    ops.node(87, 10.0, 6.0, 2.0)
if pid == 6:
    ops.node(87, 10.0, 6.0, 2.0)
if pid == 7:
    ops.node(87, 10.0, 6.0, 2.0)
if pid == 6:
    ops.node(88, 10.0, 8.0, 2.0)
if pid == 7:
    ops.node(88, 10.0, 8.0, 2.0)
if pid == 5:
    ops.node(89, 2.0, 0.0, 2.0)
if pid == 6:
    ops.node(89, 2.0, 0.0, 2.0)
if pid == 3:
    ops.node(90, 2.0, 0.0, 3.999999999999999)
if pid == 5:
    ops.node(90, 2.0, 0.0, 3.999999999999999)
if pid == 2:
    ops.node(91, 2.0, 0.0, 6.0)
if pid == 3:
    ops.node(91, 2.0, 0.0, 6.0)
if pid == 1:
    ops.node(92, 2.0, 0.0, 7.999999999999998)
if pid == 2:
    ops.node(92, 2.0, 0.0, 7.999999999999998)
if pid == 5:
    ops.node(93, 3.999999999999999, 0.0, 2.0)
if pid == 6:
    ops.node(93, 3.999999999999999, 0.0, 2.0)
if pid == 3:
    ops.node(94, 4.0, 0.0, 4.0)
if pid == 5:
    ops.node(94, 4.0, 0.0, 4.0)
if pid == 2:
    ops.node(95, 4.0, 0.0, 6.0)
if pid == 3:
    ops.node(95, 4.0, 0.0, 6.0)
if pid == 1:
    ops.node(96, 4.0, 0.0, 8.0)
if pid == 2:
    ops.node(96, 4.0, 0.0, 8.0)
if pid == 5:
    ops.node(97, 6.0, 0.0, 2.0)
if pid == 6:
    ops.node(97, 6.0, 0.0, 2.0)
if pid == 3:
    ops.node(98, 6.0, 0.0, 4.0)
if pid == 5:
    ops.node(98, 6.0, 0.0, 4.0)
if pid == 2:
    ops.node(99, 6.0, 0.0, 6.0)
if pid == 3:
    ops.node(99, 6.0, 0.0, 6.0)
if pid == 1:
    ops.node(100, 6.0, 0.0, 8.0)
if pid == 2:
    ops.node(100, 6.0, 0.0, 8.0)
if pid == 5:
    ops.node(101, 7.999999999999998, 0.0, 2.0)
if pid == 6:
    ops.node(101, 7.999999999999998, 0.0, 2.0)
if pid == 3:
    ops.node(102, 8.0, 0.0, 4.0)
if pid == 4:
    ops.node(102, 8.0, 0.0, 4.0)
if pid == 5:
    ops.node(102, 8.0, 0.0, 4.0)
if pid == 2:
    ops.node(103, 8.0, 0.0, 6.0)
if pid == 3:
    ops.node(103, 8.0, 0.0, 6.0)
if pid == 4:
    ops.node(103, 8.0, 0.0, 6.0)
if pid == 1:
    ops.node(104, 8.0, 0.0, 8.0)
if pid == 2:
    ops.node(104, 8.0, 0.0, 8.0)
if pid == 6:
    ops.node(105, 7.999999999999998, 10.0, 2.0)
if pid == 7:
    ops.node(105, 7.999999999999998, 10.0, 2.0)
if pid == 5:
    ops.node(106, 8.0, 10.0, 3.999999999999999)
if pid == 6:
    ops.node(106, 8.0, 10.0, 3.999999999999999)
if pid == 3:
    ops.node(107, 8.0, 10.0, 6.0)
if pid == 5:
    ops.node(107, 8.0, 10.0, 6.0)
if pid == 2:
    ops.node(108, 8.0, 10.0, 7.999999999999998)
if pid == 3:
    ops.node(108, 8.0, 10.0, 7.999999999999998)
if pid == 6:
    ops.node(109, 6.0, 10.0, 2.0)
if pid == 7:
    ops.node(109, 6.0, 10.0, 2.0)
if pid == 5:
    ops.node(110, 6.0, 10.0, 4.0)
if pid == 6:
    ops.node(110, 6.0, 10.0, 4.0)
if pid == 3:
    ops.node(111, 6.0, 10.0, 6.0)
if pid == 5:
    ops.node(111, 6.0, 10.0, 6.0)
if pid == 2:
    ops.node(112, 6.0, 10.0, 8.0)
if pid == 3:
    ops.node(112, 6.0, 10.0, 8.0)
if pid == 6:
    ops.node(113, 3.999999999999999, 10.0, 2.0)
if pid == 7:
    ops.node(113, 3.999999999999999, 10.0, 2.0)
if pid == 4:
    ops.node(114, 4.0, 10.0, 4.0)
if pid == 5:
    ops.node(114, 4.0, 10.0, 4.0)
if pid == 6:
    ops.node(114, 4.0, 10.0, 4.0)
if pid == 3:
    ops.node(115, 4.0, 10.0, 6.0)
if pid == 4:
    ops.node(115, 4.0, 10.0, 6.0)
if pid == 5:
    ops.node(115, 4.0, 10.0, 6.0)
if pid == 2:
    ops.node(116, 4.0, 10.0, 8.0)
if pid == 3:
    ops.node(116, 4.0, 10.0, 8.0)
if pid == 6:
    ops.node(117, 2.0, 10.0, 2.0)
if pid == 7:
    ops.node(117, 2.0, 10.0, 2.0)
if pid == 4:
    ops.node(118, 2.0, 10.0, 4.0)
if pid == 6:
    ops.node(118, 2.0, 10.0, 4.0)
if pid == 3:
    ops.node(119, 2.0, 10.0, 6.0)
if pid == 4:
    ops.node(119, 2.0, 10.0, 6.0)
if pid == 2:
    ops.node(120, 2.0, 10.0, 8.0)
if pid == 3:
    ops.node(120, 2.0, 10.0, 8.0)
if pid == 6:
    ops.node(121, 2.0, 2.0, 0.0)
if pid == 6:
    ops.node(122, 3.999999999999999, 2.0, 0.0)
if pid == 6:
    ops.node(123, 6.0, 2.0, 0.0)
if pid == 7:
    ops.node(123, 6.0, 2.0, 0.0)
if pid == 6:
    ops.node(124, 7.999999999999998, 2.0, 0.0)
if pid == 7:
    ops.node(124, 7.999999999999998, 2.0, 0.0)
if pid == 6:
    ops.node(125, 2.0, 3.999999999999999, 0.0)
if pid == 7:
    ops.node(125, 2.0, 3.999999999999999, 0.0)
if pid == 6:
    ops.node(126, 4.0, 4.0, 0.0)
if pid == 7:
    ops.node(126, 4.0, 4.0, 0.0)
if pid == 6:
    ops.node(127, 6.0, 4.0, 0.0)
if pid == 7:
    ops.node(127, 6.0, 4.0, 0.0)
if pid == 7:
    ops.node(128, 8.0, 4.0, 0.0)
if pid == 7:
    ops.node(129, 2.0, 6.0, 0.0)
if pid == 7:
    ops.node(130, 4.0, 6.0, 0.0)
if pid == 7:
    ops.node(131, 6.0, 6.0, 0.0)
if pid == 7:
    ops.node(132, 8.0, 6.0, 0.0)
if pid == 7:
    ops.node(133, 2.0, 7.999999999999998, 0.0)
if pid == 7:
    ops.node(134, 4.0, 8.0, 0.0)
if pid == 7:
    ops.node(135, 6.0, 8.0, 0.0)
if pid == 7:
    ops.node(136, 8.0, 8.0, 0.0)
if pid == 1:
    ops.node(137, 2.0, 7.999999999999998, 10.0)
if pid == 2:
    ops.node(137, 2.0, 7.999999999999998, 10.0)
if pid == 1:
    ops.node(138, 3.999999999999999, 8.0, 10.0)
if pid == 2:
    ops.node(138, 3.999999999999999, 8.0, 10.0)
if pid == 1:
    ops.node(139, 6.0, 8.0, 10.0)
if pid == 2:
    ops.node(139, 6.0, 8.0, 10.0)
if pid == 2:
    ops.node(140, 7.999999999999998, 8.0, 10.0)
if pid == 1:
    ops.node(141, 2.0, 6.0, 10.0)
if pid == 1:
    ops.node(142, 4.0, 6.0, 10.0)
if pid == 1:
    ops.node(143, 6.0, 6.0, 10.0)
if pid == 2:
    ops.node(143, 6.0, 6.0, 10.0)
if pid == 1:
    ops.node(144, 8.0, 6.0, 10.0)
if pid == 2:
    ops.node(144, 8.0, 6.0, 10.0)
if pid == 1:
    ops.node(145, 2.0, 3.999999999999999, 10.0)
if pid == 1:
    ops.node(146, 4.0, 4.0, 10.0)
if pid == 1:
    ops.node(147, 6.0, 4.0, 10.0)
if pid == 1:
    ops.node(148, 8.0, 4.0, 10.0)
if pid == 1:
    ops.node(149, 2.0, 2.0, 10.0)
if pid == 1:
    ops.node(150, 4.0, 2.0, 10.0)
if pid == 1:
    ops.node(151, 6.0, 2.0, 10.0)
if pid == 1:
    ops.node(152, 8.0, 2.0, 10.0)
if pid == 1:
    ops.node(153, 2.0, 2.0, 7.999999999999996)
if pid == 2:
    ops.node(153, 2.0, 2.0, 7.999999999999996)
if pid == 1:
    ops.node(154, 4.0, 2.0, 7.999999999999996)
if pid == 2:
    ops.node(154, 4.0, 2.0, 7.999999999999996)
if pid == 1:
    ops.node(155, 6.0, 2.0, 7.999999999999996)
if pid == 2:
    ops.node(155, 6.0, 2.0, 7.999999999999996)
if pid == 1:
    ops.node(156, 8.0, 1.999999999999999, 7.999999999999996)
if pid == 2:
    ops.node(156, 8.0, 1.999999999999999, 7.999999999999996)
if pid == 1:
    ops.node(157, 2.0, 4.0, 8.0)
if pid == 2:
    ops.node(157, 2.0, 4.0, 8.0)
if pid == 3:
    ops.node(157, 2.0, 4.0, 8.0)
if pid == 1:
    ops.node(158, 4.0, 4.0, 8.0)
if pid == 2:
    ops.node(158, 4.0, 4.0, 8.0)
if pid == 3:
    ops.node(158, 4.0, 4.0, 8.0)
if pid == 1:
    ops.node(159, 6.0, 4.0, 8.0)
if pid == 2:
    ops.node(159, 6.0, 4.0, 8.0)
if pid == 3:
    ops.node(159, 6.0, 4.0, 8.0)
if pid == 1:
    ops.node(160, 8.0, 4.0, 8.000000000000004)
if pid == 2:
    ops.node(160, 8.0, 4.0, 8.000000000000004)
if pid == 3:
    ops.node(160, 8.0, 4.0, 8.000000000000004)
if pid == 1:
    ops.node(161, 2.0, 5.999999999999996, 8.0)
if pid == 2:
    ops.node(161, 2.0, 5.999999999999996, 8.0)
if pid == 3:
    ops.node(161, 2.0, 5.999999999999996, 8.0)
if pid == 1:
    ops.node(162, 4.0, 6.0, 8.0)
if pid == 3:
    ops.node(162, 4.0, 6.0, 8.0)
if pid == 1:
    ops.node(163, 5.999999999999996, 6.0, 8.0)
if pid == 2:
    ops.node(163, 5.999999999999996, 6.0, 8.0)
if pid == 3:
    ops.node(163, 5.999999999999996, 6.0, 8.0)
if pid == 1:
    ops.node(164, 8.0, 5.999999999999996, 8.000000000000004)
if pid == 2:
    ops.node(164, 8.0, 5.999999999999996, 8.000000000000004)
if pid == 3:
    ops.node(164, 8.0, 5.999999999999996, 8.000000000000004)
if pid == 1:
    ops.node(165, 1.999999999999999, 8.0, 8.0)
if pid == 2:
    ops.node(165, 1.999999999999999, 8.0, 8.0)
if pid == 3:
    ops.node(165, 1.999999999999999, 8.0, 8.0)
if pid == 1:
    ops.node(166, 4.0, 8.0, 8.0)
if pid == 2:
    ops.node(166, 4.0, 8.0, 8.0)
if pid == 3:
    ops.node(166, 4.0, 8.0, 8.0)
if pid == 1:
    ops.node(167, 6.0, 8.0, 8.0)
if pid == 2:
    ops.node(167, 6.0, 8.0, 8.0)
if pid == 3:
    ops.node(167, 6.0, 8.0, 8.0)
if pid == 2:
    ops.node(168, 8.0, 8.0, 7.999999999999996)
if pid == 3:
    ops.node(168, 8.0, 8.0, 7.999999999999996)
if pid == 2:
    ops.node(169, 2.0, 2.0, 6.000000000000004)
if pid == 3:
    ops.node(169, 2.0, 2.0, 6.000000000000004)
if pid == 4:
    ops.node(169, 2.0, 2.0, 6.000000000000004)
if pid == 2:
    ops.node(170, 4.0, 2.0, 6.0)
if pid == 3:
    ops.node(170, 4.0, 2.0, 6.0)
if pid == 4:
    ops.node(170, 4.0, 2.0, 6.0)
if pid == 2:
    ops.node(171, 6.0, 2.0, 6.0)
if pid == 3:
    ops.node(171, 6.0, 2.0, 6.0)
if pid == 4:
    ops.node(171, 6.0, 2.0, 6.0)
if pid == 2:
    ops.node(172, 8.0, 2.0, 6.0)
if pid == 3:
    ops.node(172, 8.0, 2.0, 6.0)
if pid == 4:
    ops.node(172, 8.0, 2.0, 6.0)
if pid == 2:
    ops.node(173, 1.999999999999999, 3.999999999999998, 5.999999999999996)
if pid == 3:
    ops.node(173, 1.999999999999999, 3.999999999999998, 5.999999999999996)
if pid == 4:
    ops.node(173, 1.999999999999999, 3.999999999999998, 5.999999999999996)
if pid == 2:
    ops.node(174, 4.0, 4.0, 6.0)
if pid == 3:
    ops.node(174, 4.0, 4.0, 6.0)
if pid == 4:
    ops.node(174, 4.0, 4.0, 6.0)
if pid == 2:
    ops.node(175, 6.0, 4.0, 6.0)
if pid == 3:
    ops.node(175, 6.0, 4.0, 6.0)
if pid == 4:
    ops.node(175, 6.0, 4.0, 6.0)
if pid == 2:
    ops.node(176, 8.0, 4.0, 6.0)
if pid == 3:
    ops.node(176, 8.0, 4.0, 6.0)
if pid == 4:
    ops.node(176, 8.0, 4.0, 6.0)
if pid == 2:
    ops.node(177, 2.0, 6.0, 6.0)
if pid == 3:
    ops.node(177, 2.0, 6.0, 6.0)
if pid == 4:
    ops.node(177, 2.0, 6.0, 6.0)
if pid == 3:
    ops.node(178, 4.0, 6.0, 6.0)
if pid == 4:
    ops.node(178, 4.0, 6.0, 6.0)
if pid == 3:
    ops.node(179, 6.0, 6.0, 6.0)
if pid == 4:
    ops.node(179, 6.0, 6.0, 6.0)
if pid == 3:
    ops.node(180, 8.0, 6.0, 6.0)
if pid == 4:
    ops.node(180, 8.0, 6.0, 6.0)
if pid == 3:
    ops.node(181, 1.999999999999998, 7.999999999999996, 5.999999999999996)
if pid == 4:
    ops.node(181, 1.999999999999998, 7.999999999999996, 5.999999999999996)
if pid == 3:
    ops.node(182, 3.999999999999998, 8.0, 6.0)
if pid == 4:
    ops.node(182, 3.999999999999998, 8.0, 6.0)
if pid == 5:
    ops.node(182, 3.999999999999998, 8.0, 6.0)
if pid == 3:
    ops.node(183, 6.0, 8.0, 6.0)
if pid == 4:
    ops.node(183, 6.0, 8.0, 6.0)
if pid == 5:
    ops.node(183, 6.0, 8.0, 6.0)
if pid == 3:
    ops.node(184, 7.999999999999996, 8.0, 6.0)
if pid == 4:
    ops.node(184, 7.999999999999996, 8.0, 6.0)
if pid == 5:
    ops.node(184, 7.999999999999996, 8.0, 6.0)
if pid == 3:
    ops.node(185, 2.0, 2.0, 3.999999999999996)
if pid == 4:
    ops.node(185, 2.0, 2.0, 3.999999999999996)
if pid == 5:
    ops.node(185, 2.0, 2.0, 3.999999999999996)
if pid == 3:
    ops.node(186, 4.0, 2.0, 3.999999999999998)
if pid == 4:
    ops.node(186, 4.0, 2.0, 3.999999999999998)
if pid == 5:
    ops.node(186, 4.0, 2.0, 3.999999999999998)
if pid == 3:
    ops.node(187, 6.0, 2.0, 4.0)
if pid == 4:
    ops.node(187, 6.0, 2.0, 4.0)
if pid == 5:
    ops.node(187, 6.0, 2.0, 4.0)
if pid == 3:
    ops.node(188, 8.0, 2.0, 3.999999999999998)
if pid == 4:
    ops.node(188, 8.0, 2.0, 3.999999999999998)
if pid == 5:
    ops.node(188, 8.0, 2.0, 3.999999999999998)
if pid == 4:
    ops.node(189, 2.0, 4.0, 4.0)
if pid == 5:
    ops.node(189, 2.0, 4.0, 4.0)
if pid == 4:
    ops.node(190, 4.0, 4.0, 4.0)
if pid == 5:
    ops.node(190, 4.0, 4.0, 4.0)
if pid == 4:
    ops.node(191, 6.0, 4.0, 4.0)
if pid == 5:
    ops.node(191, 6.0, 4.0, 4.0)
if pid == 4:
    ops.node(192, 8.0, 4.0, 4.0)
if pid == 5:
    ops.node(192, 8.0, 4.0, 4.0)
if pid == 4:
    ops.node(193, 2.0, 6.0, 4.0)
if pid == 5:
    ops.node(193, 2.0, 6.0, 4.0)
if pid == 6:
    ops.node(193, 2.0, 6.0, 4.0)
if pid == 4:
    ops.node(194, 4.0, 6.0, 4.0)
if pid == 5:
    ops.node(194, 4.0, 6.0, 4.0)
if pid == 6:
    ops.node(194, 4.0, 6.0, 4.0)
if pid == 4:
    ops.node(195, 6.0, 6.0, 4.0)
if pid == 5:
    ops.node(195, 6.0, 6.0, 4.0)
if pid == 6:
    ops.node(195, 6.0, 6.0, 4.0)
if pid == 4:
    ops.node(196, 8.0, 6.0, 4.0)
if pid == 5:
    ops.node(196, 8.0, 6.0, 4.0)
if pid == 6:
    ops.node(196, 8.0, 6.0, 4.0)
if pid == 4:
    ops.node(197, 2.0, 8.0, 4.0)
if pid == 6:
    ops.node(197, 2.0, 8.0, 4.0)
if pid == 4:
    ops.node(198, 4.0, 8.0, 4.0)
if pid == 5:
    ops.node(198, 4.0, 8.0, 4.0)
if pid == 6:
    ops.node(198, 4.0, 8.0, 4.0)
if pid == 4:
    ops.node(199, 6.0, 8.0, 4.0)
if pid == 5:
    ops.node(199, 6.0, 8.0, 4.0)
if pid == 6:
    ops.node(199, 6.0, 8.0, 4.0)
if pid == 4:
    ops.node(200, 8.0, 8.0, 3.999999999999998)
if pid == 5:
    ops.node(200, 8.0, 8.0, 3.999999999999998)
if pid == 6:
    ops.node(200, 8.0, 8.0, 3.999999999999998)
if pid == 5:
    ops.node(201, 2.0, 1.999999999999999, 1.999999999999999)
if pid == 6:
    ops.node(201, 2.0, 1.999999999999999, 1.999999999999999)
if pid == 5:
    ops.node(202, 3.999999999999996, 2.0, 1.999999999999999)
if pid == 6:
    ops.node(202, 3.999999999999996, 2.0, 1.999999999999999)
if pid == 5:
    ops.node(203, 6.0, 2.0, 2.0)
if pid == 6:
    ops.node(203, 6.0, 2.0, 2.0)
if pid == 7:
    ops.node(203, 6.0, 2.0, 2.0)
if pid == 5:
    ops.node(204, 7.999999999999993, 2.0, 2.0)
if pid == 6:
    ops.node(204, 7.999999999999993, 2.0, 2.0)
if pid == 7:
    ops.node(204, 7.999999999999993, 2.0, 2.0)
if pid == 5:
    ops.node(205, 2.0, 3.999999999999996, 2.0)
if pid == 6:
    ops.node(205, 2.0, 3.999999999999996, 2.0)
if pid == 7:
    ops.node(205, 2.0, 3.999999999999996, 2.0)
if pid == 5:
    ops.node(206, 3.999999999999998, 4.0, 1.999999999999999)
if pid == 6:
    ops.node(206, 3.999999999999998, 4.0, 1.999999999999999)
if pid == 7:
    ops.node(206, 3.999999999999998, 4.0, 1.999999999999999)
if pid == 5:
    ops.node(207, 6.0, 4.0, 2.0)
if pid == 6:
    ops.node(207, 6.0, 4.0, 2.0)
if pid == 7:
    ops.node(207, 6.0, 4.0, 2.0)
if pid == 5:
    ops.node(208, 7.999999999999996, 4.0, 1.999999999999999)
if pid == 7:
    ops.node(208, 7.999999999999996, 4.0, 1.999999999999999)
if pid == 5:
    ops.node(209, 2.0, 6.0, 2.0)
if pid == 6:
    ops.node(209, 2.0, 6.0, 2.0)
if pid == 7:
    ops.node(209, 2.0, 6.0, 2.0)
if pid == 5:
    ops.node(210, 3.999999999999998, 6.0, 2.0)
if pid == 6:
    ops.node(210, 3.999999999999998, 6.0, 2.0)
if pid == 7:
    ops.node(210, 3.999999999999998, 6.0, 2.0)
if pid == 5:
    ops.node(211, 6.0, 6.0, 2.0)
if pid == 6:
    ops.node(211, 6.0, 6.0, 2.0)
if pid == 7:
    ops.node(211, 6.0, 6.0, 2.0)
if pid == 5:
    ops.node(212, 7.999999999999996, 6.0, 1.999999999999998)
if pid == 6:
    ops.node(212, 7.999999999999996, 6.0, 1.999999999999998)
if pid == 7:
    ops.node(212, 7.999999999999996, 6.0, 1.999999999999998)
if pid == 6:
    ops.node(213, 2.0, 7.999999999999993, 2.0)
if pid == 7:
    ops.node(213, 2.0, 7.999999999999993, 2.0)
if pid == 6:
    ops.node(214, 3.999999999999996, 8.0, 1.999999999999999)
if pid == 7:
    ops.node(214, 3.999999999999996, 8.0, 1.999999999999999)
if pid == 6:
    ops.node(215, 6.0, 8.0, 2.000000000000002)
if pid == 7:
    ops.node(215, 6.0, 8.0, 2.000000000000002)
if pid == 6:
    ops.node(216, 7.999999999999993, 8.0, 1.999999999999999)
if pid == 7:
    ops.node(216, 7.999999999999993, 8.0, 1.999999999999999)
ops.model("basicBuilder","-ndm",3,"-ndf",3)
if pid == 6:
    ops.node(217, 0.0, 0.0, 1.0)
if pid == 5:
    ops.node(218, 0.0, 0.0, 3.0)
if pid == 3:
    ops.node(219, 0.0, 0.0, 5.0)
if pid == 2:
    ops.node(220, 0.0, 0.0, 7.0)
if pid == 1:
    ops.node(221, 0.0, 0.0, 9.0)
if pid == 1:
    ops.node(222, 0.0, 1.0, 10.0)
if pid == 1:
    ops.node(223, 0.0, 3.0, 10.0)
if pid == 1:
    ops.node(224, 0.0, 5.0, 10.0)
if pid == 1:
    ops.node(225, 0.0, 7.0, 10.0)
if pid == 2:
    ops.node(226, 0.0, 9.0, 10.0)
if pid == 7:
    ops.node(227, 0.0, 10.0, 1.0)
if pid == 6:
    ops.node(228, 0.0, 10.0, 3.0)
if pid == 4:
    ops.node(229, 0.0, 10.0, 5.0)
if pid == 3:
    ops.node(230, 0.0, 10.0, 7.0)
if pid == 2:
    ops.node(231, 0.0, 10.0, 9.0)
if pid == 6:
    ops.node(232, 0.0, 1.0, 0.0)
if pid == 6:
    ops.node(233, 0.0, 3.0, 0.0)
if pid == 7:
    ops.node(234, 0.0, 5.0, 0.0)
if pid == 7:
    ops.node(235, 0.0, 7.0, 0.0)
if pid == 7:
    ops.node(236, 0.0, 9.0, 0.0)
if pid == 6:
    ops.node(237, 10.0, 0.0, 1.0)
if pid == 5:
    ops.node(238, 10.0, 0.0, 3.0)
if pid == 4:
    ops.node(239, 10.0, 0.0, 5.0)
if pid == 2:
    ops.node(240, 10.0, 0.0, 7.0)
if pid == 1:
    ops.node(241, 10.0, 0.0, 9.0)
if pid == 1:
    ops.node(242, 10.0, 1.0, 10.0)
if pid == 1:
    ops.node(243, 10.0, 3.0, 10.0)
if pid == 1:
    ops.node(244, 10.0, 5.0, 10.0)
if pid == 2:
    ops.node(245, 10.0, 7.0, 10.0)
if pid == 2:
    ops.node(246, 10.0, 9.0, 10.0)
if pid == 7:
    ops.node(247, 10.0, 10.0, 1.0)
if pid == 6:
    ops.node(248, 10.0, 10.0, 3.0)
if pid == 5:
    ops.node(249, 10.0, 10.0, 5.0)
if pid == 3:
    ops.node(250, 10.0, 10.0, 7.0)
if pid == 2:
    ops.node(251, 10.0, 10.0, 9.0)
if pid == 6:
    ops.node(252, 10.0, 1.0, 0.0)
if pid == 7:
    ops.node(253, 10.0, 3.0, 0.0)
if pid == 7:
    ops.node(254, 10.0, 5.0, 0.0)
if pid == 7:
    ops.node(255, 10.0, 7.0, 0.0)
if pid == 7:
    ops.node(256, 10.0, 9.0, 0.0)
if pid == 6:
    ops.node(257, 1.0, 0.0, 0.0)
if pid == 6:
    ops.node(258, 3.0, 0.0, 0.0)
if pid == 6:
    ops.node(259, 5.0, 0.0, 0.0)
if pid == 6:
    ops.node(260, 7.0, 0.0, 0.0)
if pid == 6:
    ops.node(261, 9.0, 0.0, 0.0)
if pid == 1:
    ops.node(262, 1.0, 0.0, 10.0)
if pid == 1:
    ops.node(263, 3.0, 0.0, 10.0)
if pid == 1:
    ops.node(264, 5.0, 0.0, 10.0)
if pid == 1:
    ops.node(265, 7.0, 0.0, 10.0)
if pid == 1:
    ops.node(266, 9.0, 0.0, 10.0)
if pid == 7:
    ops.node(267, 1.0, 10.0, 0.0)
if pid == 7:
    ops.node(268, 3.0, 10.0, 0.0)
if pid == 7:
    ops.node(269, 5.0, 10.0, 0.0)
if pid == 7:
    ops.node(270, 7.0, 10.0, 0.0)
if pid == 7:
    ops.node(271, 9.0, 10.0, 0.0)
if pid == 2:
    ops.node(272, 1.0, 10.0, 10.0)
if pid == 2:
    ops.node(273, 3.0, 10.0, 10.0)
if pid == 2:
    ops.node(274, 5.0, 10.0, 10.0)
if pid == 2:
    ops.node(275, 7.0, 10.0, 10.0)
if pid == 2:
    ops.node(276, 9.0, 10.0, 10.0)
if pid == 5:
    ops.node(277, 0.0, 0.9999999999999998, 2.0)
if pid == 6:
    ops.node(277, 0.0, 0.9999999999999998, 2.0)
if pid == 6:
    ops.node(278, 0.0, 2.0, 0.9999999999999998)
if pid == 5:
    ops.node(279, 0.0, 2.999999999999999, 2.0)
if pid == 6:
    ops.node(279, 0.0, 2.999999999999999, 2.0)
if pid == 6:
    ops.node(280, 0.0, 4.0, 1.0)
if pid == 7:
    ops.node(280, 0.0, 4.0, 1.0)
if pid == 5:
    ops.node(281, 0.0, 5.0, 2.0)
if pid == 7:
    ops.node(281, 0.0, 5.0, 2.0)
if pid == 7:
    ops.node(282, 0.0, 6.0, 1.0)
if pid == 6:
    ops.node(283, 0.0, 6.999999999999999, 2.0)
if pid == 7:
    ops.node(283, 0.0, 6.999999999999999, 2.0)
if pid == 7:
    ops.node(284, 0.0, 7.999999999999999, 1.0)
if pid == 6:
    ops.node(285, 0.0, 9.0, 2.0)
if pid == 7:
    ops.node(285, 0.0, 9.0, 2.0)
if pid == 3:
    ops.node(286, 0.0, 1.0, 4.0)
if pid == 5:
    ops.node(286, 0.0, 1.0, 4.0)
if pid == 5:
    ops.node(287, 0.0, 2.0, 2.999999999999999)
if pid == 4:
    ops.node(288, 0.0, 3.0, 4.0)
if pid == 5:
    ops.node(288, 0.0, 3.0, 4.0)
if pid == 5:
    ops.node(289, 0.0, 4.0, 3.0)
if pid == 4:
    ops.node(290, 0.0, 5.0, 4.0)
if pid == 5:
    ops.node(290, 0.0, 5.0, 4.0)
if pid == 5:
    ops.node(291, 0.0, 6.0, 3.0)
if pid == 6:
    ops.node(291, 0.0, 6.0, 3.0)
if pid == 4:
    ops.node(292, 0.0, 7.0, 4.0)
if pid == 6:
    ops.node(292, 0.0, 7.0, 4.0)
if pid == 6:
    ops.node(293, 0.0, 7.999999999999999, 3.0)
if pid == 4:
    ops.node(294, 0.0, 9.0, 4.0)
if pid == 6:
    ops.node(294, 0.0, 9.0, 4.0)
if pid == 2:
    ops.node(295, 0.0, 1.0, 6.0)
if pid == 3:
    ops.node(295, 0.0, 1.0, 6.0)
if pid == 3:
    ops.node(296, 0.0, 2.0, 5.0)
if pid == 4:
    ops.node(296, 0.0, 2.0, 5.0)
if pid == 2:
    ops.node(297, 0.0, 3.0, 6.0)
if pid == 4:
    ops.node(297, 0.0, 3.0, 6.0)
if pid == 4:
    ops.node(298, 0.0, 4.0, 5.0)
if pid == 2:
    ops.node(299, 0.0, 5.0, 6.0)
if pid == 4:
    ops.node(299, 0.0, 5.0, 6.0)
if pid == 4:
    ops.node(300, 0.0, 6.0, 5.0)
if pid == 3:
    ops.node(301, 0.0, 7.0, 6.0)
if pid == 4:
    ops.node(301, 0.0, 7.0, 6.0)
if pid == 4:
    ops.node(302, 0.0, 8.0, 5.0)
if pid == 3:
    ops.node(303, 0.0, 9.0, 6.0)
if pid == 4:
    ops.node(303, 0.0, 9.0, 6.0)
if pid == 1:
    ops.node(304, 0.0, 1.0, 7.999999999999999)
if pid == 2:
    ops.node(304, 0.0, 1.0, 7.999999999999999)
if pid == 2:
    ops.node(305, 0.0, 2.0, 6.999999999999999)
if pid == 1:
    ops.node(306, 0.0, 3.0, 7.999999999999999)
if pid == 2:
    ops.node(306, 0.0, 3.0, 7.999999999999999)
if pid == 2:
    ops.node(307, 0.0, 4.0, 7.0)
if pid == 1:
    ops.node(308, 0.0, 5.0, 8.0)
if pid == 2:
    ops.node(308, 0.0, 5.0, 8.0)
if pid == 2:
    ops.node(309, 0.0, 6.0, 7.0)
if pid == 3:
    ops.node(309, 0.0, 6.0, 7.0)
if pid == 1:
    ops.node(310, 0.0, 7.0, 8.0)
if pid == 3:
    ops.node(310, 0.0, 7.0, 8.0)
if pid == 3:
    ops.node(311, 0.0, 8.0, 7.0)
if pid == 2:
    ops.node(312, 0.0, 9.0, 8.0)
if pid == 3:
    ops.node(312, 0.0, 9.0, 8.0)
if pid == 1:
    ops.node(313, 0.0, 2.0, 9.0)
if pid == 1:
    ops.node(314, 0.0, 4.0, 9.0)
if pid == 1:
    ops.node(315, 0.0, 6.0, 9.0)
if pid == 1:
    ops.node(316, 0.0, 8.0, 9.0)
if pid == 2:
    ops.node(316, 0.0, 8.0, 9.0)
if pid == 1:
    ops.node(317, 10.0, 0.9999999999999998, 7.999999999999999)
if pid == 2:
    ops.node(317, 10.0, 0.9999999999999998, 7.999999999999999)
if pid == 1:
    ops.node(318, 10.0, 2.0, 9.0)
if pid == 1:
    ops.node(319, 10.0, 2.999999999999999, 7.999999999999999)
if pid == 2:
    ops.node(319, 10.0, 2.999999999999999, 7.999999999999999)
if pid == 1:
    ops.node(320, 10.0, 4.0, 9.0)
if pid == 1:
    ops.node(321, 10.0, 5.0, 8.0)
if pid == 3:
    ops.node(321, 10.0, 5.0, 8.0)
if pid == 1:
    ops.node(322, 10.0, 6.0, 9.0)
if pid == 2:
    ops.node(322, 10.0, 6.0, 9.0)
if pid == 2:
    ops.node(323, 10.0, 6.999999999999999, 8.0)
if pid == 3:
    ops.node(323, 10.0, 6.999999999999999, 8.0)
if pid == 2:
    ops.node(324, 10.0, 7.999999999999999, 9.0)
if pid == 2:
    ops.node(325, 10.0, 9.0, 8.0)
if pid == 3:
    ops.node(325, 10.0, 9.0, 8.0)
if pid == 2:
    ops.node(326, 10.0, 1.0, 6.0)
if pid == 4:
    ops.node(326, 10.0, 1.0, 6.0)
if pid == 2:
    ops.node(327, 10.0, 2.0, 6.999999999999999)
if pid == 2:
    ops.node(328, 10.0, 3.0, 6.0)
if pid == 4:
    ops.node(328, 10.0, 3.0, 6.0)
if pid == 2:
    ops.node(329, 10.0, 4.0, 7.0)
if pid == 3:
    ops.node(329, 10.0, 4.0, 7.0)
if pid == 3:
    ops.node(330, 10.0, 5.0, 6.0)
if pid == 4:
    ops.node(330, 10.0, 5.0, 6.0)
if pid == 3:
    ops.node(331, 10.0, 6.0, 7.0)
if pid == 3:
    ops.node(332, 10.0, 7.0, 6.0)
if pid == 4:
    ops.node(332, 10.0, 7.0, 6.0)
if pid == 3:
    ops.node(333, 10.0, 7.999999999999999, 7.0)
if pid == 3:
    ops.node(334, 10.0, 9.0, 6.0)
if pid == 5:
    ops.node(334, 10.0, 9.0, 6.0)
if pid == 4:
    ops.node(335, 10.0, 1.0, 4.0)
if pid == 5:
    ops.node(335, 10.0, 1.0, 4.0)
if pid == 4:
    ops.node(336, 10.0, 2.0, 5.0)
if pid == 4:
    ops.node(337, 10.0, 3.0, 4.0)
if pid == 5:
    ops.node(337, 10.0, 3.0, 4.0)
if pid == 4:
    ops.node(338, 10.0, 4.0, 5.0)
if pid == 4:
    ops.node(339, 10.0, 5.0, 4.0)
if pid == 5:
    ops.node(339, 10.0, 5.0, 4.0)
if pid == 4:
    ops.node(340, 10.0, 6.0, 5.0)
if pid == 4:
    ops.node(341, 10.0, 7.0, 4.0)
if pid == 6:
    ops.node(341, 10.0, 7.0, 4.0)
if pid == 4:
    ops.node(342, 10.0, 8.0, 5.0)
if pid == 5:
    ops.node(342, 10.0, 8.0, 5.0)
if pid == 5:
    ops.node(343, 10.0, 9.0, 4.0)
if pid == 6:
    ops.node(343, 10.0, 9.0, 4.0)
if pid == 5:
    ops.node(344, 10.0, 1.0, 2.0)
if pid == 6:
    ops.node(344, 10.0, 1.0, 2.0)
if pid == 5:
    ops.node(345, 10.0, 2.0, 3.0)
if pid == 5:
    ops.node(346, 10.0, 3.0, 2.0)
if pid == 7:
    ops.node(346, 10.0, 3.0, 2.0)
if pid == 5:
    ops.node(347, 10.0, 4.0, 3.0)
if pid == 5:
    ops.node(348, 10.0, 5.0, 2.0)
if pid == 7:
    ops.node(348, 10.0, 5.0, 2.0)
if pid == 5:
    ops.node(349, 10.0, 6.0, 3.0)
if pid == 6:
    ops.node(349, 10.0, 6.0, 3.0)
if pid == 6:
    ops.node(350, 10.0, 7.0, 2.0)
if pid == 7:
    ops.node(350, 10.0, 7.0, 2.0)
if pid == 6:
    ops.node(351, 10.0, 8.0, 3.0)
if pid == 6:
    ops.node(352, 10.0, 9.0, 2.0)
if pid == 7:
    ops.node(352, 10.0, 9.0, 2.0)
if pid == 6:
    ops.node(353, 10.0, 2.0, 1.0)
if pid == 7:
    ops.node(353, 10.0, 2.0, 1.0)
if pid == 7:
    ops.node(354, 10.0, 4.0, 1.0)
if pid == 7:
    ops.node(355, 10.0, 6.0, 1.0)
if pid == 7:
    ops.node(356, 10.0, 8.0, 1.0)
if pid == 6:
    ops.node(357, 2.0, 0.0, 0.9999999999999998)
if pid == 5:
    ops.node(358, 0.9999999999999998, 0.0, 2.0)
if pid == 6:
    ops.node(358, 0.9999999999999998, 0.0, 2.0)
if pid == 5:
    ops.node(359, 2.0, 0.0, 2.999999999999999)
if pid == 3:
    ops.node(360, 1.0, 0.0, 4.0)
if pid == 5:
    ops.node(360, 1.0, 0.0, 4.0)
if pid == 3:
    ops.node(361, 2.0, 0.0, 5.0)
if pid == 2:
    ops.node(362, 1.0, 0.0, 6.0)
if pid == 3:
    ops.node(362, 1.0, 0.0, 6.0)
if pid == 2:
    ops.node(363, 2.0, 0.0, 6.999999999999999)
if pid == 1:
    ops.node(364, 1.0, 0.0, 7.999999999999999)
if pid == 2:
    ops.node(364, 1.0, 0.0, 7.999999999999999)
if pid == 1:
    ops.node(365, 2.0, 0.0, 9.0)
if pid == 6:
    ops.node(366, 4.0, 0.0, 1.0)
if pid == 5:
    ops.node(367, 2.999999999999999, 0.0, 2.0)
if pid == 6:
    ops.node(367, 2.999999999999999, 0.0, 2.0)
if pid == 5:
    ops.node(368, 4.0, 0.0, 3.0)
if pid == 3:
    ops.node(369, 3.0, 0.0, 4.0)
if pid == 5:
    ops.node(369, 3.0, 0.0, 4.0)
if pid == 3:
    ops.node(370, 4.0, 0.0, 5.0)
if pid == 2:
    ops.node(371, 3.0, 0.0, 6.0)
if pid == 3:
    ops.node(371, 3.0, 0.0, 6.0)
if pid == 2:
    ops.node(372, 4.0, 0.0, 7.0)
if pid == 1:
    ops.node(373, 3.0, 0.0, 7.999999999999999)
if pid == 2:
    ops.node(373, 3.0, 0.0, 7.999999999999999)
if pid == 1:
    ops.node(374, 4.0, 0.0, 9.0)
if pid == 6:
    ops.node(375, 6.0, 0.0, 1.0)
if pid == 5:
    ops.node(376, 5.0, 0.0, 2.0)
if pid == 6:
    ops.node(376, 5.0, 0.0, 2.0)
if pid == 5:
    ops.node(377, 6.0, 0.0, 3.0)
if pid == 3:
    ops.node(378, 5.0, 0.0, 4.0)
if pid == 5:
    ops.node(378, 5.0, 0.0, 4.0)
if pid == 3:
    ops.node(379, 6.0, 0.0, 5.0)
if pid == 2:
    ops.node(380, 5.0, 0.0, 6.0)
if pid == 3:
    ops.node(380, 5.0, 0.0, 6.0)
if pid == 2:
    ops.node(381, 6.0, 0.0, 7.0)
if pid == 1:
    ops.node(382, 5.0, 0.0, 8.0)
if pid == 2:
    ops.node(382, 5.0, 0.0, 8.0)
if pid == 1:
    ops.node(383, 6.0, 0.0, 9.0)
if pid == 6:
    ops.node(384, 7.999999999999999, 0.0, 1.0)
if pid == 5:
    ops.node(385, 6.999999999999999, 0.0, 2.0)
if pid == 6:
    ops.node(385, 6.999999999999999, 0.0, 2.0)
if pid == 5:
    ops.node(386, 7.999999999999999, 0.0, 3.0)
if pid == 3:
    ops.node(387, 7.0, 0.0, 4.0)
if pid == 5:
    ops.node(387, 7.0, 0.0, 4.0)
if pid == 3:
    ops.node(388, 8.0, 0.0, 5.0)
if pid == 4:
    ops.node(388, 8.0, 0.0, 5.0)
if pid == 2:
    ops.node(389, 7.0, 0.0, 6.0)
if pid == 3:
    ops.node(389, 7.0, 0.0, 6.0)
if pid == 2:
    ops.node(390, 8.0, 0.0, 7.0)
if pid == 1:
    ops.node(391, 7.0, 0.0, 8.0)
if pid == 2:
    ops.node(391, 7.0, 0.0, 8.0)
if pid == 1:
    ops.node(392, 8.0, 0.0, 9.0)
if pid == 5:
    ops.node(393, 9.0, 0.0, 2.0)
if pid == 6:
    ops.node(393, 9.0, 0.0, 2.0)
if pid == 4:
    ops.node(394, 9.0, 0.0, 4.0)
if pid == 5:
    ops.node(394, 9.0, 0.0, 4.0)
if pid == 2:
    ops.node(395, 9.0, 0.0, 6.0)
if pid == 4:
    ops.node(395, 9.0, 0.0, 6.0)
if pid == 1:
    ops.node(396, 9.0, 0.0, 8.0)
if pid == 2:
    ops.node(396, 9.0, 0.0, 8.0)
if pid == 7:
    ops.node(397, 7.999999999999999, 10.0, 0.9999999999999998)
if pid == 6:
    ops.node(398, 9.0, 10.0, 2.0)
if pid == 7:
    ops.node(398, 9.0, 10.0, 2.0)
if pid == 6:
    ops.node(399, 7.999999999999999, 10.0, 2.999999999999999)
if pid == 5:
    ops.node(400, 9.0, 10.0, 4.0)
if pid == 6:
    ops.node(400, 9.0, 10.0, 4.0)
if pid == 5:
    ops.node(401, 8.0, 10.0, 5.0)
if pid == 3:
    ops.node(402, 9.0, 10.0, 6.0)
if pid == 5:
    ops.node(402, 9.0, 10.0, 6.0)
if pid == 3:
    ops.node(403, 8.0, 10.0, 6.999999999999999)
if pid == 2:
    ops.node(404, 9.0, 10.0, 7.999999999999999)
if pid == 3:
    ops.node(404, 9.0, 10.0, 7.999999999999999)
if pid == 2:
    ops.node(405, 8.0, 10.0, 9.0)
if pid == 7:
    ops.node(406, 6.0, 10.0, 1.0)
if pid == 6:
    ops.node(407, 6.999999999999999, 10.0, 2.0)
if pid == 7:
    ops.node(407, 6.999999999999999, 10.0, 2.0)
if pid == 6:
    ops.node(408, 6.0, 10.0, 3.0)
if pid == 5:
    ops.node(409, 7.0, 10.0, 4.0)
if pid == 6:
    ops.node(409, 7.0, 10.0, 4.0)
if pid == 5:
    ops.node(410, 6.0, 10.0, 5.0)
if pid == 3:
    ops.node(411, 7.0, 10.0, 6.0)
if pid == 5:
    ops.node(411, 7.0, 10.0, 6.0)
if pid == 3:
    ops.node(412, 6.0, 10.0, 7.0)
if pid == 2:
    ops.node(413, 7.0, 10.0, 7.999999999999999)
if pid == 3:
    ops.node(413, 7.0, 10.0, 7.999999999999999)
if pid == 2:
    ops.node(414, 6.0, 10.0, 9.0)
if pid == 7:
    ops.node(415, 4.0, 10.0, 1.0)
if pid == 6:
    ops.node(416, 5.0, 10.0, 2.0)
if pid == 7:
    ops.node(416, 5.0, 10.0, 2.0)
if pid == 6:
    ops.node(417, 4.0, 10.0, 3.0)
if pid == 5:
    ops.node(418, 5.0, 10.0, 4.0)
if pid == 6:
    ops.node(418, 5.0, 10.0, 4.0)
if pid == 4:
    ops.node(419, 4.0, 10.0, 5.0)
if pid == 5:
    ops.node(419, 4.0, 10.0, 5.0)
if pid == 3:
    ops.node(420, 5.0, 10.0, 6.0)
if pid == 5:
    ops.node(420, 5.0, 10.0, 6.0)
if pid == 3:
    ops.node(421, 4.0, 10.0, 7.0)
if pid == 2:
    ops.node(422, 5.0, 10.0, 8.0)
if pid == 3:
    ops.node(422, 5.0, 10.0, 8.0)
if pid == 2:
    ops.node(423, 4.0, 10.0, 9.0)
if pid == 7:
    ops.node(424, 2.0, 10.0, 1.0)
if pid == 6:
    ops.node(425, 3.0, 10.0, 2.0)
if pid == 7:
    ops.node(425, 3.0, 10.0, 2.0)
if pid == 6:
    ops.node(426, 2.0, 10.0, 3.0)
if pid == 4:
    ops.node(427, 3.0, 10.0, 4.0)
if pid == 6:
    ops.node(427, 3.0, 10.0, 4.0)
if pid == 4:
    ops.node(428, 2.0, 10.0, 5.0)
if pid == 3:
    ops.node(429, 3.0, 10.0, 6.0)
if pid == 4:
    ops.node(429, 3.0, 10.0, 6.0)
if pid == 3:
    ops.node(430, 2.0, 10.0, 7.0)
if pid == 2:
    ops.node(431, 3.0, 10.0, 8.0)
if pid == 3:
    ops.node(431, 3.0, 10.0, 8.0)
if pid == 2:
    ops.node(432, 2.0, 10.0, 9.0)
if pid == 6:
    ops.node(433, 1.0, 10.0, 2.0)
if pid == 7:
    ops.node(433, 1.0, 10.0, 2.0)
if pid == 4:
    ops.node(434, 1.0, 10.0, 4.0)
if pid == 6:
    ops.node(434, 1.0, 10.0, 4.0)
if pid == 3:
    ops.node(435, 1.0, 10.0, 6.0)
if pid == 4:
    ops.node(435, 1.0, 10.0, 6.0)
if pid == 2:
    ops.node(436, 1.0, 10.0, 8.0)
if pid == 3:
    ops.node(436, 1.0, 10.0, 8.0)
if pid == 6:
    ops.node(437, 0.9999999999999998, 2.0, 0.0)
if pid == 6:
    ops.node(438, 2.0, 0.9999999999999998, 0.0)
if pid == 6:
    ops.node(439, 2.999999999999999, 2.0, 0.0)
if pid == 6:
    ops.node(440, 4.0, 1.0, 0.0)
if pid == 6:
    ops.node(441, 5.0, 2.0, 0.0)
if pid == 6:
    ops.node(442, 6.0, 1.0, 0.0)
if pid == 6:
    ops.node(443, 6.999999999999999, 2.0, 0.0)
if pid == 7:
    ops.node(443, 6.999999999999999, 2.0, 0.0)
if pid == 6:
    ops.node(444, 7.999999999999999, 1.0, 0.0)
if pid == 6:
    ops.node(445, 9.0, 2.0, 0.0)
if pid == 7:
    ops.node(445, 9.0, 2.0, 0.0)
if pid == 6:
    ops.node(446, 1.0, 4.0, 0.0)
if pid == 7:
    ops.node(446, 1.0, 4.0, 0.0)
if pid == 6:
    ops.node(447, 2.0, 2.999999999999999, 0.0)
if pid == 6:
    ops.node(448, 3.0, 4.0, 0.0)
if pid == 7:
    ops.node(448, 3.0, 4.0, 0.0)
if pid == 6:
    ops.node(449, 4.0, 3.0, 0.0)
if pid == 6:
    ops.node(450, 5.0, 4.0, 0.0)
if pid == 7:
    ops.node(450, 5.0, 4.0, 0.0)
if pid == 6:
    ops.node(451, 6.0, 3.0, 0.0)
if pid == 7:
    ops.node(451, 6.0, 3.0, 0.0)
if pid == 7:
    ops.node(452, 7.0, 4.0, 0.0)
if pid == 7:
    ops.node(453, 7.999999999999999, 3.0, 0.0)
if pid == 7:
    ops.node(454, 9.0, 4.0, 0.0)
if pid == 7:
    ops.node(455, 1.0, 6.0, 0.0)
if pid == 7:
    ops.node(456, 2.0, 5.0, 0.0)
if pid == 7:
    ops.node(457, 3.0, 6.0, 0.0)
if pid == 7:
    ops.node(458, 4.0, 5.0, 0.0)
if pid == 7:
    ops.node(459, 5.0, 6.0, 0.0)
if pid == 7:
    ops.node(460, 6.0, 5.0, 0.0)
if pid == 7:
    ops.node(461, 7.0, 6.0, 0.0)
if pid == 7:
    ops.node(462, 8.0, 5.0, 0.0)
if pid == 7:
    ops.node(463, 9.0, 6.0, 0.0)
if pid == 7:
    ops.node(464, 1.0, 7.999999999999999, 0.0)
if pid == 7:
    ops.node(465, 2.0, 6.999999999999999, 0.0)
if pid == 7:
    ops.node(466, 3.0, 7.999999999999999, 0.0)
if pid == 7:
    ops.node(467, 4.0, 7.0, 0.0)
if pid == 7:
    ops.node(468, 5.0, 8.0, 0.0)
if pid == 7:
    ops.node(469, 6.0, 7.0, 0.0)
if pid == 7:
    ops.node(470, 7.0, 8.0, 0.0)
if pid == 7:
    ops.node(471, 8.0, 7.0, 0.0)
if pid == 7:
    ops.node(472, 9.0, 8.0, 0.0)
if pid == 7:
    ops.node(473, 2.0, 9.0, 0.0)
if pid == 7:
    ops.node(474, 4.0, 9.0, 0.0)
if pid == 7:
    ops.node(475, 6.0, 9.0, 0.0)
if pid == 7:
    ops.node(476, 8.0, 9.0, 0.0)
if pid == 1:
    ops.node(477, 0.9999999999999998, 7.999999999999999, 10.0)
if pid == 2:
    ops.node(477, 0.9999999999999998, 7.999999999999999, 10.0)
if pid == 2:
    ops.node(478, 2.0, 9.0, 10.0)
if pid == 1:
    ops.node(479, 2.999999999999999, 7.999999999999999, 10.0)
if pid == 2:
    ops.node(479, 2.999999999999999, 7.999999999999999, 10.0)
if pid == 2:
    ops.node(480, 4.0, 9.0, 10.0)
if pid == 1:
    ops.node(481, 5.0, 8.0, 10.0)
if pid == 2:
    ops.node(481, 5.0, 8.0, 10.0)
if pid == 2:
    ops.node(482, 6.0, 9.0, 10.0)
if pid == 2:
    ops.node(483, 6.999999999999999, 8.0, 10.0)
if pid == 2:
    ops.node(484, 7.999999999999999, 9.0, 10.0)
if pid == 2:
    ops.node(485, 9.0, 8.0, 10.0)
if pid == 1:
    ops.node(486, 1.0, 6.0, 10.0)
if pid == 1:
    ops.node(487, 2.0, 6.999999999999999, 10.0)
if pid == 1:
    ops.node(488, 3.0, 6.0, 10.0)
if pid == 1:
    ops.node(489, 4.0, 7.0, 10.0)
if pid == 1:
    ops.node(490, 5.0, 6.0, 10.0)
if pid == 1:
    ops.node(491, 6.0, 7.0, 10.0)
if pid == 2:
    ops.node(491, 6.0, 7.0, 10.0)
if pid == 1:
    ops.node(492, 7.0, 6.0, 10.0)
if pid == 2:
    ops.node(492, 7.0, 6.0, 10.0)
if pid == 2:
    ops.node(493, 7.999999999999999, 7.0, 10.0)
if pid == 1:
    ops.node(494, 9.0, 6.0, 10.0)
if pid == 2:
    ops.node(494, 9.0, 6.0, 10.0)
if pid == 1:
    ops.node(495, 1.0, 4.0, 10.0)
if pid == 1:
    ops.node(496, 2.0, 5.0, 10.0)
if pid == 1:
    ops.node(497, 3.0, 4.0, 10.0)
if pid == 1:
    ops.node(498, 4.0, 5.0, 10.0)
if pid == 1:
    ops.node(499, 5.0, 4.0, 10.0)
if pid == 1:
    ops.node(500, 6.0, 5.0, 10.0)
if pid == 1:
    ops.node(501, 7.0, 4.0, 10.0)
if pid == 1:
    ops.node(502, 8.0, 5.0, 10.0)
if pid == 1:
    ops.node(503, 9.0, 4.0, 10.0)
if pid == 1:
    ops.node(504, 1.0, 2.0, 10.0)
if pid == 1:
    ops.node(505, 2.0, 3.0, 10.0)
if pid == 1:
    ops.node(506, 3.0, 2.0, 10.0)
if pid == 1:
    ops.node(507, 4.0, 3.0, 10.0)
if pid == 1:
    ops.node(508, 5.0, 2.0, 10.0)
if pid == 1:
    ops.node(509, 6.0, 3.0, 10.0)
if pid == 1:
    ops.node(510, 7.0, 2.0, 10.0)
if pid == 1:
    ops.node(511, 8.0, 3.0, 10.0)
if pid == 1:
    ops.node(512, 9.0, 2.0, 10.0)
if pid == 1:
    ops.node(513, 2.0, 1.0, 10.0)
if pid == 1:
    ops.node(514, 4.0, 1.0, 10.0)
if pid == 1:
    ops.node(515, 6.0, 1.0, 10.0)
if pid == 1:
    ops.node(516, 8.0, 1.0, 10.0)
if pid == 1:
    ops.node(517, 2.0, 2.0, 8.999999999999998)
if pid == 1:
    ops.node(518, 2.0, 1.0, 7.999999999999997)
if pid == 2:
    ops.node(518, 2.0, 1.0, 7.999999999999997)
if pid == 1:
    ops.node(519, 1.0, 2.0, 7.999999999999997)
if pid == 2:
    ops.node(519, 1.0, 2.0, 7.999999999999997)
if pid == 1:
    ops.node(520, 4.0, 2.0, 8.999999999999998)
if pid == 1:
    ops.node(521, 4.0, 1.0, 7.999999999999998)
if pid == 2:
    ops.node(521, 4.0, 1.0, 7.999999999999998)
if pid == 1:
    ops.node(522, 3.0, 2.0, 7.999999999999996)
if pid == 2:
    ops.node(522, 3.0, 2.0, 7.999999999999996)
if pid == 1:
    ops.node(523, 6.0, 2.0, 8.999999999999998)
if pid == 1:
    ops.node(524, 6.0, 1.0, 7.999999999999998)
if pid == 2:
    ops.node(524, 6.0, 1.0, 7.999999999999998)
if pid == 1:
    ops.node(525, 5.0, 2.0, 7.999999999999996)
if pid == 2:
    ops.node(525, 5.0, 2.0, 7.999999999999996)
if pid == 1:
    ops.node(526, 8.0, 2.0, 8.999999999999998)
if pid == 1:
    ops.node(527, 8.0, 0.9999999999999996, 7.999999999999998)
if pid == 2:
    ops.node(527, 8.0, 0.9999999999999996, 7.999999999999998)
if pid == 1:
    ops.node(528, 7.0, 2.0, 7.999999999999996)
if pid == 2:
    ops.node(528, 7.0, 2.0, 7.999999999999996)
if pid == 1:
    ops.node(529, 9.0, 1.999999999999999, 7.999999999999997)
if pid == 2:
    ops.node(529, 9.0, 1.999999999999999, 7.999999999999997)
if pid == 1:
    ops.node(530, 2.0, 4.0, 9.0)
if pid == 1:
    ops.node(531, 2.0, 3.0, 7.999999999999998)
if pid == 2:
    ops.node(531, 2.0, 3.0, 7.999999999999998)
if pid == 1:
    ops.node(532, 1.0, 4.0, 8.0)
if pid == 2:
    ops.node(532, 1.0, 4.0, 8.0)
if pid == 1:
    ops.node(533, 4.0, 4.0, 9.0)
if pid == 1:
    ops.node(534, 4.0, 3.0, 7.999999999999998)
if pid == 2:
    ops.node(534, 4.0, 3.0, 7.999999999999998)
if pid == 1:
    ops.node(535, 3.0, 4.0, 8.0)
if pid == 2:
    ops.node(535, 3.0, 4.0, 8.0)
if pid == 3:
    ops.node(535, 3.0, 4.0, 8.0)
if pid == 1:
    ops.node(536, 6.0, 4.0, 9.0)
if pid == 1:
    ops.node(537, 6.0, 3.0, 7.999999999999998)
if pid == 2:
    ops.node(537, 6.0, 3.0, 7.999999999999998)
if pid == 1:
    ops.node(538, 5.0, 4.0, 8.0)
if pid == 2:
    ops.node(538, 5.0, 4.0, 8.0)
if pid == 3:
    ops.node(538, 5.0, 4.0, 8.0)
if pid == 1:
    ops.node(539, 8.0, 4.0, 9.000000000000002)
if pid == 1:
    ops.node(540, 8.0, 3.0, 8.0)
if pid == 2:
    ops.node(540, 8.0, 3.0, 8.0)
if pid == 1:
    ops.node(541, 7.0, 4.0, 8.000000000000002)
if pid == 2:
    ops.node(541, 7.0, 4.0, 8.000000000000002)
if pid == 3:
    ops.node(541, 7.0, 4.0, 8.000000000000002)
if pid == 1:
    ops.node(542, 9.0, 4.0, 8.000000000000002)
if pid == 2:
    ops.node(542, 9.0, 4.0, 8.000000000000002)
if pid == 3:
    ops.node(542, 9.0, 4.0, 8.000000000000002)
if pid == 1:
    ops.node(543, 2.0, 5.999999999999998, 9.0)
if pid == 1:
    ops.node(544, 2.0, 4.999999999999998, 8.0)
if pid == 2:
    ops.node(544, 2.0, 4.999999999999998, 8.0)
if pid == 3:
    ops.node(544, 2.0, 4.999999999999998, 8.0)
if pid == 1:
    ops.node(545, 1.0, 5.999999999999998, 8.0)
if pid == 2:
    ops.node(545, 1.0, 5.999999999999998, 8.0)
if pid == 3:
    ops.node(545, 1.0, 5.999999999999998, 8.0)
if pid == 1:
    ops.node(546, 4.0, 6.0, 9.0)
if pid == 1:
    ops.node(547, 4.0, 5.0, 8.0)
if pid == 3:
    ops.node(547, 4.0, 5.0, 8.0)
if pid == 1:
    ops.node(548, 3.0, 5.999999999999998, 8.0)
if pid == 3:
    ops.node(548, 3.0, 5.999999999999998, 8.0)
if pid == 1:
    ops.node(549, 5.999999999999998, 6.0, 9.0)
if pid == 2:
    ops.node(549, 5.999999999999998, 6.0, 9.0)
if pid == 1:
    ops.node(550, 5.999999999999998, 5.0, 8.0)
if pid == 3:
    ops.node(550, 5.999999999999998, 5.0, 8.0)
if pid == 1:
    ops.node(551, 4.999999999999998, 6.0, 8.0)
if pid == 3:
    ops.node(551, 4.999999999999998, 6.0, 8.0)
if pid == 1:
    ops.node(552, 8.0, 5.999999999999998, 9.000000000000002)
if pid == 2:
    ops.node(552, 8.0, 5.999999999999998, 9.000000000000002)
if pid == 1:
    ops.node(553, 8.0, 4.999999999999998, 8.000000000000004)
if pid == 3:
    ops.node(553, 8.0, 4.999999999999998, 8.000000000000004)
if pid == 1:
    ops.node(554, 6.999999999999998, 5.999999999999998, 8.000000000000002)
if pid == 2:
    ops.node(554, 6.999999999999998, 5.999999999999998, 8.000000000000002)
if pid == 3:
    ops.node(554, 6.999999999999998, 5.999999999999998, 8.000000000000002)
if pid == 1:
    ops.node(555, 9.0, 5.999999999999998, 8.000000000000002)
if pid == 2:
    ops.node(555, 9.0, 5.999999999999998, 8.000000000000002)
if pid == 3:
    ops.node(555, 9.0, 5.999999999999998, 8.000000000000002)
if pid == 1:
    ops.node(556, 1.999999999999999, 7.999999999999999, 9.0)
if pid == 2:
    ops.node(556, 1.999999999999999, 7.999999999999999, 9.0)
if pid == 1:
    ops.node(557, 2.0, 6.999999999999998, 8.0)
if pid == 3:
    ops.node(557, 2.0, 6.999999999999998, 8.0)
if pid == 1:
    ops.node(558, 0.9999999999999996, 8.0, 8.0)
if pid == 2:
    ops.node(558, 0.9999999999999996, 8.0, 8.0)
if pid == 3:
    ops.node(558, 0.9999999999999996, 8.0, 8.0)
if pid == 1:
    ops.node(559, 4.0, 8.0, 9.0)
if pid == 2:
    ops.node(559, 4.0, 8.0, 9.0)
if pid == 1:
    ops.node(560, 4.0, 7.0, 8.0)
if pid == 3:
    ops.node(560, 4.0, 7.0, 8.0)
if pid == 1:
    ops.node(561, 3.0, 8.0, 8.0)
if pid == 2:
    ops.node(561, 3.0, 8.0, 8.0)
if pid == 3:
    ops.node(561, 3.0, 8.0, 8.0)
if pid == 1:
    ops.node(562, 6.0, 8.0, 9.0)
if pid == 2:
    ops.node(562, 6.0, 8.0, 9.0)
if pid == 1:
    ops.node(563, 5.999999999999998, 7.0, 8.0)
if pid == 2:
    ops.node(563, 5.999999999999998, 7.0, 8.0)
if pid == 3:
    ops.node(563, 5.999999999999998, 7.0, 8.0)
if pid == 1:
    ops.node(564, 5.0, 8.0, 8.0)
if pid == 2:
    ops.node(564, 5.0, 8.0, 8.0)
if pid == 3:
    ops.node(564, 5.0, 8.0, 8.0)
if pid == 2:
    ops.node(565, 7.999999999999999, 8.0, 8.999999999999998)
if pid == 2:
    ops.node(566, 8.0, 6.999999999999998, 8.0)
if pid == 3:
    ops.node(566, 8.0, 6.999999999999998, 8.0)
if pid == 2:
    ops.node(567, 7.0, 8.0, 7.999999999999998)
if pid == 3:
    ops.node(567, 7.0, 8.0, 7.999999999999998)
if pid == 2:
    ops.node(568, 9.0, 7.999999999999999, 7.999999999999998)
if pid == 3:
    ops.node(568, 9.0, 7.999999999999999, 7.999999999999998)
if pid == 2:
    ops.node(569, 2.0, 9.0, 8.0)
if pid == 3:
    ops.node(569, 2.0, 9.0, 8.0)
if pid == 2:
    ops.node(570, 4.0, 9.0, 8.0)
if pid == 3:
    ops.node(570, 4.0, 9.0, 8.0)
if pid == 2:
    ops.node(571, 6.0, 9.0, 8.0)
if pid == 3:
    ops.node(571, 6.0, 9.0, 8.0)
if pid == 2:
    ops.node(572, 8.0, 9.0, 7.999999999999997)
if pid == 3:
    ops.node(572, 8.0, 9.0, 7.999999999999997)
if pid == 2:
    ops.node(573, 2.0, 2.0, 7.0)
if pid == 2:
    ops.node(574, 2.0, 1.0, 6.000000000000002)
if pid == 3:
    ops.node(574, 2.0, 1.0, 6.000000000000002)
if pid == 2:
    ops.node(575, 1.0, 2.0, 6.000000000000002)
if pid == 3:
    ops.node(575, 1.0, 2.0, 6.000000000000002)
if pid == 4:
    ops.node(575, 1.0, 2.0, 6.000000000000002)
if pid == 2:
    ops.node(576, 4.0, 2.0, 6.999999999999998)
if pid == 2:
    ops.node(577, 4.0, 1.0, 6.0)
if pid == 3:
    ops.node(577, 4.0, 1.0, 6.0)
if pid == 2:
    ops.node(578, 3.0, 2.0, 6.000000000000002)
if pid == 3:
    ops.node(578, 3.0, 2.0, 6.000000000000002)
if pid == 4:
    ops.node(578, 3.0, 2.0, 6.000000000000002)
if pid == 2:
    ops.node(579, 6.0, 2.0, 6.999999999999998)
if pid == 2:
    ops.node(580, 6.0, 1.0, 6.0)
if pid == 3:
    ops.node(580, 6.0, 1.0, 6.0)
if pid == 2:
    ops.node(581, 5.0, 2.0, 6.0)
if pid == 3:
    ops.node(581, 5.0, 2.0, 6.0)
if pid == 4:
    ops.node(581, 5.0, 2.0, 6.0)
if pid == 2:
    ops.node(582, 8.0, 2.0, 6.999999999999998)
if pid == 2:
    ops.node(583, 8.0, 1.0, 6.0)
if pid == 3:
    ops.node(583, 8.0, 1.0, 6.0)
if pid == 4:
    ops.node(583, 8.0, 1.0, 6.0)
if pid == 2:
    ops.node(584, 7.0, 2.0, 6.0)
if pid == 3:
    ops.node(584, 7.0, 2.0, 6.0)
if pid == 4:
    ops.node(584, 7.0, 2.0, 6.0)
if pid == 2:
    ops.node(585, 9.0, 2.0, 6.0)
if pid == 4:
    ops.node(585, 9.0, 2.0, 6.0)
if pid == 2:
    ops.node(586, 2.0, 3.999999999999999, 6.999999999999998)
if pid == 3:
    ops.node(586, 2.0, 3.999999999999999, 6.999999999999998)
if pid == 2:
    ops.node(587, 2.0, 2.999999999999999, 6.0)
if pid == 4:
    ops.node(587, 2.0, 2.999999999999999, 6.0)
if pid == 2:
    ops.node(588, 0.9999999999999996, 3.999999999999999, 5.999999999999998)
if pid == 4:
    ops.node(588, 0.9999999999999996, 3.999999999999999, 5.999999999999998)
if pid == 2:
    ops.node(589, 4.0, 4.0, 7.0)
if pid == 3:
    ops.node(589, 4.0, 4.0, 7.0)
if pid == 2:
    ops.node(590, 4.0, 3.0, 6.0)
if pid == 4:
    ops.node(590, 4.0, 3.0, 6.0)
if pid == 2:
    ops.node(591, 3.0, 3.999999999999999, 5.999999999999998)
if pid == 3:
    ops.node(591, 3.0, 3.999999999999999, 5.999999999999998)
if pid == 4:
    ops.node(591, 3.0, 3.999999999999999, 5.999999999999998)
if pid == 2:
    ops.node(592, 6.0, 4.0, 7.0)
if pid == 3:
    ops.node(592, 6.0, 4.0, 7.0)
if pid == 2:
    ops.node(593, 6.0, 3.0, 6.0)
if pid == 4:
    ops.node(593, 6.0, 3.0, 6.0)
if pid == 2:
    ops.node(594, 5.0, 4.0, 6.0)
if pid == 3:
    ops.node(594, 5.0, 4.0, 6.0)
if pid == 4:
    ops.node(594, 5.0, 4.0, 6.0)
if pid == 2:
    ops.node(595, 8.0, 4.0, 7.000000000000002)
if pid == 3:
    ops.node(595, 8.0, 4.0, 7.000000000000002)
if pid == 2:
    ops.node(596, 8.0, 3.0, 6.0)
if pid == 4:
    ops.node(596, 8.0, 3.0, 6.0)
if pid == 2:
    ops.node(597, 7.0, 4.0, 6.0)
if pid == 3:
    ops.node(597, 7.0, 4.0, 6.0)
if pid == 4:
    ops.node(597, 7.0, 4.0, 6.0)
if pid == 2:
    ops.node(598, 9.0, 4.0, 6.0)
if pid == 3:
    ops.node(598, 9.0, 4.0, 6.0)
if pid == 4:
    ops.node(598, 9.0, 4.0, 6.0)
if pid == 2:
    ops.node(599, 2.0, 5.999999999999998, 7.0)
if pid == 3:
    ops.node(599, 2.0, 5.999999999999998, 7.0)
if pid == 2:
    ops.node(600, 2.0, 4.999999999999999, 5.999999999999998)
if pid == 3:
    ops.node(600, 2.0, 4.999999999999999, 5.999999999999998)
if pid == 4:
    ops.node(600, 2.0, 4.999999999999999, 5.999999999999998)
if pid == 2:
    ops.node(601, 1.0, 6.0, 6.0)
if pid == 3:
    ops.node(601, 1.0, 6.0, 6.0)
if pid == 4:
    ops.node(601, 1.0, 6.0, 6.0)
if pid == 3:
    ops.node(602, 4.0, 6.0, 7.0)
if pid == 3:
    ops.node(603, 4.0, 5.0, 6.0)
if pid == 4:
    ops.node(603, 4.0, 5.0, 6.0)
if pid == 3:
    ops.node(604, 3.0, 6.0, 6.0)
if pid == 4:
    ops.node(604, 3.0, 6.0, 6.0)
if pid == 3:
    ops.node(605, 5.999999999999998, 6.0, 7.0)
if pid == 3:
    ops.node(606, 6.0, 5.0, 6.0)
if pid == 4:
    ops.node(606, 6.0, 5.0, 6.0)
if pid == 3:
    ops.node(607, 5.0, 6.0, 6.0)
if pid == 4:
    ops.node(607, 5.0, 6.0, 6.0)
if pid == 3:
    ops.node(608, 8.0, 5.999999999999998, 7.000000000000002)
if pid == 3:
    ops.node(609, 8.0, 5.0, 6.0)
if pid == 4:
    ops.node(609, 8.0, 5.0, 6.0)
if pid == 3:
    ops.node(610, 7.0, 6.0, 6.0)
if pid == 4:
    ops.node(610, 7.0, 6.0, 6.0)
if pid == 3:
    ops.node(611, 9.0, 6.0, 6.0)
if pid == 4:
    ops.node(611, 9.0, 6.0, 6.0)
if pid == 3:
    ops.node(612, 1.999999999999999, 7.999999999999998, 6.999999999999998)
if pid == 3:
    ops.node(613, 1.999999999999999, 6.999999999999998, 5.999999999999998)
if pid == 4:
    ops.node(613, 1.999999999999999, 6.999999999999998, 5.999999999999998)
if pid == 3:
    ops.node(614, 0.9999999999999991, 7.999999999999998, 5.999999999999998)
if pid == 4:
    ops.node(614, 0.9999999999999991, 7.999999999999998, 5.999999999999998)
if pid == 3:
    ops.node(615, 3.999999999999999, 8.0, 7.0)
if pid == 3:
    ops.node(616, 3.999999999999999, 7.0, 6.0)
if pid == 4:
    ops.node(616, 3.999999999999999, 7.0, 6.0)
if pid == 3:
    ops.node(617, 2.999999999999998, 7.999999999999998, 5.999999999999998)
if pid == 4:
    ops.node(617, 2.999999999999998, 7.999999999999998, 5.999999999999998)
if pid == 3:
    ops.node(618, 6.0, 8.0, 7.0)
if pid == 3:
    ops.node(619, 6.0, 7.0, 6.0)
if pid == 4:
    ops.node(619, 6.0, 7.0, 6.0)
if pid == 3:
    ops.node(620, 4.999999999999999, 8.0, 6.0)
if pid == 4:
    ops.node(620, 4.999999999999999, 8.0, 6.0)
if pid == 5:
    ops.node(620, 4.999999999999999, 8.0, 6.0)
if pid == 3:
    ops.node(621, 7.999999999999998, 8.0, 6.999999999999998)
if pid == 3:
    ops.node(622, 7.999999999999998, 7.0, 6.0)
if pid == 4:
    ops.node(622, 7.999999999999998, 7.0, 6.0)
if pid == 3:
    ops.node(623, 6.999999999999998, 8.0, 6.0)
if pid == 4:
    ops.node(623, 6.999999999999998, 8.0, 6.0)
if pid == 5:
    ops.node(623, 6.999999999999998, 8.0, 6.0)
if pid == 3:
    ops.node(624, 8.999999999999998, 8.0, 6.0)
if pid == 4:
    ops.node(624, 8.999999999999998, 8.0, 6.0)
if pid == 5:
    ops.node(624, 8.999999999999998, 8.0, 6.0)
if pid == 3:
    ops.node(625, 1.999999999999999, 8.999999999999998, 5.999999999999998)
if pid == 4:
    ops.node(625, 1.999999999999999, 8.999999999999998, 5.999999999999998)
if pid == 3:
    ops.node(626, 3.999999999999999, 9.0, 6.0)
if pid == 4:
    ops.node(626, 3.999999999999999, 9.0, 6.0)
if pid == 5:
    ops.node(626, 3.999999999999999, 9.0, 6.0)
if pid == 3:
    ops.node(627, 6.0, 9.0, 6.0)
if pid == 5:
    ops.node(627, 6.0, 9.0, 6.0)
if pid == 3:
    ops.node(628, 7.999999999999998, 9.0, 6.0)
if pid == 5:
    ops.node(628, 7.999999999999998, 9.0, 6.0)
if pid == 3:
    ops.node(629, 2.0, 2.0, 5.0)
if pid == 4:
    ops.node(629, 2.0, 2.0, 5.0)
if pid == 3:
    ops.node(630, 2.0, 1.0, 3.999999999999998)
if pid == 5:
    ops.node(630, 2.0, 1.0, 3.999999999999998)
if pid == 3:
    ops.node(631, 1.0, 2.0, 3.999999999999998)
if pid == 4:
    ops.node(631, 1.0, 2.0, 3.999999999999998)
if pid == 5:
    ops.node(631, 1.0, 2.0, 3.999999999999998)
if pid == 3:
    ops.node(632, 4.0, 2.0, 4.999999999999999)
if pid == 4:
    ops.node(632, 4.0, 2.0, 4.999999999999999)
if pid == 3:
    ops.node(633, 4.0, 1.0, 3.999999999999999)
if pid == 5:
    ops.node(633, 4.0, 1.0, 3.999999999999999)
if pid == 3:
    ops.node(634, 3.0, 2.0, 3.999999999999997)
if pid == 4:
    ops.node(634, 3.0, 2.0, 3.999999999999997)
if pid == 5:
    ops.node(634, 3.0, 2.0, 3.999999999999997)
if pid == 3:
    ops.node(635, 6.0, 2.0, 5.0)
if pid == 4:
    ops.node(635, 6.0, 2.0, 5.0)
if pid == 3:
    ops.node(636, 6.0, 1.0, 4.0)
if pid == 5:
    ops.node(636, 6.0, 1.0, 4.0)
if pid == 3:
    ops.node(637, 5.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(637, 5.0, 2.0, 3.999999999999999)
if pid == 5:
    ops.node(637, 5.0, 2.0, 3.999999999999999)
if pid == 3:
    ops.node(638, 8.0, 2.0, 4.999999999999999)
if pid == 4:
    ops.node(638, 8.0, 2.0, 4.999999999999999)
if pid == 3:
    ops.node(639, 8.0, 1.0, 3.999999999999999)
if pid == 4:
    ops.node(639, 8.0, 1.0, 3.999999999999999)
if pid == 5:
    ops.node(639, 8.0, 1.0, 3.999999999999999)
if pid == 3:
    ops.node(640, 7.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(640, 7.0, 2.0, 3.999999999999999)
if pid == 5:
    ops.node(640, 7.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(641, 9.0, 2.0, 3.999999999999999)
if pid == 5:
    ops.node(641, 9.0, 2.0, 3.999999999999999)
if pid == 4:
    ops.node(642, 2.0, 3.999999999999999, 4.999999999999998)
if pid == 4:
    ops.node(643, 2.0, 3.0, 3.999999999999998)
if pid == 5:
    ops.node(643, 2.0, 3.0, 3.999999999999998)
if pid == 4:
    ops.node(644, 1.0, 4.0, 4.0)
if pid == 5:
    ops.node(644, 1.0, 4.0, 4.0)
if pid == 4:
    ops.node(645, 4.0, 4.0, 5.0)
if pid == 4:
    ops.node(646, 4.0, 3.0, 3.999999999999999)
if pid == 5:
    ops.node(646, 4.0, 3.0, 3.999999999999999)
if pid == 4:
    ops.node(647, 3.0, 4.0, 4.0)
if pid == 5:
    ops.node(647, 3.0, 4.0, 4.0)
if pid == 4:
    ops.node(648, 6.0, 4.0, 5.0)
if pid == 4:
    ops.node(649, 6.0, 3.0, 4.0)
if pid == 5:
    ops.node(649, 6.0, 3.0, 4.0)
if pid == 4:
    ops.node(650, 5.0, 4.0, 4.0)
if pid == 5:
    ops.node(650, 5.0, 4.0, 4.0)
if pid == 4:
    ops.node(651, 8.0, 4.0, 5.0)
if pid == 4:
    ops.node(652, 8.0, 3.0, 3.999999999999999)
if pid == 5:
    ops.node(652, 8.0, 3.0, 3.999999999999999)
if pid == 4:
    ops.node(653, 7.0, 4.0, 4.0)
if pid == 5:
    ops.node(653, 7.0, 4.0, 4.0)
if pid == 4:
    ops.node(654, 9.0, 4.0, 4.0)
if pid == 5:
    ops.node(654, 9.0, 4.0, 4.0)
if pid == 4:
    ops.node(655, 2.0, 6.0, 5.0)
if pid == 4:
    ops.node(656, 2.0, 5.0, 4.0)
if pid == 5:
    ops.node(656, 2.0, 5.0, 4.0)
if pid == 4:
    ops.node(657, 1.0, 6.0, 4.0)
if pid == 5:
    ops.node(657, 1.0, 6.0, 4.0)
if pid == 6:
    ops.node(657, 1.0, 6.0, 4.0)
if pid == 4:
    ops.node(658, 4.0, 6.0, 5.0)
if pid == 4:
    ops.node(659, 4.0, 5.0, 4.0)
if pid == 5:
    ops.node(659, 4.0, 5.0, 4.0)
if pid == 4:
    ops.node(660, 3.0, 6.0, 4.0)
if pid == 5:
    ops.node(660, 3.0, 6.0, 4.0)
if pid == 6:
    ops.node(660, 3.0, 6.0, 4.0)
if pid == 4:
    ops.node(661, 6.0, 6.0, 5.0)
if pid == 4:
    ops.node(662, 6.0, 5.0, 4.0)
if pid == 5:
    ops.node(662, 6.0, 5.0, 4.0)
if pid == 4:
    ops.node(663, 5.0, 6.0, 4.0)
if pid == 5:
    ops.node(663, 5.0, 6.0, 4.0)
if pid == 6:
    ops.node(663, 5.0, 6.0, 4.0)
if pid == 4:
    ops.node(664, 8.0, 6.0, 5.0)
if pid == 4:
    ops.node(665, 8.0, 5.0, 4.0)
if pid == 5:
    ops.node(665, 8.0, 5.0, 4.0)
if pid == 4:
    ops.node(666, 7.0, 6.0, 4.0)
if pid == 5:
    ops.node(666, 7.0, 6.0, 4.0)
if pid == 6:
    ops.node(666, 7.0, 6.0, 4.0)
if pid == 4:
    ops.node(667, 9.0, 6.0, 4.0)
if pid == 5:
    ops.node(667, 9.0, 6.0, 4.0)
if pid == 6:
    ops.node(667, 9.0, 6.0, 4.0)
if pid == 4:
    ops.node(668, 1.999999999999999, 7.999999999999998, 4.999999999999998)
if pid == 4:
    ops.node(669, 2.0, 7.0, 4.0)
if pid == 6:
    ops.node(669, 2.0, 7.0, 4.0)
if pid == 4:
    ops.node(670, 1.0, 8.0, 4.0)
if pid == 6:
    ops.node(670, 1.0, 8.0, 4.0)
if pid == 4:
    ops.node(671, 3.999999999999999, 8.0, 5.0)
if pid == 5:
    ops.node(671, 3.999999999999999, 8.0, 5.0)
if pid == 4:
    ops.node(672, 4.0, 7.0, 4.0)
if pid == 6:
    ops.node(672, 4.0, 7.0, 4.0)
if pid == 4:
    ops.node(673, 3.0, 8.0, 4.0)
if pid == 6:
    ops.node(673, 3.0, 8.0, 4.0)
if pid == 4:
    ops.node(674, 6.0, 8.0, 5.0)
if pid == 5:
    ops.node(674, 6.0, 8.0, 5.0)
if pid == 4:
    ops.node(675, 6.0, 7.0, 4.0)
if pid == 6:
    ops.node(675, 6.0, 7.0, 4.0)
if pid == 4:
    ops.node(676, 5.0, 8.0, 4.0)
if pid == 5:
    ops.node(676, 5.0, 8.0, 4.0)
if pid == 6:
    ops.node(676, 5.0, 8.0, 4.0)
if pid == 4:
    ops.node(677, 7.999999999999998, 8.0, 4.999999999999999)
if pid == 5:
    ops.node(677, 7.999999999999998, 8.0, 4.999999999999999)
if pid == 4:
    ops.node(678, 8.0, 7.0, 3.999999999999999)
if pid == 6:
    ops.node(678, 8.0, 7.0, 3.999999999999999)
if pid == 4:
    ops.node(679, 7.0, 8.0, 3.999999999999999)
if pid == 5:
    ops.node(679, 7.0, 8.0, 3.999999999999999)
if pid == 6:
    ops.node(679, 7.0, 8.0, 3.999999999999999)
if pid == 4:
    ops.node(680, 9.0, 8.0, 3.999999999999999)
if pid == 5:
    ops.node(680, 9.0, 8.0, 3.999999999999999)
if pid == 6:
    ops.node(680, 9.0, 8.0, 3.999999999999999)
if pid == 4:
    ops.node(681, 2.0, 9.0, 4.0)
if pid == 6:
    ops.node(681, 2.0, 9.0, 4.0)
if pid == 4:
    ops.node(682, 4.0, 9.0, 4.0)
if pid == 5:
    ops.node(682, 4.0, 9.0, 4.0)
if pid == 6:
    ops.node(682, 4.0, 9.0, 4.0)
if pid == 5:
    ops.node(683, 6.0, 9.0, 4.0)
if pid == 6:
    ops.node(683, 6.0, 9.0, 4.0)
if pid == 5:
    ops.node(684, 8.0, 9.0, 3.999999999999999)
if pid == 6:
    ops.node(684, 8.0, 9.0, 3.999999999999999)
if pid == 5:
    ops.node(685, 2.0, 2.0, 2.999999999999998)
if pid == 5:
    ops.node(686, 2.0, 0.9999999999999996, 1.999999999999999)
if pid == 6:
    ops.node(686, 2.0, 0.9999999999999996, 1.999999999999999)
if pid == 5:
    ops.node(687, 1.0, 1.999999999999999, 1.999999999999999)
if pid == 6:
    ops.node(687, 1.0, 1.999999999999999, 1.999999999999999)
if pid == 5:
    ops.node(688, 3.999999999999998, 2.0, 2.999999999999999)
if pid == 5:
    ops.node(689, 3.999999999999998, 1.0, 2.0)
if pid == 6:
    ops.node(689, 3.999999999999998, 1.0, 2.0)
if pid == 5:
    ops.node(690, 2.999999999999998, 2.0, 1.999999999999999)
if pid == 6:
    ops.node(690, 2.999999999999998, 2.0, 1.999999999999999)
if pid == 5:
    ops.node(691, 6.0, 2.0, 3.0)
if pid == 5:
    ops.node(692, 6.0, 1.0, 2.0)
if pid == 6:
    ops.node(692, 6.0, 1.0, 2.0)
if pid == 5:
    ops.node(693, 4.999999999999998, 2.0, 2.0)
if pid == 6:
    ops.node(693, 4.999999999999998, 2.0, 2.0)
if pid == 5:
    ops.node(694, 7.999999999999996, 2.0, 2.999999999999999)
if pid == 5:
    ops.node(695, 7.999999999999996, 1.0, 2.0)
if pid == 6:
    ops.node(695, 7.999999999999996, 1.0, 2.0)
if pid == 5:
    ops.node(696, 6.999999999999996, 2.0, 2.0)
if pid == 6:
    ops.node(696, 6.999999999999996, 2.0, 2.0)
if pid == 7:
    ops.node(696, 6.999999999999996, 2.0, 2.0)
if pid == 5:
    ops.node(697, 8.999999999999996, 2.0, 2.0)
if pid == 6:
    ops.node(697, 8.999999999999996, 2.0, 2.0)
if pid == 7:
    ops.node(697, 8.999999999999996, 2.0, 2.0)
if pid == 5:
    ops.node(698, 2.0, 3.999999999999998, 3.0)
if pid == 5:
    ops.node(699, 2.0, 2.999999999999998, 2.0)
if pid == 6:
    ops.node(699, 2.0, 2.999999999999998, 2.0)
if pid == 5:
    ops.node(700, 1.0, 3.999999999999998, 2.0)
if pid == 6:
    ops.node(700, 1.0, 3.999999999999998, 2.0)
if pid == 7:
    ops.node(700, 1.0, 3.999999999999998, 2.0)
if pid == 5:
    ops.node(701, 3.999999999999999, 4.0, 3.0)
if pid == 5:
    ops.node(702, 3.999999999999997, 3.0, 1.999999999999999)
if pid == 6:
    ops.node(702, 3.999999999999997, 3.0, 1.999999999999999)
if pid == 5:
    ops.node(703, 2.999999999999999, 3.999999999999998, 2.0)
if pid == 6:
    ops.node(703, 2.999999999999999, 3.999999999999998, 2.0)
if pid == 7:
    ops.node(703, 2.999999999999999, 3.999999999999998, 2.0)
if pid == 5:
    ops.node(704, 6.0, 4.0, 3.0)
if pid == 5:
    ops.node(705, 6.0, 3.0, 2.0)
if pid == 6:
    ops.node(705, 6.0, 3.0, 2.0)
if pid == 7:
    ops.node(705, 6.0, 3.0, 2.0)
if pid == 5:
    ops.node(706, 4.999999999999999, 4.0, 2.0)
if pid == 6:
    ops.node(706, 4.999999999999999, 4.0, 2.0)
if pid == 7:
    ops.node(706, 4.999999999999999, 4.0, 2.0)
if pid == 5:
    ops.node(707, 7.999999999999998, 4.0, 3.0)
if pid == 5:
    ops.node(708, 7.999999999999995, 3.0, 2.0)
if pid == 7:
    ops.node(708, 7.999999999999995, 3.0, 2.0)
if pid == 5:
    ops.node(709, 6.999999999999998, 4.0, 2.0)
if pid == 7:
    ops.node(709, 6.999999999999998, 4.0, 2.0)
if pid == 5:
    ops.node(710, 8.999999999999998, 4.0, 2.0)
if pid == 7:
    ops.node(710, 8.999999999999998, 4.0, 2.0)
if pid == 5:
    ops.node(711, 2.0, 6.0, 3.0)
if pid == 6:
    ops.node(711, 2.0, 6.0, 3.0)
if pid == 5:
    ops.node(712, 2.0, 4.999999999999998, 2.0)
if pid == 7:
    ops.node(712, 2.0, 4.999999999999998, 2.0)
if pid == 5:
    ops.node(713, 1.0, 6.0, 2.0)
if pid == 6:
    ops.node(713, 1.0, 6.0, 2.0)
if pid == 7:
    ops.node(713, 1.0, 6.0, 2.0)
if pid == 5:
    ops.node(714, 3.999999999999999, 6.0, 3.0)
if pid == 6:
    ops.node(714, 3.999999999999999, 6.0, 3.0)
if pid == 5:
    ops.node(715, 3.999999999999998, 5.0, 2.0)
if pid == 7:
    ops.node(715, 3.999999999999998, 5.0, 2.0)
if pid == 5:
    ops.node(716, 2.999999999999999, 6.0, 2.0)
if pid == 6:
    ops.node(716, 2.999999999999999, 6.0, 2.0)
if pid == 7:
    ops.node(716, 2.999999999999999, 6.0, 2.0)
if pid == 5:
    ops.node(717, 6.0, 6.0, 3.0)
if pid == 6:
    ops.node(717, 6.0, 6.0, 3.0)
if pid == 5:
    ops.node(718, 6.0, 5.0, 2.0)
if pid == 7:
    ops.node(718, 6.0, 5.0, 2.0)
if pid == 5:
    ops.node(719, 4.999999999999999, 6.0, 2.0)
if pid == 6:
    ops.node(719, 4.999999999999999, 6.0, 2.0)
if pid == 7:
    ops.node(719, 4.999999999999999, 6.0, 2.0)
if pid == 5:
    ops.node(720, 7.999999999999998, 6.0, 2.999999999999999)
if pid == 6:
    ops.node(720, 7.999999999999998, 6.0, 2.999999999999999)
if pid == 5:
    ops.node(721, 7.999999999999996, 5.0, 1.999999999999999)
if pid == 7:
    ops.node(721, 7.999999999999996, 5.0, 1.999999999999999)
if pid == 5:
    ops.node(722, 6.999999999999998, 6.0, 1.999999999999999)
if pid == 6:
    ops.node(722, 6.999999999999998, 6.0, 1.999999999999999)
if pid == 7:
    ops.node(722, 6.999999999999998, 6.0, 1.999999999999999)
if pid == 5:
    ops.node(723, 8.999999999999998, 6.0, 1.999999999999999)
if pid == 6:
    ops.node(723, 8.999999999999998, 6.0, 1.999999999999999)
if pid == 7:
    ops.node(723, 8.999999999999998, 6.0, 1.999999999999999)
if pid == 6:
    ops.node(724, 2.0, 7.999999999999996, 3.0)
if pid == 6:
    ops.node(725, 2.0, 6.999999999999996, 2.0)
if pid == 7:
    ops.node(725, 2.0, 6.999999999999996, 2.0)
if pid == 6:
    ops.node(726, 1.0, 7.999999999999996, 2.0)
if pid == 7:
    ops.node(726, 1.0, 7.999999999999996, 2.0)
if pid == 6:
    ops.node(727, 3.999999999999998, 8.0, 3.0)
if pid == 6:
    ops.node(728, 3.999999999999997, 7.0, 2.0)
if pid == 7:
    ops.node(728, 3.999999999999997, 7.0, 2.0)
if pid == 6:
    ops.node(729, 2.999999999999998, 7.999999999999996, 2.0)
if pid == 7:
    ops.node(729, 2.999999999999998, 7.999999999999996, 2.0)
if pid == 6:
    ops.node(730, 6.0, 8.0, 3.000000000000001)
if pid == 6:
    ops.node(731, 6.0, 7.0, 2.000000000000001)
if pid == 7:
    ops.node(731, 6.0, 7.0, 2.000000000000001)
if pid == 6:
    ops.node(732, 4.999999999999998, 8.0, 2.0)
if pid == 7:
    ops.node(732, 4.999999999999998, 8.0, 2.0)
if pid == 6:
    ops.node(733, 7.999999999999996, 8.0, 2.999999999999999)
if pid == 6:
    ops.node(734, 7.999999999999995, 7.0, 1.999999999999999)
if pid == 7:
    ops.node(734, 7.999999999999995, 7.0, 1.999999999999999)
if pid == 6:
    ops.node(735, 6.999999999999996, 8.0, 2.0)
if pid == 7:
    ops.node(735, 6.999999999999996, 8.0, 2.0)
if pid == 6:
    ops.node(736, 8.999999999999996, 8.0, 2.0)
if pid == 7:
    ops.node(736, 8.999999999999996, 8.0, 2.0)
if pid == 6:
    ops.node(737, 2.0, 8.999999999999996, 2.0)
if pid == 7:
    ops.node(737, 2.0, 8.999999999999996, 2.0)
if pid == 6:
    ops.node(738, 3.999999999999998, 9.0, 2.0)
if pid == 7:
    ops.node(738, 3.999999999999998, 9.0, 2.0)
if pid == 6:
    ops.node(739, 6.0, 9.0, 2.000000000000001)
if pid == 7:
    ops.node(739, 6.0, 9.0, 2.000000000000001)
if pid == 6:
    ops.node(740, 7.999999999999996, 9.0, 1.999999999999999)
if pid == 7:
    ops.node(740, 7.999999999999996, 9.0, 1.999999999999999)
if pid == 6:
    ops.node(741, 2.0, 1.999999999999999, 0.9999999999999996)
if pid == 6:
    ops.node(742, 3.999999999999998, 2.0, 0.9999999999999996)
if pid == 6:
    ops.node(743, 6.0, 2.0, 1.0)
if pid == 7:
    ops.node(743, 6.0, 2.0, 1.0)
if pid == 6:
    ops.node(744, 7.999999999999996, 2.0, 1.0)
if pid == 7:
    ops.node(744, 7.999999999999996, 2.0, 1.0)
if pid == 6:
    ops.node(745, 2.0, 3.999999999999998, 1.0)
if pid == 7:
    ops.node(745, 2.0, 3.999999999999998, 1.0)
if pid == 6:
    ops.node(746, 3.999999999999999, 4.0, 0.9999999999999996)
if pid == 7:
    ops.node(746, 3.999999999999999, 4.0, 0.9999999999999996)
if pid == 6:
    ops.node(747, 6.0, 4.0, 1.0)
if pid == 7:
    ops.node(747, 6.0, 4.0, 1.0)
if pid == 7:
    ops.node(748, 7.999999999999998, 4.0, 0.9999999999999996)
if pid == 7:
    ops.node(749, 2.0, 6.0, 1.0)
if pid == 7:
    ops.node(750, 3.999999999999999, 6.0, 1.0)
if pid == 7:
    ops.node(751, 6.0, 6.0, 1.0)
if pid == 7:
    ops.node(752, 7.999999999999998, 6.0, 0.9999999999999991)
if pid == 7:
    ops.node(753, 2.0, 7.999999999999996, 1.0)
if pid == 7:
    ops.node(754, 3.999999999999998, 8.0, 0.9999999999999996)
if pid == 7:
    ops.node(755, 6.0, 8.0, 1.000000000000001)
if pid == 7:
    ops.node(756, 7.999999999999996, 8.0, 0.9999999999999996)
if pid == 0:
    ops.model("basicBuilder","-ndm",3,"-ndf",4)
    ops.node(1,0.0,0.0,10.0)
    ops.node(2,0.0,0.0,0.0)
    ops.node(3,0.0,10.0,10.0)
    ops.node(4,0.0,10.0,0.0)
    ops.node(5,10.0,0.0,10.0)
    ops.node(6,10.0,0.0,0.0)
    ops.node(7,10.0,10.0,10.0)
    ops.node(8,10.0,10.0,0.0)
    ops.node(9,0.0,0.0,2.0)
    ops.node(10,0.0,0.0,4.0)
    ops.node(11,0.0,0.0,6.0)
    ops.node(12,0.0,0.0,8.0)
    ops.node(13,0.0,2.0,10.0)
    ops.node(14,0.0,4.0,10.0)
    ops.node(15,0.0,6.0,10.0)
    ops.node(16,0.0,8.0,10.0)
    ops.node(17,0.0,10.0,2.0)
    ops.node(18,0.0,10.0,4.0)
    ops.node(19,0.0,10.0,6.0)
    ops.node(20,0.0,10.0,8.0)
    ops.node(21,0.0,2.0,0.0)
    ops.node(22,0.0,4.0,0.0)
    ops.node(23,0.0,6.0,0.0)
    ops.node(24,0.0,8.0,0.0)
    ops.node(25,10.0,0.0,2.0)
    ops.node(26,10.0,0.0,4.0)
    ops.node(27,10.0,0.0,6.0)
    ops.node(28,10.0,0.0,8.0)
    ops.node(29,10.0,2.0,10.0)
    ops.node(30,10.0,4.0,10.0)
    ops.node(31,10.0,6.0,10.0)
    ops.node(32,10.0,8.0,10.0)
    ops.node(33,10.0,10.0,2.0)
    ops.node(34,10.0,10.0,4.0)
    ops.node(35,10.0,10.0,6.0)
    ops.node(36,10.0,10.0,8.0)
    ops.node(37,10.0,2.0,0.0)
    ops.node(38,10.0,4.0,0.0)
    ops.node(39,10.0,6.0,0.0)
    ops.node(40,10.0,8.0,0.0)
    ops.node(41,2.0,0.0,0.0)
    ops.node(42,4.0,0.0,0.0)
    ops.node(43,6.0,0.0,0.0)
    ops.node(44,8.0,0.0,0.0)
    ops.node(45,2.0,0.0,10.0)
    ops.node(46,4.0,0.0,10.0)
    ops.node(47,6.0,0.0,10.0)
    ops.node(48,8.0,0.0,10.0)
    ops.node(49,2.0,10.0,0.0)
    ops.node(50,4.0,10.0,0.0)
    ops.node(51,6.0,10.0,0.0)
    ops.node(52,8.0,10.0,0.0)
    ops.node(53,2.0,10.0,10.0)
    ops.node(54,4.0,10.0,10.0)
    ops.node(55,6.0,10.0,10.0)
    ops.node(56,8.0,10.0,10.0)
    ops.node(57,0.0,2.0,2.0)
    ops.node(58,0.0,3.999999999999999,2.0)
    ops.node(59,0.0,6.0,2.0)
    ops.node(60,0.0,7.999999999999998,2.0)
    ops.node(61,0.0,2.0,3.999999999999999)
    ops.node(62,0.0,4.0,4.0)
    ops.node(63,0.0,6.0,4.0)
    ops.node(64,0.0,8.0,4.0)
    ops.node(65,0.0,2.0,6.0)
    ops.node(66,0.0,4.0,6.0)
    ops.node(67,0.0,6.0,6.0)
    ops.node(68,0.0,8.0,6.0)
    ops.node(69,0.0,2.0,7.999999999999998)
    ops.node(70,0.0,4.0,8.0)
    ops.node(71,0.0,6.0,8.0)
    ops.node(72,0.0,8.0,8.0)
    ops.node(73,10.0,2.0,7.999999999999998)
    ops.node(74,10.0,3.999999999999999,8.0)
    ops.node(75,10.0,6.0,8.0)
    ops.node(76,10.0,7.999999999999998,8.0)
    ops.node(77,10.0,2.0,6.0)
    ops.node(78,10.0,4.0,6.0)
    ops.node(79,10.0,6.0,6.0)
    ops.node(80,10.0,8.0,6.0)
    ops.node(81,10.0,2.0,3.999999999999999)
    ops.node(82,10.0,4.0,4.0)
    ops.node(83,10.0,6.0,4.0)
    ops.node(84,10.0,8.0,4.0)
    ops.node(85,10.0,2.0,2.0)
    ops.node(86,10.0,4.0,2.0)
    ops.node(87,10.0,6.0,2.0)
    ops.node(88,10.0,8.0,2.0)
    ops.node(89,2.0,0.0,2.0)
    ops.node(90,2.0,0.0,3.999999999999999)
    ops.node(91,2.0,0.0,6.0)
    ops.node(92,2.0,0.0,7.999999999999998)
    ops.node(93,3.999999999999999,0.0,2.0)
    ops.node(94,4.0,0.0,4.0)
    ops.node(95,4.0,0.0,6.0)
    ops.node(96,4.0,0.0,8.0)
    ops.node(97,6.0,0.0,2.0)
    ops.node(98,6.0,0.0,4.0)
    ops.node(99,6.0,0.0,6.0)
    ops.node(100,6.0,0.0,8.0)
    ops.node(101,7.999999999999998,0.0,2.0)
    ops.node(102,8.0,0.0,4.0)
    ops.node(103,8.0,0.0,6.0)
    ops.node(104,8.0,0.0,8.0)
    ops.node(105,7.999999999999998,10.0,2.0)
    ops.node(106,8.0,10.0,3.999999999999999)
    ops.node(107,8.0,10.0,6.0)
    ops.node(108,8.0,10.0,7.999999999999998)
    ops.node(109,6.0,10.0,2.0)
    ops.node(110,6.0,10.0,4.0)
    ops.node(111,6.0,10.0,6.0)
    ops.node(112,6.0,10.0,8.0)
    ops.node(113,3.999999999999999,10.0,2.0)
    ops.node(114,4.0,10.0,4.0)
    ops.node(115,4.0,10.0,6.0)
    ops.node(116,4.0,10.0,8.0)
    ops.node(117,2.0,10.0,2.0)
    ops.node(118,2.0,10.0,4.0)
    ops.node(119,2.0,10.0,6.0)
    ops.node(120,2.0,10.0,8.0)
    ops.node(121,2.0,2.0,0.0)
    ops.node(122,3.999999999999999,2.0,0.0)
    ops.node(123,6.0,2.0,0.0)
    ops.node(124,7.999999999999998,2.0,0.0)
    ops.node(125,2.0,3.999999999999999,0.0)
    ops.node(126,4.0,4.0,0.0)
    ops.node(127,6.0,4.0,0.0)
    ops.node(128,8.0,4.0,0.0)
    ops.node(129,2.0,6.0,0.0)
    ops.node(130,4.0,6.0,0.0)
    ops.node(131,6.0,6.0,0.0)
    ops.node(132,8.0,6.0,0.0)
    ops.node(133,2.0,7.999999999999998,0.0)
    ops.node(134,4.0,8.0,0.0)
    ops.node(135,6.0,8.0,0.0)
    ops.node(136,8.0,8.0,0.0)
    ops.node(137,2.0,7.999999999999998,10.0)
    ops.node(138,3.999999999999999,8.0,10.0)
    ops.node(139,6.0,8.0,10.0)
    ops.node(140,7.999999999999998,8.0,10.0)
    ops.node(141,2.0,6.0,10.0)
    ops.node(142,4.0,6.0,10.0)
    ops.node(143,6.0,6.0,10.0)
    ops.node(144,8.0,6.0,10.0)
    ops.node(145,2.0,3.999999999999999,10.0)
    ops.node(146,4.0,4.0,10.0)
    ops.node(147,6.0,4.0,10.0)
    ops.node(148,8.0,4.0,10.0)
    ops.node(149,2.0,2.0,10.0)
    ops.node(150,4.0,2.0,10.0)
    ops.node(151,6.0,2.0,10.0)
    ops.node(152,8.0,2.0,10.0)
if pid == 0:
    ops.model("basicBuilder","-ndm",3,"-ndf",3)
    ops.node(217,0.0,0.0,1.0)
    ops.node(218,0.0,0.0,3.0)
    ops.node(219,0.0,0.0,5.0)
    ops.node(220,0.0,0.0,7.0)
    ops.node(221,0.0,0.0,9.0)
    ops.node(222,0.0,1.0,10.0)
    ops.node(223,0.0,3.0,10.0)
    ops.node(224,0.0,5.0,10.0)
    ops.node(225,0.0,7.0,10.0)
    ops.node(226,0.0,9.0,10.0)
    ops.node(227,0.0,10.0,1.0)
    ops.node(228,0.0,10.0,3.0)
    ops.node(229,0.0,10.0,5.0)
    ops.node(230,0.0,10.0,7.0)
    ops.node(231,0.0,10.0,9.0)
    ops.node(232,0.0,1.0,0.0)
    ops.node(233,0.0,3.0,0.0)
    ops.node(234,0.0,5.0,0.0)
    ops.node(235,0.0,7.0,0.0)
    ops.node(236,0.0,9.0,0.0)
    ops.node(237,10.0,0.0,1.0)
    ops.node(238,10.0,0.0,3.0)
    ops.node(239,10.0,0.0,5.0)
    ops.node(240,10.0,0.0,7.0)
    ops.node(241,10.0,0.0,9.0)
    ops.node(242,10.0,1.0,10.0)
    ops.node(243,10.0,3.0,10.0)
    ops.node(244,10.0,5.0,10.0)
    ops.node(245,10.0,7.0,10.0)
    ops.node(246,10.0,9.0,10.0)
    ops.node(247,10.0,10.0,1.0)
    ops.node(248,10.0,10.0,3.0)
    ops.node(249,10.0,10.0,5.0)
    ops.node(250,10.0,10.0,7.0)
    ops.node(251,10.0,10.0,9.0)
    ops.node(252,10.0,1.0,0.0)
    ops.node(253,10.0,3.0,0.0)
    ops.node(254,10.0,5.0,0.0)
    ops.node(255,10.0,7.0,0.0)
    ops.node(256,10.0,9.0,0.0)
    ops.node(257,1.0,0.0,0.0)
    ops.node(258,3.0,0.0,0.0)
    ops.node(259,5.0,0.0,0.0)
    ops.node(260,7.0,0.0,0.0)
    ops.node(261,9.0,0.0,0.0)
    ops.node(262,1.0,0.0,10.0)
    ops.node(263,3.0,0.0,10.0)
    ops.node(264,5.0,0.0,10.0)
    ops.node(265,7.0,0.0,10.0)
    ops.node(266,9.0,0.0,10.0)
    ops.node(267,1.0,10.0,0.0)
    ops.node(268,3.0,10.0,0.0)
    ops.node(269,5.0,10.0,0.0)
    ops.node(270,7.0,10.0,0.0)
    ops.node(271,9.0,10.0,0.0)
    ops.node(272,1.0,10.0,10.0)
    ops.node(273,3.0,10.0,10.0)
    ops.node(274,5.0,10.0,10.0)
    ops.node(275,7.0,10.0,10.0)
    ops.node(276,9.0,10.0,10.0)
    ops.node(277,0.0,0.9999999999999998,2.0)
    ops.node(278,0.0,2.0,0.9999999999999998)
    ops.node(279,0.0,2.999999999999999,2.0)
    ops.node(280,0.0,4.0,1.0)
    ops.node(281,0.0,5.0,2.0)
    ops.node(282,0.0,6.0,1.0)
    ops.node(283,0.0,6.999999999999999,2.0)
    ops.node(284,0.0,7.999999999999999,1.0)
    ops.node(285,0.0,9.0,2.0)
    ops.node(286,0.0,1.0,4.0)
    ops.node(287,0.0,2.0,2.999999999999999)
    ops.node(288,0.0,3.0,4.0)
    ops.node(289,0.0,4.0,3.0)
    ops.node(290,0.0,5.0,4.0)
    ops.node(291,0.0,6.0,3.0)
    ops.node(292,0.0,7.0,4.0)
    ops.node(293,0.0,7.999999999999999,3.0)
    ops.node(294,0.0,9.0,4.0)
    ops.node(295,0.0,1.0,6.0)
    ops.node(296,0.0,2.0,5.0)
    ops.node(297,0.0,3.0,6.0)
    ops.node(298,0.0,4.0,5.0)
    ops.node(299,0.0,5.0,6.0)
    ops.node(300,0.0,6.0,5.0)
    ops.node(301,0.0,7.0,6.0)
    ops.node(302,0.0,8.0,5.0)
    ops.node(303,0.0,9.0,6.0)
    ops.node(304,0.0,1.0,7.999999999999999)
    ops.node(305,0.0,2.0,6.999999999999999)
    ops.node(306,0.0,3.0,7.999999999999999)
    ops.node(307,0.0,4.0,7.0)
    ops.node(308,0.0,5.0,8.0)
    ops.node(309,0.0,6.0,7.0)
    ops.node(310,0.0,7.0,8.0)
    ops.node(311,0.0,8.0,7.0)
    ops.node(312,0.0,9.0,8.0)
    ops.node(313,0.0,2.0,9.0)
    ops.node(314,0.0,4.0,9.0)
    ops.node(315,0.0,6.0,9.0)
    ops.node(316,0.0,8.0,9.0)
    ops.node(317,10.0,0.9999999999999998,7.999999999999999)
    ops.node(318,10.0,2.0,9.0)
    ops.node(319,10.0,2.999999999999999,7.999999999999999)
    ops.node(320,10.0,4.0,9.0)
    ops.node(321,10.0,5.0,8.0)
    ops.node(322,10.0,6.0,9.0)
    ops.node(323,10.0,6.999999999999999,8.0)
    ops.node(324,10.0,7.999999999999999,9.0)
    ops.node(325,10.0,9.0,8.0)
    ops.node(326,10.0,1.0,6.0)
    ops.node(327,10.0,2.0,6.999999999999999)
    ops.node(328,10.0,3.0,6.0)
    ops.node(329,10.0,4.0,7.0)
    ops.node(330,10.0,5.0,6.0)
    ops.node(331,10.0,6.0,7.0)
    ops.node(332,10.0,7.0,6.0)
    ops.node(333,10.0,7.999999999999999,7.0)
    ops.node(334,10.0,9.0,6.0)
    ops.node(335,10.0,1.0,4.0)
    ops.node(336,10.0,2.0,5.0)
    ops.node(337,10.0,3.0,4.0)
    ops.node(338,10.0,4.0,5.0)
    ops.node(339,10.0,5.0,4.0)
    ops.node(340,10.0,6.0,5.0)
    ops.node(341,10.0,7.0,4.0)
    ops.node(342,10.0,8.0,5.0)
    ops.node(343,10.0,9.0,4.0)
    ops.node(344,10.0,1.0,2.0)
    ops.node(345,10.0,2.0,3.0)
    ops.node(346,10.0,3.0,2.0)
    ops.node(347,10.0,4.0,3.0)
    ops.node(348,10.0,5.0,2.0)
    ops.node(349,10.0,6.0,3.0)
    ops.node(350,10.0,7.0,2.0)
    ops.node(351,10.0,8.0,3.0)
    ops.node(352,10.0,9.0,2.0)
    ops.node(353,10.0,2.0,1.0)
    ops.node(354,10.0,4.0,1.0)
    ops.node(355,10.0,6.0,1.0)
    ops.node(356,10.0,8.0,1.0)
    ops.node(357,2.0,0.0,0.9999999999999998)
    ops.node(358,0.9999999999999998,0.0,2.0)
    ops.node(359,2.0,0.0,2.999999999999999)
    ops.node(360,1.0,0.0,4.0)
    ops.node(361,2.0,0.0,5.0)
    ops.node(362,1.0,0.0,6.0)
    ops.node(363,2.0,0.0,6.999999999999999)
    ops.node(364,1.0,0.0,7.999999999999999)
    ops.node(365,2.0,0.0,9.0)
    ops.node(366,4.0,0.0,1.0)
    ops.node(367,2.999999999999999,0.0,2.0)
    ops.node(368,4.0,0.0,3.0)
    ops.node(369,3.0,0.0,4.0)
    ops.node(370,4.0,0.0,5.0)
    ops.node(371,3.0,0.0,6.0)
    ops.node(372,4.0,0.0,7.0)
    ops.node(373,3.0,0.0,7.999999999999999)
    ops.node(374,4.0,0.0,9.0)
    ops.node(375,6.0,0.0,1.0)
    ops.node(376,5.0,0.0,2.0)
    ops.node(377,6.0,0.0,3.0)
    ops.node(378,5.0,0.0,4.0)
    ops.node(379,6.0,0.0,5.0)
    ops.node(380,5.0,0.0,6.0)
    ops.node(381,6.0,0.0,7.0)
    ops.node(382,5.0,0.0,8.0)
    ops.node(383,6.0,0.0,9.0)
    ops.node(384,7.999999999999999,0.0,1.0)
    ops.node(385,6.999999999999999,0.0,2.0)
    ops.node(386,7.999999999999999,0.0,3.0)
    ops.node(387,7.0,0.0,4.0)
    ops.node(388,8.0,0.0,5.0)
    ops.node(389,7.0,0.0,6.0)
    ops.node(390,8.0,0.0,7.0)
    ops.node(391,7.0,0.0,8.0)
    ops.node(392,8.0,0.0,9.0)
    ops.node(393,9.0,0.0,2.0)
    ops.node(394,9.0,0.0,4.0)
    ops.node(395,9.0,0.0,6.0)
    ops.node(396,9.0,0.0,8.0)
    ops.node(397,7.999999999999999,10.0,0.9999999999999998)
    ops.node(398,9.0,10.0,2.0)
    ops.node(399,7.999999999999999,10.0,2.999999999999999)
    ops.node(400,9.0,10.0,4.0)
    ops.node(401,8.0,10.0,5.0)
    ops.node(402,9.0,10.0,6.0)
    ops.node(403,8.0,10.0,6.999999999999999)
    ops.node(404,9.0,10.0,7.999999999999999)
    ops.node(405,8.0,10.0,9.0)
    ops.node(406,6.0,10.0,1.0)
    ops.node(407,6.999999999999999,10.0,2.0)
    ops.node(408,6.0,10.0,3.0)
    ops.node(409,7.0,10.0,4.0)
    ops.node(410,6.0,10.0,5.0)
    ops.node(411,7.0,10.0,6.0)
    ops.node(412,6.0,10.0,7.0)
    ops.node(413,7.0,10.0,7.999999999999999)
    ops.node(414,6.0,10.0,9.0)
    ops.node(415,4.0,10.0,1.0)
    ops.node(416,5.0,10.0,2.0)
    ops.node(417,4.0,10.0,3.0)
    ops.node(418,5.0,10.0,4.0)
    ops.node(419,4.0,10.0,5.0)
    ops.node(420,5.0,10.0,6.0)
    ops.node(421,4.0,10.0,7.0)
    ops.node(422,5.0,10.0,8.0)
    ops.node(423,4.0,10.0,9.0)
    ops.node(424,2.0,10.0,1.0)
    ops.node(425,3.0,10.0,2.0)
    ops.node(426,2.0,10.0,3.0)
    ops.node(427,3.0,10.0,4.0)
    ops.node(428,2.0,10.0,5.0)
    ops.node(429,3.0,10.0,6.0)
    ops.node(430,2.0,10.0,7.0)
    ops.node(431,3.0,10.0,8.0)
    ops.node(432,2.0,10.0,9.0)
    ops.node(433,1.0,10.0,2.0)
    ops.node(434,1.0,10.0,4.0)
    ops.node(435,1.0,10.0,6.0)
    ops.node(436,1.0,10.0,8.0)
    ops.node(437,0.9999999999999998,2.0,0.0)
    ops.node(438,2.0,0.9999999999999998,0.0)
    ops.node(439,2.999999999999999,2.0,0.0)
    ops.node(440,4.0,1.0,0.0)
    ops.node(441,5.0,2.0,0.0)
    ops.node(442,6.0,1.0,0.0)
    ops.node(443,6.999999999999999,2.0,0.0)
    ops.node(444,7.999999999999999,1.0,0.0)
    ops.node(445,9.0,2.0,0.0)
    ops.node(446,1.0,4.0,0.0)
    ops.node(447,2.0,2.999999999999999,0.0)
    ops.node(448,3.0,4.0,0.0)
    ops.node(449,4.0,3.0,0.0)
    ops.node(450,5.0,4.0,0.0)
    ops.node(451,6.0,3.0,0.0)
    ops.node(452,7.0,4.0,0.0)
    ops.node(453,7.999999999999999,3.0,0.0)
    ops.node(454,9.0,4.0,0.0)
    ops.node(455,1.0,6.0,0.0)
    ops.node(456,2.0,5.0,0.0)
    ops.node(457,3.0,6.0,0.0)
    ops.node(458,4.0,5.0,0.0)
    ops.node(459,5.0,6.0,0.0)
    ops.node(460,6.0,5.0,0.0)
    ops.node(461,7.0,6.0,0.0)
    ops.node(462,8.0,5.0,0.0)
    ops.node(463,9.0,6.0,0.0)
    ops.node(464,1.0,7.999999999999999,0.0)
    ops.node(465,2.0,6.999999999999999,0.0)
    ops.node(466,3.0,7.999999999999999,0.0)
    ops.node(467,4.0,7.0,0.0)
    ops.node(468,5.0,8.0,0.0)
    ops.node(469,6.0,7.0,0.0)
    ops.node(470,7.0,8.0,0.0)
    ops.node(471,8.0,7.0,0.0)
    ops.node(472,9.0,8.0,0.0)
    ops.node(473,2.0,9.0,0.0)
    ops.node(474,4.0,9.0,0.0)
    ops.node(475,6.0,9.0,0.0)
    ops.node(476,8.0,9.0,0.0)
    ops.node(477,0.9999999999999998,7.999999999999999,10.0)
    ops.node(478,2.0,9.0,10.0)
    ops.node(479,2.999999999999999,7.999999999999999,10.0)
    ops.node(480,4.0,9.0,10.0)
    ops.node(481,5.0,8.0,10.0)
    ops.node(482,6.0,9.0,10.0)
    ops.node(483,6.999999999999999,8.0,10.0)
    ops.node(484,7.999999999999999,9.0,10.0)
    ops.node(485,9.0,8.0,10.0)
    ops.node(486,1.0,6.0,10.0)
    ops.node(487,2.0,6.999999999999999,10.0)
    ops.node(488,3.0,6.0,10.0)
    ops.node(489,4.0,7.0,10.0)
    ops.node(490,5.0,6.0,10.0)
    ops.node(491,6.0,7.0,10.0)
    ops.node(492,7.0,6.0,10.0)
    ops.node(493,7.999999999999999,7.0,10.0)
    ops.node(494,9.0,6.0,10.0)
    ops.node(495,1.0,4.0,10.0)
    ops.node(496,2.0,5.0,10.0)
    ops.node(497,3.0,4.0,10.0)
    ops.node(498,4.0,5.0,10.0)
    ops.node(499,5.0,4.0,10.0)
    ops.node(500,6.0,5.0,10.0)
    ops.node(501,7.0,4.0,10.0)
    ops.node(502,8.0,5.0,10.0)
    ops.node(503,9.0,4.0,10.0)
    ops.node(504,1.0,2.0,10.0)
    ops.node(505,2.0,3.0,10.0)
    ops.node(506,3.0,2.0,10.0)
    ops.node(507,4.0,3.0,10.0)
    ops.node(508,5.0,2.0,10.0)
    ops.node(509,6.0,3.0,10.0)
    ops.node(510,7.0,2.0,10.0)
    ops.node(511,8.0,3.0,10.0)
    ops.node(512,9.0,2.0,10.0)
    ops.node(513,2.0,1.0,10.0)
    ops.node(514,4.0,1.0,10.0)
    ops.node(515,6.0,1.0,10.0)
    ops.node(516,8.0,1.0,10.0)
    ops.model("basicBuilder","-ndm",3,"-ndf",4)
if pid == 1:
    ops.remove("sp", 1,1)
    ops.remove("sp", 1,2)
    ops.remove("sp", 1,3)
    ops.fix(1, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 1,1)
    ops.remove("sp", 1,2)
    ops.remove("sp", 1,3)
    ops.fix(1, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 2,1)
    ops.remove("sp", 2,2)
    ops.remove("sp", 2,3)
    ops.fix(2, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 2,1)
    ops.remove("sp", 2,2)
    ops.remove("sp", 2,3)
    ops.fix(2, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 3,1)
    ops.remove("sp", 3,2)
    ops.remove("sp", 3,3)
    ops.fix(3, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 3,1)
    ops.remove("sp", 3,2)
    ops.remove("sp", 3,3)
    ops.fix(3, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 4,1)
    ops.remove("sp", 4,2)
    ops.remove("sp", 4,3)
    ops.fix(4, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 4,1)
    ops.remove("sp", 4,2)
    ops.remove("sp", 4,3)
    ops.fix(4, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 5,1)
    ops.remove("sp", 5,2)
    ops.remove("sp", 5,3)
    ops.fix(5, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 5,1)
    ops.remove("sp", 5,2)
    ops.remove("sp", 5,3)
    ops.fix(5, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 6,1)
    ops.remove("sp", 6,2)
    ops.remove("sp", 6,3)
    ops.fix(6, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 6,1)
    ops.remove("sp", 6,2)
    ops.remove("sp", 6,3)
    ops.fix(6, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 7,1)
    ops.remove("sp", 7,2)
    ops.remove("sp", 7,3)
    ops.fix(7, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 7,1)
    ops.remove("sp", 7,2)
    ops.remove("sp", 7,3)
    ops.fix(7, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 8,1)
    ops.remove("sp", 8,2)
    ops.remove("sp", 8,3)
    ops.fix(8, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 8,1)
    ops.remove("sp", 8,2)
    ops.remove("sp", 8,3)
    ops.fix(8, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 9,1)
    ops.remove("sp", 9,2)
    ops.remove("sp", 9,3)
    ops.fix(9, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 9,1)
    ops.remove("sp", 9,2)
    ops.remove("sp", 9,3)
    ops.fix(9, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 9,1)
    ops.remove("sp", 9,2)
    ops.remove("sp", 9,3)
    ops.fix(9, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 10,1)
    ops.remove("sp", 10,2)
    ops.remove("sp", 10,3)
    ops.fix(10, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 10,1)
    ops.remove("sp", 10,2)
    ops.remove("sp", 10,3)
    ops.fix(10, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 10,1)
    ops.remove("sp", 10,2)
    ops.remove("sp", 10,3)
    ops.fix(10, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 11,1)
    ops.remove("sp", 11,2)
    ops.remove("sp", 11,3)
    ops.fix(11, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 11,1)
    ops.remove("sp", 11,2)
    ops.remove("sp", 11,3)
    ops.fix(11, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 11,1)
    ops.remove("sp", 11,2)
    ops.remove("sp", 11,3)
    ops.fix(11, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 12,1)
    ops.remove("sp", 12,2)
    ops.remove("sp", 12,3)
    ops.fix(12, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 12,1)
    ops.remove("sp", 12,2)
    ops.remove("sp", 12,3)
    ops.fix(12, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 12,1)
    ops.remove("sp", 12,2)
    ops.remove("sp", 12,3)
    ops.fix(12, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 13,1)
    ops.remove("sp", 13,2)
    ops.remove("sp", 13,3)
    ops.fix(13, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 13,1)
    ops.remove("sp", 13,2)
    ops.remove("sp", 13,3)
    ops.fix(13, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 14,1)
    ops.remove("sp", 14,2)
    ops.remove("sp", 14,3)
    ops.fix(14, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 14,1)
    ops.remove("sp", 14,2)
    ops.remove("sp", 14,3)
    ops.fix(14, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 15,1)
    ops.remove("sp", 15,2)
    ops.remove("sp", 15,3)
    ops.fix(15, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 15,1)
    ops.remove("sp", 15,2)
    ops.remove("sp", 15,3)
    ops.fix(15, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 16,1)
    ops.remove("sp", 16,2)
    ops.remove("sp", 16,3)
    ops.fix(16, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 16,1)
    ops.remove("sp", 16,2)
    ops.remove("sp", 16,3)
    ops.fix(16, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 16,1)
    ops.remove("sp", 16,2)
    ops.remove("sp", 16,3)
    ops.fix(16, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 17,1)
    ops.remove("sp", 17,2)
    ops.remove("sp", 17,3)
    ops.fix(17, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 17,1)
    ops.remove("sp", 17,2)
    ops.remove("sp", 17,3)
    ops.fix(17, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 17,1)
    ops.remove("sp", 17,2)
    ops.remove("sp", 17,3)
    ops.fix(17, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 18,1)
    ops.remove("sp", 18,2)
    ops.remove("sp", 18,3)
    ops.fix(18, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 18,1)
    ops.remove("sp", 18,2)
    ops.remove("sp", 18,3)
    ops.fix(18, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 18,1)
    ops.remove("sp", 18,2)
    ops.remove("sp", 18,3)
    ops.fix(18, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 19,1)
    ops.remove("sp", 19,2)
    ops.remove("sp", 19,3)
    ops.fix(19, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 19,1)
    ops.remove("sp", 19,2)
    ops.remove("sp", 19,3)
    ops.fix(19, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 19,1)
    ops.remove("sp", 19,2)
    ops.remove("sp", 19,3)
    ops.fix(19, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 20,1)
    ops.remove("sp", 20,2)
    ops.remove("sp", 20,3)
    ops.fix(20, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 20,1)
    ops.remove("sp", 20,2)
    ops.remove("sp", 20,3)
    ops.fix(20, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 20,1)
    ops.remove("sp", 20,2)
    ops.remove("sp", 20,3)
    ops.fix(20, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 21,1)
    ops.remove("sp", 21,2)
    ops.remove("sp", 21,3)
    ops.fix(21, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 21,1)
    ops.remove("sp", 21,2)
    ops.remove("sp", 21,3)
    ops.fix(21, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 22,1)
    ops.remove("sp", 22,2)
    ops.remove("sp", 22,3)
    ops.fix(22, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 22,1)
    ops.remove("sp", 22,2)
    ops.remove("sp", 22,3)
    ops.fix(22, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 22,1)
    ops.remove("sp", 22,2)
    ops.remove("sp", 22,3)
    ops.fix(22, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 23,1)
    ops.remove("sp", 23,2)
    ops.remove("sp", 23,3)
    ops.fix(23, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 23,1)
    ops.remove("sp", 23,2)
    ops.remove("sp", 23,3)
    ops.fix(23, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 24,1)
    ops.remove("sp", 24,2)
    ops.remove("sp", 24,3)
    ops.fix(24, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 24,1)
    ops.remove("sp", 24,2)
    ops.remove("sp", 24,3)
    ops.fix(24, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 25,1)
    ops.remove("sp", 25,2)
    ops.remove("sp", 25,3)
    ops.fix(25, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 25,1)
    ops.remove("sp", 25,2)
    ops.remove("sp", 25,3)
    ops.fix(25, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 25,1)
    ops.remove("sp", 25,2)
    ops.remove("sp", 25,3)
    ops.fix(25, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 26,1)
    ops.remove("sp", 26,2)
    ops.remove("sp", 26,3)
    ops.fix(26, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 26,1)
    ops.remove("sp", 26,2)
    ops.remove("sp", 26,3)
    ops.fix(26, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 26,1)
    ops.remove("sp", 26,2)
    ops.remove("sp", 26,3)
    ops.fix(26, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 27,1)
    ops.remove("sp", 27,2)
    ops.remove("sp", 27,3)
    ops.fix(27, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 27,1)
    ops.remove("sp", 27,2)
    ops.remove("sp", 27,3)
    ops.fix(27, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 27,1)
    ops.remove("sp", 27,2)
    ops.remove("sp", 27,3)
    ops.fix(27, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 28,1)
    ops.remove("sp", 28,2)
    ops.remove("sp", 28,3)
    ops.fix(28, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 28,1)
    ops.remove("sp", 28,2)
    ops.remove("sp", 28,3)
    ops.fix(28, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 28,1)
    ops.remove("sp", 28,2)
    ops.remove("sp", 28,3)
    ops.fix(28, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 29,1)
    ops.remove("sp", 29,2)
    ops.remove("sp", 29,3)
    ops.fix(29, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 29,1)
    ops.remove("sp", 29,2)
    ops.remove("sp", 29,3)
    ops.fix(29, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 30,1)
    ops.remove("sp", 30,2)
    ops.remove("sp", 30,3)
    ops.fix(30, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 30,1)
    ops.remove("sp", 30,2)
    ops.remove("sp", 30,3)
    ops.fix(30, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 31,1)
    ops.remove("sp", 31,2)
    ops.remove("sp", 31,3)
    ops.fix(31, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 31,1)
    ops.remove("sp", 31,2)
    ops.remove("sp", 31,3)
    ops.fix(31, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 31,1)
    ops.remove("sp", 31,2)
    ops.remove("sp", 31,3)
    ops.fix(31, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 32,1)
    ops.remove("sp", 32,2)
    ops.remove("sp", 32,3)
    ops.fix(32, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 32,1)
    ops.remove("sp", 32,2)
    ops.remove("sp", 32,3)
    ops.fix(32, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 33,1)
    ops.remove("sp", 33,2)
    ops.remove("sp", 33,3)
    ops.fix(33, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 33,1)
    ops.remove("sp", 33,2)
    ops.remove("sp", 33,3)
    ops.fix(33, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 33,1)
    ops.remove("sp", 33,2)
    ops.remove("sp", 33,3)
    ops.fix(33, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 34,1)
    ops.remove("sp", 34,2)
    ops.remove("sp", 34,3)
    ops.fix(34, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 34,1)
    ops.remove("sp", 34,2)
    ops.remove("sp", 34,3)
    ops.fix(34, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 34,1)
    ops.remove("sp", 34,2)
    ops.remove("sp", 34,3)
    ops.fix(34, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 35,1)
    ops.remove("sp", 35,2)
    ops.remove("sp", 35,3)
    ops.fix(35, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 35,1)
    ops.remove("sp", 35,2)
    ops.remove("sp", 35,3)
    ops.fix(35, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 35,1)
    ops.remove("sp", 35,2)
    ops.remove("sp", 35,3)
    ops.fix(35, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 36,1)
    ops.remove("sp", 36,2)
    ops.remove("sp", 36,3)
    ops.fix(36, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 36,1)
    ops.remove("sp", 36,2)
    ops.remove("sp", 36,3)
    ops.fix(36, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 36,1)
    ops.remove("sp", 36,2)
    ops.remove("sp", 36,3)
    ops.fix(36, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 37,1)
    ops.remove("sp", 37,2)
    ops.remove("sp", 37,3)
    ops.fix(37, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 37,1)
    ops.remove("sp", 37,2)
    ops.remove("sp", 37,3)
    ops.fix(37, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 37,1)
    ops.remove("sp", 37,2)
    ops.remove("sp", 37,3)
    ops.fix(37, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 38,1)
    ops.remove("sp", 38,2)
    ops.remove("sp", 38,3)
    ops.fix(38, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 38,1)
    ops.remove("sp", 38,2)
    ops.remove("sp", 38,3)
    ops.fix(38, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 39,1)
    ops.remove("sp", 39,2)
    ops.remove("sp", 39,3)
    ops.fix(39, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 39,1)
    ops.remove("sp", 39,2)
    ops.remove("sp", 39,3)
    ops.fix(39, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 40,1)
    ops.remove("sp", 40,2)
    ops.remove("sp", 40,3)
    ops.fix(40, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 40,1)
    ops.remove("sp", 40,2)
    ops.remove("sp", 40,3)
    ops.fix(40, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 57,1)
    ops.remove("sp", 57,2)
    ops.remove("sp", 57,3)
    ops.fix(57, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 57,1)
    ops.remove("sp", 57,2)
    ops.remove("sp", 57,3)
    ops.fix(57, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 57,1)
    ops.remove("sp", 57,2)
    ops.remove("sp", 57,3)
    ops.fix(57, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 58,1)
    ops.remove("sp", 58,2)
    ops.remove("sp", 58,3)
    ops.fix(58, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 58,1)
    ops.remove("sp", 58,2)
    ops.remove("sp", 58,3)
    ops.fix(58, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 58,1)
    ops.remove("sp", 58,2)
    ops.remove("sp", 58,3)
    ops.fix(58, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 58,1)
    ops.remove("sp", 58,2)
    ops.remove("sp", 58,3)
    ops.fix(58, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 59,1)
    ops.remove("sp", 59,2)
    ops.remove("sp", 59,3)
    ops.fix(59, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 59,1)
    ops.remove("sp", 59,2)
    ops.remove("sp", 59,3)
    ops.fix(59, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 59,1)
    ops.remove("sp", 59,2)
    ops.remove("sp", 59,3)
    ops.fix(59, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 59,1)
    ops.remove("sp", 59,2)
    ops.remove("sp", 59,3)
    ops.fix(59, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 60,1)
    ops.remove("sp", 60,2)
    ops.remove("sp", 60,3)
    ops.fix(60, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 60,1)
    ops.remove("sp", 60,2)
    ops.remove("sp", 60,3)
    ops.fix(60, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 60,1)
    ops.remove("sp", 60,2)
    ops.remove("sp", 60,3)
    ops.fix(60, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 61,1)
    ops.remove("sp", 61,2)
    ops.remove("sp", 61,3)
    ops.fix(61, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 61,1)
    ops.remove("sp", 61,2)
    ops.remove("sp", 61,3)
    ops.fix(61, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 61,1)
    ops.remove("sp", 61,2)
    ops.remove("sp", 61,3)
    ops.fix(61, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 61,1)
    ops.remove("sp", 61,2)
    ops.remove("sp", 61,3)
    ops.fix(61, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 62,1)
    ops.remove("sp", 62,2)
    ops.remove("sp", 62,3)
    ops.fix(62, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 62,1)
    ops.remove("sp", 62,2)
    ops.remove("sp", 62,3)
    ops.fix(62, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 62,1)
    ops.remove("sp", 62,2)
    ops.remove("sp", 62,3)
    ops.fix(62, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 63,1)
    ops.remove("sp", 63,2)
    ops.remove("sp", 63,3)
    ops.fix(63, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 63,1)
    ops.remove("sp", 63,2)
    ops.remove("sp", 63,3)
    ops.fix(63, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 63,1)
    ops.remove("sp", 63,2)
    ops.remove("sp", 63,3)
    ops.fix(63, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 63,1)
    ops.remove("sp", 63,2)
    ops.remove("sp", 63,3)
    ops.fix(63, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 64,1)
    ops.remove("sp", 64,2)
    ops.remove("sp", 64,3)
    ops.fix(64, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 64,1)
    ops.remove("sp", 64,2)
    ops.remove("sp", 64,3)
    ops.fix(64, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 64,1)
    ops.remove("sp", 64,2)
    ops.remove("sp", 64,3)
    ops.fix(64, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 65,1)
    ops.remove("sp", 65,2)
    ops.remove("sp", 65,3)
    ops.fix(65, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 65,1)
    ops.remove("sp", 65,2)
    ops.remove("sp", 65,3)
    ops.fix(65, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 65,1)
    ops.remove("sp", 65,2)
    ops.remove("sp", 65,3)
    ops.fix(65, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 65,1)
    ops.remove("sp", 65,2)
    ops.remove("sp", 65,3)
    ops.fix(65, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 66,1)
    ops.remove("sp", 66,2)
    ops.remove("sp", 66,3)
    ops.fix(66, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 66,1)
    ops.remove("sp", 66,2)
    ops.remove("sp", 66,3)
    ops.fix(66, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 66,1)
    ops.remove("sp", 66,2)
    ops.remove("sp", 66,3)
    ops.fix(66, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 67,1)
    ops.remove("sp", 67,2)
    ops.remove("sp", 67,3)
    ops.fix(67, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 67,1)
    ops.remove("sp", 67,2)
    ops.remove("sp", 67,3)
    ops.fix(67, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 67,1)
    ops.remove("sp", 67,2)
    ops.remove("sp", 67,3)
    ops.fix(67, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 67,1)
    ops.remove("sp", 67,2)
    ops.remove("sp", 67,3)
    ops.fix(67, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 68,1)
    ops.remove("sp", 68,2)
    ops.remove("sp", 68,3)
    ops.fix(68, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 68,1)
    ops.remove("sp", 68,2)
    ops.remove("sp", 68,3)
    ops.fix(68, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 68,1)
    ops.remove("sp", 68,2)
    ops.remove("sp", 68,3)
    ops.fix(68, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 69,1)
    ops.remove("sp", 69,2)
    ops.remove("sp", 69,3)
    ops.fix(69, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 69,1)
    ops.remove("sp", 69,2)
    ops.remove("sp", 69,3)
    ops.fix(69, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 69,1)
    ops.remove("sp", 69,2)
    ops.remove("sp", 69,3)
    ops.fix(69, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 70,1)
    ops.remove("sp", 70,2)
    ops.remove("sp", 70,3)
    ops.fix(70, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 70,1)
    ops.remove("sp", 70,2)
    ops.remove("sp", 70,3)
    ops.fix(70, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 70,1)
    ops.remove("sp", 70,2)
    ops.remove("sp", 70,3)
    ops.fix(70, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 71,1)
    ops.remove("sp", 71,2)
    ops.remove("sp", 71,3)
    ops.fix(71, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 71,1)
    ops.remove("sp", 71,2)
    ops.remove("sp", 71,3)
    ops.fix(71, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 71,1)
    ops.remove("sp", 71,2)
    ops.remove("sp", 71,3)
    ops.fix(71, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 71,1)
    ops.remove("sp", 71,2)
    ops.remove("sp", 71,3)
    ops.fix(71, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 72,1)
    ops.remove("sp", 72,2)
    ops.remove("sp", 72,3)
    ops.fix(72, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 72,1)
    ops.remove("sp", 72,2)
    ops.remove("sp", 72,3)
    ops.fix(72, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 72,1)
    ops.remove("sp", 72,2)
    ops.remove("sp", 72,3)
    ops.fix(72, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 72,1)
    ops.remove("sp", 72,2)
    ops.remove("sp", 72,3)
    ops.fix(72, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 73,1)
    ops.remove("sp", 73,2)
    ops.remove("sp", 73,3)
    ops.fix(73, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 73,1)
    ops.remove("sp", 73,2)
    ops.remove("sp", 73,3)
    ops.fix(73, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 73,1)
    ops.remove("sp", 73,2)
    ops.remove("sp", 73,3)
    ops.fix(73, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 74,1)
    ops.remove("sp", 74,2)
    ops.remove("sp", 74,3)
    ops.fix(74, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 74,1)
    ops.remove("sp", 74,2)
    ops.remove("sp", 74,3)
    ops.fix(74, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 74,1)
    ops.remove("sp", 74,2)
    ops.remove("sp", 74,3)
    ops.fix(74, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 74,1)
    ops.remove("sp", 74,2)
    ops.remove("sp", 74,3)
    ops.fix(74, 1, 0, 0,0)
if pid == 1:
    ops.remove("sp", 75,1)
    ops.remove("sp", 75,2)
    ops.remove("sp", 75,3)
    ops.fix(75, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 75,1)
    ops.remove("sp", 75,2)
    ops.remove("sp", 75,3)
    ops.fix(75, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 75,1)
    ops.remove("sp", 75,2)
    ops.remove("sp", 75,3)
    ops.fix(75, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 75,1)
    ops.remove("sp", 75,2)
    ops.remove("sp", 75,3)
    ops.fix(75, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 76,1)
    ops.remove("sp", 76,2)
    ops.remove("sp", 76,3)
    ops.fix(76, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 76,1)
    ops.remove("sp", 76,2)
    ops.remove("sp", 76,3)
    ops.fix(76, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 76,1)
    ops.remove("sp", 76,2)
    ops.remove("sp", 76,3)
    ops.fix(76, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 77,1)
    ops.remove("sp", 77,2)
    ops.remove("sp", 77,3)
    ops.fix(77, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 77,1)
    ops.remove("sp", 77,2)
    ops.remove("sp", 77,3)
    ops.fix(77, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 77,1)
    ops.remove("sp", 77,2)
    ops.remove("sp", 77,3)
    ops.fix(77, 1, 0, 0,0)
if pid == 2:
    ops.remove("sp", 78,1)
    ops.remove("sp", 78,2)
    ops.remove("sp", 78,3)
    ops.fix(78, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 78,1)
    ops.remove("sp", 78,2)
    ops.remove("sp", 78,3)
    ops.fix(78, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 78,1)
    ops.remove("sp", 78,2)
    ops.remove("sp", 78,3)
    ops.fix(78, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 78,1)
    ops.remove("sp", 78,2)
    ops.remove("sp", 78,3)
    ops.fix(78, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 79,1)
    ops.remove("sp", 79,2)
    ops.remove("sp", 79,3)
    ops.fix(79, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 79,1)
    ops.remove("sp", 79,2)
    ops.remove("sp", 79,3)
    ops.fix(79, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 79,1)
    ops.remove("sp", 79,2)
    ops.remove("sp", 79,3)
    ops.fix(79, 1, 0, 0,0)
if pid == 3:
    ops.remove("sp", 80,1)
    ops.remove("sp", 80,2)
    ops.remove("sp", 80,3)
    ops.fix(80, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 80,1)
    ops.remove("sp", 80,2)
    ops.remove("sp", 80,3)
    ops.fix(80, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 80,1)
    ops.remove("sp", 80,2)
    ops.remove("sp", 80,3)
    ops.fix(80, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 80,1)
    ops.remove("sp", 80,2)
    ops.remove("sp", 80,3)
    ops.fix(80, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 81,1)
    ops.remove("sp", 81,2)
    ops.remove("sp", 81,3)
    ops.fix(81, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 81,1)
    ops.remove("sp", 81,2)
    ops.remove("sp", 81,3)
    ops.fix(81, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 81,1)
    ops.remove("sp", 81,2)
    ops.remove("sp", 81,3)
    ops.fix(81, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 82,1)
    ops.remove("sp", 82,2)
    ops.remove("sp", 82,3)
    ops.fix(82, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 82,1)
    ops.remove("sp", 82,2)
    ops.remove("sp", 82,3)
    ops.fix(82, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 82,1)
    ops.remove("sp", 82,2)
    ops.remove("sp", 82,3)
    ops.fix(82, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 83,1)
    ops.remove("sp", 83,2)
    ops.remove("sp", 83,3)
    ops.fix(83, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 83,1)
    ops.remove("sp", 83,2)
    ops.remove("sp", 83,3)
    ops.fix(83, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 83,1)
    ops.remove("sp", 83,2)
    ops.remove("sp", 83,3)
    ops.fix(83, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 83,1)
    ops.remove("sp", 83,2)
    ops.remove("sp", 83,3)
    ops.fix(83, 1, 0, 0,0)
if pid == 4:
    ops.remove("sp", 84,1)
    ops.remove("sp", 84,2)
    ops.remove("sp", 84,3)
    ops.fix(84, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 84,1)
    ops.remove("sp", 84,2)
    ops.remove("sp", 84,3)
    ops.fix(84, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 84,1)
    ops.remove("sp", 84,2)
    ops.remove("sp", 84,3)
    ops.fix(84, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 84,1)
    ops.remove("sp", 84,2)
    ops.remove("sp", 84,3)
    ops.fix(84, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 85,1)
    ops.remove("sp", 85,2)
    ops.remove("sp", 85,3)
    ops.fix(85, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 85,1)
    ops.remove("sp", 85,2)
    ops.remove("sp", 85,3)
    ops.fix(85, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 85,1)
    ops.remove("sp", 85,2)
    ops.remove("sp", 85,3)
    ops.fix(85, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 85,1)
    ops.remove("sp", 85,2)
    ops.remove("sp", 85,3)
    ops.fix(85, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 86,1)
    ops.remove("sp", 86,2)
    ops.remove("sp", 86,3)
    ops.fix(86, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 86,1)
    ops.remove("sp", 86,2)
    ops.remove("sp", 86,3)
    ops.fix(86, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 86,1)
    ops.remove("sp", 86,2)
    ops.remove("sp", 86,3)
    ops.fix(86, 1, 0, 0,0)
if pid == 5:
    ops.remove("sp", 87,1)
    ops.remove("sp", 87,2)
    ops.remove("sp", 87,3)
    ops.fix(87, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 87,1)
    ops.remove("sp", 87,2)
    ops.remove("sp", 87,3)
    ops.fix(87, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 87,1)
    ops.remove("sp", 87,2)
    ops.remove("sp", 87,3)
    ops.fix(87, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 87,1)
    ops.remove("sp", 87,2)
    ops.remove("sp", 87,3)
    ops.fix(87, 1, 0, 0,0)
if pid == 6:
    ops.remove("sp", 88,1)
    ops.remove("sp", 88,2)
    ops.remove("sp", 88,3)
    ops.fix(88, 1, 0, 0,0)
if pid == 0:
    ops.remove("sp", 88,1)
    ops.remove("sp", 88,2)
    ops.remove("sp", 88,3)
    ops.fix(88, 1, 0, 0,0)
if pid == 7:
    ops.remove("sp", 88,1)
    ops.remove("sp", 88,2)
    ops.remove("sp", 88,3)
    ops.fix(88, 1, 0, 0,0)
ops.model("basicBuilder","-ndm",3,"-ndf",3)
if pid == 6:
    ops.remove("sp", 217,1)
    ops.remove("sp", 217,2)
    ops.remove("sp", 217,3)
    ops.fix(217, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 217,1)
    ops.remove("sp", 217,2)
    ops.remove("sp", 217,3)
    ops.fix(217, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 218,1)
    ops.remove("sp", 218,2)
    ops.remove("sp", 218,3)
    ops.fix(218, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 218,1)
    ops.remove("sp", 218,2)
    ops.remove("sp", 218,3)
    ops.fix(218, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 219,1)
    ops.remove("sp", 219,2)
    ops.remove("sp", 219,3)
    ops.fix(219, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 219,1)
    ops.remove("sp", 219,2)
    ops.remove("sp", 219,3)
    ops.fix(219, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 220,1)
    ops.remove("sp", 220,2)
    ops.remove("sp", 220,3)
    ops.fix(220, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 220,1)
    ops.remove("sp", 220,2)
    ops.remove("sp", 220,3)
    ops.fix(220, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 221,1)
    ops.remove("sp", 221,2)
    ops.remove("sp", 221,3)
    ops.fix(221, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 221,1)
    ops.remove("sp", 221,2)
    ops.remove("sp", 221,3)
    ops.fix(221, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 222,1)
    ops.remove("sp", 222,2)
    ops.remove("sp", 222,3)
    ops.fix(222, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 222,1)
    ops.remove("sp", 222,2)
    ops.remove("sp", 222,3)
    ops.fix(222, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 223,1)
    ops.remove("sp", 223,2)
    ops.remove("sp", 223,3)
    ops.fix(223, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 223,1)
    ops.remove("sp", 223,2)
    ops.remove("sp", 223,3)
    ops.fix(223, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 224,1)
    ops.remove("sp", 224,2)
    ops.remove("sp", 224,3)
    ops.fix(224, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 224,1)
    ops.remove("sp", 224,2)
    ops.remove("sp", 224,3)
    ops.fix(224, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 225,1)
    ops.remove("sp", 225,2)
    ops.remove("sp", 225,3)
    ops.fix(225, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 225,1)
    ops.remove("sp", 225,2)
    ops.remove("sp", 225,3)
    ops.fix(225, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 226,1)
    ops.remove("sp", 226,2)
    ops.remove("sp", 226,3)
    ops.fix(226, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 226,1)
    ops.remove("sp", 226,2)
    ops.remove("sp", 226,3)
    ops.fix(226, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 227,1)
    ops.remove("sp", 227,2)
    ops.remove("sp", 227,3)
    ops.fix(227, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 227,1)
    ops.remove("sp", 227,2)
    ops.remove("sp", 227,3)
    ops.fix(227, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 228,1)
    ops.remove("sp", 228,2)
    ops.remove("sp", 228,3)
    ops.fix(228, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 228,1)
    ops.remove("sp", 228,2)
    ops.remove("sp", 228,3)
    ops.fix(228, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 229,1)
    ops.remove("sp", 229,2)
    ops.remove("sp", 229,3)
    ops.fix(229, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 229,1)
    ops.remove("sp", 229,2)
    ops.remove("sp", 229,3)
    ops.fix(229, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 230,1)
    ops.remove("sp", 230,2)
    ops.remove("sp", 230,3)
    ops.fix(230, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 230,1)
    ops.remove("sp", 230,2)
    ops.remove("sp", 230,3)
    ops.fix(230, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 231,1)
    ops.remove("sp", 231,2)
    ops.remove("sp", 231,3)
    ops.fix(231, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 231,1)
    ops.remove("sp", 231,2)
    ops.remove("sp", 231,3)
    ops.fix(231, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 232,1)
    ops.remove("sp", 232,2)
    ops.remove("sp", 232,3)
    ops.fix(232, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 232,1)
    ops.remove("sp", 232,2)
    ops.remove("sp", 232,3)
    ops.fix(232, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 233,1)
    ops.remove("sp", 233,2)
    ops.remove("sp", 233,3)
    ops.fix(233, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 233,1)
    ops.remove("sp", 233,2)
    ops.remove("sp", 233,3)
    ops.fix(233, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 234,1)
    ops.remove("sp", 234,2)
    ops.remove("sp", 234,3)
    ops.fix(234, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 234,1)
    ops.remove("sp", 234,2)
    ops.remove("sp", 234,3)
    ops.fix(234, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 235,1)
    ops.remove("sp", 235,2)
    ops.remove("sp", 235,3)
    ops.fix(235, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 235,1)
    ops.remove("sp", 235,2)
    ops.remove("sp", 235,3)
    ops.fix(235, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 236,1)
    ops.remove("sp", 236,2)
    ops.remove("sp", 236,3)
    ops.fix(236, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 236,1)
    ops.remove("sp", 236,2)
    ops.remove("sp", 236,3)
    ops.fix(236, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 237,1)
    ops.remove("sp", 237,2)
    ops.remove("sp", 237,3)
    ops.fix(237, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 237,1)
    ops.remove("sp", 237,2)
    ops.remove("sp", 237,3)
    ops.fix(237, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 238,1)
    ops.remove("sp", 238,2)
    ops.remove("sp", 238,3)
    ops.fix(238, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 238,1)
    ops.remove("sp", 238,2)
    ops.remove("sp", 238,3)
    ops.fix(238, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 239,1)
    ops.remove("sp", 239,2)
    ops.remove("sp", 239,3)
    ops.fix(239, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 239,1)
    ops.remove("sp", 239,2)
    ops.remove("sp", 239,3)
    ops.fix(239, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 240,1)
    ops.remove("sp", 240,2)
    ops.remove("sp", 240,3)
    ops.fix(240, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 240,1)
    ops.remove("sp", 240,2)
    ops.remove("sp", 240,3)
    ops.fix(240, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 241,1)
    ops.remove("sp", 241,2)
    ops.remove("sp", 241,3)
    ops.fix(241, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 241,1)
    ops.remove("sp", 241,2)
    ops.remove("sp", 241,3)
    ops.fix(241, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 242,1)
    ops.remove("sp", 242,2)
    ops.remove("sp", 242,3)
    ops.fix(242, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 242,1)
    ops.remove("sp", 242,2)
    ops.remove("sp", 242,3)
    ops.fix(242, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 243,1)
    ops.remove("sp", 243,2)
    ops.remove("sp", 243,3)
    ops.fix(243, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 243,1)
    ops.remove("sp", 243,2)
    ops.remove("sp", 243,3)
    ops.fix(243, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 244,1)
    ops.remove("sp", 244,2)
    ops.remove("sp", 244,3)
    ops.fix(244, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 244,1)
    ops.remove("sp", 244,2)
    ops.remove("sp", 244,3)
    ops.fix(244, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 245,1)
    ops.remove("sp", 245,2)
    ops.remove("sp", 245,3)
    ops.fix(245, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 245,1)
    ops.remove("sp", 245,2)
    ops.remove("sp", 245,3)
    ops.fix(245, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 246,1)
    ops.remove("sp", 246,2)
    ops.remove("sp", 246,3)
    ops.fix(246, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 246,1)
    ops.remove("sp", 246,2)
    ops.remove("sp", 246,3)
    ops.fix(246, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 247,1)
    ops.remove("sp", 247,2)
    ops.remove("sp", 247,3)
    ops.fix(247, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 247,1)
    ops.remove("sp", 247,2)
    ops.remove("sp", 247,3)
    ops.fix(247, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 248,1)
    ops.remove("sp", 248,2)
    ops.remove("sp", 248,3)
    ops.fix(248, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 248,1)
    ops.remove("sp", 248,2)
    ops.remove("sp", 248,3)
    ops.fix(248, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 249,1)
    ops.remove("sp", 249,2)
    ops.remove("sp", 249,3)
    ops.fix(249, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 249,1)
    ops.remove("sp", 249,2)
    ops.remove("sp", 249,3)
    ops.fix(249, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 250,1)
    ops.remove("sp", 250,2)
    ops.remove("sp", 250,3)
    ops.fix(250, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 250,1)
    ops.remove("sp", 250,2)
    ops.remove("sp", 250,3)
    ops.fix(250, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 251,1)
    ops.remove("sp", 251,2)
    ops.remove("sp", 251,3)
    ops.fix(251, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 251,1)
    ops.remove("sp", 251,2)
    ops.remove("sp", 251,3)
    ops.fix(251, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 252,1)
    ops.remove("sp", 252,2)
    ops.remove("sp", 252,3)
    ops.fix(252, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 252,1)
    ops.remove("sp", 252,2)
    ops.remove("sp", 252,3)
    ops.fix(252, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 253,1)
    ops.remove("sp", 253,2)
    ops.remove("sp", 253,3)
    ops.fix(253, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 253,1)
    ops.remove("sp", 253,2)
    ops.remove("sp", 253,3)
    ops.fix(253, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 254,1)
    ops.remove("sp", 254,2)
    ops.remove("sp", 254,3)
    ops.fix(254, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 254,1)
    ops.remove("sp", 254,2)
    ops.remove("sp", 254,3)
    ops.fix(254, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 255,1)
    ops.remove("sp", 255,2)
    ops.remove("sp", 255,3)
    ops.fix(255, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 255,1)
    ops.remove("sp", 255,2)
    ops.remove("sp", 255,3)
    ops.fix(255, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 256,1)
    ops.remove("sp", 256,2)
    ops.remove("sp", 256,3)
    ops.fix(256, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 256,1)
    ops.remove("sp", 256,2)
    ops.remove("sp", 256,3)
    ops.fix(256, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 277,1)
    ops.remove("sp", 277,2)
    ops.remove("sp", 277,3)
    ops.fix(277, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 277,1)
    ops.remove("sp", 277,2)
    ops.remove("sp", 277,3)
    ops.fix(277, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 277,1)
    ops.remove("sp", 277,2)
    ops.remove("sp", 277,3)
    ops.fix(277, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 278,1)
    ops.remove("sp", 278,2)
    ops.remove("sp", 278,3)
    ops.fix(278, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 278,1)
    ops.remove("sp", 278,2)
    ops.remove("sp", 278,3)
    ops.fix(278, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 279,1)
    ops.remove("sp", 279,2)
    ops.remove("sp", 279,3)
    ops.fix(279, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 279,1)
    ops.remove("sp", 279,2)
    ops.remove("sp", 279,3)
    ops.fix(279, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 279,1)
    ops.remove("sp", 279,2)
    ops.remove("sp", 279,3)
    ops.fix(279, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 280,1)
    ops.remove("sp", 280,2)
    ops.remove("sp", 280,3)
    ops.fix(280, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 280,1)
    ops.remove("sp", 280,2)
    ops.remove("sp", 280,3)
    ops.fix(280, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 280,1)
    ops.remove("sp", 280,2)
    ops.remove("sp", 280,3)
    ops.fix(280, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 281,1)
    ops.remove("sp", 281,2)
    ops.remove("sp", 281,3)
    ops.fix(281, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 281,1)
    ops.remove("sp", 281,2)
    ops.remove("sp", 281,3)
    ops.fix(281, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 281,1)
    ops.remove("sp", 281,2)
    ops.remove("sp", 281,3)
    ops.fix(281, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 282,1)
    ops.remove("sp", 282,2)
    ops.remove("sp", 282,3)
    ops.fix(282, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 282,1)
    ops.remove("sp", 282,2)
    ops.remove("sp", 282,3)
    ops.fix(282, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 283,1)
    ops.remove("sp", 283,2)
    ops.remove("sp", 283,3)
    ops.fix(283, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 283,1)
    ops.remove("sp", 283,2)
    ops.remove("sp", 283,3)
    ops.fix(283, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 283,1)
    ops.remove("sp", 283,2)
    ops.remove("sp", 283,3)
    ops.fix(283, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 284,1)
    ops.remove("sp", 284,2)
    ops.remove("sp", 284,3)
    ops.fix(284, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 284,1)
    ops.remove("sp", 284,2)
    ops.remove("sp", 284,3)
    ops.fix(284, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 285,1)
    ops.remove("sp", 285,2)
    ops.remove("sp", 285,3)
    ops.fix(285, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 285,1)
    ops.remove("sp", 285,2)
    ops.remove("sp", 285,3)
    ops.fix(285, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 285,1)
    ops.remove("sp", 285,2)
    ops.remove("sp", 285,3)
    ops.fix(285, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 286,1)
    ops.remove("sp", 286,2)
    ops.remove("sp", 286,3)
    ops.fix(286, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 286,1)
    ops.remove("sp", 286,2)
    ops.remove("sp", 286,3)
    ops.fix(286, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 286,1)
    ops.remove("sp", 286,2)
    ops.remove("sp", 286,3)
    ops.fix(286, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 287,1)
    ops.remove("sp", 287,2)
    ops.remove("sp", 287,3)
    ops.fix(287, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 287,1)
    ops.remove("sp", 287,2)
    ops.remove("sp", 287,3)
    ops.fix(287, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 288,1)
    ops.remove("sp", 288,2)
    ops.remove("sp", 288,3)
    ops.fix(288, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 288,1)
    ops.remove("sp", 288,2)
    ops.remove("sp", 288,3)
    ops.fix(288, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 288,1)
    ops.remove("sp", 288,2)
    ops.remove("sp", 288,3)
    ops.fix(288, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 289,1)
    ops.remove("sp", 289,2)
    ops.remove("sp", 289,3)
    ops.fix(289, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 289,1)
    ops.remove("sp", 289,2)
    ops.remove("sp", 289,3)
    ops.fix(289, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 290,1)
    ops.remove("sp", 290,2)
    ops.remove("sp", 290,3)
    ops.fix(290, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 290,1)
    ops.remove("sp", 290,2)
    ops.remove("sp", 290,3)
    ops.fix(290, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 290,1)
    ops.remove("sp", 290,2)
    ops.remove("sp", 290,3)
    ops.fix(290, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 291,1)
    ops.remove("sp", 291,2)
    ops.remove("sp", 291,3)
    ops.fix(291, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 291,1)
    ops.remove("sp", 291,2)
    ops.remove("sp", 291,3)
    ops.fix(291, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 291,1)
    ops.remove("sp", 291,2)
    ops.remove("sp", 291,3)
    ops.fix(291, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 292,1)
    ops.remove("sp", 292,2)
    ops.remove("sp", 292,3)
    ops.fix(292, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 292,1)
    ops.remove("sp", 292,2)
    ops.remove("sp", 292,3)
    ops.fix(292, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 292,1)
    ops.remove("sp", 292,2)
    ops.remove("sp", 292,3)
    ops.fix(292, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 293,1)
    ops.remove("sp", 293,2)
    ops.remove("sp", 293,3)
    ops.fix(293, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 293,1)
    ops.remove("sp", 293,2)
    ops.remove("sp", 293,3)
    ops.fix(293, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 294,1)
    ops.remove("sp", 294,2)
    ops.remove("sp", 294,3)
    ops.fix(294, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 294,1)
    ops.remove("sp", 294,2)
    ops.remove("sp", 294,3)
    ops.fix(294, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 294,1)
    ops.remove("sp", 294,2)
    ops.remove("sp", 294,3)
    ops.fix(294, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 295,1)
    ops.remove("sp", 295,2)
    ops.remove("sp", 295,3)
    ops.fix(295, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 295,1)
    ops.remove("sp", 295,2)
    ops.remove("sp", 295,3)
    ops.fix(295, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 295,1)
    ops.remove("sp", 295,2)
    ops.remove("sp", 295,3)
    ops.fix(295, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 296,1)
    ops.remove("sp", 296,2)
    ops.remove("sp", 296,3)
    ops.fix(296, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 296,1)
    ops.remove("sp", 296,2)
    ops.remove("sp", 296,3)
    ops.fix(296, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 296,1)
    ops.remove("sp", 296,2)
    ops.remove("sp", 296,3)
    ops.fix(296, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 297,1)
    ops.remove("sp", 297,2)
    ops.remove("sp", 297,3)
    ops.fix(297, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 297,1)
    ops.remove("sp", 297,2)
    ops.remove("sp", 297,3)
    ops.fix(297, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 297,1)
    ops.remove("sp", 297,2)
    ops.remove("sp", 297,3)
    ops.fix(297, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 298,1)
    ops.remove("sp", 298,2)
    ops.remove("sp", 298,3)
    ops.fix(298, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 298,1)
    ops.remove("sp", 298,2)
    ops.remove("sp", 298,3)
    ops.fix(298, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 299,1)
    ops.remove("sp", 299,2)
    ops.remove("sp", 299,3)
    ops.fix(299, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 299,1)
    ops.remove("sp", 299,2)
    ops.remove("sp", 299,3)
    ops.fix(299, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 299,1)
    ops.remove("sp", 299,2)
    ops.remove("sp", 299,3)
    ops.fix(299, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 300,1)
    ops.remove("sp", 300,2)
    ops.remove("sp", 300,3)
    ops.fix(300, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 300,1)
    ops.remove("sp", 300,2)
    ops.remove("sp", 300,3)
    ops.fix(300, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 301,1)
    ops.remove("sp", 301,2)
    ops.remove("sp", 301,3)
    ops.fix(301, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 301,1)
    ops.remove("sp", 301,2)
    ops.remove("sp", 301,3)
    ops.fix(301, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 301,1)
    ops.remove("sp", 301,2)
    ops.remove("sp", 301,3)
    ops.fix(301, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 302,1)
    ops.remove("sp", 302,2)
    ops.remove("sp", 302,3)
    ops.fix(302, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 302,1)
    ops.remove("sp", 302,2)
    ops.remove("sp", 302,3)
    ops.fix(302, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 303,1)
    ops.remove("sp", 303,2)
    ops.remove("sp", 303,3)
    ops.fix(303, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 303,1)
    ops.remove("sp", 303,2)
    ops.remove("sp", 303,3)
    ops.fix(303, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 303,1)
    ops.remove("sp", 303,2)
    ops.remove("sp", 303,3)
    ops.fix(303, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 304,1)
    ops.remove("sp", 304,2)
    ops.remove("sp", 304,3)
    ops.fix(304, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 304,1)
    ops.remove("sp", 304,2)
    ops.remove("sp", 304,3)
    ops.fix(304, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 304,1)
    ops.remove("sp", 304,2)
    ops.remove("sp", 304,3)
    ops.fix(304, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 305,1)
    ops.remove("sp", 305,2)
    ops.remove("sp", 305,3)
    ops.fix(305, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 305,1)
    ops.remove("sp", 305,2)
    ops.remove("sp", 305,3)
    ops.fix(305, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 306,1)
    ops.remove("sp", 306,2)
    ops.remove("sp", 306,3)
    ops.fix(306, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 306,1)
    ops.remove("sp", 306,2)
    ops.remove("sp", 306,3)
    ops.fix(306, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 306,1)
    ops.remove("sp", 306,2)
    ops.remove("sp", 306,3)
    ops.fix(306, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 307,1)
    ops.remove("sp", 307,2)
    ops.remove("sp", 307,3)
    ops.fix(307, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 307,1)
    ops.remove("sp", 307,2)
    ops.remove("sp", 307,3)
    ops.fix(307, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 308,1)
    ops.remove("sp", 308,2)
    ops.remove("sp", 308,3)
    ops.fix(308, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 308,1)
    ops.remove("sp", 308,2)
    ops.remove("sp", 308,3)
    ops.fix(308, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 308,1)
    ops.remove("sp", 308,2)
    ops.remove("sp", 308,3)
    ops.fix(308, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 309,1)
    ops.remove("sp", 309,2)
    ops.remove("sp", 309,3)
    ops.fix(309, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 309,1)
    ops.remove("sp", 309,2)
    ops.remove("sp", 309,3)
    ops.fix(309, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 309,1)
    ops.remove("sp", 309,2)
    ops.remove("sp", 309,3)
    ops.fix(309, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 310,1)
    ops.remove("sp", 310,2)
    ops.remove("sp", 310,3)
    ops.fix(310, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 310,1)
    ops.remove("sp", 310,2)
    ops.remove("sp", 310,3)
    ops.fix(310, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 310,1)
    ops.remove("sp", 310,2)
    ops.remove("sp", 310,3)
    ops.fix(310, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 311,1)
    ops.remove("sp", 311,2)
    ops.remove("sp", 311,3)
    ops.fix(311, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 311,1)
    ops.remove("sp", 311,2)
    ops.remove("sp", 311,3)
    ops.fix(311, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 312,1)
    ops.remove("sp", 312,2)
    ops.remove("sp", 312,3)
    ops.fix(312, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 312,1)
    ops.remove("sp", 312,2)
    ops.remove("sp", 312,3)
    ops.fix(312, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 312,1)
    ops.remove("sp", 312,2)
    ops.remove("sp", 312,3)
    ops.fix(312, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 313,1)
    ops.remove("sp", 313,2)
    ops.remove("sp", 313,3)
    ops.fix(313, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 313,1)
    ops.remove("sp", 313,2)
    ops.remove("sp", 313,3)
    ops.fix(313, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 314,1)
    ops.remove("sp", 314,2)
    ops.remove("sp", 314,3)
    ops.fix(314, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 314,1)
    ops.remove("sp", 314,2)
    ops.remove("sp", 314,3)
    ops.fix(314, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 315,1)
    ops.remove("sp", 315,2)
    ops.remove("sp", 315,3)
    ops.fix(315, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 315,1)
    ops.remove("sp", 315,2)
    ops.remove("sp", 315,3)
    ops.fix(315, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 316,1)
    ops.remove("sp", 316,2)
    ops.remove("sp", 316,3)
    ops.fix(316, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 316,1)
    ops.remove("sp", 316,2)
    ops.remove("sp", 316,3)
    ops.fix(316, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 316,1)
    ops.remove("sp", 316,2)
    ops.remove("sp", 316,3)
    ops.fix(316, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 317,1)
    ops.remove("sp", 317,2)
    ops.remove("sp", 317,3)
    ops.fix(317, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 317,1)
    ops.remove("sp", 317,2)
    ops.remove("sp", 317,3)
    ops.fix(317, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 317,1)
    ops.remove("sp", 317,2)
    ops.remove("sp", 317,3)
    ops.fix(317, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 318,1)
    ops.remove("sp", 318,2)
    ops.remove("sp", 318,3)
    ops.fix(318, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 318,1)
    ops.remove("sp", 318,2)
    ops.remove("sp", 318,3)
    ops.fix(318, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 319,1)
    ops.remove("sp", 319,2)
    ops.remove("sp", 319,3)
    ops.fix(319, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 319,1)
    ops.remove("sp", 319,2)
    ops.remove("sp", 319,3)
    ops.fix(319, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 319,1)
    ops.remove("sp", 319,2)
    ops.remove("sp", 319,3)
    ops.fix(319, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 320,1)
    ops.remove("sp", 320,2)
    ops.remove("sp", 320,3)
    ops.fix(320, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 320,1)
    ops.remove("sp", 320,2)
    ops.remove("sp", 320,3)
    ops.fix(320, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 321,1)
    ops.remove("sp", 321,2)
    ops.remove("sp", 321,3)
    ops.fix(321, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 321,1)
    ops.remove("sp", 321,2)
    ops.remove("sp", 321,3)
    ops.fix(321, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 321,1)
    ops.remove("sp", 321,2)
    ops.remove("sp", 321,3)
    ops.fix(321, 1, 0, 0)
if pid == 1:
    ops.remove("sp", 322,1)
    ops.remove("sp", 322,2)
    ops.remove("sp", 322,3)
    ops.fix(322, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 322,1)
    ops.remove("sp", 322,2)
    ops.remove("sp", 322,3)
    ops.fix(322, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 322,1)
    ops.remove("sp", 322,2)
    ops.remove("sp", 322,3)
    ops.fix(322, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 323,1)
    ops.remove("sp", 323,2)
    ops.remove("sp", 323,3)
    ops.fix(323, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 323,1)
    ops.remove("sp", 323,2)
    ops.remove("sp", 323,3)
    ops.fix(323, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 323,1)
    ops.remove("sp", 323,2)
    ops.remove("sp", 323,3)
    ops.fix(323, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 324,1)
    ops.remove("sp", 324,2)
    ops.remove("sp", 324,3)
    ops.fix(324, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 324,1)
    ops.remove("sp", 324,2)
    ops.remove("sp", 324,3)
    ops.fix(324, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 325,1)
    ops.remove("sp", 325,2)
    ops.remove("sp", 325,3)
    ops.fix(325, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 325,1)
    ops.remove("sp", 325,2)
    ops.remove("sp", 325,3)
    ops.fix(325, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 325,1)
    ops.remove("sp", 325,2)
    ops.remove("sp", 325,3)
    ops.fix(325, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 326,1)
    ops.remove("sp", 326,2)
    ops.remove("sp", 326,3)
    ops.fix(326, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 326,1)
    ops.remove("sp", 326,2)
    ops.remove("sp", 326,3)
    ops.fix(326, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 326,1)
    ops.remove("sp", 326,2)
    ops.remove("sp", 326,3)
    ops.fix(326, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 327,1)
    ops.remove("sp", 327,2)
    ops.remove("sp", 327,3)
    ops.fix(327, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 327,1)
    ops.remove("sp", 327,2)
    ops.remove("sp", 327,3)
    ops.fix(327, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 328,1)
    ops.remove("sp", 328,2)
    ops.remove("sp", 328,3)
    ops.fix(328, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 328,1)
    ops.remove("sp", 328,2)
    ops.remove("sp", 328,3)
    ops.fix(328, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 328,1)
    ops.remove("sp", 328,2)
    ops.remove("sp", 328,3)
    ops.fix(328, 1, 0, 0)
if pid == 2:
    ops.remove("sp", 329,1)
    ops.remove("sp", 329,2)
    ops.remove("sp", 329,3)
    ops.fix(329, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 329,1)
    ops.remove("sp", 329,2)
    ops.remove("sp", 329,3)
    ops.fix(329, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 329,1)
    ops.remove("sp", 329,2)
    ops.remove("sp", 329,3)
    ops.fix(329, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 330,1)
    ops.remove("sp", 330,2)
    ops.remove("sp", 330,3)
    ops.fix(330, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 330,1)
    ops.remove("sp", 330,2)
    ops.remove("sp", 330,3)
    ops.fix(330, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 330,1)
    ops.remove("sp", 330,2)
    ops.remove("sp", 330,3)
    ops.fix(330, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 331,1)
    ops.remove("sp", 331,2)
    ops.remove("sp", 331,3)
    ops.fix(331, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 331,1)
    ops.remove("sp", 331,2)
    ops.remove("sp", 331,3)
    ops.fix(331, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 332,1)
    ops.remove("sp", 332,2)
    ops.remove("sp", 332,3)
    ops.fix(332, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 332,1)
    ops.remove("sp", 332,2)
    ops.remove("sp", 332,3)
    ops.fix(332, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 332,1)
    ops.remove("sp", 332,2)
    ops.remove("sp", 332,3)
    ops.fix(332, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 333,1)
    ops.remove("sp", 333,2)
    ops.remove("sp", 333,3)
    ops.fix(333, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 333,1)
    ops.remove("sp", 333,2)
    ops.remove("sp", 333,3)
    ops.fix(333, 1, 0, 0)
if pid == 3:
    ops.remove("sp", 334,1)
    ops.remove("sp", 334,2)
    ops.remove("sp", 334,3)
    ops.fix(334, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 334,1)
    ops.remove("sp", 334,2)
    ops.remove("sp", 334,3)
    ops.fix(334, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 334,1)
    ops.remove("sp", 334,2)
    ops.remove("sp", 334,3)
    ops.fix(334, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 335,1)
    ops.remove("sp", 335,2)
    ops.remove("sp", 335,3)
    ops.fix(335, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 335,1)
    ops.remove("sp", 335,2)
    ops.remove("sp", 335,3)
    ops.fix(335, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 335,1)
    ops.remove("sp", 335,2)
    ops.remove("sp", 335,3)
    ops.fix(335, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 336,1)
    ops.remove("sp", 336,2)
    ops.remove("sp", 336,3)
    ops.fix(336, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 336,1)
    ops.remove("sp", 336,2)
    ops.remove("sp", 336,3)
    ops.fix(336, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 337,1)
    ops.remove("sp", 337,2)
    ops.remove("sp", 337,3)
    ops.fix(337, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 337,1)
    ops.remove("sp", 337,2)
    ops.remove("sp", 337,3)
    ops.fix(337, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 337,1)
    ops.remove("sp", 337,2)
    ops.remove("sp", 337,3)
    ops.fix(337, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 338,1)
    ops.remove("sp", 338,2)
    ops.remove("sp", 338,3)
    ops.fix(338, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 338,1)
    ops.remove("sp", 338,2)
    ops.remove("sp", 338,3)
    ops.fix(338, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 339,1)
    ops.remove("sp", 339,2)
    ops.remove("sp", 339,3)
    ops.fix(339, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 339,1)
    ops.remove("sp", 339,2)
    ops.remove("sp", 339,3)
    ops.fix(339, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 339,1)
    ops.remove("sp", 339,2)
    ops.remove("sp", 339,3)
    ops.fix(339, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 340,1)
    ops.remove("sp", 340,2)
    ops.remove("sp", 340,3)
    ops.fix(340, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 340,1)
    ops.remove("sp", 340,2)
    ops.remove("sp", 340,3)
    ops.fix(340, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 341,1)
    ops.remove("sp", 341,2)
    ops.remove("sp", 341,3)
    ops.fix(341, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 341,1)
    ops.remove("sp", 341,2)
    ops.remove("sp", 341,3)
    ops.fix(341, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 341,1)
    ops.remove("sp", 341,2)
    ops.remove("sp", 341,3)
    ops.fix(341, 1, 0, 0)
if pid == 4:
    ops.remove("sp", 342,1)
    ops.remove("sp", 342,2)
    ops.remove("sp", 342,3)
    ops.fix(342, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 342,1)
    ops.remove("sp", 342,2)
    ops.remove("sp", 342,3)
    ops.fix(342, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 342,1)
    ops.remove("sp", 342,2)
    ops.remove("sp", 342,3)
    ops.fix(342, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 343,1)
    ops.remove("sp", 343,2)
    ops.remove("sp", 343,3)
    ops.fix(343, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 343,1)
    ops.remove("sp", 343,2)
    ops.remove("sp", 343,3)
    ops.fix(343, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 343,1)
    ops.remove("sp", 343,2)
    ops.remove("sp", 343,3)
    ops.fix(343, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 344,1)
    ops.remove("sp", 344,2)
    ops.remove("sp", 344,3)
    ops.fix(344, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 344,1)
    ops.remove("sp", 344,2)
    ops.remove("sp", 344,3)
    ops.fix(344, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 344,1)
    ops.remove("sp", 344,2)
    ops.remove("sp", 344,3)
    ops.fix(344, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 345,1)
    ops.remove("sp", 345,2)
    ops.remove("sp", 345,3)
    ops.fix(345, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 345,1)
    ops.remove("sp", 345,2)
    ops.remove("sp", 345,3)
    ops.fix(345, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 346,1)
    ops.remove("sp", 346,2)
    ops.remove("sp", 346,3)
    ops.fix(346, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 346,1)
    ops.remove("sp", 346,2)
    ops.remove("sp", 346,3)
    ops.fix(346, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 346,1)
    ops.remove("sp", 346,2)
    ops.remove("sp", 346,3)
    ops.fix(346, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 347,1)
    ops.remove("sp", 347,2)
    ops.remove("sp", 347,3)
    ops.fix(347, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 347,1)
    ops.remove("sp", 347,2)
    ops.remove("sp", 347,3)
    ops.fix(347, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 348,1)
    ops.remove("sp", 348,2)
    ops.remove("sp", 348,3)
    ops.fix(348, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 348,1)
    ops.remove("sp", 348,2)
    ops.remove("sp", 348,3)
    ops.fix(348, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 348,1)
    ops.remove("sp", 348,2)
    ops.remove("sp", 348,3)
    ops.fix(348, 1, 0, 0)
if pid == 5:
    ops.remove("sp", 349,1)
    ops.remove("sp", 349,2)
    ops.remove("sp", 349,3)
    ops.fix(349, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 349,1)
    ops.remove("sp", 349,2)
    ops.remove("sp", 349,3)
    ops.fix(349, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 349,1)
    ops.remove("sp", 349,2)
    ops.remove("sp", 349,3)
    ops.fix(349, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 350,1)
    ops.remove("sp", 350,2)
    ops.remove("sp", 350,3)
    ops.fix(350, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 350,1)
    ops.remove("sp", 350,2)
    ops.remove("sp", 350,3)
    ops.fix(350, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 350,1)
    ops.remove("sp", 350,2)
    ops.remove("sp", 350,3)
    ops.fix(350, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 351,1)
    ops.remove("sp", 351,2)
    ops.remove("sp", 351,3)
    ops.fix(351, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 351,1)
    ops.remove("sp", 351,2)
    ops.remove("sp", 351,3)
    ops.fix(351, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 352,1)
    ops.remove("sp", 352,2)
    ops.remove("sp", 352,3)
    ops.fix(352, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 352,1)
    ops.remove("sp", 352,2)
    ops.remove("sp", 352,3)
    ops.fix(352, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 352,1)
    ops.remove("sp", 352,2)
    ops.remove("sp", 352,3)
    ops.fix(352, 1, 0, 0)
if pid == 6:
    ops.remove("sp", 353,1)
    ops.remove("sp", 353,2)
    ops.remove("sp", 353,3)
    ops.fix(353, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 353,1)
    ops.remove("sp", 353,2)
    ops.remove("sp", 353,3)
    ops.fix(353, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 353,1)
    ops.remove("sp", 353,2)
    ops.remove("sp", 353,3)
    ops.fix(353, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 354,1)
    ops.remove("sp", 354,2)
    ops.remove("sp", 354,3)
    ops.fix(354, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 354,1)
    ops.remove("sp", 354,2)
    ops.remove("sp", 354,3)
    ops.fix(354, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 355,1)
    ops.remove("sp", 355,2)
    ops.remove("sp", 355,3)
    ops.fix(355, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 355,1)
    ops.remove("sp", 355,2)
    ops.remove("sp", 355,3)
    ops.fix(355, 1, 0, 0)
if pid == 7:
    ops.remove("sp", 356,1)
    ops.remove("sp", 356,2)
    ops.remove("sp", 356,3)
    ops.fix(356, 1, 0, 0)
if pid == 0:
    ops.remove("sp", 356,1)
    ops.remove("sp", 356,2)
    ops.remove("sp", 356,3)
    ops.fix(356, 1, 0, 0)
    ops.model("basicBuilder","-ndm",3,"-ndf",4)
if pid == 1:
    ops.remove("sp", 1,1)
    ops.remove("sp", 1,2)
    ops.remove("sp", 1,3)
    ops.fix(1, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 1,1)
    ops.remove("sp", 1,2)
    ops.remove("sp", 1,3)
    ops.fix(1, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 2,1)
    ops.remove("sp", 2,2)
    ops.remove("sp", 2,3)
    ops.fix(2, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 2,1)
    ops.remove("sp", 2,2)
    ops.remove("sp", 2,3)
    ops.fix(2, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 3,1)
    ops.remove("sp", 3,2)
    ops.remove("sp", 3,3)
    ops.fix(3, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 3,1)
    ops.remove("sp", 3,2)
    ops.remove("sp", 3,3)
    ops.fix(3, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 4,1)
    ops.remove("sp", 4,2)
    ops.remove("sp", 4,3)
    ops.fix(4, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 4,1)
    ops.remove("sp", 4,2)
    ops.remove("sp", 4,3)
    ops.fix(4, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 5,1)
    ops.remove("sp", 5,2)
    ops.remove("sp", 5,3)
    ops.fix(5, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 5,1)
    ops.remove("sp", 5,2)
    ops.remove("sp", 5,3)
    ops.fix(5, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 6,1)
    ops.remove("sp", 6,2)
    ops.remove("sp", 6,3)
    ops.fix(6, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 6,1)
    ops.remove("sp", 6,2)
    ops.remove("sp", 6,3)
    ops.fix(6, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 7,1)
    ops.remove("sp", 7,2)
    ops.remove("sp", 7,3)
    ops.fix(7, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 7,1)
    ops.remove("sp", 7,2)
    ops.remove("sp", 7,3)
    ops.fix(7, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 8,1)
    ops.remove("sp", 8,2)
    ops.remove("sp", 8,3)
    ops.fix(8, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 8,1)
    ops.remove("sp", 8,2)
    ops.remove("sp", 8,3)
    ops.fix(8, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 9,1)
    ops.remove("sp", 9,2)
    ops.remove("sp", 9,3)
    ops.fix(9, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 9,1)
    ops.remove("sp", 9,2)
    ops.remove("sp", 9,3)
    ops.fix(9, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 9,1)
    ops.remove("sp", 9,2)
    ops.remove("sp", 9,3)
    ops.fix(9, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 10,1)
    ops.remove("sp", 10,2)
    ops.remove("sp", 10,3)
    ops.fix(10, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 10,1)
    ops.remove("sp", 10,2)
    ops.remove("sp", 10,3)
    ops.fix(10, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 10,1)
    ops.remove("sp", 10,2)
    ops.remove("sp", 10,3)
    ops.fix(10, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 11,1)
    ops.remove("sp", 11,2)
    ops.remove("sp", 11,3)
    ops.fix(11, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 11,1)
    ops.remove("sp", 11,2)
    ops.remove("sp", 11,3)
    ops.fix(11, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 11,1)
    ops.remove("sp", 11,2)
    ops.remove("sp", 11,3)
    ops.fix(11, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 12,1)
    ops.remove("sp", 12,2)
    ops.remove("sp", 12,3)
    ops.fix(12, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 12,1)
    ops.remove("sp", 12,2)
    ops.remove("sp", 12,3)
    ops.fix(12, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 12,1)
    ops.remove("sp", 12,2)
    ops.remove("sp", 12,3)
    ops.fix(12, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 17,1)
    ops.remove("sp", 17,2)
    ops.remove("sp", 17,3)
    ops.fix(17, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 17,1)
    ops.remove("sp", 17,2)
    ops.remove("sp", 17,3)
    ops.fix(17, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 17,1)
    ops.remove("sp", 17,2)
    ops.remove("sp", 17,3)
    ops.fix(17, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 18,1)
    ops.remove("sp", 18,2)
    ops.remove("sp", 18,3)
    ops.fix(18, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 18,1)
    ops.remove("sp", 18,2)
    ops.remove("sp", 18,3)
    ops.fix(18, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 18,1)
    ops.remove("sp", 18,2)
    ops.remove("sp", 18,3)
    ops.fix(18, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 19,1)
    ops.remove("sp", 19,2)
    ops.remove("sp", 19,3)
    ops.fix(19, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 19,1)
    ops.remove("sp", 19,2)
    ops.remove("sp", 19,3)
    ops.fix(19, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 19,1)
    ops.remove("sp", 19,2)
    ops.remove("sp", 19,3)
    ops.fix(19, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 20,1)
    ops.remove("sp", 20,2)
    ops.remove("sp", 20,3)
    ops.fix(20, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 20,1)
    ops.remove("sp", 20,2)
    ops.remove("sp", 20,3)
    ops.fix(20, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 20,1)
    ops.remove("sp", 20,2)
    ops.remove("sp", 20,3)
    ops.fix(20, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 25,1)
    ops.remove("sp", 25,2)
    ops.remove("sp", 25,3)
    ops.fix(25, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 25,1)
    ops.remove("sp", 25,2)
    ops.remove("sp", 25,3)
    ops.fix(25, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 25,1)
    ops.remove("sp", 25,2)
    ops.remove("sp", 25,3)
    ops.fix(25, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 26,1)
    ops.remove("sp", 26,2)
    ops.remove("sp", 26,3)
    ops.fix(26, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 26,1)
    ops.remove("sp", 26,2)
    ops.remove("sp", 26,3)
    ops.fix(26, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 26,1)
    ops.remove("sp", 26,2)
    ops.remove("sp", 26,3)
    ops.fix(26, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 27,1)
    ops.remove("sp", 27,2)
    ops.remove("sp", 27,3)
    ops.fix(27, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 27,1)
    ops.remove("sp", 27,2)
    ops.remove("sp", 27,3)
    ops.fix(27, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 27,1)
    ops.remove("sp", 27,2)
    ops.remove("sp", 27,3)
    ops.fix(27, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 28,1)
    ops.remove("sp", 28,2)
    ops.remove("sp", 28,3)
    ops.fix(28, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 28,1)
    ops.remove("sp", 28,2)
    ops.remove("sp", 28,3)
    ops.fix(28, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 28,1)
    ops.remove("sp", 28,2)
    ops.remove("sp", 28,3)
    ops.fix(28, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 33,1)
    ops.remove("sp", 33,2)
    ops.remove("sp", 33,3)
    ops.fix(33, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 33,1)
    ops.remove("sp", 33,2)
    ops.remove("sp", 33,3)
    ops.fix(33, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 33,1)
    ops.remove("sp", 33,2)
    ops.remove("sp", 33,3)
    ops.fix(33, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 34,1)
    ops.remove("sp", 34,2)
    ops.remove("sp", 34,3)
    ops.fix(34, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 34,1)
    ops.remove("sp", 34,2)
    ops.remove("sp", 34,3)
    ops.fix(34, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 34,1)
    ops.remove("sp", 34,2)
    ops.remove("sp", 34,3)
    ops.fix(34, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 35,1)
    ops.remove("sp", 35,2)
    ops.remove("sp", 35,3)
    ops.fix(35, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 35,1)
    ops.remove("sp", 35,2)
    ops.remove("sp", 35,3)
    ops.fix(35, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 35,1)
    ops.remove("sp", 35,2)
    ops.remove("sp", 35,3)
    ops.fix(35, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 36,1)
    ops.remove("sp", 36,2)
    ops.remove("sp", 36,3)
    ops.fix(36, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 36,1)
    ops.remove("sp", 36,2)
    ops.remove("sp", 36,3)
    ops.fix(36, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 36,1)
    ops.remove("sp", 36,2)
    ops.remove("sp", 36,3)
    ops.fix(36, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 41,1)
    ops.remove("sp", 41,2)
    ops.remove("sp", 41,3)
    ops.fix(41, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 41,1)
    ops.remove("sp", 41,2)
    ops.remove("sp", 41,3)
    ops.fix(41, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 42,1)
    ops.remove("sp", 42,2)
    ops.remove("sp", 42,3)
    ops.fix(42, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 42,1)
    ops.remove("sp", 42,2)
    ops.remove("sp", 42,3)
    ops.fix(42, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 43,1)
    ops.remove("sp", 43,2)
    ops.remove("sp", 43,3)
    ops.fix(43, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 43,1)
    ops.remove("sp", 43,2)
    ops.remove("sp", 43,3)
    ops.fix(43, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 44,1)
    ops.remove("sp", 44,2)
    ops.remove("sp", 44,3)
    ops.fix(44, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 44,1)
    ops.remove("sp", 44,2)
    ops.remove("sp", 44,3)
    ops.fix(44, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 45,1)
    ops.remove("sp", 45,2)
    ops.remove("sp", 45,3)
    ops.fix(45, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 45,1)
    ops.remove("sp", 45,2)
    ops.remove("sp", 45,3)
    ops.fix(45, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 46,1)
    ops.remove("sp", 46,2)
    ops.remove("sp", 46,3)
    ops.fix(46, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 46,1)
    ops.remove("sp", 46,2)
    ops.remove("sp", 46,3)
    ops.fix(46, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 47,1)
    ops.remove("sp", 47,2)
    ops.remove("sp", 47,3)
    ops.fix(47, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 47,1)
    ops.remove("sp", 47,2)
    ops.remove("sp", 47,3)
    ops.fix(47, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 48,1)
    ops.remove("sp", 48,2)
    ops.remove("sp", 48,3)
    ops.fix(48, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 48,1)
    ops.remove("sp", 48,2)
    ops.remove("sp", 48,3)
    ops.fix(48, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 49,1)
    ops.remove("sp", 49,2)
    ops.remove("sp", 49,3)
    ops.fix(49, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 49,1)
    ops.remove("sp", 49,2)
    ops.remove("sp", 49,3)
    ops.fix(49, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 50,1)
    ops.remove("sp", 50,2)
    ops.remove("sp", 50,3)
    ops.fix(50, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 50,1)
    ops.remove("sp", 50,2)
    ops.remove("sp", 50,3)
    ops.fix(50, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 51,1)
    ops.remove("sp", 51,2)
    ops.remove("sp", 51,3)
    ops.fix(51, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 51,1)
    ops.remove("sp", 51,2)
    ops.remove("sp", 51,3)
    ops.fix(51, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 52,1)
    ops.remove("sp", 52,2)
    ops.remove("sp", 52,3)
    ops.fix(52, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 52,1)
    ops.remove("sp", 52,2)
    ops.remove("sp", 52,3)
    ops.fix(52, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 53,1)
    ops.remove("sp", 53,2)
    ops.remove("sp", 53,3)
    ops.fix(53, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 53,1)
    ops.remove("sp", 53,2)
    ops.remove("sp", 53,3)
    ops.fix(53, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 54,1)
    ops.remove("sp", 54,2)
    ops.remove("sp", 54,3)
    ops.fix(54, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 54,1)
    ops.remove("sp", 54,2)
    ops.remove("sp", 54,3)
    ops.fix(54, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 55,1)
    ops.remove("sp", 55,2)
    ops.remove("sp", 55,3)
    ops.fix(55, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 55,1)
    ops.remove("sp", 55,2)
    ops.remove("sp", 55,3)
    ops.fix(55, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 56,1)
    ops.remove("sp", 56,2)
    ops.remove("sp", 56,3)
    ops.fix(56, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 56,1)
    ops.remove("sp", 56,2)
    ops.remove("sp", 56,3)
    ops.fix(56, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 89,1)
    ops.remove("sp", 89,2)
    ops.remove("sp", 89,3)
    ops.fix(89, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 89,1)
    ops.remove("sp", 89,2)
    ops.remove("sp", 89,3)
    ops.fix(89, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 89,1)
    ops.remove("sp", 89,2)
    ops.remove("sp", 89,3)
    ops.fix(89, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 90,1)
    ops.remove("sp", 90,2)
    ops.remove("sp", 90,3)
    ops.fix(90, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 90,1)
    ops.remove("sp", 90,2)
    ops.remove("sp", 90,3)
    ops.fix(90, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 90,1)
    ops.remove("sp", 90,2)
    ops.remove("sp", 90,3)
    ops.fix(90, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 91,1)
    ops.remove("sp", 91,2)
    ops.remove("sp", 91,3)
    ops.fix(91, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 91,1)
    ops.remove("sp", 91,2)
    ops.remove("sp", 91,3)
    ops.fix(91, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 91,1)
    ops.remove("sp", 91,2)
    ops.remove("sp", 91,3)
    ops.fix(91, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 92,1)
    ops.remove("sp", 92,2)
    ops.remove("sp", 92,3)
    ops.fix(92, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 92,1)
    ops.remove("sp", 92,2)
    ops.remove("sp", 92,3)
    ops.fix(92, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 92,1)
    ops.remove("sp", 92,2)
    ops.remove("sp", 92,3)
    ops.fix(92, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 93,1)
    ops.remove("sp", 93,2)
    ops.remove("sp", 93,3)
    ops.fix(93, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 93,1)
    ops.remove("sp", 93,2)
    ops.remove("sp", 93,3)
    ops.fix(93, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 93,1)
    ops.remove("sp", 93,2)
    ops.remove("sp", 93,3)
    ops.fix(93, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 94,1)
    ops.remove("sp", 94,2)
    ops.remove("sp", 94,3)
    ops.fix(94, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 94,1)
    ops.remove("sp", 94,2)
    ops.remove("sp", 94,3)
    ops.fix(94, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 94,1)
    ops.remove("sp", 94,2)
    ops.remove("sp", 94,3)
    ops.fix(94, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 95,1)
    ops.remove("sp", 95,2)
    ops.remove("sp", 95,3)
    ops.fix(95, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 95,1)
    ops.remove("sp", 95,2)
    ops.remove("sp", 95,3)
    ops.fix(95, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 95,1)
    ops.remove("sp", 95,2)
    ops.remove("sp", 95,3)
    ops.fix(95, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 96,1)
    ops.remove("sp", 96,2)
    ops.remove("sp", 96,3)
    ops.fix(96, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 96,1)
    ops.remove("sp", 96,2)
    ops.remove("sp", 96,3)
    ops.fix(96, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 96,1)
    ops.remove("sp", 96,2)
    ops.remove("sp", 96,3)
    ops.fix(96, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 97,1)
    ops.remove("sp", 97,2)
    ops.remove("sp", 97,3)
    ops.fix(97, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 97,1)
    ops.remove("sp", 97,2)
    ops.remove("sp", 97,3)
    ops.fix(97, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 97,1)
    ops.remove("sp", 97,2)
    ops.remove("sp", 97,3)
    ops.fix(97, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 98,1)
    ops.remove("sp", 98,2)
    ops.remove("sp", 98,3)
    ops.fix(98, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 98,1)
    ops.remove("sp", 98,2)
    ops.remove("sp", 98,3)
    ops.fix(98, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 98,1)
    ops.remove("sp", 98,2)
    ops.remove("sp", 98,3)
    ops.fix(98, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 99,1)
    ops.remove("sp", 99,2)
    ops.remove("sp", 99,3)
    ops.fix(99, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 99,1)
    ops.remove("sp", 99,2)
    ops.remove("sp", 99,3)
    ops.fix(99, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 99,1)
    ops.remove("sp", 99,2)
    ops.remove("sp", 99,3)
    ops.fix(99, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 100,1)
    ops.remove("sp", 100,2)
    ops.remove("sp", 100,3)
    ops.fix(100, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 100,1)
    ops.remove("sp", 100,2)
    ops.remove("sp", 100,3)
    ops.fix(100, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 100,1)
    ops.remove("sp", 100,2)
    ops.remove("sp", 100,3)
    ops.fix(100, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 101,1)
    ops.remove("sp", 101,2)
    ops.remove("sp", 101,3)
    ops.fix(101, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 101,1)
    ops.remove("sp", 101,2)
    ops.remove("sp", 101,3)
    ops.fix(101, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 101,1)
    ops.remove("sp", 101,2)
    ops.remove("sp", 101,3)
    ops.fix(101, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 102,1)
    ops.remove("sp", 102,2)
    ops.remove("sp", 102,3)
    ops.fix(102, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 102,1)
    ops.remove("sp", 102,2)
    ops.remove("sp", 102,3)
    ops.fix(102, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 102,1)
    ops.remove("sp", 102,2)
    ops.remove("sp", 102,3)
    ops.fix(102, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 102,1)
    ops.remove("sp", 102,2)
    ops.remove("sp", 102,3)
    ops.fix(102, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 103,1)
    ops.remove("sp", 103,2)
    ops.remove("sp", 103,3)
    ops.fix(103, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 103,1)
    ops.remove("sp", 103,2)
    ops.remove("sp", 103,3)
    ops.fix(103, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 103,1)
    ops.remove("sp", 103,2)
    ops.remove("sp", 103,3)
    ops.fix(103, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 103,1)
    ops.remove("sp", 103,2)
    ops.remove("sp", 103,3)
    ops.fix(103, 0, 1, 0,0)
if pid == 1:
    ops.remove("sp", 104,1)
    ops.remove("sp", 104,2)
    ops.remove("sp", 104,3)
    ops.fix(104, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 104,1)
    ops.remove("sp", 104,2)
    ops.remove("sp", 104,3)
    ops.fix(104, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 104,1)
    ops.remove("sp", 104,2)
    ops.remove("sp", 104,3)
    ops.fix(104, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 105,1)
    ops.remove("sp", 105,2)
    ops.remove("sp", 105,3)
    ops.fix(105, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 105,1)
    ops.remove("sp", 105,2)
    ops.remove("sp", 105,3)
    ops.fix(105, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 105,1)
    ops.remove("sp", 105,2)
    ops.remove("sp", 105,3)
    ops.fix(105, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 106,1)
    ops.remove("sp", 106,2)
    ops.remove("sp", 106,3)
    ops.fix(106, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 106,1)
    ops.remove("sp", 106,2)
    ops.remove("sp", 106,3)
    ops.fix(106, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 106,1)
    ops.remove("sp", 106,2)
    ops.remove("sp", 106,3)
    ops.fix(106, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 107,1)
    ops.remove("sp", 107,2)
    ops.remove("sp", 107,3)
    ops.fix(107, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 107,1)
    ops.remove("sp", 107,2)
    ops.remove("sp", 107,3)
    ops.fix(107, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 107,1)
    ops.remove("sp", 107,2)
    ops.remove("sp", 107,3)
    ops.fix(107, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 108,1)
    ops.remove("sp", 108,2)
    ops.remove("sp", 108,3)
    ops.fix(108, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 108,1)
    ops.remove("sp", 108,2)
    ops.remove("sp", 108,3)
    ops.fix(108, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 108,1)
    ops.remove("sp", 108,2)
    ops.remove("sp", 108,3)
    ops.fix(108, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 109,1)
    ops.remove("sp", 109,2)
    ops.remove("sp", 109,3)
    ops.fix(109, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 109,1)
    ops.remove("sp", 109,2)
    ops.remove("sp", 109,3)
    ops.fix(109, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 109,1)
    ops.remove("sp", 109,2)
    ops.remove("sp", 109,3)
    ops.fix(109, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 110,1)
    ops.remove("sp", 110,2)
    ops.remove("sp", 110,3)
    ops.fix(110, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 110,1)
    ops.remove("sp", 110,2)
    ops.remove("sp", 110,3)
    ops.fix(110, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 110,1)
    ops.remove("sp", 110,2)
    ops.remove("sp", 110,3)
    ops.fix(110, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 111,1)
    ops.remove("sp", 111,2)
    ops.remove("sp", 111,3)
    ops.fix(111, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 111,1)
    ops.remove("sp", 111,2)
    ops.remove("sp", 111,3)
    ops.fix(111, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 111,1)
    ops.remove("sp", 111,2)
    ops.remove("sp", 111,3)
    ops.fix(111, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 112,1)
    ops.remove("sp", 112,2)
    ops.remove("sp", 112,3)
    ops.fix(112, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 112,1)
    ops.remove("sp", 112,2)
    ops.remove("sp", 112,3)
    ops.fix(112, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 112,1)
    ops.remove("sp", 112,2)
    ops.remove("sp", 112,3)
    ops.fix(112, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 113,1)
    ops.remove("sp", 113,2)
    ops.remove("sp", 113,3)
    ops.fix(113, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 113,1)
    ops.remove("sp", 113,2)
    ops.remove("sp", 113,3)
    ops.fix(113, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 113,1)
    ops.remove("sp", 113,2)
    ops.remove("sp", 113,3)
    ops.fix(113, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 114,1)
    ops.remove("sp", 114,2)
    ops.remove("sp", 114,3)
    ops.fix(114, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 114,1)
    ops.remove("sp", 114,2)
    ops.remove("sp", 114,3)
    ops.fix(114, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 114,1)
    ops.remove("sp", 114,2)
    ops.remove("sp", 114,3)
    ops.fix(114, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 114,1)
    ops.remove("sp", 114,2)
    ops.remove("sp", 114,3)
    ops.fix(114, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 115,1)
    ops.remove("sp", 115,2)
    ops.remove("sp", 115,3)
    ops.fix(115, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 115,1)
    ops.remove("sp", 115,2)
    ops.remove("sp", 115,3)
    ops.fix(115, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 115,1)
    ops.remove("sp", 115,2)
    ops.remove("sp", 115,3)
    ops.fix(115, 0, 1, 0,0)
if pid == 5:
    ops.remove("sp", 115,1)
    ops.remove("sp", 115,2)
    ops.remove("sp", 115,3)
    ops.fix(115, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 116,1)
    ops.remove("sp", 116,2)
    ops.remove("sp", 116,3)
    ops.fix(116, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 116,1)
    ops.remove("sp", 116,2)
    ops.remove("sp", 116,3)
    ops.fix(116, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 116,1)
    ops.remove("sp", 116,2)
    ops.remove("sp", 116,3)
    ops.fix(116, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 117,1)
    ops.remove("sp", 117,2)
    ops.remove("sp", 117,3)
    ops.fix(117, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 117,1)
    ops.remove("sp", 117,2)
    ops.remove("sp", 117,3)
    ops.fix(117, 0, 1, 0,0)
if pid == 7:
    ops.remove("sp", 117,1)
    ops.remove("sp", 117,2)
    ops.remove("sp", 117,3)
    ops.fix(117, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 118,1)
    ops.remove("sp", 118,2)
    ops.remove("sp", 118,3)
    ops.fix(118, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 118,1)
    ops.remove("sp", 118,2)
    ops.remove("sp", 118,3)
    ops.fix(118, 0, 1, 0,0)
if pid == 6:
    ops.remove("sp", 118,1)
    ops.remove("sp", 118,2)
    ops.remove("sp", 118,3)
    ops.fix(118, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 119,1)
    ops.remove("sp", 119,2)
    ops.remove("sp", 119,3)
    ops.fix(119, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 119,1)
    ops.remove("sp", 119,2)
    ops.remove("sp", 119,3)
    ops.fix(119, 0, 1, 0,0)
if pid == 4:
    ops.remove("sp", 119,1)
    ops.remove("sp", 119,2)
    ops.remove("sp", 119,3)
    ops.fix(119, 0, 1, 0,0)
if pid == 2:
    ops.remove("sp", 120,1)
    ops.remove("sp", 120,2)
    ops.remove("sp", 120,3)
    ops.fix(120, 0, 1, 0,0)
if pid == 0:
    ops.remove("sp", 120,1)
    ops.remove("sp", 120,2)
    ops.remove("sp", 120,3)
    ops.fix(120, 0, 1, 0,0)
if pid == 3:
    ops.remove("sp", 120,1)
    ops.remove("sp", 120,2)
    ops.remove("sp", 120,3)
    ops.fix(120, 0, 1, 0,0)
ops.model("basicBuilder","-ndm",3,"-ndf",3)
if pid == 6:
    ops.remove("sp", 217,1)
    ops.remove("sp", 217,2)
    ops.remove("sp", 217,3)
    ops.fix(217, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 217,1)
    ops.remove("sp", 217,2)
    ops.remove("sp", 217,3)
    ops.fix(217, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 218,1)
    ops.remove("sp", 218,2)
    ops.remove("sp", 218,3)
    ops.fix(218, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 218,1)
    ops.remove("sp", 218,2)
    ops.remove("sp", 218,3)
    ops.fix(218, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 219,1)
    ops.remove("sp", 219,2)
    ops.remove("sp", 219,3)
    ops.fix(219, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 219,1)
    ops.remove("sp", 219,2)
    ops.remove("sp", 219,3)
    ops.fix(219, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 220,1)
    ops.remove("sp", 220,2)
    ops.remove("sp", 220,3)
    ops.fix(220, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 220,1)
    ops.remove("sp", 220,2)
    ops.remove("sp", 220,3)
    ops.fix(220, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 221,1)
    ops.remove("sp", 221,2)
    ops.remove("sp", 221,3)
    ops.fix(221, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 221,1)
    ops.remove("sp", 221,2)
    ops.remove("sp", 221,3)
    ops.fix(221, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 227,1)
    ops.remove("sp", 227,2)
    ops.remove("sp", 227,3)
    ops.fix(227, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 227,1)
    ops.remove("sp", 227,2)
    ops.remove("sp", 227,3)
    ops.fix(227, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 228,1)
    ops.remove("sp", 228,2)
    ops.remove("sp", 228,3)
    ops.fix(228, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 228,1)
    ops.remove("sp", 228,2)
    ops.remove("sp", 228,3)
    ops.fix(228, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 229,1)
    ops.remove("sp", 229,2)
    ops.remove("sp", 229,3)
    ops.fix(229, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 229,1)
    ops.remove("sp", 229,2)
    ops.remove("sp", 229,3)
    ops.fix(229, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 230,1)
    ops.remove("sp", 230,2)
    ops.remove("sp", 230,3)
    ops.fix(230, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 230,1)
    ops.remove("sp", 230,2)
    ops.remove("sp", 230,3)
    ops.fix(230, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 231,1)
    ops.remove("sp", 231,2)
    ops.remove("sp", 231,3)
    ops.fix(231, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 231,1)
    ops.remove("sp", 231,2)
    ops.remove("sp", 231,3)
    ops.fix(231, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 237,1)
    ops.remove("sp", 237,2)
    ops.remove("sp", 237,3)
    ops.fix(237, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 237,1)
    ops.remove("sp", 237,2)
    ops.remove("sp", 237,3)
    ops.fix(237, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 238,1)
    ops.remove("sp", 238,2)
    ops.remove("sp", 238,3)
    ops.fix(238, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 238,1)
    ops.remove("sp", 238,2)
    ops.remove("sp", 238,3)
    ops.fix(238, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 239,1)
    ops.remove("sp", 239,2)
    ops.remove("sp", 239,3)
    ops.fix(239, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 239,1)
    ops.remove("sp", 239,2)
    ops.remove("sp", 239,3)
    ops.fix(239, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 240,1)
    ops.remove("sp", 240,2)
    ops.remove("sp", 240,3)
    ops.fix(240, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 240,1)
    ops.remove("sp", 240,2)
    ops.remove("sp", 240,3)
    ops.fix(240, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 241,1)
    ops.remove("sp", 241,2)
    ops.remove("sp", 241,3)
    ops.fix(241, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 241,1)
    ops.remove("sp", 241,2)
    ops.remove("sp", 241,3)
    ops.fix(241, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 247,1)
    ops.remove("sp", 247,2)
    ops.remove("sp", 247,3)
    ops.fix(247, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 247,1)
    ops.remove("sp", 247,2)
    ops.remove("sp", 247,3)
    ops.fix(247, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 248,1)
    ops.remove("sp", 248,2)
    ops.remove("sp", 248,3)
    ops.fix(248, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 248,1)
    ops.remove("sp", 248,2)
    ops.remove("sp", 248,3)
    ops.fix(248, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 249,1)
    ops.remove("sp", 249,2)
    ops.remove("sp", 249,3)
    ops.fix(249, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 249,1)
    ops.remove("sp", 249,2)
    ops.remove("sp", 249,3)
    ops.fix(249, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 250,1)
    ops.remove("sp", 250,2)
    ops.remove("sp", 250,3)
    ops.fix(250, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 250,1)
    ops.remove("sp", 250,2)
    ops.remove("sp", 250,3)
    ops.fix(250, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 251,1)
    ops.remove("sp", 251,2)
    ops.remove("sp", 251,3)
    ops.fix(251, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 251,1)
    ops.remove("sp", 251,2)
    ops.remove("sp", 251,3)
    ops.fix(251, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 257,1)
    ops.remove("sp", 257,2)
    ops.remove("sp", 257,3)
    ops.fix(257, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 257,1)
    ops.remove("sp", 257,2)
    ops.remove("sp", 257,3)
    ops.fix(257, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 258,1)
    ops.remove("sp", 258,2)
    ops.remove("sp", 258,3)
    ops.fix(258, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 258,1)
    ops.remove("sp", 258,2)
    ops.remove("sp", 258,3)
    ops.fix(258, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 259,1)
    ops.remove("sp", 259,2)
    ops.remove("sp", 259,3)
    ops.fix(259, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 259,1)
    ops.remove("sp", 259,2)
    ops.remove("sp", 259,3)
    ops.fix(259, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 260,1)
    ops.remove("sp", 260,2)
    ops.remove("sp", 260,3)
    ops.fix(260, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 260,1)
    ops.remove("sp", 260,2)
    ops.remove("sp", 260,3)
    ops.fix(260, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 261,1)
    ops.remove("sp", 261,2)
    ops.remove("sp", 261,3)
    ops.fix(261, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 261,1)
    ops.remove("sp", 261,2)
    ops.remove("sp", 261,3)
    ops.fix(261, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 262,1)
    ops.remove("sp", 262,2)
    ops.remove("sp", 262,3)
    ops.fix(262, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 262,1)
    ops.remove("sp", 262,2)
    ops.remove("sp", 262,3)
    ops.fix(262, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 263,1)
    ops.remove("sp", 263,2)
    ops.remove("sp", 263,3)
    ops.fix(263, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 263,1)
    ops.remove("sp", 263,2)
    ops.remove("sp", 263,3)
    ops.fix(263, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 264,1)
    ops.remove("sp", 264,2)
    ops.remove("sp", 264,3)
    ops.fix(264, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 264,1)
    ops.remove("sp", 264,2)
    ops.remove("sp", 264,3)
    ops.fix(264, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 265,1)
    ops.remove("sp", 265,2)
    ops.remove("sp", 265,3)
    ops.fix(265, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 265,1)
    ops.remove("sp", 265,2)
    ops.remove("sp", 265,3)
    ops.fix(265, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 266,1)
    ops.remove("sp", 266,2)
    ops.remove("sp", 266,3)
    ops.fix(266, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 266,1)
    ops.remove("sp", 266,2)
    ops.remove("sp", 266,3)
    ops.fix(266, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 267,1)
    ops.remove("sp", 267,2)
    ops.remove("sp", 267,3)
    ops.fix(267, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 267,1)
    ops.remove("sp", 267,2)
    ops.remove("sp", 267,3)
    ops.fix(267, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 268,1)
    ops.remove("sp", 268,2)
    ops.remove("sp", 268,3)
    ops.fix(268, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 268,1)
    ops.remove("sp", 268,2)
    ops.remove("sp", 268,3)
    ops.fix(268, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 269,1)
    ops.remove("sp", 269,2)
    ops.remove("sp", 269,3)
    ops.fix(269, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 269,1)
    ops.remove("sp", 269,2)
    ops.remove("sp", 269,3)
    ops.fix(269, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 270,1)
    ops.remove("sp", 270,2)
    ops.remove("sp", 270,3)
    ops.fix(270, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 270,1)
    ops.remove("sp", 270,2)
    ops.remove("sp", 270,3)
    ops.fix(270, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 271,1)
    ops.remove("sp", 271,2)
    ops.remove("sp", 271,3)
    ops.fix(271, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 271,1)
    ops.remove("sp", 271,2)
    ops.remove("sp", 271,3)
    ops.fix(271, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 272,1)
    ops.remove("sp", 272,2)
    ops.remove("sp", 272,3)
    ops.fix(272, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 272,1)
    ops.remove("sp", 272,2)
    ops.remove("sp", 272,3)
    ops.fix(272, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 273,1)
    ops.remove("sp", 273,2)
    ops.remove("sp", 273,3)
    ops.fix(273, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 273,1)
    ops.remove("sp", 273,2)
    ops.remove("sp", 273,3)
    ops.fix(273, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 274,1)
    ops.remove("sp", 274,2)
    ops.remove("sp", 274,3)
    ops.fix(274, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 274,1)
    ops.remove("sp", 274,2)
    ops.remove("sp", 274,3)
    ops.fix(274, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 275,1)
    ops.remove("sp", 275,2)
    ops.remove("sp", 275,3)
    ops.fix(275, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 275,1)
    ops.remove("sp", 275,2)
    ops.remove("sp", 275,3)
    ops.fix(275, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 276,1)
    ops.remove("sp", 276,2)
    ops.remove("sp", 276,3)
    ops.fix(276, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 276,1)
    ops.remove("sp", 276,2)
    ops.remove("sp", 276,3)
    ops.fix(276, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 357,1)
    ops.remove("sp", 357,2)
    ops.remove("sp", 357,3)
    ops.fix(357, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 357,1)
    ops.remove("sp", 357,2)
    ops.remove("sp", 357,3)
    ops.fix(357, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 358,1)
    ops.remove("sp", 358,2)
    ops.remove("sp", 358,3)
    ops.fix(358, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 358,1)
    ops.remove("sp", 358,2)
    ops.remove("sp", 358,3)
    ops.fix(358, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 358,1)
    ops.remove("sp", 358,2)
    ops.remove("sp", 358,3)
    ops.fix(358, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 359,1)
    ops.remove("sp", 359,2)
    ops.remove("sp", 359,3)
    ops.fix(359, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 359,1)
    ops.remove("sp", 359,2)
    ops.remove("sp", 359,3)
    ops.fix(359, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 360,1)
    ops.remove("sp", 360,2)
    ops.remove("sp", 360,3)
    ops.fix(360, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 360,1)
    ops.remove("sp", 360,2)
    ops.remove("sp", 360,3)
    ops.fix(360, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 360,1)
    ops.remove("sp", 360,2)
    ops.remove("sp", 360,3)
    ops.fix(360, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 361,1)
    ops.remove("sp", 361,2)
    ops.remove("sp", 361,3)
    ops.fix(361, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 361,1)
    ops.remove("sp", 361,2)
    ops.remove("sp", 361,3)
    ops.fix(361, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 362,1)
    ops.remove("sp", 362,2)
    ops.remove("sp", 362,3)
    ops.fix(362, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 362,1)
    ops.remove("sp", 362,2)
    ops.remove("sp", 362,3)
    ops.fix(362, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 362,1)
    ops.remove("sp", 362,2)
    ops.remove("sp", 362,3)
    ops.fix(362, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 363,1)
    ops.remove("sp", 363,2)
    ops.remove("sp", 363,3)
    ops.fix(363, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 363,1)
    ops.remove("sp", 363,2)
    ops.remove("sp", 363,3)
    ops.fix(363, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 364,1)
    ops.remove("sp", 364,2)
    ops.remove("sp", 364,3)
    ops.fix(364, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 364,1)
    ops.remove("sp", 364,2)
    ops.remove("sp", 364,3)
    ops.fix(364, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 364,1)
    ops.remove("sp", 364,2)
    ops.remove("sp", 364,3)
    ops.fix(364, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 365,1)
    ops.remove("sp", 365,2)
    ops.remove("sp", 365,3)
    ops.fix(365, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 365,1)
    ops.remove("sp", 365,2)
    ops.remove("sp", 365,3)
    ops.fix(365, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 366,1)
    ops.remove("sp", 366,2)
    ops.remove("sp", 366,3)
    ops.fix(366, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 366,1)
    ops.remove("sp", 366,2)
    ops.remove("sp", 366,3)
    ops.fix(366, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 367,1)
    ops.remove("sp", 367,2)
    ops.remove("sp", 367,3)
    ops.fix(367, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 367,1)
    ops.remove("sp", 367,2)
    ops.remove("sp", 367,3)
    ops.fix(367, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 367,1)
    ops.remove("sp", 367,2)
    ops.remove("sp", 367,3)
    ops.fix(367, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 368,1)
    ops.remove("sp", 368,2)
    ops.remove("sp", 368,3)
    ops.fix(368, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 368,1)
    ops.remove("sp", 368,2)
    ops.remove("sp", 368,3)
    ops.fix(368, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 369,1)
    ops.remove("sp", 369,2)
    ops.remove("sp", 369,3)
    ops.fix(369, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 369,1)
    ops.remove("sp", 369,2)
    ops.remove("sp", 369,3)
    ops.fix(369, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 369,1)
    ops.remove("sp", 369,2)
    ops.remove("sp", 369,3)
    ops.fix(369, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 370,1)
    ops.remove("sp", 370,2)
    ops.remove("sp", 370,3)
    ops.fix(370, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 370,1)
    ops.remove("sp", 370,2)
    ops.remove("sp", 370,3)
    ops.fix(370, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 371,1)
    ops.remove("sp", 371,2)
    ops.remove("sp", 371,3)
    ops.fix(371, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 371,1)
    ops.remove("sp", 371,2)
    ops.remove("sp", 371,3)
    ops.fix(371, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 371,1)
    ops.remove("sp", 371,2)
    ops.remove("sp", 371,3)
    ops.fix(371, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 372,1)
    ops.remove("sp", 372,2)
    ops.remove("sp", 372,3)
    ops.fix(372, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 372,1)
    ops.remove("sp", 372,2)
    ops.remove("sp", 372,3)
    ops.fix(372, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 373,1)
    ops.remove("sp", 373,2)
    ops.remove("sp", 373,3)
    ops.fix(373, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 373,1)
    ops.remove("sp", 373,2)
    ops.remove("sp", 373,3)
    ops.fix(373, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 373,1)
    ops.remove("sp", 373,2)
    ops.remove("sp", 373,3)
    ops.fix(373, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 374,1)
    ops.remove("sp", 374,2)
    ops.remove("sp", 374,3)
    ops.fix(374, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 374,1)
    ops.remove("sp", 374,2)
    ops.remove("sp", 374,3)
    ops.fix(374, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 375,1)
    ops.remove("sp", 375,2)
    ops.remove("sp", 375,3)
    ops.fix(375, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 375,1)
    ops.remove("sp", 375,2)
    ops.remove("sp", 375,3)
    ops.fix(375, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 376,1)
    ops.remove("sp", 376,2)
    ops.remove("sp", 376,3)
    ops.fix(376, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 376,1)
    ops.remove("sp", 376,2)
    ops.remove("sp", 376,3)
    ops.fix(376, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 376,1)
    ops.remove("sp", 376,2)
    ops.remove("sp", 376,3)
    ops.fix(376, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 377,1)
    ops.remove("sp", 377,2)
    ops.remove("sp", 377,3)
    ops.fix(377, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 377,1)
    ops.remove("sp", 377,2)
    ops.remove("sp", 377,3)
    ops.fix(377, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 378,1)
    ops.remove("sp", 378,2)
    ops.remove("sp", 378,3)
    ops.fix(378, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 378,1)
    ops.remove("sp", 378,2)
    ops.remove("sp", 378,3)
    ops.fix(378, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 378,1)
    ops.remove("sp", 378,2)
    ops.remove("sp", 378,3)
    ops.fix(378, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 379,1)
    ops.remove("sp", 379,2)
    ops.remove("sp", 379,3)
    ops.fix(379, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 379,1)
    ops.remove("sp", 379,2)
    ops.remove("sp", 379,3)
    ops.fix(379, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 380,1)
    ops.remove("sp", 380,2)
    ops.remove("sp", 380,3)
    ops.fix(380, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 380,1)
    ops.remove("sp", 380,2)
    ops.remove("sp", 380,3)
    ops.fix(380, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 380,1)
    ops.remove("sp", 380,2)
    ops.remove("sp", 380,3)
    ops.fix(380, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 381,1)
    ops.remove("sp", 381,2)
    ops.remove("sp", 381,3)
    ops.fix(381, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 381,1)
    ops.remove("sp", 381,2)
    ops.remove("sp", 381,3)
    ops.fix(381, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 382,1)
    ops.remove("sp", 382,2)
    ops.remove("sp", 382,3)
    ops.fix(382, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 382,1)
    ops.remove("sp", 382,2)
    ops.remove("sp", 382,3)
    ops.fix(382, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 382,1)
    ops.remove("sp", 382,2)
    ops.remove("sp", 382,3)
    ops.fix(382, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 383,1)
    ops.remove("sp", 383,2)
    ops.remove("sp", 383,3)
    ops.fix(383, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 383,1)
    ops.remove("sp", 383,2)
    ops.remove("sp", 383,3)
    ops.fix(383, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 384,1)
    ops.remove("sp", 384,2)
    ops.remove("sp", 384,3)
    ops.fix(384, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 384,1)
    ops.remove("sp", 384,2)
    ops.remove("sp", 384,3)
    ops.fix(384, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 385,1)
    ops.remove("sp", 385,2)
    ops.remove("sp", 385,3)
    ops.fix(385, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 385,1)
    ops.remove("sp", 385,2)
    ops.remove("sp", 385,3)
    ops.fix(385, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 385,1)
    ops.remove("sp", 385,2)
    ops.remove("sp", 385,3)
    ops.fix(385, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 386,1)
    ops.remove("sp", 386,2)
    ops.remove("sp", 386,3)
    ops.fix(386, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 386,1)
    ops.remove("sp", 386,2)
    ops.remove("sp", 386,3)
    ops.fix(386, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 387,1)
    ops.remove("sp", 387,2)
    ops.remove("sp", 387,3)
    ops.fix(387, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 387,1)
    ops.remove("sp", 387,2)
    ops.remove("sp", 387,3)
    ops.fix(387, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 387,1)
    ops.remove("sp", 387,2)
    ops.remove("sp", 387,3)
    ops.fix(387, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 388,1)
    ops.remove("sp", 388,2)
    ops.remove("sp", 388,3)
    ops.fix(388, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 388,1)
    ops.remove("sp", 388,2)
    ops.remove("sp", 388,3)
    ops.fix(388, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 388,1)
    ops.remove("sp", 388,2)
    ops.remove("sp", 388,3)
    ops.fix(388, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 389,1)
    ops.remove("sp", 389,2)
    ops.remove("sp", 389,3)
    ops.fix(389, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 389,1)
    ops.remove("sp", 389,2)
    ops.remove("sp", 389,3)
    ops.fix(389, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 389,1)
    ops.remove("sp", 389,2)
    ops.remove("sp", 389,3)
    ops.fix(389, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 390,1)
    ops.remove("sp", 390,2)
    ops.remove("sp", 390,3)
    ops.fix(390, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 390,1)
    ops.remove("sp", 390,2)
    ops.remove("sp", 390,3)
    ops.fix(390, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 391,1)
    ops.remove("sp", 391,2)
    ops.remove("sp", 391,3)
    ops.fix(391, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 391,1)
    ops.remove("sp", 391,2)
    ops.remove("sp", 391,3)
    ops.fix(391, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 391,1)
    ops.remove("sp", 391,2)
    ops.remove("sp", 391,3)
    ops.fix(391, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 392,1)
    ops.remove("sp", 392,2)
    ops.remove("sp", 392,3)
    ops.fix(392, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 392,1)
    ops.remove("sp", 392,2)
    ops.remove("sp", 392,3)
    ops.fix(392, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 393,1)
    ops.remove("sp", 393,2)
    ops.remove("sp", 393,3)
    ops.fix(393, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 393,1)
    ops.remove("sp", 393,2)
    ops.remove("sp", 393,3)
    ops.fix(393, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 393,1)
    ops.remove("sp", 393,2)
    ops.remove("sp", 393,3)
    ops.fix(393, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 394,1)
    ops.remove("sp", 394,2)
    ops.remove("sp", 394,3)
    ops.fix(394, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 394,1)
    ops.remove("sp", 394,2)
    ops.remove("sp", 394,3)
    ops.fix(394, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 394,1)
    ops.remove("sp", 394,2)
    ops.remove("sp", 394,3)
    ops.fix(394, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 395,1)
    ops.remove("sp", 395,2)
    ops.remove("sp", 395,3)
    ops.fix(395, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 395,1)
    ops.remove("sp", 395,2)
    ops.remove("sp", 395,3)
    ops.fix(395, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 395,1)
    ops.remove("sp", 395,2)
    ops.remove("sp", 395,3)
    ops.fix(395, 0, 1, 0)
if pid == 1:
    ops.remove("sp", 396,1)
    ops.remove("sp", 396,2)
    ops.remove("sp", 396,3)
    ops.fix(396, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 396,1)
    ops.remove("sp", 396,2)
    ops.remove("sp", 396,3)
    ops.fix(396, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 396,1)
    ops.remove("sp", 396,2)
    ops.remove("sp", 396,3)
    ops.fix(396, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 397,1)
    ops.remove("sp", 397,2)
    ops.remove("sp", 397,3)
    ops.fix(397, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 397,1)
    ops.remove("sp", 397,2)
    ops.remove("sp", 397,3)
    ops.fix(397, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 398,1)
    ops.remove("sp", 398,2)
    ops.remove("sp", 398,3)
    ops.fix(398, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 398,1)
    ops.remove("sp", 398,2)
    ops.remove("sp", 398,3)
    ops.fix(398, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 398,1)
    ops.remove("sp", 398,2)
    ops.remove("sp", 398,3)
    ops.fix(398, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 399,1)
    ops.remove("sp", 399,2)
    ops.remove("sp", 399,3)
    ops.fix(399, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 399,1)
    ops.remove("sp", 399,2)
    ops.remove("sp", 399,3)
    ops.fix(399, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 400,1)
    ops.remove("sp", 400,2)
    ops.remove("sp", 400,3)
    ops.fix(400, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 400,1)
    ops.remove("sp", 400,2)
    ops.remove("sp", 400,3)
    ops.fix(400, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 400,1)
    ops.remove("sp", 400,2)
    ops.remove("sp", 400,3)
    ops.fix(400, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 401,1)
    ops.remove("sp", 401,2)
    ops.remove("sp", 401,3)
    ops.fix(401, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 401,1)
    ops.remove("sp", 401,2)
    ops.remove("sp", 401,3)
    ops.fix(401, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 402,1)
    ops.remove("sp", 402,2)
    ops.remove("sp", 402,3)
    ops.fix(402, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 402,1)
    ops.remove("sp", 402,2)
    ops.remove("sp", 402,3)
    ops.fix(402, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 402,1)
    ops.remove("sp", 402,2)
    ops.remove("sp", 402,3)
    ops.fix(402, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 403,1)
    ops.remove("sp", 403,2)
    ops.remove("sp", 403,3)
    ops.fix(403, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 403,1)
    ops.remove("sp", 403,2)
    ops.remove("sp", 403,3)
    ops.fix(403, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 404,1)
    ops.remove("sp", 404,2)
    ops.remove("sp", 404,3)
    ops.fix(404, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 404,1)
    ops.remove("sp", 404,2)
    ops.remove("sp", 404,3)
    ops.fix(404, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 404,1)
    ops.remove("sp", 404,2)
    ops.remove("sp", 404,3)
    ops.fix(404, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 405,1)
    ops.remove("sp", 405,2)
    ops.remove("sp", 405,3)
    ops.fix(405, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 405,1)
    ops.remove("sp", 405,2)
    ops.remove("sp", 405,3)
    ops.fix(405, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 406,1)
    ops.remove("sp", 406,2)
    ops.remove("sp", 406,3)
    ops.fix(406, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 406,1)
    ops.remove("sp", 406,2)
    ops.remove("sp", 406,3)
    ops.fix(406, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 407,1)
    ops.remove("sp", 407,2)
    ops.remove("sp", 407,3)
    ops.fix(407, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 407,1)
    ops.remove("sp", 407,2)
    ops.remove("sp", 407,3)
    ops.fix(407, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 407,1)
    ops.remove("sp", 407,2)
    ops.remove("sp", 407,3)
    ops.fix(407, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 408,1)
    ops.remove("sp", 408,2)
    ops.remove("sp", 408,3)
    ops.fix(408, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 408,1)
    ops.remove("sp", 408,2)
    ops.remove("sp", 408,3)
    ops.fix(408, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 409,1)
    ops.remove("sp", 409,2)
    ops.remove("sp", 409,3)
    ops.fix(409, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 409,1)
    ops.remove("sp", 409,2)
    ops.remove("sp", 409,3)
    ops.fix(409, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 409,1)
    ops.remove("sp", 409,2)
    ops.remove("sp", 409,3)
    ops.fix(409, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 410,1)
    ops.remove("sp", 410,2)
    ops.remove("sp", 410,3)
    ops.fix(410, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 410,1)
    ops.remove("sp", 410,2)
    ops.remove("sp", 410,3)
    ops.fix(410, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 411,1)
    ops.remove("sp", 411,2)
    ops.remove("sp", 411,3)
    ops.fix(411, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 411,1)
    ops.remove("sp", 411,2)
    ops.remove("sp", 411,3)
    ops.fix(411, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 411,1)
    ops.remove("sp", 411,2)
    ops.remove("sp", 411,3)
    ops.fix(411, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 412,1)
    ops.remove("sp", 412,2)
    ops.remove("sp", 412,3)
    ops.fix(412, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 412,1)
    ops.remove("sp", 412,2)
    ops.remove("sp", 412,3)
    ops.fix(412, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 413,1)
    ops.remove("sp", 413,2)
    ops.remove("sp", 413,3)
    ops.fix(413, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 413,1)
    ops.remove("sp", 413,2)
    ops.remove("sp", 413,3)
    ops.fix(413, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 413,1)
    ops.remove("sp", 413,2)
    ops.remove("sp", 413,3)
    ops.fix(413, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 414,1)
    ops.remove("sp", 414,2)
    ops.remove("sp", 414,3)
    ops.fix(414, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 414,1)
    ops.remove("sp", 414,2)
    ops.remove("sp", 414,3)
    ops.fix(414, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 415,1)
    ops.remove("sp", 415,2)
    ops.remove("sp", 415,3)
    ops.fix(415, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 415,1)
    ops.remove("sp", 415,2)
    ops.remove("sp", 415,3)
    ops.fix(415, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 416,1)
    ops.remove("sp", 416,2)
    ops.remove("sp", 416,3)
    ops.fix(416, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 416,1)
    ops.remove("sp", 416,2)
    ops.remove("sp", 416,3)
    ops.fix(416, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 416,1)
    ops.remove("sp", 416,2)
    ops.remove("sp", 416,3)
    ops.fix(416, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 417,1)
    ops.remove("sp", 417,2)
    ops.remove("sp", 417,3)
    ops.fix(417, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 417,1)
    ops.remove("sp", 417,2)
    ops.remove("sp", 417,3)
    ops.fix(417, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 418,1)
    ops.remove("sp", 418,2)
    ops.remove("sp", 418,3)
    ops.fix(418, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 418,1)
    ops.remove("sp", 418,2)
    ops.remove("sp", 418,3)
    ops.fix(418, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 418,1)
    ops.remove("sp", 418,2)
    ops.remove("sp", 418,3)
    ops.fix(418, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 419,1)
    ops.remove("sp", 419,2)
    ops.remove("sp", 419,3)
    ops.fix(419, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 419,1)
    ops.remove("sp", 419,2)
    ops.remove("sp", 419,3)
    ops.fix(419, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 419,1)
    ops.remove("sp", 419,2)
    ops.remove("sp", 419,3)
    ops.fix(419, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 420,1)
    ops.remove("sp", 420,2)
    ops.remove("sp", 420,3)
    ops.fix(420, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 420,1)
    ops.remove("sp", 420,2)
    ops.remove("sp", 420,3)
    ops.fix(420, 0, 1, 0)
if pid == 5:
    ops.remove("sp", 420,1)
    ops.remove("sp", 420,2)
    ops.remove("sp", 420,3)
    ops.fix(420, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 421,1)
    ops.remove("sp", 421,2)
    ops.remove("sp", 421,3)
    ops.fix(421, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 421,1)
    ops.remove("sp", 421,2)
    ops.remove("sp", 421,3)
    ops.fix(421, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 422,1)
    ops.remove("sp", 422,2)
    ops.remove("sp", 422,3)
    ops.fix(422, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 422,1)
    ops.remove("sp", 422,2)
    ops.remove("sp", 422,3)
    ops.fix(422, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 422,1)
    ops.remove("sp", 422,2)
    ops.remove("sp", 422,3)
    ops.fix(422, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 423,1)
    ops.remove("sp", 423,2)
    ops.remove("sp", 423,3)
    ops.fix(423, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 423,1)
    ops.remove("sp", 423,2)
    ops.remove("sp", 423,3)
    ops.fix(423, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 424,1)
    ops.remove("sp", 424,2)
    ops.remove("sp", 424,3)
    ops.fix(424, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 424,1)
    ops.remove("sp", 424,2)
    ops.remove("sp", 424,3)
    ops.fix(424, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 425,1)
    ops.remove("sp", 425,2)
    ops.remove("sp", 425,3)
    ops.fix(425, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 425,1)
    ops.remove("sp", 425,2)
    ops.remove("sp", 425,3)
    ops.fix(425, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 425,1)
    ops.remove("sp", 425,2)
    ops.remove("sp", 425,3)
    ops.fix(425, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 426,1)
    ops.remove("sp", 426,2)
    ops.remove("sp", 426,3)
    ops.fix(426, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 426,1)
    ops.remove("sp", 426,2)
    ops.remove("sp", 426,3)
    ops.fix(426, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 427,1)
    ops.remove("sp", 427,2)
    ops.remove("sp", 427,3)
    ops.fix(427, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 427,1)
    ops.remove("sp", 427,2)
    ops.remove("sp", 427,3)
    ops.fix(427, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 427,1)
    ops.remove("sp", 427,2)
    ops.remove("sp", 427,3)
    ops.fix(427, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 428,1)
    ops.remove("sp", 428,2)
    ops.remove("sp", 428,3)
    ops.fix(428, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 428,1)
    ops.remove("sp", 428,2)
    ops.remove("sp", 428,3)
    ops.fix(428, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 429,1)
    ops.remove("sp", 429,2)
    ops.remove("sp", 429,3)
    ops.fix(429, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 429,1)
    ops.remove("sp", 429,2)
    ops.remove("sp", 429,3)
    ops.fix(429, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 429,1)
    ops.remove("sp", 429,2)
    ops.remove("sp", 429,3)
    ops.fix(429, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 430,1)
    ops.remove("sp", 430,2)
    ops.remove("sp", 430,3)
    ops.fix(430, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 430,1)
    ops.remove("sp", 430,2)
    ops.remove("sp", 430,3)
    ops.fix(430, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 431,1)
    ops.remove("sp", 431,2)
    ops.remove("sp", 431,3)
    ops.fix(431, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 431,1)
    ops.remove("sp", 431,2)
    ops.remove("sp", 431,3)
    ops.fix(431, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 431,1)
    ops.remove("sp", 431,2)
    ops.remove("sp", 431,3)
    ops.fix(431, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 432,1)
    ops.remove("sp", 432,2)
    ops.remove("sp", 432,3)
    ops.fix(432, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 432,1)
    ops.remove("sp", 432,2)
    ops.remove("sp", 432,3)
    ops.fix(432, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 433,1)
    ops.remove("sp", 433,2)
    ops.remove("sp", 433,3)
    ops.fix(433, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 433,1)
    ops.remove("sp", 433,2)
    ops.remove("sp", 433,3)
    ops.fix(433, 0, 1, 0)
if pid == 7:
    ops.remove("sp", 433,1)
    ops.remove("sp", 433,2)
    ops.remove("sp", 433,3)
    ops.fix(433, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 434,1)
    ops.remove("sp", 434,2)
    ops.remove("sp", 434,3)
    ops.fix(434, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 434,1)
    ops.remove("sp", 434,2)
    ops.remove("sp", 434,3)
    ops.fix(434, 0, 1, 0)
if pid == 6:
    ops.remove("sp", 434,1)
    ops.remove("sp", 434,2)
    ops.remove("sp", 434,3)
    ops.fix(434, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 435,1)
    ops.remove("sp", 435,2)
    ops.remove("sp", 435,3)
    ops.fix(435, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 435,1)
    ops.remove("sp", 435,2)
    ops.remove("sp", 435,3)
    ops.fix(435, 0, 1, 0)
if pid == 4:
    ops.remove("sp", 435,1)
    ops.remove("sp", 435,2)
    ops.remove("sp", 435,3)
    ops.fix(435, 0, 1, 0)
if pid == 2:
    ops.remove("sp", 436,1)
    ops.remove("sp", 436,2)
    ops.remove("sp", 436,3)
    ops.fix(436, 0, 1, 0)
if pid == 0:
    ops.remove("sp", 436,1)
    ops.remove("sp", 436,2)
    ops.remove("sp", 436,3)
    ops.fix(436, 0, 1, 0)
if pid == 3:
    ops.remove("sp", 436,1)
    ops.remove("sp", 436,2)
    ops.remove("sp", 436,3)
    ops.fix(436, 0, 1, 0)
    ops.model("basicBuilder","-ndm",3,"-ndf",4)
if pid == 6:
    ops.remove("sp", 2,1)
    ops.remove("sp", 2,2)
    ops.remove("sp", 2,3)
    ops.fix(2, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 2,1)
    ops.remove("sp", 2,2)
    ops.remove("sp", 2,3)
    ops.fix(2, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 4,1)
    ops.remove("sp", 4,2)
    ops.remove("sp", 4,3)
    ops.fix(4, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 4,1)
    ops.remove("sp", 4,2)
    ops.remove("sp", 4,3)
    ops.fix(4, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 6,1)
    ops.remove("sp", 6,2)
    ops.remove("sp", 6,3)
    ops.fix(6, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 6,1)
    ops.remove("sp", 6,2)
    ops.remove("sp", 6,3)
    ops.fix(6, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 8,1)
    ops.remove("sp", 8,2)
    ops.remove("sp", 8,3)
    ops.fix(8, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 8,1)
    ops.remove("sp", 8,2)
    ops.remove("sp", 8,3)
    ops.fix(8, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 21,1)
    ops.remove("sp", 21,2)
    ops.remove("sp", 21,3)
    ops.fix(21, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 21,1)
    ops.remove("sp", 21,2)
    ops.remove("sp", 21,3)
    ops.fix(21, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 22,1)
    ops.remove("sp", 22,2)
    ops.remove("sp", 22,3)
    ops.fix(22, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 22,1)
    ops.remove("sp", 22,2)
    ops.remove("sp", 22,3)
    ops.fix(22, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 22,1)
    ops.remove("sp", 22,2)
    ops.remove("sp", 22,3)
    ops.fix(22, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 23,1)
    ops.remove("sp", 23,2)
    ops.remove("sp", 23,3)
    ops.fix(23, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 23,1)
    ops.remove("sp", 23,2)
    ops.remove("sp", 23,3)
    ops.fix(23, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 24,1)
    ops.remove("sp", 24,2)
    ops.remove("sp", 24,3)
    ops.fix(24, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 24,1)
    ops.remove("sp", 24,2)
    ops.remove("sp", 24,3)
    ops.fix(24, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 37,1)
    ops.remove("sp", 37,2)
    ops.remove("sp", 37,3)
    ops.fix(37, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 37,1)
    ops.remove("sp", 37,2)
    ops.remove("sp", 37,3)
    ops.fix(37, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 37,1)
    ops.remove("sp", 37,2)
    ops.remove("sp", 37,3)
    ops.fix(37, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 38,1)
    ops.remove("sp", 38,2)
    ops.remove("sp", 38,3)
    ops.fix(38, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 38,1)
    ops.remove("sp", 38,2)
    ops.remove("sp", 38,3)
    ops.fix(38, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 39,1)
    ops.remove("sp", 39,2)
    ops.remove("sp", 39,3)
    ops.fix(39, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 39,1)
    ops.remove("sp", 39,2)
    ops.remove("sp", 39,3)
    ops.fix(39, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 40,1)
    ops.remove("sp", 40,2)
    ops.remove("sp", 40,3)
    ops.fix(40, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 40,1)
    ops.remove("sp", 40,2)
    ops.remove("sp", 40,3)
    ops.fix(40, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 41,1)
    ops.remove("sp", 41,2)
    ops.remove("sp", 41,3)
    ops.fix(41, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 41,1)
    ops.remove("sp", 41,2)
    ops.remove("sp", 41,3)
    ops.fix(41, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 42,1)
    ops.remove("sp", 42,2)
    ops.remove("sp", 42,3)
    ops.fix(42, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 42,1)
    ops.remove("sp", 42,2)
    ops.remove("sp", 42,3)
    ops.fix(42, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 43,1)
    ops.remove("sp", 43,2)
    ops.remove("sp", 43,3)
    ops.fix(43, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 43,1)
    ops.remove("sp", 43,2)
    ops.remove("sp", 43,3)
    ops.fix(43, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 44,1)
    ops.remove("sp", 44,2)
    ops.remove("sp", 44,3)
    ops.fix(44, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 44,1)
    ops.remove("sp", 44,2)
    ops.remove("sp", 44,3)
    ops.fix(44, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 49,1)
    ops.remove("sp", 49,2)
    ops.remove("sp", 49,3)
    ops.fix(49, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 49,1)
    ops.remove("sp", 49,2)
    ops.remove("sp", 49,3)
    ops.fix(49, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 50,1)
    ops.remove("sp", 50,2)
    ops.remove("sp", 50,3)
    ops.fix(50, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 50,1)
    ops.remove("sp", 50,2)
    ops.remove("sp", 50,3)
    ops.fix(50, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 51,1)
    ops.remove("sp", 51,2)
    ops.remove("sp", 51,3)
    ops.fix(51, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 51,1)
    ops.remove("sp", 51,2)
    ops.remove("sp", 51,3)
    ops.fix(51, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 52,1)
    ops.remove("sp", 52,2)
    ops.remove("sp", 52,3)
    ops.fix(52, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 52,1)
    ops.remove("sp", 52,2)
    ops.remove("sp", 52,3)
    ops.fix(52, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 121,1)
    ops.remove("sp", 121,2)
    ops.remove("sp", 121,3)
    ops.fix(121, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 121,1)
    ops.remove("sp", 121,2)
    ops.remove("sp", 121,3)
    ops.fix(121, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 122,1)
    ops.remove("sp", 122,2)
    ops.remove("sp", 122,3)
    ops.fix(122, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 122,1)
    ops.remove("sp", 122,2)
    ops.remove("sp", 122,3)
    ops.fix(122, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 123,1)
    ops.remove("sp", 123,2)
    ops.remove("sp", 123,3)
    ops.fix(123, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 123,1)
    ops.remove("sp", 123,2)
    ops.remove("sp", 123,3)
    ops.fix(123, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 123,1)
    ops.remove("sp", 123,2)
    ops.remove("sp", 123,3)
    ops.fix(123, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 124,1)
    ops.remove("sp", 124,2)
    ops.remove("sp", 124,3)
    ops.fix(124, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 124,1)
    ops.remove("sp", 124,2)
    ops.remove("sp", 124,3)
    ops.fix(124, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 124,1)
    ops.remove("sp", 124,2)
    ops.remove("sp", 124,3)
    ops.fix(124, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 125,1)
    ops.remove("sp", 125,2)
    ops.remove("sp", 125,3)
    ops.fix(125, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 125,1)
    ops.remove("sp", 125,2)
    ops.remove("sp", 125,3)
    ops.fix(125, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 125,1)
    ops.remove("sp", 125,2)
    ops.remove("sp", 125,3)
    ops.fix(125, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 126,1)
    ops.remove("sp", 126,2)
    ops.remove("sp", 126,3)
    ops.fix(126, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 126,1)
    ops.remove("sp", 126,2)
    ops.remove("sp", 126,3)
    ops.fix(126, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 126,1)
    ops.remove("sp", 126,2)
    ops.remove("sp", 126,3)
    ops.fix(126, 0, 0, 1,0)
if pid == 6:
    ops.remove("sp", 127,1)
    ops.remove("sp", 127,2)
    ops.remove("sp", 127,3)
    ops.fix(127, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 127,1)
    ops.remove("sp", 127,2)
    ops.remove("sp", 127,3)
    ops.fix(127, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 127,1)
    ops.remove("sp", 127,2)
    ops.remove("sp", 127,3)
    ops.fix(127, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 128,1)
    ops.remove("sp", 128,2)
    ops.remove("sp", 128,3)
    ops.fix(128, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 128,1)
    ops.remove("sp", 128,2)
    ops.remove("sp", 128,3)
    ops.fix(128, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 129,1)
    ops.remove("sp", 129,2)
    ops.remove("sp", 129,3)
    ops.fix(129, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 129,1)
    ops.remove("sp", 129,2)
    ops.remove("sp", 129,3)
    ops.fix(129, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 130,1)
    ops.remove("sp", 130,2)
    ops.remove("sp", 130,3)
    ops.fix(130, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 130,1)
    ops.remove("sp", 130,2)
    ops.remove("sp", 130,3)
    ops.fix(130, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 131,1)
    ops.remove("sp", 131,2)
    ops.remove("sp", 131,3)
    ops.fix(131, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 131,1)
    ops.remove("sp", 131,2)
    ops.remove("sp", 131,3)
    ops.fix(131, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 132,1)
    ops.remove("sp", 132,2)
    ops.remove("sp", 132,3)
    ops.fix(132, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 132,1)
    ops.remove("sp", 132,2)
    ops.remove("sp", 132,3)
    ops.fix(132, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 133,1)
    ops.remove("sp", 133,2)
    ops.remove("sp", 133,3)
    ops.fix(133, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 133,1)
    ops.remove("sp", 133,2)
    ops.remove("sp", 133,3)
    ops.fix(133, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 134,1)
    ops.remove("sp", 134,2)
    ops.remove("sp", 134,3)
    ops.fix(134, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 134,1)
    ops.remove("sp", 134,2)
    ops.remove("sp", 134,3)
    ops.fix(134, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 135,1)
    ops.remove("sp", 135,2)
    ops.remove("sp", 135,3)
    ops.fix(135, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 135,1)
    ops.remove("sp", 135,2)
    ops.remove("sp", 135,3)
    ops.fix(135, 0, 0, 1,0)
if pid == 7:
    ops.remove("sp", 136,1)
    ops.remove("sp", 136,2)
    ops.remove("sp", 136,3)
    ops.fix(136, 0, 0, 1,0)
if pid == 0:
    ops.remove("sp", 136,1)
    ops.remove("sp", 136,2)
    ops.remove("sp", 136,3)
    ops.fix(136, 0, 0, 1,0)
ops.model("basicBuilder","-ndm",3,"-ndf",3)
if pid == 6:
    ops.remove("sp", 232,1)
    ops.remove("sp", 232,2)
    ops.remove("sp", 232,3)
    ops.fix(232, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 232,1)
    ops.remove("sp", 232,2)
    ops.remove("sp", 232,3)
    ops.fix(232, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 233,1)
    ops.remove("sp", 233,2)
    ops.remove("sp", 233,3)
    ops.fix(233, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 233,1)
    ops.remove("sp", 233,2)
    ops.remove("sp", 233,3)
    ops.fix(233, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 234,1)
    ops.remove("sp", 234,2)
    ops.remove("sp", 234,3)
    ops.fix(234, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 234,1)
    ops.remove("sp", 234,2)
    ops.remove("sp", 234,3)
    ops.fix(234, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 235,1)
    ops.remove("sp", 235,2)
    ops.remove("sp", 235,3)
    ops.fix(235, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 235,1)
    ops.remove("sp", 235,2)
    ops.remove("sp", 235,3)
    ops.fix(235, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 236,1)
    ops.remove("sp", 236,2)
    ops.remove("sp", 236,3)
    ops.fix(236, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 236,1)
    ops.remove("sp", 236,2)
    ops.remove("sp", 236,3)
    ops.fix(236, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 252,1)
    ops.remove("sp", 252,2)
    ops.remove("sp", 252,3)
    ops.fix(252, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 252,1)
    ops.remove("sp", 252,2)
    ops.remove("sp", 252,3)
    ops.fix(252, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 253,1)
    ops.remove("sp", 253,2)
    ops.remove("sp", 253,3)
    ops.fix(253, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 253,1)
    ops.remove("sp", 253,2)
    ops.remove("sp", 253,3)
    ops.fix(253, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 254,1)
    ops.remove("sp", 254,2)
    ops.remove("sp", 254,3)
    ops.fix(254, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 254,1)
    ops.remove("sp", 254,2)
    ops.remove("sp", 254,3)
    ops.fix(254, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 255,1)
    ops.remove("sp", 255,2)
    ops.remove("sp", 255,3)
    ops.fix(255, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 255,1)
    ops.remove("sp", 255,2)
    ops.remove("sp", 255,3)
    ops.fix(255, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 256,1)
    ops.remove("sp", 256,2)
    ops.remove("sp", 256,3)
    ops.fix(256, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 256,1)
    ops.remove("sp", 256,2)
    ops.remove("sp", 256,3)
    ops.fix(256, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 257,1)
    ops.remove("sp", 257,2)
    ops.remove("sp", 257,3)
    ops.fix(257, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 257,1)
    ops.remove("sp", 257,2)
    ops.remove("sp", 257,3)
    ops.fix(257, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 258,1)
    ops.remove("sp", 258,2)
    ops.remove("sp", 258,3)
    ops.fix(258, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 258,1)
    ops.remove("sp", 258,2)
    ops.remove("sp", 258,3)
    ops.fix(258, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 259,1)
    ops.remove("sp", 259,2)
    ops.remove("sp", 259,3)
    ops.fix(259, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 259,1)
    ops.remove("sp", 259,2)
    ops.remove("sp", 259,3)
    ops.fix(259, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 260,1)
    ops.remove("sp", 260,2)
    ops.remove("sp", 260,3)
    ops.fix(260, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 260,1)
    ops.remove("sp", 260,2)
    ops.remove("sp", 260,3)
    ops.fix(260, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 261,1)
    ops.remove("sp", 261,2)
    ops.remove("sp", 261,3)
    ops.fix(261, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 261,1)
    ops.remove("sp", 261,2)
    ops.remove("sp", 261,3)
    ops.fix(261, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 267,1)
    ops.remove("sp", 267,2)
    ops.remove("sp", 267,3)
    ops.fix(267, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 267,1)
    ops.remove("sp", 267,2)
    ops.remove("sp", 267,3)
    ops.fix(267, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 268,1)
    ops.remove("sp", 268,2)
    ops.remove("sp", 268,3)
    ops.fix(268, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 268,1)
    ops.remove("sp", 268,2)
    ops.remove("sp", 268,3)
    ops.fix(268, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 269,1)
    ops.remove("sp", 269,2)
    ops.remove("sp", 269,3)
    ops.fix(269, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 269,1)
    ops.remove("sp", 269,2)
    ops.remove("sp", 269,3)
    ops.fix(269, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 270,1)
    ops.remove("sp", 270,2)
    ops.remove("sp", 270,3)
    ops.fix(270, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 270,1)
    ops.remove("sp", 270,2)
    ops.remove("sp", 270,3)
    ops.fix(270, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 271,1)
    ops.remove("sp", 271,2)
    ops.remove("sp", 271,3)
    ops.fix(271, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 271,1)
    ops.remove("sp", 271,2)
    ops.remove("sp", 271,3)
    ops.fix(271, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 437,1)
    ops.remove("sp", 437,2)
    ops.remove("sp", 437,3)
    ops.fix(437, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 437,1)
    ops.remove("sp", 437,2)
    ops.remove("sp", 437,3)
    ops.fix(437, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 438,1)
    ops.remove("sp", 438,2)
    ops.remove("sp", 438,3)
    ops.fix(438, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 438,1)
    ops.remove("sp", 438,2)
    ops.remove("sp", 438,3)
    ops.fix(438, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 439,1)
    ops.remove("sp", 439,2)
    ops.remove("sp", 439,3)
    ops.fix(439, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 439,1)
    ops.remove("sp", 439,2)
    ops.remove("sp", 439,3)
    ops.fix(439, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 440,1)
    ops.remove("sp", 440,2)
    ops.remove("sp", 440,3)
    ops.fix(440, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 440,1)
    ops.remove("sp", 440,2)
    ops.remove("sp", 440,3)
    ops.fix(440, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 441,1)
    ops.remove("sp", 441,2)
    ops.remove("sp", 441,3)
    ops.fix(441, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 441,1)
    ops.remove("sp", 441,2)
    ops.remove("sp", 441,3)
    ops.fix(441, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 442,1)
    ops.remove("sp", 442,2)
    ops.remove("sp", 442,3)
    ops.fix(442, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 442,1)
    ops.remove("sp", 442,2)
    ops.remove("sp", 442,3)
    ops.fix(442, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 443,1)
    ops.remove("sp", 443,2)
    ops.remove("sp", 443,3)
    ops.fix(443, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 443,1)
    ops.remove("sp", 443,2)
    ops.remove("sp", 443,3)
    ops.fix(443, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 443,1)
    ops.remove("sp", 443,2)
    ops.remove("sp", 443,3)
    ops.fix(443, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 444,1)
    ops.remove("sp", 444,2)
    ops.remove("sp", 444,3)
    ops.fix(444, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 444,1)
    ops.remove("sp", 444,2)
    ops.remove("sp", 444,3)
    ops.fix(444, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 445,1)
    ops.remove("sp", 445,2)
    ops.remove("sp", 445,3)
    ops.fix(445, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 445,1)
    ops.remove("sp", 445,2)
    ops.remove("sp", 445,3)
    ops.fix(445, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 445,1)
    ops.remove("sp", 445,2)
    ops.remove("sp", 445,3)
    ops.fix(445, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 446,1)
    ops.remove("sp", 446,2)
    ops.remove("sp", 446,3)
    ops.fix(446, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 446,1)
    ops.remove("sp", 446,2)
    ops.remove("sp", 446,3)
    ops.fix(446, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 446,1)
    ops.remove("sp", 446,2)
    ops.remove("sp", 446,3)
    ops.fix(446, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 447,1)
    ops.remove("sp", 447,2)
    ops.remove("sp", 447,3)
    ops.fix(447, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 447,1)
    ops.remove("sp", 447,2)
    ops.remove("sp", 447,3)
    ops.fix(447, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 448,1)
    ops.remove("sp", 448,2)
    ops.remove("sp", 448,3)
    ops.fix(448, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 448,1)
    ops.remove("sp", 448,2)
    ops.remove("sp", 448,3)
    ops.fix(448, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 448,1)
    ops.remove("sp", 448,2)
    ops.remove("sp", 448,3)
    ops.fix(448, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 449,1)
    ops.remove("sp", 449,2)
    ops.remove("sp", 449,3)
    ops.fix(449, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 449,1)
    ops.remove("sp", 449,2)
    ops.remove("sp", 449,3)
    ops.fix(449, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 450,1)
    ops.remove("sp", 450,2)
    ops.remove("sp", 450,3)
    ops.fix(450, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 450,1)
    ops.remove("sp", 450,2)
    ops.remove("sp", 450,3)
    ops.fix(450, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 450,1)
    ops.remove("sp", 450,2)
    ops.remove("sp", 450,3)
    ops.fix(450, 0, 0, 1)
if pid == 6:
    ops.remove("sp", 451,1)
    ops.remove("sp", 451,2)
    ops.remove("sp", 451,3)
    ops.fix(451, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 451,1)
    ops.remove("sp", 451,2)
    ops.remove("sp", 451,3)
    ops.fix(451, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 451,1)
    ops.remove("sp", 451,2)
    ops.remove("sp", 451,3)
    ops.fix(451, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 452,1)
    ops.remove("sp", 452,2)
    ops.remove("sp", 452,3)
    ops.fix(452, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 452,1)
    ops.remove("sp", 452,2)
    ops.remove("sp", 452,3)
    ops.fix(452, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 453,1)
    ops.remove("sp", 453,2)
    ops.remove("sp", 453,3)
    ops.fix(453, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 453,1)
    ops.remove("sp", 453,2)
    ops.remove("sp", 453,3)
    ops.fix(453, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 454,1)
    ops.remove("sp", 454,2)
    ops.remove("sp", 454,3)
    ops.fix(454, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 454,1)
    ops.remove("sp", 454,2)
    ops.remove("sp", 454,3)
    ops.fix(454, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 455,1)
    ops.remove("sp", 455,2)
    ops.remove("sp", 455,3)
    ops.fix(455, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 455,1)
    ops.remove("sp", 455,2)
    ops.remove("sp", 455,3)
    ops.fix(455, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 456,1)
    ops.remove("sp", 456,2)
    ops.remove("sp", 456,3)
    ops.fix(456, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 456,1)
    ops.remove("sp", 456,2)
    ops.remove("sp", 456,3)
    ops.fix(456, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 457,1)
    ops.remove("sp", 457,2)
    ops.remove("sp", 457,3)
    ops.fix(457, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 457,1)
    ops.remove("sp", 457,2)
    ops.remove("sp", 457,3)
    ops.fix(457, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 458,1)
    ops.remove("sp", 458,2)
    ops.remove("sp", 458,3)
    ops.fix(458, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 458,1)
    ops.remove("sp", 458,2)
    ops.remove("sp", 458,3)
    ops.fix(458, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 459,1)
    ops.remove("sp", 459,2)
    ops.remove("sp", 459,3)
    ops.fix(459, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 459,1)
    ops.remove("sp", 459,2)
    ops.remove("sp", 459,3)
    ops.fix(459, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 460,1)
    ops.remove("sp", 460,2)
    ops.remove("sp", 460,3)
    ops.fix(460, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 460,1)
    ops.remove("sp", 460,2)
    ops.remove("sp", 460,3)
    ops.fix(460, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 461,1)
    ops.remove("sp", 461,2)
    ops.remove("sp", 461,3)
    ops.fix(461, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 461,1)
    ops.remove("sp", 461,2)
    ops.remove("sp", 461,3)
    ops.fix(461, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 462,1)
    ops.remove("sp", 462,2)
    ops.remove("sp", 462,3)
    ops.fix(462, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 462,1)
    ops.remove("sp", 462,2)
    ops.remove("sp", 462,3)
    ops.fix(462, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 463,1)
    ops.remove("sp", 463,2)
    ops.remove("sp", 463,3)
    ops.fix(463, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 463,1)
    ops.remove("sp", 463,2)
    ops.remove("sp", 463,3)
    ops.fix(463, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 464,1)
    ops.remove("sp", 464,2)
    ops.remove("sp", 464,3)
    ops.fix(464, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 464,1)
    ops.remove("sp", 464,2)
    ops.remove("sp", 464,3)
    ops.fix(464, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 465,1)
    ops.remove("sp", 465,2)
    ops.remove("sp", 465,3)
    ops.fix(465, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 465,1)
    ops.remove("sp", 465,2)
    ops.remove("sp", 465,3)
    ops.fix(465, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 466,1)
    ops.remove("sp", 466,2)
    ops.remove("sp", 466,3)
    ops.fix(466, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 466,1)
    ops.remove("sp", 466,2)
    ops.remove("sp", 466,3)
    ops.fix(466, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 467,1)
    ops.remove("sp", 467,2)
    ops.remove("sp", 467,3)
    ops.fix(467, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 467,1)
    ops.remove("sp", 467,2)
    ops.remove("sp", 467,3)
    ops.fix(467, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 468,1)
    ops.remove("sp", 468,2)
    ops.remove("sp", 468,3)
    ops.fix(468, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 468,1)
    ops.remove("sp", 468,2)
    ops.remove("sp", 468,3)
    ops.fix(468, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 469,1)
    ops.remove("sp", 469,2)
    ops.remove("sp", 469,3)
    ops.fix(469, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 469,1)
    ops.remove("sp", 469,2)
    ops.remove("sp", 469,3)
    ops.fix(469, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 470,1)
    ops.remove("sp", 470,2)
    ops.remove("sp", 470,3)
    ops.fix(470, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 470,1)
    ops.remove("sp", 470,2)
    ops.remove("sp", 470,3)
    ops.fix(470, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 471,1)
    ops.remove("sp", 471,2)
    ops.remove("sp", 471,3)
    ops.fix(471, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 471,1)
    ops.remove("sp", 471,2)
    ops.remove("sp", 471,3)
    ops.fix(471, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 472,1)
    ops.remove("sp", 472,2)
    ops.remove("sp", 472,3)
    ops.fix(472, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 472,1)
    ops.remove("sp", 472,2)
    ops.remove("sp", 472,3)
    ops.fix(472, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 473,1)
    ops.remove("sp", 473,2)
    ops.remove("sp", 473,3)
    ops.fix(473, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 473,1)
    ops.remove("sp", 473,2)
    ops.remove("sp", 473,3)
    ops.fix(473, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 474,1)
    ops.remove("sp", 474,2)
    ops.remove("sp", 474,3)
    ops.fix(474, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 474,1)
    ops.remove("sp", 474,2)
    ops.remove("sp", 474,3)
    ops.fix(474, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 475,1)
    ops.remove("sp", 475,2)
    ops.remove("sp", 475,3)
    ops.fix(475, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 475,1)
    ops.remove("sp", 475,2)
    ops.remove("sp", 475,3)
    ops.fix(475, 0, 0, 1)
if pid == 7:
    ops.remove("sp", 476,1)
    ops.remove("sp", 476,2)
    ops.remove("sp", 476,3)
    ops.fix(476, 0, 0, 1)
if pid == 0:
    ops.remove("sp", 476,1)
    ops.remove("sp", 476,2)
    ops.remove("sp", 476,3)
    ops.fix(476, 0, 0, 1)
    ops.model("basicBuilder","-ndm",3,"-ndf",4)
if pid == 1:
    ops.remove("sp", 1,1)
    ops.remove("sp", 1,2)
    ops.remove("sp", 1,3)
    ops.fix(1, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 1,1)
    ops.remove("sp", 1,2)
    ops.remove("sp", 1,3)
    ops.fix(1, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 3,1)
    ops.remove("sp", 3,2)
    ops.remove("sp", 3,3)
    ops.fix(3, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 3,1)
    ops.remove("sp", 3,2)
    ops.remove("sp", 3,3)
    ops.fix(3, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 5,1)
    ops.remove("sp", 5,2)
    ops.remove("sp", 5,3)
    ops.fix(5, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 5,1)
    ops.remove("sp", 5,2)
    ops.remove("sp", 5,3)
    ops.fix(5, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 7,1)
    ops.remove("sp", 7,2)
    ops.remove("sp", 7,3)
    ops.fix(7, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 7,1)
    ops.remove("sp", 7,2)
    ops.remove("sp", 7,3)
    ops.fix(7, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 13,1)
    ops.remove("sp", 13,2)
    ops.remove("sp", 13,3)
    ops.fix(13, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 13,1)
    ops.remove("sp", 13,2)
    ops.remove("sp", 13,3)
    ops.fix(13, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 14,1)
    ops.remove("sp", 14,2)
    ops.remove("sp", 14,3)
    ops.fix(14, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 14,1)
    ops.remove("sp", 14,2)
    ops.remove("sp", 14,3)
    ops.fix(14, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 15,1)
    ops.remove("sp", 15,2)
    ops.remove("sp", 15,3)
    ops.fix(15, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 15,1)
    ops.remove("sp", 15,2)
    ops.remove("sp", 15,3)
    ops.fix(15, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 16,1)
    ops.remove("sp", 16,2)
    ops.remove("sp", 16,3)
    ops.fix(16, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 16,1)
    ops.remove("sp", 16,2)
    ops.remove("sp", 16,3)
    ops.fix(16, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 16,1)
    ops.remove("sp", 16,2)
    ops.remove("sp", 16,3)
    ops.fix(16, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 29,1)
    ops.remove("sp", 29,2)
    ops.remove("sp", 29,3)
    ops.fix(29, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 29,1)
    ops.remove("sp", 29,2)
    ops.remove("sp", 29,3)
    ops.fix(29, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 30,1)
    ops.remove("sp", 30,2)
    ops.remove("sp", 30,3)
    ops.fix(30, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 30,1)
    ops.remove("sp", 30,2)
    ops.remove("sp", 30,3)
    ops.fix(30, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 31,1)
    ops.remove("sp", 31,2)
    ops.remove("sp", 31,3)
    ops.fix(31, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 31,1)
    ops.remove("sp", 31,2)
    ops.remove("sp", 31,3)
    ops.fix(31, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 31,1)
    ops.remove("sp", 31,2)
    ops.remove("sp", 31,3)
    ops.fix(31, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 32,1)
    ops.remove("sp", 32,2)
    ops.remove("sp", 32,3)
    ops.fix(32, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 32,1)
    ops.remove("sp", 32,2)
    ops.remove("sp", 32,3)
    ops.fix(32, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 45,1)
    ops.remove("sp", 45,2)
    ops.remove("sp", 45,3)
    ops.fix(45, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 45,1)
    ops.remove("sp", 45,2)
    ops.remove("sp", 45,3)
    ops.fix(45, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 46,1)
    ops.remove("sp", 46,2)
    ops.remove("sp", 46,3)
    ops.fix(46, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 46,1)
    ops.remove("sp", 46,2)
    ops.remove("sp", 46,3)
    ops.fix(46, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 47,1)
    ops.remove("sp", 47,2)
    ops.remove("sp", 47,3)
    ops.fix(47, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 47,1)
    ops.remove("sp", 47,2)
    ops.remove("sp", 47,3)
    ops.fix(47, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 48,1)
    ops.remove("sp", 48,2)
    ops.remove("sp", 48,3)
    ops.fix(48, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 48,1)
    ops.remove("sp", 48,2)
    ops.remove("sp", 48,3)
    ops.fix(48, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 53,1)
    ops.remove("sp", 53,2)
    ops.remove("sp", 53,3)
    ops.fix(53, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 53,1)
    ops.remove("sp", 53,2)
    ops.remove("sp", 53,3)
    ops.fix(53, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 54,1)
    ops.remove("sp", 54,2)
    ops.remove("sp", 54,3)
    ops.fix(54, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 54,1)
    ops.remove("sp", 54,2)
    ops.remove("sp", 54,3)
    ops.fix(54, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 55,1)
    ops.remove("sp", 55,2)
    ops.remove("sp", 55,3)
    ops.fix(55, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 55,1)
    ops.remove("sp", 55,2)
    ops.remove("sp", 55,3)
    ops.fix(55, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 56,1)
    ops.remove("sp", 56,2)
    ops.remove("sp", 56,3)
    ops.fix(56, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 56,1)
    ops.remove("sp", 56,2)
    ops.remove("sp", 56,3)
    ops.fix(56, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 137,1)
    ops.remove("sp", 137,2)
    ops.remove("sp", 137,3)
    ops.fix(137, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 137,1)
    ops.remove("sp", 137,2)
    ops.remove("sp", 137,3)
    ops.fix(137, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 137,1)
    ops.remove("sp", 137,2)
    ops.remove("sp", 137,3)
    ops.fix(137, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 138,1)
    ops.remove("sp", 138,2)
    ops.remove("sp", 138,3)
    ops.fix(138, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 138,1)
    ops.remove("sp", 138,2)
    ops.remove("sp", 138,3)
    ops.fix(138, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 138,1)
    ops.remove("sp", 138,2)
    ops.remove("sp", 138,3)
    ops.fix(138, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 139,1)
    ops.remove("sp", 139,2)
    ops.remove("sp", 139,3)
    ops.fix(139, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 139,1)
    ops.remove("sp", 139,2)
    ops.remove("sp", 139,3)
    ops.fix(139, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 139,1)
    ops.remove("sp", 139,2)
    ops.remove("sp", 139,3)
    ops.fix(139, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 140,1)
    ops.remove("sp", 140,2)
    ops.remove("sp", 140,3)
    ops.fix(140, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 140,1)
    ops.remove("sp", 140,2)
    ops.remove("sp", 140,3)
    ops.fix(140, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 141,1)
    ops.remove("sp", 141,2)
    ops.remove("sp", 141,3)
    ops.fix(141, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 141,1)
    ops.remove("sp", 141,2)
    ops.remove("sp", 141,3)
    ops.fix(141, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 142,1)
    ops.remove("sp", 142,2)
    ops.remove("sp", 142,3)
    ops.fix(142, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 142,1)
    ops.remove("sp", 142,2)
    ops.remove("sp", 142,3)
    ops.fix(142, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 143,1)
    ops.remove("sp", 143,2)
    ops.remove("sp", 143,3)
    ops.fix(143, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 143,1)
    ops.remove("sp", 143,2)
    ops.remove("sp", 143,3)
    ops.fix(143, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 143,1)
    ops.remove("sp", 143,2)
    ops.remove("sp", 143,3)
    ops.fix(143, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 144,1)
    ops.remove("sp", 144,2)
    ops.remove("sp", 144,3)
    ops.fix(144, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 144,1)
    ops.remove("sp", 144,2)
    ops.remove("sp", 144,3)
    ops.fix(144, 0, 0, 0,1)
if pid == 2:
    ops.remove("sp", 144,1)
    ops.remove("sp", 144,2)
    ops.remove("sp", 144,3)
    ops.fix(144, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 145,1)
    ops.remove("sp", 145,2)
    ops.remove("sp", 145,3)
    ops.fix(145, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 145,1)
    ops.remove("sp", 145,2)
    ops.remove("sp", 145,3)
    ops.fix(145, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 146,1)
    ops.remove("sp", 146,2)
    ops.remove("sp", 146,3)
    ops.fix(146, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 146,1)
    ops.remove("sp", 146,2)
    ops.remove("sp", 146,3)
    ops.fix(146, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 147,1)
    ops.remove("sp", 147,2)
    ops.remove("sp", 147,3)
    ops.fix(147, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 147,1)
    ops.remove("sp", 147,2)
    ops.remove("sp", 147,3)
    ops.fix(147, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 148,1)
    ops.remove("sp", 148,2)
    ops.remove("sp", 148,3)
    ops.fix(148, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 148,1)
    ops.remove("sp", 148,2)
    ops.remove("sp", 148,3)
    ops.fix(148, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 149,1)
    ops.remove("sp", 149,2)
    ops.remove("sp", 149,3)
    ops.fix(149, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 149,1)
    ops.remove("sp", 149,2)
    ops.remove("sp", 149,3)
    ops.fix(149, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 150,1)
    ops.remove("sp", 150,2)
    ops.remove("sp", 150,3)
    ops.fix(150, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 150,1)
    ops.remove("sp", 150,2)
    ops.remove("sp", 150,3)
    ops.fix(150, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 151,1)
    ops.remove("sp", 151,2)
    ops.remove("sp", 151,3)
    ops.fix(151, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 151,1)
    ops.remove("sp", 151,2)
    ops.remove("sp", 151,3)
    ops.fix(151, 0, 0, 0,1)
if pid == 1:
    ops.remove("sp", 152,1)
    ops.remove("sp", 152,2)
    ops.remove("sp", 152,3)
    ops.fix(152, 0, 0, 0,1)
if pid == 0:
    ops.remove("sp", 152,1)
    ops.remove("sp", 152,2)
    ops.remove("sp", 152,3)
    ops.fix(152, 0, 0, 0,1)
ops.model("basicBuilder","-ndm",3,"-ndf",3)
if pid == 1:
    ops.remove("sp", 222,1)
    ops.remove("sp", 222,2)
    ops.remove("sp", 222,3)
    ops.fix(222, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 222,1)
    ops.remove("sp", 222,2)
    ops.remove("sp", 222,3)
    ops.fix(222, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 223,1)
    ops.remove("sp", 223,2)
    ops.remove("sp", 223,3)
    ops.fix(223, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 223,1)
    ops.remove("sp", 223,2)
    ops.remove("sp", 223,3)
    ops.fix(223, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 224,1)
    ops.remove("sp", 224,2)
    ops.remove("sp", 224,3)
    ops.fix(224, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 224,1)
    ops.remove("sp", 224,2)
    ops.remove("sp", 224,3)
    ops.fix(224, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 225,1)
    ops.remove("sp", 225,2)
    ops.remove("sp", 225,3)
    ops.fix(225, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 225,1)
    ops.remove("sp", 225,2)
    ops.remove("sp", 225,3)
    ops.fix(225, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 226,1)
    ops.remove("sp", 226,2)
    ops.remove("sp", 226,3)
    ops.fix(226, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 226,1)
    ops.remove("sp", 226,2)
    ops.remove("sp", 226,3)
    ops.fix(226, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 242,1)
    ops.remove("sp", 242,2)
    ops.remove("sp", 242,3)
    ops.fix(242, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 242,1)
    ops.remove("sp", 242,2)
    ops.remove("sp", 242,3)
    ops.fix(242, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 243,1)
    ops.remove("sp", 243,2)
    ops.remove("sp", 243,3)
    ops.fix(243, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 243,1)
    ops.remove("sp", 243,2)
    ops.remove("sp", 243,3)
    ops.fix(243, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 244,1)
    ops.remove("sp", 244,2)
    ops.remove("sp", 244,3)
    ops.fix(244, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 244,1)
    ops.remove("sp", 244,2)
    ops.remove("sp", 244,3)
    ops.fix(244, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 245,1)
    ops.remove("sp", 245,2)
    ops.remove("sp", 245,3)
    ops.fix(245, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 245,1)
    ops.remove("sp", 245,2)
    ops.remove("sp", 245,3)
    ops.fix(245, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 246,1)
    ops.remove("sp", 246,2)
    ops.remove("sp", 246,3)
    ops.fix(246, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 246,1)
    ops.remove("sp", 246,2)
    ops.remove("sp", 246,3)
    ops.fix(246, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 262,1)
    ops.remove("sp", 262,2)
    ops.remove("sp", 262,3)
    ops.fix(262, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 262,1)
    ops.remove("sp", 262,2)
    ops.remove("sp", 262,3)
    ops.fix(262, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 263,1)
    ops.remove("sp", 263,2)
    ops.remove("sp", 263,3)
    ops.fix(263, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 263,1)
    ops.remove("sp", 263,2)
    ops.remove("sp", 263,3)
    ops.fix(263, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 264,1)
    ops.remove("sp", 264,2)
    ops.remove("sp", 264,3)
    ops.fix(264, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 264,1)
    ops.remove("sp", 264,2)
    ops.remove("sp", 264,3)
    ops.fix(264, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 265,1)
    ops.remove("sp", 265,2)
    ops.remove("sp", 265,3)
    ops.fix(265, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 265,1)
    ops.remove("sp", 265,2)
    ops.remove("sp", 265,3)
    ops.fix(265, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 266,1)
    ops.remove("sp", 266,2)
    ops.remove("sp", 266,3)
    ops.fix(266, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 266,1)
    ops.remove("sp", 266,2)
    ops.remove("sp", 266,3)
    ops.fix(266, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 272,1)
    ops.remove("sp", 272,2)
    ops.remove("sp", 272,3)
    ops.fix(272, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 272,1)
    ops.remove("sp", 272,2)
    ops.remove("sp", 272,3)
    ops.fix(272, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 273,1)
    ops.remove("sp", 273,2)
    ops.remove("sp", 273,3)
    ops.fix(273, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 273,1)
    ops.remove("sp", 273,2)
    ops.remove("sp", 273,3)
    ops.fix(273, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 274,1)
    ops.remove("sp", 274,2)
    ops.remove("sp", 274,3)
    ops.fix(274, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 274,1)
    ops.remove("sp", 274,2)
    ops.remove("sp", 274,3)
    ops.fix(274, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 275,1)
    ops.remove("sp", 275,2)
    ops.remove("sp", 275,3)
    ops.fix(275, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 275,1)
    ops.remove("sp", 275,2)
    ops.remove("sp", 275,3)
    ops.fix(275, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 276,1)
    ops.remove("sp", 276,2)
    ops.remove("sp", 276,3)
    ops.fix(276, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 276,1)
    ops.remove("sp", 276,2)
    ops.remove("sp", 276,3)
    ops.fix(276, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 477,1)
    ops.remove("sp", 477,2)
    ops.remove("sp", 477,3)
    ops.fix(477, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 477,1)
    ops.remove("sp", 477,2)
    ops.remove("sp", 477,3)
    ops.fix(477, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 477,1)
    ops.remove("sp", 477,2)
    ops.remove("sp", 477,3)
    ops.fix(477, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 478,1)
    ops.remove("sp", 478,2)
    ops.remove("sp", 478,3)
    ops.fix(478, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 478,1)
    ops.remove("sp", 478,2)
    ops.remove("sp", 478,3)
    ops.fix(478, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 479,1)
    ops.remove("sp", 479,2)
    ops.remove("sp", 479,3)
    ops.fix(479, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 479,1)
    ops.remove("sp", 479,2)
    ops.remove("sp", 479,3)
    ops.fix(479, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 479,1)
    ops.remove("sp", 479,2)
    ops.remove("sp", 479,3)
    ops.fix(479, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 480,1)
    ops.remove("sp", 480,2)
    ops.remove("sp", 480,3)
    ops.fix(480, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 480,1)
    ops.remove("sp", 480,2)
    ops.remove("sp", 480,3)
    ops.fix(480, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 481,1)
    ops.remove("sp", 481,2)
    ops.remove("sp", 481,3)
    ops.fix(481, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 481,1)
    ops.remove("sp", 481,2)
    ops.remove("sp", 481,3)
    ops.fix(481, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 481,1)
    ops.remove("sp", 481,2)
    ops.remove("sp", 481,3)
    ops.fix(481, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 482,1)
    ops.remove("sp", 482,2)
    ops.remove("sp", 482,3)
    ops.fix(482, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 482,1)
    ops.remove("sp", 482,2)
    ops.remove("sp", 482,3)
    ops.fix(482, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 483,1)
    ops.remove("sp", 483,2)
    ops.remove("sp", 483,3)
    ops.fix(483, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 483,1)
    ops.remove("sp", 483,2)
    ops.remove("sp", 483,3)
    ops.fix(483, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 484,1)
    ops.remove("sp", 484,2)
    ops.remove("sp", 484,3)
    ops.fix(484, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 484,1)
    ops.remove("sp", 484,2)
    ops.remove("sp", 484,3)
    ops.fix(484, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 485,1)
    ops.remove("sp", 485,2)
    ops.remove("sp", 485,3)
    ops.fix(485, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 485,1)
    ops.remove("sp", 485,2)
    ops.remove("sp", 485,3)
    ops.fix(485, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 486,1)
    ops.remove("sp", 486,2)
    ops.remove("sp", 486,3)
    ops.fix(486, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 486,1)
    ops.remove("sp", 486,2)
    ops.remove("sp", 486,3)
    ops.fix(486, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 487,1)
    ops.remove("sp", 487,2)
    ops.remove("sp", 487,3)
    ops.fix(487, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 487,1)
    ops.remove("sp", 487,2)
    ops.remove("sp", 487,3)
    ops.fix(487, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 488,1)
    ops.remove("sp", 488,2)
    ops.remove("sp", 488,3)
    ops.fix(488, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 488,1)
    ops.remove("sp", 488,2)
    ops.remove("sp", 488,3)
    ops.fix(488, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 489,1)
    ops.remove("sp", 489,2)
    ops.remove("sp", 489,3)
    ops.fix(489, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 489,1)
    ops.remove("sp", 489,2)
    ops.remove("sp", 489,3)
    ops.fix(489, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 490,1)
    ops.remove("sp", 490,2)
    ops.remove("sp", 490,3)
    ops.fix(490, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 490,1)
    ops.remove("sp", 490,2)
    ops.remove("sp", 490,3)
    ops.fix(490, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 491,1)
    ops.remove("sp", 491,2)
    ops.remove("sp", 491,3)
    ops.fix(491, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 491,1)
    ops.remove("sp", 491,2)
    ops.remove("sp", 491,3)
    ops.fix(491, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 491,1)
    ops.remove("sp", 491,2)
    ops.remove("sp", 491,3)
    ops.fix(491, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 492,1)
    ops.remove("sp", 492,2)
    ops.remove("sp", 492,3)
    ops.fix(492, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 492,1)
    ops.remove("sp", 492,2)
    ops.remove("sp", 492,3)
    ops.fix(492, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 492,1)
    ops.remove("sp", 492,2)
    ops.remove("sp", 492,3)
    ops.fix(492, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 493,1)
    ops.remove("sp", 493,2)
    ops.remove("sp", 493,3)
    ops.fix(493, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 493,1)
    ops.remove("sp", 493,2)
    ops.remove("sp", 493,3)
    ops.fix(493, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 494,1)
    ops.remove("sp", 494,2)
    ops.remove("sp", 494,3)
    ops.fix(494, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 494,1)
    ops.remove("sp", 494,2)
    ops.remove("sp", 494,3)
    ops.fix(494, 0, 0, 0)
if pid == 2:
    ops.remove("sp", 494,1)
    ops.remove("sp", 494,2)
    ops.remove("sp", 494,3)
    ops.fix(494, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 495,1)
    ops.remove("sp", 495,2)
    ops.remove("sp", 495,3)
    ops.fix(495, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 495,1)
    ops.remove("sp", 495,2)
    ops.remove("sp", 495,3)
    ops.fix(495, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 496,1)
    ops.remove("sp", 496,2)
    ops.remove("sp", 496,3)
    ops.fix(496, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 496,1)
    ops.remove("sp", 496,2)
    ops.remove("sp", 496,3)
    ops.fix(496, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 497,1)
    ops.remove("sp", 497,2)
    ops.remove("sp", 497,3)
    ops.fix(497, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 497,1)
    ops.remove("sp", 497,2)
    ops.remove("sp", 497,3)
    ops.fix(497, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 498,1)
    ops.remove("sp", 498,2)
    ops.remove("sp", 498,3)
    ops.fix(498, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 498,1)
    ops.remove("sp", 498,2)
    ops.remove("sp", 498,3)
    ops.fix(498, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 499,1)
    ops.remove("sp", 499,2)
    ops.remove("sp", 499,3)
    ops.fix(499, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 499,1)
    ops.remove("sp", 499,2)
    ops.remove("sp", 499,3)
    ops.fix(499, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 500,1)
    ops.remove("sp", 500,2)
    ops.remove("sp", 500,3)
    ops.fix(500, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 500,1)
    ops.remove("sp", 500,2)
    ops.remove("sp", 500,3)
    ops.fix(500, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 501,1)
    ops.remove("sp", 501,2)
    ops.remove("sp", 501,3)
    ops.fix(501, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 501,1)
    ops.remove("sp", 501,2)
    ops.remove("sp", 501,3)
    ops.fix(501, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 502,1)
    ops.remove("sp", 502,2)
    ops.remove("sp", 502,3)
    ops.fix(502, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 502,1)
    ops.remove("sp", 502,2)
    ops.remove("sp", 502,3)
    ops.fix(502, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 503,1)
    ops.remove("sp", 503,2)
    ops.remove("sp", 503,3)
    ops.fix(503, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 503,1)
    ops.remove("sp", 503,2)
    ops.remove("sp", 503,3)
    ops.fix(503, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 504,1)
    ops.remove("sp", 504,2)
    ops.remove("sp", 504,3)
    ops.fix(504, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 504,1)
    ops.remove("sp", 504,2)
    ops.remove("sp", 504,3)
    ops.fix(504, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 505,1)
    ops.remove("sp", 505,2)
    ops.remove("sp", 505,3)
    ops.fix(505, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 505,1)
    ops.remove("sp", 505,2)
    ops.remove("sp", 505,3)
    ops.fix(505, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 506,1)
    ops.remove("sp", 506,2)
    ops.remove("sp", 506,3)
    ops.fix(506, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 506,1)
    ops.remove("sp", 506,2)
    ops.remove("sp", 506,3)
    ops.fix(506, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 507,1)
    ops.remove("sp", 507,2)
    ops.remove("sp", 507,3)
    ops.fix(507, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 507,1)
    ops.remove("sp", 507,2)
    ops.remove("sp", 507,3)
    ops.fix(507, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 508,1)
    ops.remove("sp", 508,2)
    ops.remove("sp", 508,3)
    ops.fix(508, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 508,1)
    ops.remove("sp", 508,2)
    ops.remove("sp", 508,3)
    ops.fix(508, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 509,1)
    ops.remove("sp", 509,2)
    ops.remove("sp", 509,3)
    ops.fix(509, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 509,1)
    ops.remove("sp", 509,2)
    ops.remove("sp", 509,3)
    ops.fix(509, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 510,1)
    ops.remove("sp", 510,2)
    ops.remove("sp", 510,3)
    ops.fix(510, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 510,1)
    ops.remove("sp", 510,2)
    ops.remove("sp", 510,3)
    ops.fix(510, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 511,1)
    ops.remove("sp", 511,2)
    ops.remove("sp", 511,3)
    ops.fix(511, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 511,1)
    ops.remove("sp", 511,2)
    ops.remove("sp", 511,3)
    ops.fix(511, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 512,1)
    ops.remove("sp", 512,2)
    ops.remove("sp", 512,3)
    ops.fix(512, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 512,1)
    ops.remove("sp", 512,2)
    ops.remove("sp", 512,3)
    ops.fix(512, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 513,1)
    ops.remove("sp", 513,2)
    ops.remove("sp", 513,3)
    ops.fix(513, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 513,1)
    ops.remove("sp", 513,2)
    ops.remove("sp", 513,3)
    ops.fix(513, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 514,1)
    ops.remove("sp", 514,2)
    ops.remove("sp", 514,3)
    ops.fix(514, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 514,1)
    ops.remove("sp", 514,2)
    ops.remove("sp", 514,3)
    ops.fix(514, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 515,1)
    ops.remove("sp", 515,2)
    ops.remove("sp", 515,3)
    ops.fix(515, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 515,1)
    ops.remove("sp", 515,2)
    ops.remove("sp", 515,3)
    ops.fix(515, 0, 0, 0)
if pid == 1:
    ops.remove("sp", 516,1)
    ops.remove("sp", 516,2)
    ops.remove("sp", 516,3)
    ops.fix(516, 0, 0, 0)
if pid == 0:
    ops.remove("sp", 516,1)
    ops.remove("sp", 516,2)
    ops.remove("sp", 516,3)
    ops.fix(516, 0, 0, 0)
if pid == 1:
    ops.element('20_8_BrickUP',211,45, 92, 12, 1, 149, 153, 69, 13, 365,364, 221, 262, 517, 519, 313, 504, 513, 518,304, 222, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',212,46, 96, 92, 45, 150, 154, 153, 149, 374,373, 365, 263, 520, 522, 517, 506, 514, 521,518, 513, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',213,47, 100, 96, 46, 151, 155, 154, 150, 383,382, 374, 264, 523, 525, 520, 508, 515, 524,521, 514, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',214,48, 104, 100, 47, 152, 156, 155, 151, 392,391, 383, 265, 526, 528, 523, 510, 516, 527,524, 515, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',215,5, 28, 104, 48, 29, 73, 156, 152, 241,396, 392, 266, 318, 529, 526, 512, 242, 317,527, 516, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',216,149, 153, 69, 13, 145, 157, 70, 14, 517,519, 313, 504, 530, 532, 314, 495, 505, 531,306, 223, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',217,150, 154, 153, 149, 146, 158, 157, 145, 520,522, 517, 506, 533, 535, 530, 497, 507, 534,531, 505, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',218,151, 155, 154, 150, 147, 159, 158, 146, 523,525, 520, 508, 536, 538, 533, 499, 509, 537,534, 507, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',219,152, 156, 155, 151, 148, 160, 159, 147, 526,528, 523, 510, 539, 541, 536, 501, 511, 540,537, 509, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',220,29, 73, 156, 152, 30, 74, 160, 148, 318,529, 526, 512, 320, 542, 539, 503, 243, 319,540, 511, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',221,145, 157, 70, 14, 141, 161, 71, 15, 530,532, 314, 495, 543, 545, 315, 486, 496, 544,308, 224, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',222,146, 158, 157, 145, 142, 162, 161, 141, 533,535, 530, 497, 546, 548, 543, 488, 498, 547,544, 496, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',223,147, 159, 158, 146, 143, 163, 162, 142, 536,538, 533, 499, 549, 551, 546, 490, 500, 550,547, 498, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',224,148, 160, 159, 147, 144, 164, 163, 143, 539,541, 536, 501, 552, 554, 549, 492, 502, 553,550, 500, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',225,30, 74, 160, 148, 31, 75, 164, 144, 320,542, 539, 503, 322, 555, 552, 494, 244, 321,553, 502, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',226,141, 161, 71, 15, 137, 165, 72, 16, 543,545, 315, 486, 556, 558, 316, 477, 487, 557,310, 225, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',227,142, 162, 161, 141, 138, 166, 165, 137, 546,548, 543, 488, 559, 561, 556, 479, 489, 560,557, 487, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 1:
    ops.element('20_8_BrickUP',228,143, 163, 162, 142, 139, 167, 166, 138, 549,551, 546, 490, 562, 564, 559, 481, 491, 563,560, 489, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',229,144, 164, 163, 143, 140, 168, 167, 139, 552,554, 549, 492, 565, 567, 562, 483, 493, 566,563, 491, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',230,31, 75, 164, 144, 32, 76, 168, 140, 322,555, 552, 494, 324, 568, 565, 485, 245, 323,566, 493, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',231,137, 165, 72, 16, 53, 120, 20, 3, 556,558, 316, 477, 432, 436, 231, 272, 478, 569,312, 226, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',232,138, 166, 165, 137, 54, 116, 120, 53, 559,561, 556, 479, 423, 431, 432, 273, 480, 570,569, 478, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',233,139, 167, 166, 138, 55, 112, 116, 54, 562,564, 559, 481, 414, 422, 423, 274, 482, 571,570, 480, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',234,140, 168, 167, 139, 56, 108, 112, 55, 565,567, 562, 483, 405, 413, 414, 275, 484, 572,571, 482, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',235,32, 76, 168, 140, 7, 36, 108, 56, 324,568, 565, 485, 251, 404, 405, 276, 246, 325,572, 484, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',236,92, 91, 11, 12, 153, 169, 65, 69, 363,362, 220, 364, 573, 575, 305, 519, 518, 574,295, 304, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',237,96, 95, 91, 92, 154, 170, 169, 153, 372,371, 363, 373, 576, 578, 573, 522, 521, 577,574, 518, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',238,100, 99, 95, 96, 155, 171, 170, 154, 381,380, 372, 382, 579, 581, 576, 525, 524, 580,577, 521, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',239,104, 103, 99, 100, 156, 172, 171, 155, 390,389, 381, 391, 582, 584, 579, 528, 527, 583,580, 524, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',240,28, 27, 103, 104, 73, 77, 172, 156, 240,395, 390, 396, 327, 585, 582, 529, 317, 326,583, 527, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',241,153, 169, 65, 69, 157, 173, 66, 70, 573,575, 305, 519, 586, 588, 307, 532, 531, 587,297, 306, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',242,154, 170, 169, 153, 158, 174, 173, 157, 576,578, 573, 522, 589, 591, 586, 535, 534, 590,587, 531, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',243,155, 171, 170, 154, 159, 175, 174, 158, 579,581, 576, 525, 592, 594, 589, 538, 537, 593,590, 534, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',244,156, 172, 171, 155, 160, 176, 175, 159, 582,584, 579, 528, 595, 597, 592, 541, 540, 596,593, 537, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',245,73, 77, 172, 156, 74, 78, 176, 160, 327,585, 582, 529, 329, 598, 595, 542, 319, 328,596, 540, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 2:
    ops.element('20_8_BrickUP',246,157, 173, 66, 70, 161, 177, 67, 71, 586,588, 307, 532, 599, 601, 309, 545, 544, 600,299, 308, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',247,158, 174, 173, 157, 162, 178, 177, 161, 589,591, 586, 535, 602, 604, 599, 548, 547, 603,600, 544, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',248,159, 175, 174, 158, 163, 179, 178, 162, 592,594, 589, 538, 605, 607, 602, 551, 550, 606,603, 547, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',249,160, 176, 175, 159, 164, 180, 179, 163, 595,597, 592, 541, 608, 610, 605, 554, 553, 609,606, 550, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',250,74, 78, 176, 160, 75, 79, 180, 164, 329,598, 595, 542, 331, 611, 608, 555, 321, 330,609, 553, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',251,161, 177, 67, 71, 165, 181, 68, 72, 599,601, 309, 545, 612, 614, 311, 558, 557, 613,301, 310, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',252,162, 178, 177, 161, 166, 182, 181, 165, 602,604, 599, 548, 615, 617, 612, 561, 560, 616,613, 557, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',253,163, 179, 178, 162, 167, 183, 182, 166, 605,607, 602, 551, 618, 620, 615, 564, 563, 619,616, 560, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',254,164, 180, 179, 163, 168, 184, 183, 167, 608,610, 605, 554, 621, 623, 618, 567, 566, 622,619, 563, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',255,75, 79, 180, 164, 76, 80, 184, 168, 331,611, 608, 555, 333, 624, 621, 568, 323, 332,622, 566, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',256,165, 181, 68, 72, 120, 119, 19, 20, 612,614, 311, 558, 430, 435, 230, 436, 569, 625,303, 312, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',257,166, 182, 181, 165, 116, 115, 119, 120, 615,617, 612, 561, 421, 429, 430, 431, 570, 626,625, 569, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',258,167, 183, 182, 166, 112, 111, 115, 116, 618,620, 615, 564, 412, 420, 421, 422, 571, 627,626, 570, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',259,168, 184, 183, 167, 108, 107, 111, 112, 621,623, 618, 567, 403, 411, 412, 413, 572, 628,627, 571, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',260,76, 80, 184, 168, 36, 35, 107, 108, 333,624, 621, 568, 250, 402, 403, 404, 325, 334,628, 572, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',261,91, 90, 10, 11, 169, 185, 61, 65, 361,360, 219, 362, 629, 631, 296, 575, 574, 630,286, 295, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',262,95, 94, 90, 91, 170, 186, 185, 169, 370,369, 361, 371, 632, 634, 629, 578, 577, 633,630, 574, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',263,99, 98, 94, 95, 171, 187, 186, 170, 379,378, 370, 380, 635, 637, 632, 581, 580, 636,633, 577, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 3:
    ops.element('20_8_BrickUP',264,103, 102, 98, 99, 172, 188, 187, 171, 388,387, 379, 389, 638, 640, 635, 584, 583, 639,636, 580, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',265,27, 26, 102, 103, 77, 81, 188, 172, 239,394, 388, 395, 336, 641, 638, 585, 326, 335,639, 583, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',266,169, 185, 61, 65, 173, 189, 62, 66, 629,631, 296, 575, 642, 644, 298, 588, 587, 643,288, 297, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',267,170, 186, 185, 169, 174, 190, 189, 173, 632,634, 629, 578, 645, 647, 642, 591, 590, 646,643, 587, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',268,171, 187, 186, 170, 175, 191, 190, 174, 635,637, 632, 581, 648, 650, 645, 594, 593, 649,646, 590, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',269,172, 188, 187, 171, 176, 192, 191, 175, 638,640, 635, 584, 651, 653, 648, 597, 596, 652,649, 593, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',270,77, 81, 188, 172, 78, 82, 192, 176, 336,641, 638, 585, 338, 654, 651, 598, 328, 337,652, 596, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',271,173, 189, 62, 66, 177, 193, 63, 67, 642,644, 298, 588, 655, 657, 300, 601, 600, 656,290, 299, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',272,174, 190, 189, 173, 178, 194, 193, 177, 645,647, 642, 591, 658, 660, 655, 604, 603, 659,656, 600, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',273,175, 191, 190, 174, 179, 195, 194, 178, 648,650, 645, 594, 661, 663, 658, 607, 606, 662,659, 603, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',274,176, 192, 191, 175, 180, 196, 195, 179, 651,653, 648, 597, 664, 666, 661, 610, 609, 665,662, 606, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',275,78, 82, 192, 176, 79, 83, 196, 180, 338,654, 651, 598, 340, 667, 664, 611, 330, 339,665, 609, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',276,177, 193, 63, 67, 181, 197, 64, 68, 655,657, 300, 601, 668, 670, 302, 614, 613, 669,292, 301, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',277,178, 194, 193, 177, 182, 198, 197, 181, 658,660, 655, 604, 671, 673, 668, 617, 616, 672,669, 613, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',278,179, 195, 194, 178, 183, 199, 198, 182, 661,663, 658, 607, 674, 676, 671, 620, 619, 675,672, 616, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',279,180, 196, 195, 179, 184, 200, 199, 183, 664,666, 661, 610, 677, 679, 674, 623, 622, 678,675, 619, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',280,79, 83, 196, 180, 80, 84, 200, 184, 340,667, 664, 611, 342, 680, 677, 624, 332, 341,678, 622, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',281,181, 197, 64, 68, 119, 118, 18, 19, 668,670, 302, 614, 428, 434, 229, 435, 625, 681,294, 303, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 4:
    ops.element('20_8_BrickUP',282,182, 198, 197, 181, 115, 114, 118, 119, 671,673, 668, 617, 419, 427, 428, 429, 626, 682,681, 625, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',283,183, 199, 198, 182, 111, 110, 114, 115, 674,676, 671, 620, 410, 418, 419, 420, 627, 683,682, 626, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',284,184, 200, 199, 183, 107, 106, 110, 111, 677,679, 674, 623, 401, 409, 410, 411, 628, 684,683, 627, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',285,80, 84, 200, 184, 35, 34, 106, 107, 342,680, 677, 624, 249, 400, 401, 402, 334, 343,684, 628, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',286,90, 89, 9, 10, 185, 201, 57, 61, 359,358, 218, 360, 685, 687, 287, 631, 630, 686,277, 286, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',287,94, 93, 89, 90, 186, 202, 201, 185, 368,367, 359, 369, 688, 690, 685, 634, 633, 689,686, 630, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',288,98, 97, 93, 94, 187, 203, 202, 186, 377,376, 368, 378, 691, 693, 688, 637, 636, 692,689, 633, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',289,102, 101, 97, 98, 188, 204, 203, 187, 386,385, 377, 387, 694, 696, 691, 640, 639, 695,692, 636, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',290,26, 25, 101, 102, 81, 85, 204, 188, 238,393, 386, 394, 345, 697, 694, 641, 335, 344,695, 639, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',291,185, 201, 57, 61, 189, 205, 58, 62, 685,687, 287, 631, 698, 700, 289, 644, 643, 699,279, 288, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',292,186, 202, 201, 185, 190, 206, 205, 189, 688,690, 685, 634, 701, 703, 698, 647, 646, 702,699, 643, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',293,187, 203, 202, 186, 191, 207, 206, 190, 691,693, 688, 637, 704, 706, 701, 650, 649, 705,702, 646, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',294,188, 204, 203, 187, 192, 208, 207, 191, 694,696, 691, 640, 707, 709, 704, 653, 652, 708,705, 649, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',295,81, 85, 204, 188, 82, 86, 208, 192, 345,697, 694, 641, 347, 710, 707, 654, 337, 346,708, 652, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',296,189, 205, 58, 62, 193, 209, 59, 63, 698,700, 289, 644, 711, 713, 291, 657, 656, 712,281, 290, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',297,190, 206, 205, 189, 194, 210, 209, 193, 701,703, 698, 647, 714, 716, 711, 660, 659, 715,712, 656, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',298,191, 207, 206, 190, 195, 211, 210, 194, 704,706, 701, 650, 717, 719, 714, 663, 662, 718,715, 659, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',299,192, 208, 207, 191, 196, 212, 211, 195, 707,709, 704, 653, 720, 722, 717, 666, 665, 721,718, 662, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 5:
    ops.element('20_8_BrickUP',300,82, 86, 208, 192, 83, 87, 212, 196, 347,710, 707, 654, 349, 723, 720, 667, 339, 348,721, 665, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',301,193, 209, 59, 63, 197, 213, 60, 64, 711,713, 291, 657, 724, 726, 293, 670, 669, 725,283, 292, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',302,194, 210, 209, 193, 198, 214, 213, 197, 714,716, 711, 660, 727, 729, 724, 673, 672, 728,725, 669, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',303,195, 211, 210, 194, 199, 215, 214, 198, 717,719, 714, 663, 730, 732, 727, 676, 675, 731,728, 672, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',304,196, 212, 211, 195, 200, 216, 215, 199, 720,722, 717, 666, 733, 735, 730, 679, 678, 734,731, 675, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',305,83, 87, 212, 196, 84, 88, 216, 200, 349,723, 720, 667, 351, 736, 733, 680, 341, 350,734, 678, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',306,197, 213, 60, 64, 118, 117, 17, 18, 724,726, 293, 670, 426, 433, 228, 434, 681, 737,285, 294, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',307,198, 214, 213, 197, 114, 113, 117, 118, 727,729, 724, 673, 417, 425, 426, 427, 682, 738,737, 681, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',308,199, 215, 214, 198, 110, 109, 113, 114, 730,732, 727, 676, 408, 416, 417, 418, 683, 739,738, 682, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',309,200, 216, 215, 199, 106, 105, 109, 110, 733,735, 730, 679, 399, 407, 408, 409, 684, 740,739, 683, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',310,84, 88, 216, 200, 34, 33, 105, 106, 351,736, 733, 680, 248, 398, 399, 400, 343, 352,740, 684, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',311,89, 41, 2, 9, 201, 121, 21, 57, 357,257, 217, 358, 741, 437, 278, 687, 686, 438,232, 277, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',312,93, 42, 41, 89, 202, 122, 121, 201, 366,258, 357, 367, 742, 439, 741, 690, 689, 440,438, 686, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',313,97, 43, 42, 93, 203, 123, 122, 202, 375,259, 366, 376, 743, 441, 742, 693, 692, 442,440, 689, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',314,101, 44, 43, 97, 204, 124, 123, 203, 384,260, 375, 385, 744, 443, 743, 696, 695, 444,442, 692, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',315,25, 6, 44, 101, 85, 37, 124, 204, 237,261, 384, 393, 353, 445, 744, 697, 344, 252,444, 695, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',316,201, 121, 21, 57, 205, 125, 22, 58, 741,437, 278, 687, 745, 446, 280, 700, 699, 447,233, 279, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',317,202, 122, 121, 201, 206, 126, 125, 205, 742,439, 741, 690, 746, 448, 745, 703, 702, 449,447, 699, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 6:
    ops.element('20_8_BrickUP',318,203, 123, 122, 202, 207, 127, 126, 206, 743,441, 742, 693, 747, 450, 746, 706, 705, 451,449, 702, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',319,204, 124, 123, 203, 208, 128, 127, 207, 744,443, 743, 696, 748, 452, 747, 709, 708, 453,451, 705, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',320,85, 37, 124, 204, 86, 38, 128, 208, 353,445, 744, 697, 354, 454, 748, 710, 346, 253,453, 708, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',321,205, 125, 22, 58, 209, 129, 23, 59, 745,446, 280, 700, 749, 455, 282, 713, 712, 456,234, 281, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',322,206, 126, 125, 205, 210, 130, 129, 209, 746,448, 745, 703, 750, 457, 749, 716, 715, 458,456, 712, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',323,207, 127, 126, 206, 211, 131, 130, 210, 747,450, 746, 706, 751, 459, 750, 719, 718, 460,458, 715, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',324,208, 128, 127, 207, 212, 132, 131, 211, 748,452, 747, 709, 752, 461, 751, 722, 721, 462,460, 718, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',325,86, 38, 128, 208, 87, 39, 132, 212, 354,454, 748, 710, 355, 463, 752, 723, 348, 254,462, 721, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',326,209, 129, 23, 59, 213, 133, 24, 60, 749,455, 282, 713, 753, 464, 284, 726, 725, 465,235, 283, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',327,210, 130, 129, 209, 214, 134, 133, 213, 750,457, 749, 716, 754, 466, 753, 729, 728, 467,465, 725, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',328,211, 131, 130, 210, 215, 135, 134, 214, 751,459, 750, 719, 755, 468, 754, 732, 731, 469,467, 728, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',329,212, 132, 131, 211, 216, 136, 135, 215, 752,461, 751, 722, 756, 470, 755, 735, 734, 471,469, 731, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',330,87, 39, 132, 212, 88, 40, 136, 216, 355,463, 752, 723, 356, 472, 756, 736, 350, 255,471, 734, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',331,213, 133, 24, 60, 117, 49, 4, 17, 753,464, 284, 726, 424, 267, 227, 433, 737, 473,236, 285, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',332,214, 134, 133, 213, 113, 50, 49, 117, 754,466, 753, 729, 415, 268, 424, 425, 738, 474,473, 737, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',333,215, 135, 134, 214, 109, 51, 50, 113, 755,468, 754, 732, 406, 269, 415, 416, 739, 475,474, 738, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',334,216, 136, 135, 215, 105, 52, 51, 109, 756,470, 755, 735, 397, 270, 406, 407, 740, 476,475, 739, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.element('20_8_BrickUP',335,88, 40, 136, 216, 33, 8, 52, 105, 356,472, 756, 736, 247, 271, 397, 398, 352, 256,476, 740, 1, 2.2e6, 1, 1.0, 1.0, 1.0, 0.0, 0.0,-9.81)
if pid == 7:
    ops.node(757,5.0,5.0,0.0)
    ops.node(758,5.0,5.0,0.0)
    ops.fix(758,1,1,1)
    ops.fix(757,0,1,1)
    ops.equalDOF(int(458), int(757),1)
    ops.uniaxialMaterial('Viscous',2,225000.0, 1)
    dir = [1]
    ops.element('zeroLength', 336, 758, 757, '-mat', 2, '-dir', *dir)
if pid == 1:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',1, 519,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',1, 519,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',1, 519,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',45, 522,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',45, 522,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',45, 522,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',46, 525,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',46, 525,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',46, 525,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',47, 528,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',47, 528,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',47, 528,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',5, 529,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',5, 529,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',5, 529,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',13, 532,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',13, 532,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',13, 532,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',145, 535,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',145, 535,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',145, 535,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',146, 538,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',146, 538,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',146, 538,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',147, 541,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',147, 541,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',147, 541,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',29, 542,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',29, 542,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',29, 542,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',14, 545,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',14, 545,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',14, 545,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',141, 548,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',141, 548,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',141, 548,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',142, 551,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',142, 551,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',142, 551,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',143, 554,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',143, 554,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',143, 554,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',30, 555,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',30, 555,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',30, 555,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',15, 558,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',15, 558,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',15, 558,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',137, 561,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',137, 561,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',137, 561,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',138, 564,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',138, 564,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',138, 564,'-dof', 4, 'vel')
if pid == 2:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',139, 567,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',139, 567,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',139, 567,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',31, 568,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',31, 568,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',31, 568,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',3, 569,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',3, 569,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',3, 569,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',53, 570,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',53, 570,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',53, 570,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',54, 571,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',54, 571,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',54, 571,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',55, 572,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',55, 572,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',55, 572,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',7, 572,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',7, 572,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',7, 572,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',11, 575,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',11, 575,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',11, 575,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',91, 578,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',91, 578,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',91, 578,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',95, 581,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',95, 581,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',95, 581,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',99, 584,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',99, 584,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',99, 584,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',27, 585,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',27, 585,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',27, 585,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',65, 588,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',65, 588,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',65, 588,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',153, 591,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',153, 591,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',153, 591,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',154, 594,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',154, 594,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',154, 594,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',155, 597,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',155, 597,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',155, 597,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',73, 598,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',73, 598,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',73, 598,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',66, 601,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',66, 601,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',66, 601,'-dof', 4, 'vel')
if pid == 3:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',157, 604,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',157, 604,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',157, 604,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',158, 607,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',158, 607,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',158, 607,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',159, 610,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',159, 610,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',159, 610,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',74, 611,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',74, 611,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',74, 611,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',67, 614,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',67, 614,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',67, 614,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',161, 617,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',161, 617,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',161, 617,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',162, 620,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',162, 620,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',162, 620,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',163, 623,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',163, 623,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',163, 623,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',75, 624,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',75, 624,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',75, 624,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',19, 625,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',19, 625,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',19, 625,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',115, 626,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',115, 626,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',115, 626,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',111, 627,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',111, 627,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',111, 627,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',107, 628,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',107, 628,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',107, 628,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',35, 628,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',35, 628,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',35, 628,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',10, 631,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',10, 631,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',10, 631,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',90, 634,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',90, 634,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',90, 634,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',94, 637,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',94, 637,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',94, 637,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',98, 640,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',98, 640,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',98, 640,'-dof', 4, 'vel')
if pid == 4:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',26, 641,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',26, 641,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',26, 641,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',61, 644,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',61, 644,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',61, 644,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',169, 647,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',169, 647,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',169, 647,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',170, 650,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',170, 650,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',170, 650,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',171, 653,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',171, 653,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',171, 653,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',77, 654,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',77, 654,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',77, 654,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',62, 657,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',62, 657,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',62, 657,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',173, 660,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',173, 660,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',173, 660,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',174, 663,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',174, 663,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',174, 663,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',175, 666,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',175, 666,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',175, 666,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',78, 667,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',78, 667,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',78, 667,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',63, 670,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',63, 670,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',63, 670,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',177, 673,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',177, 673,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',177, 673,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',178, 676,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',178, 676,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',178, 676,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',179, 679,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',179, 679,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',179, 679,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',79, 680,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',79, 680,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',79, 680,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',18, 681,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',18, 681,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',18, 681,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',114, 682,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',114, 682,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',114, 682,'-dof', 4, 'vel')
if pid == 5:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',110, 683,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',110, 683,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',110, 683,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',106, 684,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',106, 684,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',106, 684,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',34, 684,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',34, 684,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',34, 684,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',9, 687,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',9, 687,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',9, 687,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',89, 690,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',89, 690,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',89, 690,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',93, 693,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',93, 693,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',93, 693,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',97, 696,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',97, 696,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',97, 696,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',25, 697,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',25, 697,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',25, 697,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',57, 700,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',57, 700,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',57, 700,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',185, 703,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',185, 703,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',185, 703,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',186, 706,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',186, 706,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',186, 706,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',187, 709,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',187, 709,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',187, 709,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',81, 710,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',81, 710,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',81, 710,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',58, 713,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',58, 713,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',58, 713,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',189, 716,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',189, 716,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',189, 716,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',190, 719,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',190, 719,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',190, 719,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',191, 722,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',191, 722,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',191, 722,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',82, 723,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',82, 723,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',82, 723,'-dof', 4, 'vel')
if pid == 6:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',59, 726,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',59, 726,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',59, 726,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',193, 729,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',193, 729,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',193, 729,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',194, 732,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',194, 732,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',194, 732,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',195, 735,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',195, 735,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',195, 735,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',83, 736,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',83, 736,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',83, 736,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',17, 737,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',17, 737,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',17, 737,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',113, 738,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',113, 738,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',113, 738,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',109, 739,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',109, 739,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',109, 739,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',105, 740,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',105, 740,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',105, 740,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',33, 740,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',33, 740,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',33, 740,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',2, 741,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',2, 741,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',2, 741,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',41, 742,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',41, 742,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',41, 742,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',42, 743,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',42, 743,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',42, 743,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',43, 744,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',43, 744,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',43, 744,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',6, 744,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',6, 744,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',6, 744,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',21, 745,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',21, 745,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',21, 745,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',121, 746,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',121, 746,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',121, 746,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',122, 747,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',122, 747,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',122, 747,'-dof', 4, 'vel')
if pid == 7:
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',123, 748,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',123, 748,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',123, 748,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',37, 748,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',37, 748,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',37, 748,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',22, 749,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',22, 749,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',22, 749,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',125, 750,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',125, 750,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',125, 750,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',126, 751,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',126, 751,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',126, 751,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',127, 752,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',127, 752,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',127, 752,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',38, 752,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',38, 752,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',38, 752,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',23, 753,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',23, 753,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',23, 753,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',129, 754,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',129, 754,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',129, 754,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',130, 755,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',130, 755,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',130, 755,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',131, 756,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',131, 756,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',131, 756,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',39, 756,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',39, 756,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',39, 756,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',4, 753,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',4, 753,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',4, 753,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',49, 754,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',49, 754,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',49, 754,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',50, 755,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',50, 755,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',50, 755,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',51, 756,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',51, 756,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',51, 756,'-dof', 4, 'vel')
    ops.recorder('Node','-file','Gdisplacement.out','-time','-nodeRange',8, 756,'-dof', 1, 2, 3, 'disp')
    ops.recorder('Node','-file','Gacceleration.out','-time','-nodeRange',8, 756,'-dof', 1, 2, 3, 'accel')
    ops.recorder('Node','-file','GporePressure.out','-time','-nodeRange',8, 756,'-dof', 4, 'vel')
if pid == 1:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 211,228,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 211,228,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 211,228,'material','1','strain')
if pid == 2:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 229,246,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 229,246,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 229,246,'material','1','strain')
if pid == 3:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 247,264,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 247,264,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 247,264,'material','1','strain')
if pid == 4:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 265,282,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 265,282,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 265,282,'material','1','strain')
if pid == 5:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 283,300,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 283,300,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 283,300,'material','1','strain')
if pid == 6:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 301,318,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 301,318,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 301,318,'material','1','strain')
if pid == 7:
    ops.recorder('Element','-file','Gstress.out','-time','-eleRange', 319,335,'material','1','stress')
    ops.recorder('Element','-file','Ggauss.out','-time','-eleRange', 319,335,'material','1','gausspoint')
    ops.recorder('Element','-file','Gstrain.out','-time','-eleRange', 319,335,'material','1','strain')
motionDT = 0.005
recDT = 10*0.005
motionSteps = 2500
nSteps = 2500
dT = 0.005
print('static phase')
ops.model("basicBuilder","-ndm",3,"-ndf",4)
ops.updateMaterialStage('-material', 1, '-stage', 0)
ops.updateMaterialStage('-material', 2, '-stage', 0)
ops.constraints('Penalty', 1.e18, 1.e18)
ops.test('NormDispIncr', 1.0e-6, 500, 1)
ops.algorithm('KrylovNewton')
ops.numberer('ParallelRCM')
ops.system('Mumps')
ops.integrator('Newmark', 0.5, 0.25)
ops.analysis('Transient')
startT = tt.time()
ops.analyze(1,1)
ops.updateMaterialStage('-material', 1, '-stage', 1)
ops.updateMaterialStage('-material', 2, '-stage', 1)
ops.domainChange()
if pid == 1:
    ops.parameter(1, 'element', 211,'hPerm')
    ops.parameter(2, 'element', 211,'vPerm')
    ops.updateParameter(1,0.1)
    ops.updateParameter(2,0.1)
if pid == 1:
    ops.parameter(3, 'element', 212,'hPerm')
    ops.parameter(4, 'element', 212,'vPerm')
    ops.updateParameter(3,0.1)
    ops.updateParameter(4,0.1)
if pid == 1:
    ops.parameter(5, 'element', 213,'hPerm')
    ops.parameter(6, 'element', 213,'vPerm')
    ops.updateParameter(5,0.1)
    ops.updateParameter(6,0.1)
if pid == 1:
    ops.parameter(7, 'element', 214,'hPerm')
    ops.parameter(8, 'element', 214,'vPerm')
    ops.updateParameter(7,0.1)
    ops.updateParameter(8,0.1)
if pid == 1:
    ops.parameter(9, 'element', 215,'hPerm')
    ops.parameter(10, 'element', 215,'vPerm')
    ops.updateParameter(9,0.1)
    ops.updateParameter(10,0.1)
if pid == 1:
    ops.parameter(11, 'element', 216,'hPerm')
    ops.parameter(12, 'element', 216,'vPerm')
    ops.updateParameter(11,0.1)
    ops.updateParameter(12,0.1)
if pid == 1:
    ops.parameter(13, 'element', 217,'hPerm')
    ops.parameter(14, 'element', 217,'vPerm')
    ops.updateParameter(13,0.1)
    ops.updateParameter(14,0.1)
if pid == 1:
    ops.parameter(15, 'element', 218,'hPerm')
    ops.parameter(16, 'element', 218,'vPerm')
    ops.updateParameter(15,0.1)
    ops.updateParameter(16,0.1)
if pid == 1:
    ops.parameter(17, 'element', 219,'hPerm')
    ops.parameter(18, 'element', 219,'vPerm')
    ops.updateParameter(17,0.1)
    ops.updateParameter(18,0.1)
if pid == 1:
    ops.parameter(19, 'element', 220,'hPerm')
    ops.parameter(20, 'element', 220,'vPerm')
    ops.updateParameter(19,0.1)
    ops.updateParameter(20,0.1)
if pid == 1:
    ops.parameter(21, 'element', 221,'hPerm')
    ops.parameter(22, 'element', 221,'vPerm')
    ops.updateParameter(21,0.1)
    ops.updateParameter(22,0.1)
if pid == 1:
    ops.parameter(23, 'element', 222,'hPerm')
    ops.parameter(24, 'element', 222,'vPerm')
    ops.updateParameter(23,0.1)
    ops.updateParameter(24,0.1)
if pid == 1:
    ops.parameter(25, 'element', 223,'hPerm')
    ops.parameter(26, 'element', 223,'vPerm')
    ops.updateParameter(25,0.1)
    ops.updateParameter(26,0.1)
if pid == 1:
    ops.parameter(27, 'element', 224,'hPerm')
    ops.parameter(28, 'element', 224,'vPerm')
    ops.updateParameter(27,0.1)
    ops.updateParameter(28,0.1)
if pid == 1:
    ops.parameter(29, 'element', 225,'hPerm')
    ops.parameter(30, 'element', 225,'vPerm')
    ops.updateParameter(29,0.1)
    ops.updateParameter(30,0.1)
if pid == 1:
    ops.parameter(31, 'element', 226,'hPerm')
    ops.parameter(32, 'element', 226,'vPerm')
    ops.updateParameter(31,0.1)
    ops.updateParameter(32,0.1)
if pid == 1:
    ops.parameter(33, 'element', 227,'hPerm')
    ops.parameter(34, 'element', 227,'vPerm')
    ops.updateParameter(33,0.1)
    ops.updateParameter(34,0.1)
if pid == 1:
    ops.parameter(35, 'element', 228,'hPerm')
    ops.parameter(36, 'element', 228,'vPerm')
    ops.updateParameter(35,0.1)
    ops.updateParameter(36,0.1)
if pid == 2:
    ops.parameter(37, 'element', 229,'hPerm')
    ops.parameter(38, 'element', 229,'vPerm')
    ops.updateParameter(37,0.1)
    ops.updateParameter(38,0.1)
if pid == 2:
    ops.parameter(39, 'element', 230,'hPerm')
    ops.parameter(40, 'element', 230,'vPerm')
    ops.updateParameter(39,0.1)
    ops.updateParameter(40,0.1)
if pid == 2:
    ops.parameter(41, 'element', 231,'hPerm')
    ops.parameter(42, 'element', 231,'vPerm')
    ops.updateParameter(41,0.1)
    ops.updateParameter(42,0.1)
if pid == 2:
    ops.parameter(43, 'element', 232,'hPerm')
    ops.parameter(44, 'element', 232,'vPerm')
    ops.updateParameter(43,0.1)
    ops.updateParameter(44,0.1)
if pid == 2:
    ops.parameter(45, 'element', 233,'hPerm')
    ops.parameter(46, 'element', 233,'vPerm')
    ops.updateParameter(45,0.1)
    ops.updateParameter(46,0.1)
if pid == 2:
    ops.parameter(47, 'element', 234,'hPerm')
    ops.parameter(48, 'element', 234,'vPerm')
    ops.updateParameter(47,0.1)
    ops.updateParameter(48,0.1)
if pid == 2:
    ops.parameter(49, 'element', 235,'hPerm')
    ops.parameter(50, 'element', 235,'vPerm')
    ops.updateParameter(49,0.1)
    ops.updateParameter(50,0.1)
if pid == 2:
    ops.parameter(51, 'element', 236,'hPerm')
    ops.parameter(52, 'element', 236,'vPerm')
    ops.updateParameter(51,0.1)
    ops.updateParameter(52,0.1)
if pid == 2:
    ops.parameter(53, 'element', 237,'hPerm')
    ops.parameter(54, 'element', 237,'vPerm')
    ops.updateParameter(53,0.1)
    ops.updateParameter(54,0.1)
if pid == 2:
    ops.parameter(55, 'element', 238,'hPerm')
    ops.parameter(56, 'element', 238,'vPerm')
    ops.updateParameter(55,0.1)
    ops.updateParameter(56,0.1)
if pid == 2:
    ops.parameter(57, 'element', 239,'hPerm')
    ops.parameter(58, 'element', 239,'vPerm')
    ops.updateParameter(57,0.1)
    ops.updateParameter(58,0.1)
if pid == 2:
    ops.parameter(59, 'element', 240,'hPerm')
    ops.parameter(60, 'element', 240,'vPerm')
    ops.updateParameter(59,0.1)
    ops.updateParameter(60,0.1)
if pid == 2:
    ops.parameter(61, 'element', 241,'hPerm')
    ops.parameter(62, 'element', 241,'vPerm')
    ops.updateParameter(61,0.1)
    ops.updateParameter(62,0.1)
if pid == 2:
    ops.parameter(63, 'element', 242,'hPerm')
    ops.parameter(64, 'element', 242,'vPerm')
    ops.updateParameter(63,0.1)
    ops.updateParameter(64,0.1)
if pid == 2:
    ops.parameter(65, 'element', 243,'hPerm')
    ops.parameter(66, 'element', 243,'vPerm')
    ops.updateParameter(65,0.1)
    ops.updateParameter(66,0.1)
if pid == 2:
    ops.parameter(67, 'element', 244,'hPerm')
    ops.parameter(68, 'element', 244,'vPerm')
    ops.updateParameter(67,0.1)
    ops.updateParameter(68,0.1)
if pid == 2:
    ops.parameter(69, 'element', 245,'hPerm')
    ops.parameter(70, 'element', 245,'vPerm')
    ops.updateParameter(69,0.1)
    ops.updateParameter(70,0.1)
if pid == 2:
    ops.parameter(71, 'element', 246,'hPerm')
    ops.parameter(72, 'element', 246,'vPerm')
    ops.updateParameter(71,0.1)
    ops.updateParameter(72,0.1)
if pid == 3:
    ops.parameter(73, 'element', 247,'hPerm')
    ops.parameter(74, 'element', 247,'vPerm')
    ops.updateParameter(73,0.1)
    ops.updateParameter(74,0.1)
if pid == 3:
    ops.parameter(75, 'element', 248,'hPerm')
    ops.parameter(76, 'element', 248,'vPerm')
    ops.updateParameter(75,0.1)
    ops.updateParameter(76,0.1)
if pid == 3:
    ops.parameter(77, 'element', 249,'hPerm')
    ops.parameter(78, 'element', 249,'vPerm')
    ops.updateParameter(77,0.1)
    ops.updateParameter(78,0.1)
if pid == 3:
    ops.parameter(79, 'element', 250,'hPerm')
    ops.parameter(80, 'element', 250,'vPerm')
    ops.updateParameter(79,0.1)
    ops.updateParameter(80,0.1)
if pid == 3:
    ops.parameter(81, 'element', 251,'hPerm')
    ops.parameter(82, 'element', 251,'vPerm')
    ops.updateParameter(81,0.1)
    ops.updateParameter(82,0.1)
if pid == 3:
    ops.parameter(83, 'element', 252,'hPerm')
    ops.parameter(84, 'element', 252,'vPerm')
    ops.updateParameter(83,0.1)
    ops.updateParameter(84,0.1)
if pid == 3:
    ops.parameter(85, 'element', 253,'hPerm')
    ops.parameter(86, 'element', 253,'vPerm')
    ops.updateParameter(85,0.1)
    ops.updateParameter(86,0.1)
if pid == 3:
    ops.parameter(87, 'element', 254,'hPerm')
    ops.parameter(88, 'element', 254,'vPerm')
    ops.updateParameter(87,0.1)
    ops.updateParameter(88,0.1)
if pid == 3:
    ops.parameter(89, 'element', 255,'hPerm')
    ops.parameter(90, 'element', 255,'vPerm')
    ops.updateParameter(89,0.1)
    ops.updateParameter(90,0.1)
if pid == 3:
    ops.parameter(91, 'element', 256,'hPerm')
    ops.parameter(92, 'element', 256,'vPerm')
    ops.updateParameter(91,0.1)
    ops.updateParameter(92,0.1)
if pid == 3:
    ops.parameter(93, 'element', 257,'hPerm')
    ops.parameter(94, 'element', 257,'vPerm')
    ops.updateParameter(93,0.1)
    ops.updateParameter(94,0.1)
if pid == 3:
    ops.parameter(95, 'element', 258,'hPerm')
    ops.parameter(96, 'element', 258,'vPerm')
    ops.updateParameter(95,0.1)
    ops.updateParameter(96,0.1)
if pid == 3:
    ops.parameter(97, 'element', 259,'hPerm')
    ops.parameter(98, 'element', 259,'vPerm')
    ops.updateParameter(97,0.1)
    ops.updateParameter(98,0.1)
if pid == 3:
    ops.parameter(99, 'element', 260,'hPerm')
    ops.parameter(100, 'element', 260,'vPerm')
    ops.updateParameter(99,0.1)
    ops.updateParameter(100,0.1)
if pid == 3:
    ops.parameter(101, 'element', 261,'hPerm')
    ops.parameter(102, 'element', 261,'vPerm')
    ops.updateParameter(101,0.1)
    ops.updateParameter(102,0.1)
if pid == 3:
    ops.parameter(103, 'element', 262,'hPerm')
    ops.parameter(104, 'element', 262,'vPerm')
    ops.updateParameter(103,0.1)
    ops.updateParameter(104,0.1)
if pid == 3:
    ops.parameter(105, 'element', 263,'hPerm')
    ops.parameter(106, 'element', 263,'vPerm')
    ops.updateParameter(105,0.1)
    ops.updateParameter(106,0.1)
if pid == 3:
    ops.parameter(107, 'element', 264,'hPerm')
    ops.parameter(108, 'element', 264,'vPerm')
    ops.updateParameter(107,0.1)
    ops.updateParameter(108,0.1)
if pid == 4:
    ops.parameter(109, 'element', 265,'hPerm')
    ops.parameter(110, 'element', 265,'vPerm')
    ops.updateParameter(109,0.1)
    ops.updateParameter(110,0.1)
if pid == 4:
    ops.parameter(111, 'element', 266,'hPerm')
    ops.parameter(112, 'element', 266,'vPerm')
    ops.updateParameter(111,0.1)
    ops.updateParameter(112,0.1)
if pid == 4:
    ops.parameter(113, 'element', 267,'hPerm')
    ops.parameter(114, 'element', 267,'vPerm')
    ops.updateParameter(113,0.1)
    ops.updateParameter(114,0.1)
if pid == 4:
    ops.parameter(115, 'element', 268,'hPerm')
    ops.parameter(116, 'element', 268,'vPerm')
    ops.updateParameter(115,0.1)
    ops.updateParameter(116,0.1)
if pid == 4:
    ops.parameter(117, 'element', 269,'hPerm')
    ops.parameter(118, 'element', 269,'vPerm')
    ops.updateParameter(117,0.1)
    ops.updateParameter(118,0.1)
if pid == 4:
    ops.parameter(119, 'element', 270,'hPerm')
    ops.parameter(120, 'element', 270,'vPerm')
    ops.updateParameter(119,0.1)
    ops.updateParameter(120,0.1)
if pid == 4:
    ops.parameter(121, 'element', 271,'hPerm')
    ops.parameter(122, 'element', 271,'vPerm')
    ops.updateParameter(121,0.1)
    ops.updateParameter(122,0.1)
if pid == 4:
    ops.parameter(123, 'element', 272,'hPerm')
    ops.parameter(124, 'element', 272,'vPerm')
    ops.updateParameter(123,0.1)
    ops.updateParameter(124,0.1)
if pid == 4:
    ops.parameter(125, 'element', 273,'hPerm')
    ops.parameter(126, 'element', 273,'vPerm')
    ops.updateParameter(125,0.1)
    ops.updateParameter(126,0.1)
if pid == 4:
    ops.parameter(127, 'element', 274,'hPerm')
    ops.parameter(128, 'element', 274,'vPerm')
    ops.updateParameter(127,0.1)
    ops.updateParameter(128,0.1)
if pid == 4:
    ops.parameter(129, 'element', 275,'hPerm')
    ops.parameter(130, 'element', 275,'vPerm')
    ops.updateParameter(129,0.1)
    ops.updateParameter(130,0.1)
if pid == 4:
    ops.parameter(131, 'element', 276,'hPerm')
    ops.parameter(132, 'element', 276,'vPerm')
    ops.updateParameter(131,0.1)
    ops.updateParameter(132,0.1)
if pid == 4:
    ops.parameter(133, 'element', 277,'hPerm')
    ops.parameter(134, 'element', 277,'vPerm')
    ops.updateParameter(133,0.1)
    ops.updateParameter(134,0.1)
if pid == 4:
    ops.parameter(135, 'element', 278,'hPerm')
    ops.parameter(136, 'element', 278,'vPerm')
    ops.updateParameter(135,0.1)
    ops.updateParameter(136,0.1)
if pid == 4:
    ops.parameter(137, 'element', 279,'hPerm')
    ops.parameter(138, 'element', 279,'vPerm')
    ops.updateParameter(137,0.1)
    ops.updateParameter(138,0.1)
if pid == 4:
    ops.parameter(139, 'element', 280,'hPerm')
    ops.parameter(140, 'element', 280,'vPerm')
    ops.updateParameter(139,0.1)
    ops.updateParameter(140,0.1)
if pid == 4:
    ops.parameter(141, 'element', 281,'hPerm')
    ops.parameter(142, 'element', 281,'vPerm')
    ops.updateParameter(141,0.1)
    ops.updateParameter(142,0.1)
if pid == 4:
    ops.parameter(143, 'element', 282,'hPerm')
    ops.parameter(144, 'element', 282,'vPerm')
    ops.updateParameter(143,0.1)
    ops.updateParameter(144,0.1)
if pid == 5:
    ops.parameter(145, 'element', 283,'hPerm')
    ops.parameter(146, 'element', 283,'vPerm')
    ops.updateParameter(145,0.1)
    ops.updateParameter(146,0.1)
if pid == 5:
    ops.parameter(147, 'element', 284,'hPerm')
    ops.parameter(148, 'element', 284,'vPerm')
    ops.updateParameter(147,0.1)
    ops.updateParameter(148,0.1)
if pid == 5:
    ops.parameter(149, 'element', 285,'hPerm')
    ops.parameter(150, 'element', 285,'vPerm')
    ops.updateParameter(149,0.1)
    ops.updateParameter(150,0.1)
if pid == 5:
    ops.parameter(151, 'element', 286,'hPerm')
    ops.parameter(152, 'element', 286,'vPerm')
    ops.updateParameter(151,0.1)
    ops.updateParameter(152,0.1)
if pid == 5:
    ops.parameter(153, 'element', 287,'hPerm')
    ops.parameter(154, 'element', 287,'vPerm')
    ops.updateParameter(153,0.1)
    ops.updateParameter(154,0.1)
if pid == 5:
    ops.parameter(155, 'element', 288,'hPerm')
    ops.parameter(156, 'element', 288,'vPerm')
    ops.updateParameter(155,0.1)
    ops.updateParameter(156,0.1)
if pid == 5:
    ops.parameter(157, 'element', 289,'hPerm')
    ops.parameter(158, 'element', 289,'vPerm')
    ops.updateParameter(157,0.1)
    ops.updateParameter(158,0.1)
if pid == 5:
    ops.parameter(159, 'element', 290,'hPerm')
    ops.parameter(160, 'element', 290,'vPerm')
    ops.updateParameter(159,0.1)
    ops.updateParameter(160,0.1)
if pid == 5:
    ops.parameter(161, 'element', 291,'hPerm')
    ops.parameter(162, 'element', 291,'vPerm')
    ops.updateParameter(161,0.1)
    ops.updateParameter(162,0.1)
if pid == 5:
    ops.parameter(163, 'element', 292,'hPerm')
    ops.parameter(164, 'element', 292,'vPerm')
    ops.updateParameter(163,0.1)
    ops.updateParameter(164,0.1)
if pid == 5:
    ops.parameter(165, 'element', 293,'hPerm')
    ops.parameter(166, 'element', 293,'vPerm')
    ops.updateParameter(165,0.1)
    ops.updateParameter(166,0.1)
if pid == 5:
    ops.parameter(167, 'element', 294,'hPerm')
    ops.parameter(168, 'element', 294,'vPerm')
    ops.updateParameter(167,0.1)
    ops.updateParameter(168,0.1)
if pid == 5:
    ops.parameter(169, 'element', 295,'hPerm')
    ops.parameter(170, 'element', 295,'vPerm')
    ops.updateParameter(169,0.1)
    ops.updateParameter(170,0.1)
if pid == 5:
    ops.parameter(171, 'element', 296,'hPerm')
    ops.parameter(172, 'element', 296,'vPerm')
    ops.updateParameter(171,0.1)
    ops.updateParameter(172,0.1)
if pid == 5:
    ops.parameter(173, 'element', 297,'hPerm')
    ops.parameter(174, 'element', 297,'vPerm')
    ops.updateParameter(173,0.1)
    ops.updateParameter(174,0.1)
if pid == 5:
    ops.parameter(175, 'element', 298,'hPerm')
    ops.parameter(176, 'element', 298,'vPerm')
    ops.updateParameter(175,0.1)
    ops.updateParameter(176,0.1)
if pid == 5:
    ops.parameter(177, 'element', 299,'hPerm')
    ops.parameter(178, 'element', 299,'vPerm')
    ops.updateParameter(177,0.1)
    ops.updateParameter(178,0.1)
if pid == 5:
    ops.parameter(179, 'element', 300,'hPerm')
    ops.parameter(180, 'element', 300,'vPerm')
    ops.updateParameter(179,0.1)
    ops.updateParameter(180,0.1)
if pid == 6:
    ops.parameter(181, 'element', 301,'hPerm')
    ops.parameter(182, 'element', 301,'vPerm')
    ops.updateParameter(181,0.1)
    ops.updateParameter(182,0.1)
if pid == 6:
    ops.parameter(183, 'element', 302,'hPerm')
    ops.parameter(184, 'element', 302,'vPerm')
    ops.updateParameter(183,0.1)
    ops.updateParameter(184,0.1)
if pid == 6:
    ops.parameter(185, 'element', 303,'hPerm')
    ops.parameter(186, 'element', 303,'vPerm')
    ops.updateParameter(185,0.1)
    ops.updateParameter(186,0.1)
if pid == 6:
    ops.parameter(187, 'element', 304,'hPerm')
    ops.parameter(188, 'element', 304,'vPerm')
    ops.updateParameter(187,0.1)
    ops.updateParameter(188,0.1)
if pid == 6:
    ops.parameter(189, 'element', 305,'hPerm')
    ops.parameter(190, 'element', 305,'vPerm')
    ops.updateParameter(189,0.1)
    ops.updateParameter(190,0.1)
if pid == 6:
    ops.parameter(191, 'element', 306,'hPerm')
    ops.parameter(192, 'element', 306,'vPerm')
    ops.updateParameter(191,0.1)
    ops.updateParameter(192,0.1)
if pid == 6:
    ops.parameter(193, 'element', 307,'hPerm')
    ops.parameter(194, 'element', 307,'vPerm')
    ops.updateParameter(193,0.1)
    ops.updateParameter(194,0.1)
if pid == 6:
    ops.parameter(195, 'element', 308,'hPerm')
    ops.parameter(196, 'element', 308,'vPerm')
    ops.updateParameter(195,0.1)
    ops.updateParameter(196,0.1)
if pid == 6:
    ops.parameter(197, 'element', 309,'hPerm')
    ops.parameter(198, 'element', 309,'vPerm')
    ops.updateParameter(197,0.1)
    ops.updateParameter(198,0.1)
if pid == 6:
    ops.parameter(199, 'element', 310,'hPerm')
    ops.parameter(200, 'element', 310,'vPerm')
    ops.updateParameter(199,0.1)
    ops.updateParameter(200,0.1)
if pid == 6:
    ops.parameter(201, 'element', 311,'hPerm')
    ops.parameter(202, 'element', 311,'vPerm')
    ops.updateParameter(201,0.1)
    ops.updateParameter(202,0.1)
if pid == 6:
    ops.parameter(203, 'element', 312,'hPerm')
    ops.parameter(204, 'element', 312,'vPerm')
    ops.updateParameter(203,0.1)
    ops.updateParameter(204,0.1)
if pid == 6:
    ops.parameter(205, 'element', 313,'hPerm')
    ops.parameter(206, 'element', 313,'vPerm')
    ops.updateParameter(205,0.1)
    ops.updateParameter(206,0.1)
if pid == 6:
    ops.parameter(207, 'element', 314,'hPerm')
    ops.parameter(208, 'element', 314,'vPerm')
    ops.updateParameter(207,0.1)
    ops.updateParameter(208,0.1)
if pid == 6:
    ops.parameter(209, 'element', 315,'hPerm')
    ops.parameter(210, 'element', 315,'vPerm')
    ops.updateParameter(209,0.1)
    ops.updateParameter(210,0.1)
if pid == 6:
    ops.parameter(211, 'element', 316,'hPerm')
    ops.parameter(212, 'element', 316,'vPerm')
    ops.updateParameter(211,0.1)
    ops.updateParameter(212,0.1)
if pid == 6:
    ops.parameter(213, 'element', 317,'hPerm')
    ops.parameter(214, 'element', 317,'vPerm')
    ops.updateParameter(213,0.1)
    ops.updateParameter(214,0.1)
if pid == 6:
    ops.parameter(215, 'element', 318,'hPerm')
    ops.parameter(216, 'element', 318,'vPerm')
    ops.updateParameter(215,0.1)
    ops.updateParameter(216,0.1)
if pid == 7:
    ops.parameter(217, 'element', 319,'hPerm')
    ops.parameter(218, 'element', 319,'vPerm')
    ops.updateParameter(217,0.1)
    ops.updateParameter(218,0.1)
if pid == 7:
    ops.parameter(219, 'element', 320,'hPerm')
    ops.parameter(220, 'element', 320,'vPerm')
    ops.updateParameter(219,0.1)
    ops.updateParameter(220,0.1)
if pid == 7:
    ops.parameter(221, 'element', 321,'hPerm')
    ops.parameter(222, 'element', 321,'vPerm')
    ops.updateParameter(221,0.1)
    ops.updateParameter(222,0.1)
if pid == 7:
    ops.parameter(223, 'element', 322,'hPerm')
    ops.parameter(224, 'element', 322,'vPerm')
    ops.updateParameter(223,0.1)
    ops.updateParameter(224,0.1)
if pid == 7:
    ops.parameter(225, 'element', 323,'hPerm')
    ops.parameter(226, 'element', 323,'vPerm')
    ops.updateParameter(225,0.1)
    ops.updateParameter(226,0.1)
if pid == 7:
    ops.parameter(227, 'element', 324,'hPerm')
    ops.parameter(228, 'element', 324,'vPerm')
    ops.updateParameter(227,0.1)
    ops.updateParameter(228,0.1)
if pid == 7:
    ops.parameter(229, 'element', 325,'hPerm')
    ops.parameter(230, 'element', 325,'vPerm')
    ops.updateParameter(229,0.1)
    ops.updateParameter(230,0.1)
if pid == 7:
    ops.parameter(231, 'element', 326,'hPerm')
    ops.parameter(232, 'element', 326,'vPerm')
    ops.updateParameter(231,0.1)
    ops.updateParameter(232,0.1)
if pid == 7:
    ops.parameter(233, 'element', 327,'hPerm')
    ops.parameter(234, 'element', 327,'vPerm')
    ops.updateParameter(233,0.1)
    ops.updateParameter(234,0.1)
if pid == 7:
    ops.parameter(235, 'element', 328,'hPerm')
    ops.parameter(236, 'element', 328,'vPerm')
    ops.updateParameter(235,0.1)
    ops.updateParameter(236,0.1)
if pid == 7:
    ops.parameter(237, 'element', 329,'hPerm')
    ops.parameter(238, 'element', 329,'vPerm')
    ops.updateParameter(237,0.1)
    ops.updateParameter(238,0.1)
if pid == 7:
    ops.parameter(239, 'element', 330,'hPerm')
    ops.parameter(240, 'element', 330,'vPerm')
    ops.updateParameter(239,0.1)
    ops.updateParameter(240,0.1)
if pid == 7:
    ops.parameter(241, 'element', 331,'hPerm')
    ops.parameter(242, 'element', 331,'vPerm')
    ops.updateParameter(241,0.1)
    ops.updateParameter(242,0.1)
if pid == 7:
    ops.parameter(243, 'element', 332,'hPerm')
    ops.parameter(244, 'element', 332,'vPerm')
    ops.updateParameter(243,0.1)
    ops.updateParameter(244,0.1)
if pid == 7:
    ops.parameter(245, 'element', 333,'hPerm')
    ops.parameter(246, 'element', 333,'vPerm')
    ops.updateParameter(245,0.1)
    ops.updateParameter(246,0.1)
if pid == 7:
    ops.parameter(247, 'element', 334,'hPerm')
    ops.parameter(248, 'element', 334,'vPerm')
    ops.updateParameter(247,0.1)
    ops.updateParameter(248,0.1)
if pid == 7:
    ops.parameter(249, 'element', 335,'hPerm')
    ops.parameter(250, 'element', 335,'vPerm')
    ops.updateParameter(249,0.1)
    ops.updateParameter(250,0.1)
ops.reactions()
ops.timeSeries('Constant',1)
ops.pattern('Plain',1,1,'-fact',1.0)
if pid == 1:
    ops.load(1, 0.2832492130898981,7.341539243350084,-31.76699263733651,0.0)
    ops.remove('sp',1,1)
    ops.remove('sp',1,2)
    ops.remove('sp',1,3)
if pid == 0:
    ops.load(1, 0.2832492130898981,7.341539243350084,-31.76699263733651,0.0)
    ops.remove("sp",1,1)
    ops.remove("sp",1,2)
    ops.remove("sp",1,3)
if pid == 6:
    ops.load(2, 100.79827646802579,146.86734409214736,202.28794150768752,0.0)
    ops.remove('sp',2,1)
    ops.remove('sp',2,2)
    ops.remove('sp',2,3)
if pid == 0:
    ops.load(2, 100.79827646802579,146.86734409214736,202.28794150768752,0.0)
    ops.remove("sp",2,1)
    ops.remove("sp",2,2)
    ops.remove("sp",2,3)
if pid == 2:
    ops.load(3, 3.7759764422278526,-10.694613139748698,-32.61624676527381,0.0)
    ops.remove('sp',3,1)
    ops.remove('sp',3,2)
    ops.remove('sp',3,3)
if pid == 0:
    ops.load(3, 3.7759764422278526,-10.694613139748698,-32.61624676527381,0.0)
    ops.remove("sp",3,1)
    ops.remove("sp",3,2)
    ops.remove("sp",3,3)
if pid == 7:
    ops.load(4, 22.131988323902608,-149.0886864178346,26.593405397168805,0.0)
    ops.remove('sp',4,1)
    ops.remove('sp',4,2)
    ops.remove('sp',4,3)
if pid == 0:
    ops.load(4, 22.131988323902608,-149.0886864178346,26.593405397168805,0.0)
    ops.remove("sp",4,1)
    ops.remove("sp",4,2)
    ops.remove("sp",4,3)
if pid == 1:
    ops.load(5, -0.011356717292737297,0.010678728402159303,-35.85799333215676,0.0)
    ops.remove('sp',5,1)
    ops.remove('sp',5,2)
    ops.remove('sp',5,3)
if pid == 0:
    ops.load(5, -0.011356717292737297,0.010678728402159303,-35.85799333215676,0.0)
    ops.remove("sp",5,1)
    ops.remove("sp",5,2)
    ops.remove("sp",5,3)
if pid == 6:
    ops.load(6, 1.6954369880928077,17.47110506476242,-64.21395496442213,0.0)
    ops.remove('sp',6,1)
    ops.remove('sp',6,2)
    ops.remove('sp',6,3)
if pid == 0:
    ops.load(6, 1.6954369880928077,17.47110506476242,-64.21395496442213,0.0)
    ops.remove("sp",6,1)
    ops.remove("sp",6,2)
    ops.remove("sp",6,3)
if pid == 2:
    ops.load(7, 0.038067799223255566,-0.0561123617359604,-35.49383987051327,0.0)
    ops.remove('sp',7,1)
    ops.remove('sp',7,2)
    ops.remove('sp',7,3)
if pid == 0:
    ops.load(7, 0.038067799223255566,-0.0561123617359604,-35.49383987051327,0.0)
    ops.remove("sp",7,1)
    ops.remove("sp",7,2)
    ops.remove("sp",7,3)
if pid == 7:
    ops.load(8, 15.60064238782315,32.39930525518136,-80.45459257005359,0.0)
    ops.remove('sp',8,1)
    ops.remove('sp',8,2)
    ops.remove('sp',8,3)
if pid == 0:
    ops.load(8, 15.60064238782315,32.39930525518136,-80.45459257005359,0.0)
    ops.remove("sp",8,1)
    ops.remove("sp",8,2)
    ops.remove("sp",8,3)
if pid == 5:
    ops.load(9, 59.235813623651445,175.6733105270079,42.190072504567965,0.0)
    ops.remove('sp',9,1)
    ops.remove('sp',9,2)
    ops.remove('sp',9,3)
if pid == 0:
    ops.load(9, 59.235813623651445,175.6733105270079,42.190072504567965,0.0)
    ops.remove("sp",9,1)
    ops.remove("sp",9,2)
    ops.remove("sp",9,3)
if pid == 6:
    ops.load(9, 59.235813623651445,175.6733105270079,42.190072504567965,0.0)
    ops.remove('sp',9,1)
    ops.remove('sp',9,2)
    ops.remove('sp',9,3)
if pid == 0:
    ops.load(9, 59.235813623651445,175.6733105270079,42.190072504567965,0.0)
    ops.remove("sp",9,1)
    ops.remove("sp",9,2)
    ops.remove("sp",9,3)
if pid == 3:
    ops.load(10, 25.724537059749387,119.30548603936,-39.06790614480522,0.0)
    ops.remove('sp',10,1)
    ops.remove('sp',10,2)
    ops.remove('sp',10,3)
if pid == 0:
    ops.load(10, 25.724537059749387,119.30548603936,-39.06790614480522,0.0)
    ops.remove("sp",10,1)
    ops.remove("sp",10,2)
    ops.remove("sp",10,3)
if pid == 5:
    ops.load(10, 25.724537059749387,119.30548603936,-39.06790614480522,0.0)
    ops.remove('sp',10,1)
    ops.remove('sp',10,2)
    ops.remove('sp',10,3)
if pid == 0:
    ops.load(10, 25.724537059749387,119.30548603936,-39.06790614480522,0.0)
    ops.remove("sp",10,1)
    ops.remove("sp",10,2)
    ops.remove("sp",10,3)
if pid == 2:
    ops.load(11, 26.128781817410918,98.1424649066694,-56.43635725624311,0.0)
    ops.remove('sp',11,1)
    ops.remove('sp',11,2)
    ops.remove('sp',11,3)
if pid == 0:
    ops.load(11, 26.128781817410918,98.1424649066694,-56.43635725624311,0.0)
    ops.remove("sp",11,1)
    ops.remove("sp",11,2)
    ops.remove("sp",11,3)
if pid == 3:
    ops.load(11, 26.128781817410918,98.1424649066694,-56.43635725624311,0.0)
    ops.remove('sp',11,1)
    ops.remove('sp',11,2)
    ops.remove('sp',11,3)
if pid == 0:
    ops.load(11, 26.128781817410918,98.1424649066694,-56.43635725624311,0.0)
    ops.remove("sp",11,1)
    ops.remove("sp",11,2)
    ops.remove("sp",11,3)
if pid == 1:
    ops.load(12, 15.026785482646343,53.13414954407972,-60.015280904341765,0.0)
    ops.remove('sp',12,1)
    ops.remove('sp',12,2)
    ops.remove('sp',12,3)
if pid == 0:
    ops.load(12, 15.026785482646343,53.13414954407972,-60.015280904341765,0.0)
    ops.remove("sp",12,1)
    ops.remove("sp",12,2)
    ops.remove("sp",12,3)
if pid == 2:
    ops.load(12, 15.026785482646343,53.13414954407972,-60.015280904341765,0.0)
    ops.remove('sp',12,1)
    ops.remove('sp',12,2)
    ops.remove('sp',12,3)
if pid == 0:
    ops.load(12, 15.026785482646343,53.13414954407972,-60.015280904341765,0.0)
    ops.remove("sp",12,1)
    ops.remove("sp",12,2)
    ops.remove("sp",12,3)
if pid == 1:
    ops.load(13, 6.9519733483019674,2.2075532285805988,-72.44743799506719,0.0)
    ops.remove('sp',13,1)
    ops.remove('sp',13,2)
    ops.remove('sp',13,3)
if pid == 0:
    ops.load(13, 6.9519733483019674,2.2075532285805988,-72.44743799506719,0.0)
    ops.remove("sp",13,1)
    ops.remove("sp",13,2)
    ops.remove("sp",13,3)
if pid == 1:
    ops.load(14, -3.4141649107715972,-0.011185429377524758,-75.6852796454905,0.0)
    ops.remove('sp',14,1)
    ops.remove('sp',14,2)
    ops.remove('sp',14,3)
if pid == 0:
    ops.load(14, -3.4141649107715972,-0.011185429377524758,-75.6852796454905,0.0)
    ops.remove("sp",14,1)
    ops.remove("sp",14,2)
    ops.remove("sp",14,3)
if pid == 1:
    ops.load(15, -2.8631352057547246,-0.4525136967675445,-76.09074352541336,0.0)
    ops.remove('sp',15,1)
    ops.remove('sp',15,2)
    ops.remove('sp',15,3)
if pid == 0:
    ops.load(15, -2.8631352057547246,-0.4525136967675445,-76.09074352541336,0.0)
    ops.remove("sp",15,1)
    ops.remove("sp",15,2)
    ops.remove("sp",15,3)
if pid == 1:
    ops.load(16, 6.49420727817548,-2.5438000772920306,-72.32378059908248,0.0)
    ops.remove('sp',16,1)
    ops.remove('sp',16,2)
    ops.remove('sp',16,3)
if pid == 0:
    ops.load(16, 6.49420727817548,-2.5438000772920306,-72.32378059908248,0.0)
    ops.remove("sp",16,1)
    ops.remove("sp",16,2)
    ops.remove("sp",16,3)
if pid == 2:
    ops.load(16, 6.49420727817548,-2.5438000772920306,-72.32378059908248,0.0)
    ops.remove('sp',16,1)
    ops.remove('sp',16,2)
    ops.remove('sp',16,3)
if pid == 0:
    ops.load(16, 6.49420727817548,-2.5438000772920306,-72.32378059908248,0.0)
    ops.remove("sp",16,1)
    ops.remove("sp",16,2)
    ops.remove("sp",16,3)
if pid == 6:
    ops.load(17, 46.81992828698587,-201.2234834867894,-37.00276604898287,0.0)
    ops.remove('sp',17,1)
    ops.remove('sp',17,2)
    ops.remove('sp',17,3)
if pid == 0:
    ops.load(17, 46.81992828698587,-201.2234834867894,-37.00276604898287,0.0)
    ops.remove("sp",17,1)
    ops.remove("sp",17,2)
    ops.remove("sp",17,3)
if pid == 7:
    ops.load(17, 46.81992828698587,-201.2234834867894,-37.00276604898287,0.0)
    ops.remove('sp',17,1)
    ops.remove('sp',17,2)
    ops.remove('sp',17,3)
if pid == 0:
    ops.load(17, 46.81992828698587,-201.2234834867894,-37.00276604898287,0.0)
    ops.remove("sp",17,1)
    ops.remove("sp",17,2)
    ops.remove("sp",17,3)
if pid == 4:
    ops.load(18, 40.11010005355999,-142.2750987988618,-48.640934206766204,0.0)
    ops.remove('sp',18,1)
    ops.remove('sp',18,2)
    ops.remove('sp',18,3)
if pid == 0:
    ops.load(18, 40.11010005355999,-142.2750987988618,-48.640934206766204,0.0)
    ops.remove("sp",18,1)
    ops.remove("sp",18,2)
    ops.remove("sp",18,3)
if pid == 6:
    ops.load(18, 40.11010005355999,-142.2750987988618,-48.640934206766204,0.0)
    ops.remove('sp',18,1)
    ops.remove('sp',18,2)
    ops.remove('sp',18,3)
if pid == 0:
    ops.load(18, 40.11010005355999,-142.2750987988618,-48.640934206766204,0.0)
    ops.remove("sp",18,1)
    ops.remove("sp",18,2)
    ops.remove("sp",18,3)
if pid == 3:
    ops.load(19, 28.338271508507145,-105.12740232139329,-56.247189530331084,0.0)
    ops.remove('sp',19,1)
    ops.remove('sp',19,2)
    ops.remove('sp',19,3)
if pid == 0:
    ops.load(19, 28.338271508507145,-105.12740232139329,-56.247189530331084,0.0)
    ops.remove("sp",19,1)
    ops.remove("sp",19,2)
    ops.remove("sp",19,3)
if pid == 4:
    ops.load(19, 28.338271508507145,-105.12740232139329,-56.247189530331084,0.0)
    ops.remove('sp',19,1)
    ops.remove('sp',19,2)
    ops.remove('sp',19,3)
if pid == 0:
    ops.load(19, 28.338271508507145,-105.12740232139329,-56.247189530331084,0.0)
    ops.remove("sp",19,1)
    ops.remove("sp",19,2)
    ops.remove("sp",19,3)
if pid == 2:
    ops.load(20, 12.258577976098778,-54.65810195047705,-61.72871667673337,0.0)
    ops.remove('sp',20,1)
    ops.remove('sp',20,2)
    ops.remove('sp',20,3)
if pid == 0:
    ops.load(20, 12.258577976098778,-54.65810195047705,-61.72871667673337,0.0)
    ops.remove("sp",20,1)
    ops.remove("sp",20,2)
    ops.remove("sp",20,3)
if pid == 3:
    ops.load(20, 12.258577976098778,-54.65810195047705,-61.72871667673337,0.0)
    ops.remove('sp',20,1)
    ops.remove('sp',20,2)
    ops.remove('sp',20,3)
if pid == 0:
    ops.load(20, 12.258577976098778,-54.65810195047705,-61.72871667673337,0.0)
    ops.remove("sp",20,1)
    ops.remove("sp",20,2)
    ops.remove("sp",20,3)
if pid == 6:
    ops.load(21, 148.1047477997979,41.61320690231041,287.5451338534407,0.0)
    ops.remove('sp',21,1)
    ops.remove('sp',21,2)
    ops.remove('sp',21,3)
if pid == 0:
    ops.load(21, 148.1047477997979,41.61320690231041,287.5451338534407,0.0)
    ops.remove("sp",21,1)
    ops.remove("sp",21,2)
    ops.remove("sp",21,3)
if pid == 6:
    ops.load(22, 55.40112378436793,-11.347056162200753,98.99750112216998,0.0)
    ops.remove('sp',22,1)
    ops.remove('sp',22,2)
    ops.remove('sp',22,3)
if pid == 0:
    ops.load(22, 55.40112378436793,-11.347056162200753,98.99750112216998,0.0)
    ops.remove("sp",22,1)
    ops.remove("sp",22,2)
    ops.remove("sp",22,3)
if pid == 7:
    ops.load(22, 55.40112378436793,-11.347056162200753,98.99750112216998,0.0)
    ops.remove('sp',22,1)
    ops.remove('sp',22,2)
    ops.remove('sp',22,3)
if pid == 0:
    ops.load(22, 55.40112378436793,-11.347056162200753,98.99750112216998,0.0)
    ops.remove("sp",22,1)
    ops.remove("sp",22,2)
    ops.remove("sp",22,3)
if pid == 7:
    ops.load(23, -22.018882536731276,6.290518330726173,-86.03274604825245,0.0)
    ops.remove('sp',23,1)
    ops.remove('sp',23,2)
    ops.remove('sp',23,3)
if pid == 0:
    ops.load(23, -22.018882536731276,6.290518330726173,-86.03274604825245,0.0)
    ops.remove("sp",23,1)
    ops.remove("sp",23,2)
    ops.remove("sp",23,3)
if pid == 7:
    ops.load(24, -19.04939206463377,-67.79045396719803,-83.62234245171948,0.0)
    ops.remove('sp',24,1)
    ops.remove('sp',24,2)
    ops.remove('sp',24,3)
if pid == 0:
    ops.load(24, -19.04939206463377,-67.79045396719803,-83.62234245171948,0.0)
    ops.remove("sp",24,1)
    ops.remove("sp",24,2)
    ops.remove("sp",24,3)
if pid == 5:
    ops.load(25, -9.794367073800085,8.724385100574997,-93.65213102137827,0.0)
    ops.remove('sp',25,1)
    ops.remove('sp',25,2)
    ops.remove('sp',25,3)
if pid == 0:
    ops.load(25, -9.794367073800085,8.724385100574997,-93.65213102137827,0.0)
    ops.remove("sp",25,1)
    ops.remove("sp",25,2)
    ops.remove("sp",25,3)
if pid == 6:
    ops.load(25, -9.794367073800085,8.724385100574997,-93.65213102137827,0.0)
    ops.remove('sp',25,1)
    ops.remove('sp',25,2)
    ops.remove('sp',25,3)
if pid == 0:
    ops.load(25, -9.794367073800085,8.724385100574997,-93.65213102137827,0.0)
    ops.remove("sp",25,1)
    ops.remove("sp",25,2)
    ops.remove("sp",25,3)
if pid == 4:
    ops.load(26, -13.06615600779622,19.78765738325911,-14.381404366248663,0.0)
    ops.remove('sp',26,1)
    ops.remove('sp',26,2)
    ops.remove('sp',26,3)
if pid == 0:
    ops.load(26, -13.06615600779622,19.78765738325911,-14.381404366248663,0.0)
    ops.remove("sp",26,1)
    ops.remove("sp",26,2)
    ops.remove("sp",26,3)
if pid == 5:
    ops.load(26, -13.06615600779622,19.78765738325911,-14.381404366248663,0.0)
    ops.remove('sp',26,1)
    ops.remove('sp',26,2)
    ops.remove('sp',26,3)
if pid == 0:
    ops.load(26, -13.06615600779622,19.78765738325911,-14.381404366248663,0.0)
    ops.remove("sp",26,1)
    ops.remove("sp",26,2)
    ops.remove("sp",26,3)
if pid == 2:
    ops.load(27, -3.371998073836661,5.05472212768186,-27.35648695435298,0.0)
    ops.remove('sp',27,1)
    ops.remove('sp',27,2)
    ops.remove('sp',27,3)
if pid == 0:
    ops.load(27, -3.371998073836661,5.05472212768186,-27.35648695435298,0.0)
    ops.remove("sp",27,1)
    ops.remove("sp",27,2)
    ops.remove("sp",27,3)
if pid == 4:
    ops.load(27, -3.371998073836661,5.05472212768186,-27.35648695435298,0.0)
    ops.remove('sp',27,1)
    ops.remove('sp',27,2)
    ops.remove('sp',27,3)
if pid == 0:
    ops.load(27, -3.371998073836661,5.05472212768186,-27.35648695435298,0.0)
    ops.remove("sp",27,1)
    ops.remove("sp",27,2)
    ops.remove("sp",27,3)
if pid == 1:
    ops.load(28, -1.1722101254563875,-1.049620934730482,-53.953990206322324,0.0)
    ops.remove('sp',28,1)
    ops.remove('sp',28,2)
    ops.remove('sp',28,3)
if pid == 0:
    ops.load(28, -1.1722101254563875,-1.049620934730482,-53.953990206322324,0.0)
    ops.remove("sp",28,1)
    ops.remove("sp",28,2)
    ops.remove("sp",28,3)
if pid == 2:
    ops.load(28, -1.1722101254563875,-1.049620934730482,-53.953990206322324,0.0)
    ops.remove('sp',28,1)
    ops.remove('sp',28,2)
    ops.remove('sp',28,3)
if pid == 0:
    ops.load(28, -1.1722101254563875,-1.049620934730482,-53.953990206322324,0.0)
    ops.remove("sp",28,1)
    ops.remove("sp",28,2)
    ops.remove("sp",28,3)
if pid == 1:
    ops.load(29, -0.06901609337740702,-0.0024363362003722126,-71.88411306507766,0.0)
    ops.remove('sp',29,1)
    ops.remove('sp',29,2)
    ops.remove('sp',29,3)
if pid == 0:
    ops.load(29, -0.06901609337740702,-0.0024363362003722126,-71.88411306507766,0.0)
    ops.remove("sp",29,1)
    ops.remove("sp",29,2)
    ops.remove("sp",29,3)
if pid == 1:
    ops.load(30, -0.07400833825483169,-0.0026142438634007004,-71.91813336682779,0.0)
    ops.remove('sp',30,1)
    ops.remove('sp',30,2)
    ops.remove('sp',30,3)
if pid == 0:
    ops.load(30, -0.07400833825483169,-0.0026142438634007004,-71.91813336682779,0.0)
    ops.remove("sp",30,1)
    ops.remove("sp",30,2)
    ops.remove("sp",30,3)
if pid == 1:
    ops.load(31, -0.07796952947985875,-0.003517166187228561,-71.92016307849923,0.0)
    ops.remove('sp',31,1)
    ops.remove('sp',31,2)
    ops.remove('sp',31,3)
if pid == 0:
    ops.load(31, -0.07796952947985875,-0.003517166187228561,-71.92016307849923,0.0)
    ops.remove("sp",31,1)
    ops.remove("sp",31,2)
    ops.remove("sp",31,3)
if pid == 2:
    ops.load(31, -0.07796952947985875,-0.003517166187228561,-71.92016307849923,0.0)
    ops.remove('sp',31,1)
    ops.remove('sp',31,2)
    ops.remove('sp',31,3)
if pid == 0:
    ops.load(31, -0.07796952947985875,-0.003517166187228561,-71.92016307849923,0.0)
    ops.remove("sp",31,1)
    ops.remove("sp",31,2)
    ops.remove("sp",31,3)
if pid == 2:
    ops.load(32, -0.025375174824664167,-0.10467622131136425,-71.51607620150115,0.0)
    ops.remove('sp',32,1)
    ops.remove('sp',32,2)
    ops.remove('sp',32,3)
if pid == 0:
    ops.load(32, -0.025375174824664167,-0.10467622131136425,-71.51607620150115,0.0)
    ops.remove("sp",32,1)
    ops.remove("sp",32,2)
    ops.remove("sp",32,3)
if pid == 6:
    ops.load(33, 2.437431755159791,24.07432306692629,-119.66688445143114,0.0)
    ops.remove('sp',33,1)
    ops.remove('sp',33,2)
    ops.remove('sp',33,3)
if pid == 0:
    ops.load(33, 2.437431755159791,24.07432306692629,-119.66688445143114,0.0)
    ops.remove("sp",33,1)
    ops.remove("sp",33,2)
    ops.remove("sp",33,3)
if pid == 7:
    ops.load(33, 2.437431755159791,24.07432306692629,-119.66688445143114,0.0)
    ops.remove('sp',33,1)
    ops.remove('sp',33,2)
    ops.remove('sp',33,3)
if pid == 0:
    ops.load(33, 2.437431755159791,24.07432306692629,-119.66688445143114,0.0)
    ops.remove("sp",33,1)
    ops.remove("sp",33,2)
    ops.remove("sp",33,3)
if pid == 5:
    ops.load(34, -5.476871660095497,15.554633806196032,-22.433966635606332,0.0)
    ops.remove('sp',34,1)
    ops.remove('sp',34,2)
    ops.remove('sp',34,3)
if pid == 0:
    ops.load(34, -5.476871660095497,15.554633806196032,-22.433966635606332,0.0)
    ops.remove("sp",34,1)
    ops.remove("sp",34,2)
    ops.remove("sp",34,3)
if pid == 6:
    ops.load(34, -5.476871660095497,15.554633806196032,-22.433966635606332,0.0)
    ops.remove('sp',34,1)
    ops.remove('sp',34,2)
    ops.remove('sp',34,3)
if pid == 0:
    ops.load(34, -5.476871660095497,15.554633806196032,-22.433966635606332,0.0)
    ops.remove("sp",34,1)
    ops.remove("sp",34,2)
    ops.remove("sp",34,3)
if pid == 3:
    ops.load(35, -1.706464663581597,5.594704057696119,-44.386610731100276,0.0)
    ops.remove('sp',35,1)
    ops.remove('sp',35,2)
    ops.remove('sp',35,3)
if pid == 0:
    ops.load(35, -1.706464663581597,5.594704057696119,-44.386610731100276,0.0)
    ops.remove("sp",35,1)
    ops.remove("sp",35,2)
    ops.remove("sp",35,3)
if pid == 5:
    ops.load(35, -1.706464663581597,5.594704057696119,-44.386610731100276,0.0)
    ops.remove('sp',35,1)
    ops.remove('sp',35,2)
    ops.remove('sp',35,3)
if pid == 0:
    ops.load(35, -1.706464663581597,5.594704057696119,-44.386610731100276,0.0)
    ops.remove("sp",35,1)
    ops.remove("sp",35,2)
    ops.remove("sp",35,3)
if pid == 2:
    ops.load(36, -0.050143897229149886,1.1778919370869663,-60.30895201540668,0.0)
    ops.remove('sp',36,1)
    ops.remove('sp',36,2)
    ops.remove('sp',36,3)
if pid == 0:
    ops.load(36, -0.050143897229149886,1.1778919370869663,-60.30895201540668,0.0)
    ops.remove("sp",36,1)
    ops.remove("sp",36,2)
    ops.remove("sp",36,3)
if pid == 3:
    ops.load(36, -0.050143897229149886,1.1778919370869663,-60.30895201540668,0.0)
    ops.remove('sp',36,1)
    ops.remove('sp',36,2)
    ops.remove('sp',36,3)
if pid == 0:
    ops.load(36, -0.050143897229149886,1.1778919370869663,-60.30895201540668,0.0)
    ops.remove("sp",36,1)
    ops.remove("sp",36,2)
    ops.remove("sp",36,3)
if pid == 6:
    ops.load(37, 17.412304540703985,0.8571745940558557,-94.70892407731122,0.0)
    ops.remove('sp',37,1)
    ops.remove('sp',37,2)
    ops.remove('sp',37,3)
if pid == 0:
    ops.load(37, 17.412304540703985,0.8571745940558557,-94.70892407731122,0.0)
    ops.remove("sp",37,1)
    ops.remove("sp",37,2)
    ops.remove("sp",37,3)
if pid == 7:
    ops.load(37, 17.412304540703985,0.8571745940558557,-94.70892407731122,0.0)
    ops.remove('sp',37,1)
    ops.remove('sp',37,2)
    ops.remove('sp',37,3)
if pid == 0:
    ops.load(37, 17.412304540703985,0.8571745940558557,-94.70892407731122,0.0)
    ops.remove("sp",37,1)
    ops.remove("sp",37,2)
    ops.remove("sp",37,3)
if pid == 7:
    ops.load(38, 27.79173239574935,-3.424284700703919,-73.92595736053705,0.0)
    ops.remove('sp',38,1)
    ops.remove('sp',38,2)
    ops.remove('sp',38,3)
if pid == 0:
    ops.load(38, 27.79173239574935,-3.424284700703919,-73.92595736053705,0.0)
    ops.remove("sp",38,1)
    ops.remove("sp",38,2)
    ops.remove("sp",38,3)
if pid == 7:
    ops.load(39, 27.215276600224847,-0.7645759992125392,-75.52243363508407,0.0)
    ops.remove('sp',39,1)
    ops.remove('sp',39,2)
    ops.remove('sp',39,3)
if pid == 0:
    ops.load(39, 27.215276600224847,-0.7645759992125392,-75.52243363508407,0.0)
    ops.remove("sp",39,1)
    ops.remove("sp",39,2)
    ops.remove("sp",39,3)
if pid == 7:
    ops.load(40, 20.943979947825305,12.023336934878355,-85.08849988766639,0.0)
    ops.remove('sp',40,1)
    ops.remove('sp',40,2)
    ops.remove('sp',40,3)
if pid == 0:
    ops.load(40, 20.943979947825305,12.023336934878355,-85.08849988766639,0.0)
    ops.remove("sp",40,1)
    ops.remove("sp",40,2)
    ops.remove("sp",40,3)
if pid == 5:
    ops.load(57, 86.81397210733034,65.11165734896237,98.98378607768908,0.0)
    ops.remove('sp',57,1)
    ops.remove('sp',57,2)
    ops.remove('sp',57,3)
if pid == 0:
    ops.load(57, 86.81397210733034,65.11165734896237,98.98378607768908,0.0)
    ops.remove("sp",57,1)
    ops.remove("sp",57,2)
    ops.remove("sp",57,3)
if pid == 6:
    ops.load(57, 86.81397210733034,65.11165734896237,98.98378607768908,0.0)
    ops.remove('sp',57,1)
    ops.remove('sp',57,2)
    ops.remove('sp',57,3)
if pid == 0:
    ops.load(57, 86.81397210733034,65.11165734896237,98.98378607768908,0.0)
    ops.remove("sp",57,1)
    ops.remove("sp",57,2)
    ops.remove("sp",57,3)
if pid == 5:
    ops.load(58, 22.000160340863502,24.85187289913386,-51.976593798326945,0.0)
    ops.remove('sp',58,1)
    ops.remove('sp',58,2)
    ops.remove('sp',58,3)
if pid == 0:
    ops.load(58, 22.000160340863502,24.85187289913386,-51.976593798326945,0.0)
    ops.remove("sp",58,1)
    ops.remove("sp",58,2)
    ops.remove("sp",58,3)
if pid == 6:
    ops.load(58, 22.000160340863502,24.85187289913386,-51.976593798326945,0.0)
    ops.remove('sp',58,1)
    ops.remove('sp',58,2)
    ops.remove('sp',58,3)
if pid == 0:
    ops.load(58, 22.000160340863502,24.85187289913386,-51.976593798326945,0.0)
    ops.remove("sp",58,1)
    ops.remove("sp",58,2)
    ops.remove("sp",58,3)
if pid == 7:
    ops.load(58, 22.000160340863502,24.85187289913386,-51.976593798326945,0.0)
    ops.remove('sp',58,1)
    ops.remove('sp',58,2)
    ops.remove('sp',58,3)
if pid == 0:
    ops.load(58, 22.000160340863502,24.85187289913386,-51.976593798326945,0.0)
    ops.remove("sp",58,1)
    ops.remove("sp",58,2)
    ops.remove("sp",58,3)
if pid == 5:
    ops.load(59, -19.96728514413165,0.3444592651696561,-156.6253990835707,0.0)
    ops.remove('sp',59,1)
    ops.remove('sp',59,2)
    ops.remove('sp',59,3)
if pid == 0:
    ops.load(59, -19.96728514413165,0.3444592651696561,-156.6253990835707,0.0)
    ops.remove("sp",59,1)
    ops.remove("sp",59,2)
    ops.remove("sp",59,3)
if pid == 6:
    ops.load(59, -19.96728514413165,0.3444592651696561,-156.6253990835707,0.0)
    ops.remove('sp',59,1)
    ops.remove('sp',59,2)
    ops.remove('sp',59,3)
if pid == 0:
    ops.load(59, -19.96728514413165,0.3444592651696561,-156.6253990835707,0.0)
    ops.remove("sp",59,1)
    ops.remove("sp",59,2)
    ops.remove("sp",59,3)
if pid == 7:
    ops.load(59, -19.96728514413165,0.3444592651696561,-156.6253990835707,0.0)
    ops.remove('sp',59,1)
    ops.remove('sp',59,2)
    ops.remove('sp',59,3)
if pid == 0:
    ops.load(59, -19.96728514413165,0.3444592651696561,-156.6253990835707,0.0)
    ops.remove("sp",59,1)
    ops.remove("sp",59,2)
    ops.remove("sp",59,3)
if pid == 6:
    ops.load(60, 7.3117818142452,-72.23108573280184,-98.05677491149606,0.0)
    ops.remove('sp',60,1)
    ops.remove('sp',60,2)
    ops.remove('sp',60,3)
if pid == 0:
    ops.load(60, 7.3117818142452,-72.23108573280184,-98.05677491149606,0.0)
    ops.remove("sp",60,1)
    ops.remove("sp",60,2)
    ops.remove("sp",60,3)
if pid == 7:
    ops.load(60, 7.3117818142452,-72.23108573280184,-98.05677491149606,0.0)
    ops.remove('sp',60,1)
    ops.remove('sp',60,2)
    ops.remove('sp',60,3)
if pid == 0:
    ops.load(60, 7.3117818142452,-72.23108573280184,-98.05677491149606,0.0)
    ops.remove("sp",60,1)
    ops.remove("sp",60,2)
    ops.remove("sp",60,3)
if pid == 3:
    ops.load(61, 18.03470022813712,64.97981448499402,-102.4023615477231,0.0)
    ops.remove('sp',61,1)
    ops.remove('sp',61,2)
    ops.remove('sp',61,3)
if pid == 0:
    ops.load(61, 18.03470022813712,64.97981448499402,-102.4023615477231,0.0)
    ops.remove("sp",61,1)
    ops.remove("sp",61,2)
    ops.remove("sp",61,3)
if pid == 4:
    ops.load(61, 18.03470022813712,64.97981448499402,-102.4023615477231,0.0)
    ops.remove('sp',61,1)
    ops.remove('sp',61,2)
    ops.remove('sp',61,3)
if pid == 0:
    ops.load(61, 18.03470022813712,64.97981448499402,-102.4023615477231,0.0)
    ops.remove("sp",61,1)
    ops.remove("sp",61,2)
    ops.remove("sp",61,3)
if pid == 5:
    ops.load(61, 18.03470022813712,64.97981448499402,-102.4023615477231,0.0)
    ops.remove('sp',61,1)
    ops.remove('sp',61,2)
    ops.remove('sp',61,3)
if pid == 0:
    ops.load(61, 18.03470022813712,64.97981448499402,-102.4023615477231,0.0)
    ops.remove("sp",61,1)
    ops.remove("sp",61,2)
    ops.remove("sp",61,3)
if pid == 4:
    ops.load(62, 1.054288175971718,2.8338640398186463,-138.36463137469343,0.0)
    ops.remove('sp',62,1)
    ops.remove('sp',62,2)
    ops.remove('sp',62,3)
if pid == 0:
    ops.load(62, 1.054288175971718,2.8338640398186463,-138.36463137469343,0.0)
    ops.remove("sp",62,1)
    ops.remove("sp",62,2)
    ops.remove("sp",62,3)
if pid == 5:
    ops.load(62, 1.054288175971718,2.8338640398186463,-138.36463137469343,0.0)
    ops.remove('sp',62,1)
    ops.remove('sp',62,2)
    ops.remove('sp',62,3)
if pid == 0:
    ops.load(62, 1.054288175971718,2.8338640398186463,-138.36463137469343,0.0)
    ops.remove("sp",62,1)
    ops.remove("sp",62,2)
    ops.remove("sp",62,3)
if pid == 4:
    ops.load(63, 0.26099622315815135,-0.16222890480177374,-142.66096842713884,0.0)
    ops.remove('sp',63,1)
    ops.remove('sp',63,2)
    ops.remove('sp',63,3)
if pid == 0:
    ops.load(63, 0.26099622315815135,-0.16222890480177374,-142.66096842713884,0.0)
    ops.remove("sp",63,1)
    ops.remove("sp",63,2)
    ops.remove("sp",63,3)
if pid == 5:
    ops.load(63, 0.26099622315815135,-0.16222890480177374,-142.66096842713884,0.0)
    ops.remove('sp',63,1)
    ops.remove('sp',63,2)
    ops.remove('sp',63,3)
if pid == 0:
    ops.load(63, 0.26099622315815135,-0.16222890480177374,-142.66096842713884,0.0)
    ops.remove("sp",63,1)
    ops.remove("sp",63,2)
    ops.remove("sp",63,3)
if pid == 6:
    ops.load(63, 0.26099622315815135,-0.16222890480177374,-142.66096842713884,0.0)
    ops.remove('sp',63,1)
    ops.remove('sp',63,2)
    ops.remove('sp',63,3)
if pid == 0:
    ops.load(63, 0.26099622315815135,-0.16222890480177374,-142.66096842713884,0.0)
    ops.remove("sp",63,1)
    ops.remove("sp",63,2)
    ops.remove("sp",63,3)
if pid == 4:
    ops.load(64, 19.87920720464973,-73.86159239846643,-119.6708857340848,0.0)
    ops.remove('sp',64,1)
    ops.remove('sp',64,2)
    ops.remove('sp',64,3)
if pid == 0:
    ops.load(64, 19.87920720464973,-73.86159239846643,-119.6708857340848,0.0)
    ops.remove("sp",64,1)
    ops.remove("sp",64,2)
    ops.remove("sp",64,3)
if pid == 6:
    ops.load(64, 19.87920720464973,-73.86159239846643,-119.6708857340848,0.0)
    ops.remove('sp',64,1)
    ops.remove('sp',64,2)
    ops.remove('sp',64,3)
if pid == 0:
    ops.load(64, 19.87920720464973,-73.86159239846643,-119.6708857340848,0.0)
    ops.remove("sp",64,1)
    ops.remove("sp",64,2)
    ops.remove("sp",64,3)
if pid == 2:
    ops.load(65, 12.45273488843937,48.977287440636275,-127.3735409116507,0.0)
    ops.remove('sp',65,1)
    ops.remove('sp',65,2)
    ops.remove('sp',65,3)
if pid == 0:
    ops.load(65, 12.45273488843937,48.977287440636275,-127.3735409116507,0.0)
    ops.remove("sp",65,1)
    ops.remove("sp",65,2)
    ops.remove("sp",65,3)
if pid == 3:
    ops.load(65, 12.45273488843937,48.977287440636275,-127.3735409116507,0.0)
    ops.remove('sp',65,1)
    ops.remove('sp',65,2)
    ops.remove('sp',65,3)
if pid == 0:
    ops.load(65, 12.45273488843937,48.977287440636275,-127.3735409116507,0.0)
    ops.remove("sp",65,1)
    ops.remove("sp",65,2)
    ops.remove("sp",65,3)
if pid == 4:
    ops.load(65, 12.45273488843937,48.977287440636275,-127.3735409116507,0.0)
    ops.remove('sp',65,1)
    ops.remove('sp',65,2)
    ops.remove('sp',65,3)
if pid == 0:
    ops.load(65, 12.45273488843937,48.977287440636275,-127.3735409116507,0.0)
    ops.remove("sp",65,1)
    ops.remove("sp",65,2)
    ops.remove("sp",65,3)
if pid == 2:
    ops.load(66, 0.11055955779892847,0.4208743135268225,-143.75516369871121,0.0)
    ops.remove('sp',66,1)
    ops.remove('sp',66,2)
    ops.remove('sp',66,3)
if pid == 0:
    ops.load(66, 0.11055955779892847,0.4208743135268225,-143.75516369871121,0.0)
    ops.remove("sp",66,1)
    ops.remove("sp",66,2)
    ops.remove("sp",66,3)
if pid == 4:
    ops.load(66, 0.11055955779892847,0.4208743135268225,-143.75516369871121,0.0)
    ops.remove('sp',66,1)
    ops.remove('sp',66,2)
    ops.remove('sp',66,3)
if pid == 0:
    ops.load(66, 0.11055955779892847,0.4208743135268225,-143.75516369871121,0.0)
    ops.remove("sp",66,1)
    ops.remove("sp",66,2)
    ops.remove("sp",66,3)
if pid == 2:
    ops.load(67, 0.12780797697378482,-0.4956187718685861,-143.64145867827693,0.0)
    ops.remove('sp',67,1)
    ops.remove('sp',67,2)
    ops.remove('sp',67,3)
if pid == 0:
    ops.load(67, 0.12780797697378482,-0.4956187718685861,-143.64145867827693,0.0)
    ops.remove("sp",67,1)
    ops.remove("sp",67,2)
    ops.remove("sp",67,3)
if pid == 3:
    ops.load(67, 0.12780797697378482,-0.4956187718685861,-143.64145867827693,0.0)
    ops.remove('sp',67,1)
    ops.remove('sp',67,2)
    ops.remove('sp',67,3)
if pid == 0:
    ops.load(67, 0.12780797697378482,-0.4956187718685861,-143.64145867827693,0.0)
    ops.remove("sp",67,1)
    ops.remove("sp",67,2)
    ops.remove("sp",67,3)
if pid == 4:
    ops.load(67, 0.12780797697378482,-0.4956187718685861,-143.64145867827693,0.0)
    ops.remove('sp',67,1)
    ops.remove('sp',67,2)
    ops.remove('sp',67,3)
if pid == 0:
    ops.load(67, 0.12780797697378482,-0.4956187718685861,-143.64145867827693,0.0)
    ops.remove("sp",67,1)
    ops.remove("sp",67,2)
    ops.remove("sp",67,3)
if pid == 3:
    ops.load(68, 14.516804089538834,-51.55931154861456,-126.2713501619326,0.0)
    ops.remove('sp',68,1)
    ops.remove('sp',68,2)
    ops.remove('sp',68,3)
if pid == 0:
    ops.load(68, 14.516804089538834,-51.55931154861456,-126.2713501619326,0.0)
    ops.remove("sp",68,1)
    ops.remove("sp",68,2)
    ops.remove("sp",68,3)
if pid == 4:
    ops.load(68, 14.516804089538834,-51.55931154861456,-126.2713501619326,0.0)
    ops.remove('sp',68,1)
    ops.remove('sp',68,2)
    ops.remove('sp',68,3)
if pid == 0:
    ops.load(68, 14.516804089538834,-51.55931154861456,-126.2713501619326,0.0)
    ops.remove("sp",68,1)
    ops.remove("sp",68,2)
    ops.remove("sp",68,3)
if pid == 1:
    ops.load(69, 8.770595525424026,26.548110758650864,-139.02991514567026,0.0)
    ops.remove('sp',69,1)
    ops.remove('sp',69,2)
    ops.remove('sp',69,3)
if pid == 0:
    ops.load(69, 8.770595525424026,26.548110758650864,-139.02991514567026,0.0)
    ops.remove("sp",69,1)
    ops.remove("sp",69,2)
    ops.remove("sp",69,3)
if pid == 2:
    ops.load(69, 8.770595525424026,26.548110758650864,-139.02991514567026,0.0)
    ops.remove('sp',69,1)
    ops.remove('sp',69,2)
    ops.remove('sp',69,3)
if pid == 0:
    ops.load(69, 8.770595525424026,26.548110758650864,-139.02991514567026,0.0)
    ops.remove("sp",69,1)
    ops.remove("sp",69,2)
    ops.remove("sp",69,3)
if pid == 1:
    ops.load(70, 0.9776379147916631,-0.7456404885779452,-155.5951440925798,0.0)
    ops.remove('sp',70,1)
    ops.remove('sp',70,2)
    ops.remove('sp',70,3)
if pid == 0:
    ops.load(70, 0.9776379147916631,-0.7456404885779452,-155.5951440925798,0.0)
    ops.remove("sp",70,1)
    ops.remove("sp",70,2)
    ops.remove("sp",70,3)
if pid == 2:
    ops.load(70, 0.9776379147916631,-0.7456404885779452,-155.5951440925798,0.0)
    ops.remove('sp',70,1)
    ops.remove('sp',70,2)
    ops.remove('sp',70,3)
if pid == 0:
    ops.load(70, 0.9776379147916631,-0.7456404885779452,-155.5951440925798,0.0)
    ops.remove("sp",70,1)
    ops.remove("sp",70,2)
    ops.remove("sp",70,3)
if pid == 1:
    ops.load(71, 1.0203836235432577,0.2980147283401705,-155.82978165888878,0.0)
    ops.remove('sp',71,1)
    ops.remove('sp',71,2)
    ops.remove('sp',71,3)
if pid == 0:
    ops.load(71, 1.0203836235432577,0.2980147283401705,-155.82978165888878,0.0)
    ops.remove("sp",71,1)
    ops.remove("sp",71,2)
    ops.remove("sp",71,3)
if pid == 2:
    ops.load(71, 1.0203836235432577,0.2980147283401705,-155.82978165888878,0.0)
    ops.remove('sp',71,1)
    ops.remove('sp',71,2)
    ops.remove('sp',71,3)
if pid == 0:
    ops.load(71, 1.0203836235432577,0.2980147283401705,-155.82978165888878,0.0)
    ops.remove("sp",71,1)
    ops.remove("sp",71,2)
    ops.remove("sp",71,3)
if pid == 3:
    ops.load(71, 1.0203836235432577,0.2980147283401705,-155.82978165888878,0.0)
    ops.remove('sp',71,1)
    ops.remove('sp',71,2)
    ops.remove('sp',71,3)
if pid == 0:
    ops.load(71, 1.0203836235432577,0.2980147283401705,-155.82978165888878,0.0)
    ops.remove("sp",71,1)
    ops.remove("sp",71,2)
    ops.remove("sp",71,3)
if pid == 1:
    ops.load(72, 8.99062136051338,-28.74127660322496,-138.08225777139268,0.0)
    ops.remove('sp',72,1)
    ops.remove('sp',72,2)
    ops.remove('sp',72,3)
if pid == 0:
    ops.load(72, 8.99062136051338,-28.74127660322496,-138.08225777139268,0.0)
    ops.remove("sp",72,1)
    ops.remove("sp",72,2)
    ops.remove("sp",72,3)
if pid == 2:
    ops.load(72, 8.99062136051338,-28.74127660322496,-138.08225777139268,0.0)
    ops.remove('sp',72,1)
    ops.remove('sp',72,2)
    ops.remove('sp',72,3)
if pid == 0:
    ops.load(72, 8.99062136051338,-28.74127660322496,-138.08225777139268,0.0)
    ops.remove("sp",72,1)
    ops.remove("sp",72,2)
    ops.remove("sp",72,3)
if pid == 3:
    ops.load(72, 8.99062136051338,-28.74127660322496,-138.08225777139268,0.0)
    ops.remove('sp',72,1)
    ops.remove('sp',72,2)
    ops.remove('sp',72,3)
if pid == 0:
    ops.load(72, 8.99062136051338,-28.74127660322496,-138.08225777139268,0.0)
    ops.remove("sp",72,1)
    ops.remove("sp",72,2)
    ops.remove("sp",72,3)
if pid == 1:
    ops.load(73, -0.6752301746037328,0.3747353329961798,-117.8857849014135,0.0)
    ops.remove('sp',73,1)
    ops.remove('sp',73,2)
    ops.remove('sp',73,3)
if pid == 0:
    ops.load(73, -0.6752301746037328,0.3747353329961798,-117.8857849014135,0.0)
    ops.remove("sp",73,1)
    ops.remove("sp",73,2)
    ops.remove("sp",73,3)
if pid == 2:
    ops.load(73, -0.6752301746037328,0.3747353329961798,-117.8857849014135,0.0)
    ops.remove('sp',73,1)
    ops.remove('sp',73,2)
    ops.remove('sp',73,3)
if pid == 0:
    ops.load(73, -0.6752301746037328,0.3747353329961798,-117.8857849014135,0.0)
    ops.remove("sp",73,1)
    ops.remove("sp",73,2)
    ops.remove("sp",73,3)
if pid == 1:
    ops.load(74, 0.6003408032158313,0.8588369407043039,-123.88353555725516,0.0)
    ops.remove('sp',74,1)
    ops.remove('sp',74,2)
    ops.remove('sp',74,3)
if pid == 0:
    ops.load(74, 0.6003408032158313,0.8588369407043039,-123.88353555725516,0.0)
    ops.remove("sp",74,1)
    ops.remove("sp",74,2)
    ops.remove("sp",74,3)
if pid == 2:
    ops.load(74, 0.6003408032158313,0.8588369407043039,-123.88353555725516,0.0)
    ops.remove('sp',74,1)
    ops.remove('sp',74,2)
    ops.remove('sp',74,3)
if pid == 0:
    ops.load(74, 0.6003408032158313,0.8588369407043039,-123.88353555725516,0.0)
    ops.remove("sp",74,1)
    ops.remove("sp",74,2)
    ops.remove("sp",74,3)
if pid == 3:
    ops.load(74, 0.6003408032158313,0.8588369407043039,-123.88353555725516,0.0)
    ops.remove('sp',74,1)
    ops.remove('sp',74,2)
    ops.remove('sp',74,3)
if pid == 0:
    ops.load(74, 0.6003408032158313,0.8588369407043039,-123.88353555725516,0.0)
    ops.remove("sp",74,1)
    ops.remove("sp",74,2)
    ops.remove("sp",74,3)
if pid == 1:
    ops.load(75, 0.506911547608581,0.05794220281732887,-123.16594037874586,0.0)
    ops.remove('sp',75,1)
    ops.remove('sp',75,2)
    ops.remove('sp',75,3)
if pid == 0:
    ops.load(75, 0.506911547608581,0.05794220281732887,-123.16594037874586,0.0)
    ops.remove("sp",75,1)
    ops.remove("sp",75,2)
    ops.remove("sp",75,3)
if pid == 2:
    ops.load(75, 0.506911547608581,0.05794220281732887,-123.16594037874586,0.0)
    ops.remove('sp',75,1)
    ops.remove('sp',75,2)
    ops.remove('sp',75,3)
if pid == 0:
    ops.load(75, 0.506911547608581,0.05794220281732887,-123.16594037874586,0.0)
    ops.remove("sp",75,1)
    ops.remove("sp",75,2)
    ops.remove("sp",75,3)
if pid == 3:
    ops.load(75, 0.506911547608581,0.05794220281732887,-123.16594037874586,0.0)
    ops.remove('sp',75,1)
    ops.remove('sp',75,2)
    ops.remove('sp',75,3)
if pid == 0:
    ops.load(75, 0.506911547608581,0.05794220281732887,-123.16594037874586,0.0)
    ops.remove("sp",75,1)
    ops.remove("sp",75,2)
    ops.remove("sp",75,3)
if pid == 2:
    ops.load(76, 0.035945598698279985,0.5898143801071007,-121.37783763942194,0.0)
    ops.remove('sp',76,1)
    ops.remove('sp',76,2)
    ops.remove('sp',76,3)
if pid == 0:
    ops.load(76, 0.035945598698279985,0.5898143801071007,-121.37783763942194,0.0)
    ops.remove("sp",76,1)
    ops.remove("sp",76,2)
    ops.remove("sp",76,3)
if pid == 3:
    ops.load(76, 0.035945598698279985,0.5898143801071007,-121.37783763942194,0.0)
    ops.remove('sp',76,1)
    ops.remove('sp',76,2)
    ops.remove('sp',76,3)
if pid == 0:
    ops.load(76, 0.035945598698279985,0.5898143801071007,-121.37783763942194,0.0)
    ops.remove("sp",76,1)
    ops.remove("sp",76,2)
    ops.remove("sp",76,3)
if pid == 2:
    ops.load(77, -4.3902032427569235,1.1713364197149856,-82.43532177645312,0.0)
    ops.remove('sp',77,1)
    ops.remove('sp',77,2)
    ops.remove('sp',77,3)
if pid == 0:
    ops.load(77, -4.3902032427569235,1.1713364197149856,-82.43532177645312,0.0)
    ops.remove("sp",77,1)
    ops.remove("sp",77,2)
    ops.remove("sp",77,3)
if pid == 4:
    ops.load(77, -4.3902032427569235,1.1713364197149856,-82.43532177645312,0.0)
    ops.remove('sp',77,1)
    ops.remove('sp',77,2)
    ops.remove('sp',77,3)
if pid == 0:
    ops.load(77, -4.3902032427569235,1.1713364197149856,-82.43532177645312,0.0)
    ops.remove("sp",77,1)
    ops.remove("sp",77,2)
    ops.remove("sp",77,3)
if pid == 2:
    ops.load(78, 2.9936545631134295,2.9634668413544007,-91.0886217886515,0.0)
    ops.remove('sp',78,1)
    ops.remove('sp',78,2)
    ops.remove('sp',78,3)
if pid == 0:
    ops.load(78, 2.9936545631134295,2.9634668413544007,-91.0886217886515,0.0)
    ops.remove("sp",78,1)
    ops.remove("sp",78,2)
    ops.remove("sp",78,3)
if pid == 3:
    ops.load(78, 2.9936545631134295,2.9634668413544007,-91.0886217886515,0.0)
    ops.remove('sp',78,1)
    ops.remove('sp',78,2)
    ops.remove('sp',78,3)
if pid == 0:
    ops.load(78, 2.9936545631134295,2.9634668413544007,-91.0886217886515,0.0)
    ops.remove("sp",78,1)
    ops.remove("sp",78,2)
    ops.remove("sp",78,3)
if pid == 4:
    ops.load(78, 2.9936545631134295,2.9634668413544007,-91.0886217886515,0.0)
    ops.remove('sp',78,1)
    ops.remove('sp',78,2)
    ops.remove('sp',78,3)
if pid == 0:
    ops.load(78, 2.9936545631134295,2.9634668413544007,-91.0886217886515,0.0)
    ops.remove("sp",78,1)
    ops.remove("sp",78,2)
    ops.remove("sp",78,3)
if pid == 3:
    ops.load(79, 2.334806068882362,0.2799160294439238,-92.58199972901579,0.0)
    ops.remove('sp',79,1)
    ops.remove('sp',79,2)
    ops.remove('sp',79,3)
if pid == 0:
    ops.load(79, 2.334806068882362,0.2799160294439238,-92.58199972901579,0.0)
    ops.remove("sp",79,1)
    ops.remove("sp",79,2)
    ops.remove("sp",79,3)
if pid == 4:
    ops.load(79, 2.334806068882362,0.2799160294439238,-92.58199972901579,0.0)
    ops.remove('sp',79,1)
    ops.remove('sp',79,2)
    ops.remove('sp',79,3)
if pid == 0:
    ops.load(79, 2.334806068882362,0.2799160294439238,-92.58199972901579,0.0)
    ops.remove("sp",79,1)
    ops.remove("sp",79,2)
    ops.remove("sp",79,3)
if pid == 3:
    ops.load(80, -3.033027230821244,7.1285503704347795,-92.97601068145732,0.0)
    ops.remove('sp',80,1)
    ops.remove('sp',80,2)
    ops.remove('sp',80,3)
if pid == 0:
    ops.load(80, -3.033027230821244,7.1285503704347795,-92.97601068145732,0.0)
    ops.remove("sp",80,1)
    ops.remove("sp",80,2)
    ops.remove("sp",80,3)
if pid == 4:
    ops.load(80, -3.033027230821244,7.1285503704347795,-92.97601068145732,0.0)
    ops.remove('sp',80,1)
    ops.remove('sp',80,2)
    ops.remove('sp',80,3)
if pid == 0:
    ops.load(80, -3.033027230821244,7.1285503704347795,-92.97601068145732,0.0)
    ops.remove("sp",80,1)
    ops.remove("sp",80,2)
    ops.remove("sp",80,3)
if pid == 5:
    ops.load(80, -3.033027230821244,7.1285503704347795,-92.97601068145732,0.0)
    ops.remove('sp',80,1)
    ops.remove('sp',80,2)
    ops.remove('sp',80,3)
if pid == 0:
    ops.load(80, -3.033027230821244,7.1285503704347795,-92.97601068145732,0.0)
    ops.remove("sp",80,1)
    ops.remove("sp",80,2)
    ops.remove("sp",80,3)
if pid == 4:
    ops.load(81, -7.343975436243816,9.39712156204067,-42.327368409001274,0.0)
    ops.remove('sp',81,1)
    ops.remove('sp',81,2)
    ops.remove('sp',81,3)
if pid == 0:
    ops.load(81, -7.343975436243816,9.39712156204067,-42.327368409001274,0.0)
    ops.remove("sp",81,1)
    ops.remove("sp",81,2)
    ops.remove("sp",81,3)
if pid == 5:
    ops.load(81, -7.343975436243816,9.39712156204067,-42.327368409001274,0.0)
    ops.remove('sp',81,1)
    ops.remove('sp',81,2)
    ops.remove('sp',81,3)
if pid == 0:
    ops.load(81, -7.343975436243816,9.39712156204067,-42.327368409001274,0.0)
    ops.remove("sp",81,1)
    ops.remove("sp",81,2)
    ops.remove("sp",81,3)
if pid == 4:
    ops.load(82, 13.546706378707405,3.3822523112815794,-47.75280665906557,0.0)
    ops.remove('sp',82,1)
    ops.remove('sp',82,2)
    ops.remove('sp',82,3)
if pid == 0:
    ops.load(82, 13.546706378707405,3.3822523112815794,-47.75280665906557,0.0)
    ops.remove("sp",82,1)
    ops.remove("sp",82,2)
    ops.remove("sp",82,3)
if pid == 5:
    ops.load(82, 13.546706378707405,3.3822523112815794,-47.75280665906557,0.0)
    ops.remove('sp',82,1)
    ops.remove('sp',82,2)
    ops.remove('sp',82,3)
if pid == 0:
    ops.load(82, 13.546706378707405,3.3822523112815794,-47.75280665906557,0.0)
    ops.remove("sp",82,1)
    ops.remove("sp",82,2)
    ops.remove("sp",82,3)
if pid == 4:
    ops.load(83, 11.74111154418907,-0.21364611928688504,-48.784173492617036,0.0)
    ops.remove('sp',83,1)
    ops.remove('sp',83,2)
    ops.remove('sp',83,3)
if pid == 0:
    ops.load(83, 11.74111154418907,-0.21364611928688504,-48.784173492617036,0.0)
    ops.remove("sp",83,1)
    ops.remove("sp",83,2)
    ops.remove("sp",83,3)
if pid == 5:
    ops.load(83, 11.74111154418907,-0.21364611928688504,-48.784173492617036,0.0)
    ops.remove('sp',83,1)
    ops.remove('sp',83,2)
    ops.remove('sp',83,3)
if pid == 0:
    ops.load(83, 11.74111154418907,-0.21364611928688504,-48.784173492617036,0.0)
    ops.remove("sp",83,1)
    ops.remove("sp",83,2)
    ops.remove("sp",83,3)
if pid == 6:
    ops.load(83, 11.74111154418907,-0.21364611928688504,-48.784173492617036,0.0)
    ops.remove('sp',83,1)
    ops.remove('sp',83,2)
    ops.remove('sp',83,3)
if pid == 0:
    ops.load(83, 11.74111154418907,-0.21364611928688504,-48.784173492617036,0.0)
    ops.remove("sp",83,1)
    ops.remove("sp",83,2)
    ops.remove("sp",83,3)
if pid == 4:
    ops.load(84, -2.666097307037842,13.638252443756407,-48.877069210976266,0.0)
    ops.remove('sp',84,1)
    ops.remove('sp',84,2)
    ops.remove('sp',84,3)
if pid == 0:
    ops.load(84, -2.666097307037842,13.638252443756407,-48.877069210976266,0.0)
    ops.remove("sp",84,1)
    ops.remove("sp",84,2)
    ops.remove("sp",84,3)
if pid == 5:
    ops.load(84, -2.666097307037842,13.638252443756407,-48.877069210976266,0.0)
    ops.remove('sp',84,1)
    ops.remove('sp',84,2)
    ops.remove('sp',84,3)
if pid == 0:
    ops.load(84, -2.666097307037842,13.638252443756407,-48.877069210976266,0.0)
    ops.remove("sp",84,1)
    ops.remove("sp",84,2)
    ops.remove("sp",84,3)
if pid == 6:
    ops.load(84, -2.666097307037842,13.638252443756407,-48.877069210976266,0.0)
    ops.remove('sp',84,1)
    ops.remove('sp',84,2)
    ops.remove('sp',84,3)
if pid == 0:
    ops.load(84, -2.666097307037842,13.638252443756407,-48.877069210976266,0.0)
    ops.remove("sp",84,1)
    ops.remove("sp",84,2)
    ops.remove("sp",84,3)
if pid == 5:
    ops.load(85, -21.297166420282046,-21.44186461124816,-209.30685736317264,0.0)
    ops.remove('sp',85,1)
    ops.remove('sp',85,2)
    ops.remove('sp',85,3)
if pid == 0:
    ops.load(85, -21.297166420282046,-21.44186461124816,-209.30685736317264,0.0)
    ops.remove("sp",85,1)
    ops.remove("sp",85,2)
    ops.remove("sp",85,3)
if pid == 6:
    ops.load(85, -21.297166420282046,-21.44186461124816,-209.30685736317264,0.0)
    ops.remove('sp',85,1)
    ops.remove('sp',85,2)
    ops.remove('sp',85,3)
if pid == 0:
    ops.load(85, -21.297166420282046,-21.44186461124816,-209.30685736317264,0.0)
    ops.remove("sp",85,1)
    ops.remove("sp",85,2)
    ops.remove("sp",85,3)
if pid == 7:
    ops.load(85, -21.297166420282046,-21.44186461124816,-209.30685736317264,0.0)
    ops.remove('sp',85,1)
    ops.remove('sp',85,2)
    ops.remove('sp',85,3)
if pid == 0:
    ops.load(85, -21.297166420282046,-21.44186461124816,-209.30685736317264,0.0)
    ops.remove("sp",85,1)
    ops.remove("sp",85,2)
    ops.remove("sp",85,3)
if pid == 5:
    ops.load(86, 29.410474491544562,3.1201497258085436,-194.72337539837787,0.0)
    ops.remove('sp',86,1)
    ops.remove('sp',86,2)
    ops.remove('sp',86,3)
if pid == 0:
    ops.load(86, 29.410474491544562,3.1201497258085436,-194.72337539837787,0.0)
    ops.remove("sp",86,1)
    ops.remove("sp",86,2)
    ops.remove("sp",86,3)
if pid == 7:
    ops.load(86, 29.410474491544562,3.1201497258085436,-194.72337539837787,0.0)
    ops.remove('sp',86,1)
    ops.remove('sp',86,2)
    ops.remove('sp',86,3)
if pid == 0:
    ops.load(86, 29.410474491544562,3.1201497258085436,-194.72337539837787,0.0)
    ops.remove("sp",86,1)
    ops.remove("sp",86,2)
    ops.remove("sp",86,3)
if pid == 5:
    ops.load(87, 31.187975032566513,-3.953813413069021,-202.04779611338637,0.0)
    ops.remove('sp',87,1)
    ops.remove('sp',87,2)
    ops.remove('sp',87,3)
if pid == 0:
    ops.load(87, 31.187975032566513,-3.953813413069021,-202.04779611338637,0.0)
    ops.remove("sp",87,1)
    ops.remove("sp",87,2)
    ops.remove("sp",87,3)
if pid == 6:
    ops.load(87, 31.187975032566513,-3.953813413069021,-202.04779611338637,0.0)
    ops.remove('sp',87,1)
    ops.remove('sp',87,2)
    ops.remove('sp',87,3)
if pid == 0:
    ops.load(87, 31.187975032566513,-3.953813413069021,-202.04779611338637,0.0)
    ops.remove("sp",87,1)
    ops.remove("sp",87,2)
    ops.remove("sp",87,3)
if pid == 7:
    ops.load(87, 31.187975032566513,-3.953813413069021,-202.04779611338637,0.0)
    ops.remove('sp',87,1)
    ops.remove('sp',87,2)
    ops.remove('sp',87,3)
if pid == 0:
    ops.load(87, 31.187975032566513,-3.953813413069021,-202.04779611338637,0.0)
    ops.remove("sp",87,1)
    ops.remove("sp",87,2)
    ops.remove("sp",87,3)
if pid == 6:
    ops.load(88, 8.349046587923267,19.77267412931986,-205.06002767728634,0.0)
    ops.remove('sp',88,1)
    ops.remove('sp',88,2)
    ops.remove('sp',88,3)
if pid == 0:
    ops.load(88, 8.349046587923267,19.77267412931986,-205.06002767728634,0.0)
    ops.remove("sp",88,1)
    ops.remove("sp",88,2)
    ops.remove("sp",88,3)
if pid == 7:
    ops.load(88, 8.349046587923267,19.77267412931986,-205.06002767728634,0.0)
    ops.remove('sp',88,1)
    ops.remove('sp',88,2)
    ops.remove('sp',88,3)
if pid == 0:
    ops.load(88, 8.349046587923267,19.77267412931986,-205.06002767728634,0.0)
    ops.remove("sp",88,1)
    ops.remove("sp",88,2)
    ops.remove("sp",88,3)
if pid == 6:
    ops.load(217, 154.35581585853635,-70.13865525345305,-99.23527466663569)
    ops.remove('sp',217,1)
    ops.remove('sp',217,2)
    ops.remove('sp',217,3)
if pid == 0:
    ops.remove("sp",217,1)
    ops.remove("sp",217,2)
    ops.remove("sp",217,3)
    ops.load(217, 154.35581585853635,-70.13865525345305,-99.23527466663569)
if pid == 5:
    ops.load(218, 139.96328140831488,0.7516822800120281,21.19804455133456)
    ops.remove('sp',218,1)
    ops.remove('sp',218,2)
    ops.remove('sp',218,3)
if pid == 0:
    ops.remove("sp",218,1)
    ops.remove("sp",218,2)
    ops.remove("sp",218,3)
    ops.load(218, 139.96328140831488,0.7516822800120281,21.19804455133456)
if pid == 3:
    ops.load(219, 133.51684884534063,0.28709236142928907,33.680842368199336)
    ops.remove('sp',219,1)
    ops.remove('sp',219,2)
    ops.remove('sp',219,3)
if pid == 0:
    ops.remove("sp",219,1)
    ops.remove("sp",219,2)
    ops.remove("sp",219,3)
    ops.load(219, 133.51684884534063,0.28709236142928907,33.680842368199336)
if pid == 2:
    ops.load(220, 90.82401470018797,3.8047124402181196,33.868706688897795)
    ops.remove('sp',220,1)
    ops.remove('sp',220,2)
    ops.remove('sp',220,3)
if pid == 0:
    ops.remove("sp",220,1)
    ops.remove("sp",220,2)
    ops.remove("sp",220,3)
    ops.load(220, 90.82401470018797,3.8047124402181196,33.868706688897795)
if pid == 1:
    ops.load(221, 34.014221552116695,1.8856731936466047,38.602626802050246)
    ops.remove('sp',221,1)
    ops.remove('sp',221,2)
    ops.remove('sp',221,3)
if pid == 0:
    ops.remove("sp",221,1)
    ops.remove("sp",221,2)
    ops.remove("sp",221,3)
    ops.load(221, 34.014221552116695,1.8856731936466047,38.602626802050246)
if pid == 1:
    ops.load(222, 16.76697196934695,-1.0436167092149777,35.972902694278)
    ops.remove('sp',222,1)
    ops.remove('sp',222,2)
    ops.remove('sp',222,3)
if pid == 0:
    ops.remove("sp",222,1)
    ops.remove("sp",222,2)
    ops.remove("sp",222,3)
    ops.load(222, 16.76697196934695,-1.0436167092149777,35.972902694278)
if pid == 1:
    ops.load(223, 31.1955490185909,-1.2124304334480178,35.95950549330445)
    ops.remove('sp',223,1)
    ops.remove('sp',223,2)
    ops.remove('sp',223,3)
if pid == 0:
    ops.remove("sp",223,1)
    ops.remove("sp",223,2)
    ops.remove("sp",223,3)
    ops.load(223, 31.1955490185909,-1.2124304334480178,35.95950549330445)
if pid == 1:
    ops.load(224, 37.78805322594224,0.3490143736617986,36.6328369665299)
    ops.remove('sp',224,1)
    ops.remove('sp',224,2)
    ops.remove('sp',224,3)
if pid == 0:
    ops.remove("sp",224,1)
    ops.remove("sp",224,2)
    ops.remove("sp",224,3)
    ops.load(224, 37.78805322594224,0.3490143736617986,36.6328369665299)
if pid == 1:
    ops.load(225, 34.811182462943236,1.1668967231895,35.2857451704799)
    ops.remove('sp',225,1)
    ops.remove('sp',225,2)
    ops.remove('sp',225,3)
if pid == 0:
    ops.remove("sp",225,1)
    ops.remove("sp",225,2)
    ops.remove("sp",225,3)
    ops.load(225, 34.811182462943236,1.1668967231895,35.2857451704799)
if pid == 2:
    ops.load(226, 18.665880915388424,0.910180730119039,36.094643339623815)
    ops.remove('sp',226,1)
    ops.remove('sp',226,2)
    ops.remove('sp',226,3)
if pid == 0:
    ops.remove("sp",226,1)
    ops.remove("sp",226,2)
    ops.remove("sp",226,3)
    ops.load(226, 18.665880915388424,0.910180730119039,36.094643339623815)
if pid == 7:
    ops.load(227, 356.67489748979074,-10.686260229215168,48.99673991679928)
    ops.remove('sp',227,1)
    ops.remove('sp',227,2)
    ops.remove('sp',227,3)
if pid == 0:
    ops.remove("sp",227,1)
    ops.remove("sp",227,2)
    ops.remove("sp",227,3)
    ops.load(227, 356.67489748979074,-10.686260229215168,48.99673991679928)
if pid == 6:
    ops.load(228, 177.13925945566803,-0.8323893738906949,19.46329463181325)
    ops.remove('sp',228,1)
    ops.remove('sp',228,2)
    ops.remove('sp',228,3)
if pid == 0:
    ops.remove("sp",228,1)
    ops.remove("sp",228,2)
    ops.remove("sp",228,3)
    ops.load(228, 177.13925945566803,-0.8323893738906949,19.46329463181325)
if pid == 4:
    ops.load(229, 147.36060857139117,-3.4970789033429592,34.62523813033073)
    ops.remove('sp',229,1)
    ops.remove('sp',229,2)
    ops.remove('sp',229,3)
if pid == 0:
    ops.remove("sp",229,1)
    ops.remove("sp",229,2)
    ops.remove("sp",229,3)
    ops.load(229, 147.36060857139117,-3.4970789033429592,34.62523813033073)
if pid == 3:
    ops.load(230, 98.50191974329468,-3.9647662730990465,33.08026607931566)
    ops.remove('sp',230,1)
    ops.remove('sp',230,2)
    ops.remove('sp',230,3)
if pid == 0:
    ops.remove("sp",230,1)
    ops.remove("sp",230,2)
    ops.remove("sp",230,3)
    ops.load(230, 98.50191974329468,-3.9647662730990465,33.08026607931566)
if pid == 2:
    ops.load(231, 35.3391545669312,-1.7634579723706272,40.8102552737904)
    ops.remove('sp',231,1)
    ops.remove('sp',231,2)
    ops.remove('sp',231,3)
if pid == 0:
    ops.remove("sp",231,1)
    ops.remove("sp",231,2)
    ops.remove("sp",231,3)
    ops.load(231, 35.3391545669312,-1.7634579723706272,40.8102552737904)
if pid == 6:
    ops.load(232, 341.4510651468483,-18.466549693034448,223.65583507954213)
    ops.remove('sp',232,1)
    ops.remove('sp',232,2)
    ops.remove('sp',232,3)
if pid == 0:
    ops.remove("sp",232,1)
    ops.remove("sp",232,2)
    ops.remove("sp",232,3)
    ops.load(232, 341.4510651468483,-18.466549693034448,223.65583507954213)
if pid == 6:
    ops.load(233, 373.5105590952754,-12.51901218426025,322.0678352392394)
    ops.remove('sp',233,1)
    ops.remove('sp',233,2)
    ops.remove('sp',233,3)
if pid == 0:
    ops.remove("sp",233,1)
    ops.remove("sp",233,2)
    ops.remove("sp",233,3)
    ops.load(233, 373.5105590952754,-12.51901218426025,322.0678352392394)
if pid == 7:
    ops.load(234, 18.918334535615525,-15.504247089114648,95.10304407050555)
    ops.remove('sp',234,1)
    ops.remove('sp',234,2)
    ops.remove('sp',234,3)
if pid == 0:
    ops.remove("sp",234,1)
    ops.remove("sp",234,2)
    ops.remove("sp",234,3)
    ops.load(234, 18.918334535615525,-15.504247089114648,95.10304407050555)
if pid == 7:
    ops.load(235, 20.204467629453905,-5.320906668796625,86.40947021536202)
    ops.remove('sp',235,1)
    ops.remove('sp',235,2)
    ops.remove('sp',235,3)
if pid == 0:
    ops.remove("sp",235,1)
    ops.remove("sp",235,2)
    ops.remove("sp",235,3)
    ops.load(235, 20.204467629453905,-5.320906668796625,86.40947021536202)
if pid == 7:
    ops.load(236, -0.08159963631453525,121.96365860492905,68.24744566139157)
    ops.remove('sp',236,1)
    ops.remove('sp',236,2)
    ops.remove('sp',236,3)
if pid == 0:
    ops.remove("sp",236,1)
    ops.remove("sp",236,2)
    ops.remove("sp",236,3)
    ops.load(236, -0.08159963631453525,121.96365860492905,68.24744566139157)
if pid == 6:
    ops.load(237, -27.68605850299901,15.740891598706565,111.28963295709454)
    ops.remove('sp',237,1)
    ops.remove('sp',237,2)
    ops.remove('sp',237,3)
if pid == 0:
    ops.remove("sp",237,1)
    ops.remove("sp",237,2)
    ops.remove("sp",237,3)
    ops.load(237, -27.68605850299901,15.740891598706565,111.28963295709454)
if pid == 5:
    ops.load(238, 6.6143593445335895,-9.643212117419633,8.331183729505806)
    ops.remove('sp',238,1)
    ops.remove('sp',238,2)
    ops.remove('sp',238,3)
if pid == 0:
    ops.remove("sp",238,1)
    ops.remove("sp",238,2)
    ops.remove("sp",238,3)
    ops.load(238, 6.6143593445335895,-9.643212117419633,8.331183729505806)
if pid == 4:
    ops.load(239, 2.8564106451845825,-6.342466097242271,8.289987940687432)
    ops.remove('sp',239,1)
    ops.remove('sp',239,2)
    ops.remove('sp',239,3)
if pid == 0:
    ops.remove("sp",239,1)
    ops.remove("sp",239,2)
    ops.remove("sp",239,3)
    ops.load(239, 2.8564106451845825,-6.342466097242271,8.289987940687432)
if pid == 2:
    ops.load(240, 2.0493654048919234,2.480548615971744,20.927576570890672)
    ops.remove('sp',240,1)
    ops.remove('sp',240,2)
    ops.remove('sp',240,3)
if pid == 0:
    ops.remove("sp",240,1)
    ops.remove("sp",240,2)
    ops.remove("sp",240,3)
    ops.load(240, 2.0493654048919234,2.480548615971744,20.927576570890672)
if pid == 1:
    ops.load(241, 0.07409651520097348,-0.053294511331544975,47.869404464331666)
    ops.remove('sp',241,1)
    ops.remove('sp',241,2)
    ops.remove('sp',241,3)
if pid == 0:
    ops.remove("sp",241,1)
    ops.remove("sp",241,2)
    ops.remove("sp",241,3)
    ops.load(241, 0.07409651520097348,-0.053294511331544975,47.869404464331666)
if pid == 1:
    ops.load(242, 0.03045918626503007,0.03853238754892056,47.80978546427686)
    ops.remove('sp',242,1)
    ops.remove('sp',242,2)
    ops.remove('sp',242,3)
if pid == 0:
    ops.remove("sp",242,1)
    ops.remove("sp",242,2)
    ops.remove("sp",242,3)
    ops.load(242, 0.03045918626503007,0.03853238754892056,47.80978546427686)
if pid == 1:
    ops.load(243, 0.04094981792332905,-0.002139843131879156,47.83533846709287)
    ops.remove('sp',243,1)
    ops.remove('sp',243,2)
    ops.remove('sp',243,3)
if pid == 0:
    ops.remove("sp",243,1)
    ops.remove("sp",243,2)
    ops.remove("sp",243,3)
    ops.load(243, 0.04094981792332905,-0.002139843131879156,47.83533846709287)
if pid == 1:
    ops.load(244, 0.05836232043010453,-0.0035947289650096943,47.85511711019286)
    ops.remove('sp',244,1)
    ops.remove('sp',244,2)
    ops.remove('sp',244,3)
if pid == 0:
    ops.remove("sp",244,1)
    ops.remove("sp",244,2)
    ops.remove("sp",244,3)
    ops.load(244, 0.05836232043010453,-0.0035947289650096943,47.85511711019286)
if pid == 2:
    ops.load(245, 0.051788273595359355,-0.0032543351631376333,47.8147814301392)
    ops.remove('sp',245,1)
    ops.remove('sp',245,2)
    ops.remove('sp',245,3)
if pid == 0:
    ops.remove("sp",245,1)
    ops.remove("sp",245,2)
    ops.remove("sp",245,3)
    ops.load(245, 0.051788273595359355,-0.0032543351631376333,47.8147814301392)
if pid == 2:
    ops.load(246, 0.0677247255706117,0.02656565580463245,47.65880350953019)
    ops.remove('sp',246,1)
    ops.remove('sp',246,2)
    ops.remove('sp',246,3)
if pid == 0:
    ops.remove("sp",246,1)
    ops.remove("sp",246,2)
    ops.remove("sp",246,3)
    ops.load(246, 0.0677247255706117,0.02656565580463245,47.65880350953019)
if pid == 7:
    ops.load(247, -39.082884146562904,-87.85668020611035,189.34162461921588)
    ops.remove('sp',247,1)
    ops.remove('sp',247,2)
    ops.remove('sp',247,3)
if pid == 0:
    ops.remove("sp",247,1)
    ops.remove("sp",247,2)
    ops.remove("sp",247,3)
    ops.load(247, -39.082884146562904,-87.85668020611035,189.34162461921588)
if pid == 6:
    ops.load(248, 6.326047424708265,-23.579798222860767,11.071170105012705)
    ops.remove('sp',248,1)
    ops.remove('sp',248,2)
    ops.remove('sp',248,3)
if pid == 0:
    ops.remove("sp",248,1)
    ops.remove("sp",248,2)
    ops.remove("sp",248,3)
    ops.load(248, 6.326047424708265,-23.579798222860767,11.071170105012705)
if pid == 5:
    ops.load(249, 4.011568755493805,-9.8194939772576,23.53746360065123)
    ops.remove('sp',249,1)
    ops.remove('sp',249,2)
    ops.remove('sp',249,3)
if pid == 0:
    ops.remove("sp",249,1)
    ops.remove("sp",249,2)
    ops.remove("sp",249,3)
    ops.load(249, 4.011568755493805,-9.8194939772576,23.53746360065123)
if pid == 3:
    ops.load(250, 0.8530207712777196,-2.362860801592734,32.0513971198978)
    ops.remove('sp',250,1)
    ops.remove('sp',250,2)
    ops.remove('sp',250,3)
if pid == 0:
    ops.remove("sp",250,1)
    ops.remove("sp",250,2)
    ops.remove("sp",250,3)
    ops.load(250, 0.8530207712777196,-2.362860801592734,32.0513971198978)
if pid == 2:
    ops.load(251, 0.07462250210480434,0.007569401007810726,47.48713240541267)
    ops.remove('sp',251,1)
    ops.remove('sp',251,2)
    ops.remove('sp',251,3)
if pid == 0:
    ops.remove("sp",251,1)
    ops.remove("sp",251,2)
    ops.remove("sp",251,3)
    ops.load(251, 0.07462250210480434,0.007569401007810726,47.48713240541267)
if pid == 6:
    ops.load(252, -21.324733863465937,-28.482220920863192,127.74012688482479)
    ops.remove('sp',252,1)
    ops.remove('sp',252,2)
    ops.remove('sp',252,3)
if pid == 0:
    ops.remove("sp",252,1)
    ops.remove("sp",252,2)
    ops.remove("sp",252,3)
    ops.load(252, -21.324733863465937,-28.482220920863192,127.74012688482479)
if pid == 7:
    ops.load(253, -63.30041326281064,14.612860473647077,227.96267103575582)
    ops.remove('sp',253,1)
    ops.remove('sp',253,2)
    ops.remove('sp',253,3)
if pid == 0:
    ops.remove("sp",253,1)
    ops.remove("sp",253,2)
    ops.remove("sp",253,3)
    ops.load(253, -63.30041326281064,14.612860473647077,227.96267103575582)
if pid == 7:
    ops.load(254, -57.23350713278621,0.4505362588782699,215.3353991197845)
    ops.remove('sp',254,1)
    ops.remove('sp',254,2)
    ops.remove('sp',254,3)
if pid == 0:
    ops.remove("sp",254,1)
    ops.remove("sp",254,2)
    ops.remove("sp",254,3)
    ops.load(254, -57.23350713278621,0.4505362588782699,215.3353991197845)
if pid == 7:
    ops.load(255, -62.15478930878252,-1.0139134821220104,231.02230860469814)
    ops.remove('sp',255,1)
    ops.remove('sp',255,2)
    ops.remove('sp',255,3)
if pid == 0:
    ops.remove("sp",255,1)
    ops.remove("sp",255,2)
    ops.remove("sp",255,3)
    ops.load(255, -62.15478930878252,-1.0139134821220104,231.02230860469814)
if pid == 7:
    ops.load(256, -46.79089034623699,-23.69445090777269,200.6885833192341)
    ops.remove('sp',256,1)
    ops.remove('sp',256,2)
    ops.remove('sp',256,3)
if pid == 0:
    ops.remove("sp",256,1)
    ops.remove("sp",256,2)
    ops.remove("sp",256,3)
    ops.load(256, -46.79089034623699,-23.69445090777269,200.6885833192341)
if pid == 5:
    ops.load(277, -22.703227099426122,-103.75703122722095,-77.44302581071383)
    ops.remove('sp',277,1)
    ops.remove('sp',277,2)
    ops.remove('sp',277,3)
if pid == 0:
    ops.remove("sp",277,1)
    ops.remove("sp",277,2)
    ops.remove("sp",277,3)
    ops.load(277, -22.703227099426122,-103.75703122722095,-77.44302581071383)
if pid == 6:
    ops.load(277, -22.703227099426122,-103.75703122722095,-77.44302581071383)
    ops.remove('sp',277,1)
    ops.remove('sp',277,2)
    ops.remove('sp',277,3)
if pid == 0:
    ops.remove("sp",277,1)
    ops.remove("sp",277,2)
    ops.remove("sp",277,3)
    ops.load(277, -22.703227099426122,-103.75703122722095,-77.44302581071383)
if pid == 6:
    ops.load(278, -65.6091776302516,-17.50027021933809,-211.67240996907296)
    ops.remove('sp',278,1)
    ops.remove('sp',278,2)
    ops.remove('sp',278,3)
if pid == 0:
    ops.remove("sp",278,1)
    ops.remove("sp",278,2)
    ops.remove("sp",278,3)
    ops.load(278, -65.6091776302516,-17.50027021933809,-211.67240996907296)
if pid == 5:
    ops.load(279, -0.05871566519881255,-8.801316176483336,-90.0772937577646)
    ops.remove('sp',279,1)
    ops.remove('sp',279,2)
    ops.remove('sp',279,3)
if pid == 0:
    ops.remove("sp",279,1)
    ops.remove("sp",279,2)
    ops.remove("sp",279,3)
    ops.load(279, -0.05871566519881255,-8.801316176483336,-90.0772937577646)
if pid == 6:
    ops.load(279, -0.05871566519881255,-8.801316176483336,-90.0772937577646)
    ops.remove('sp',279,1)
    ops.remove('sp',279,2)
    ops.remove('sp',279,3)
if pid == 0:
    ops.remove("sp",279,1)
    ops.remove("sp",279,2)
    ops.remove("sp",279,3)
    ops.load(279, -0.05871566519881255,-8.801316176483336,-90.0772937577646)
if pid == 6:
    ops.load(280, 13.742724533019024,-76.91833824270407,14.608960862145523)
    ops.remove('sp',280,1)
    ops.remove('sp',280,2)
    ops.remove('sp',280,3)
if pid == 0:
    ops.remove("sp",280,1)
    ops.remove("sp",280,2)
    ops.remove("sp",280,3)
    ops.load(280, 13.742724533019024,-76.91833824270407,14.608960862145523)
if pid == 7:
    ops.load(280, 13.742724533019024,-76.91833824270407,14.608960862145523)
    ops.remove('sp',280,1)
    ops.remove('sp',280,2)
    ops.remove('sp',280,3)
if pid == 0:
    ops.remove("sp",280,1)
    ops.remove("sp",280,2)
    ops.remove("sp",280,3)
    ops.load(280, 13.742724533019024,-76.91833824270407,14.608960862145523)
if pid == 5:
    ops.load(281, 11.841167564366163,-6.362957398099374,43.620853807142474)
    ops.remove('sp',281,1)
    ops.remove('sp',281,2)
    ops.remove('sp',281,3)
if pid == 0:
    ops.remove("sp",281,1)
    ops.remove("sp",281,2)
    ops.remove("sp",281,3)
    ops.load(281, 11.841167564366163,-6.362957398099374,43.620853807142474)
if pid == 7:
    ops.load(281, 11.841167564366163,-6.362957398099374,43.620853807142474)
    ops.remove('sp',281,1)
    ops.remove('sp',281,2)
    ops.remove('sp',281,3)
if pid == 0:
    ops.remove("sp",281,1)
    ops.remove("sp",281,2)
    ops.remove("sp",281,3)
    ops.load(281, 11.841167564366163,-6.362957398099374,43.620853807142474)
if pid == 7:
    ops.load(282, 58.579817549302916,2.297037307456087,183.29426177071213)
    ops.remove('sp',282,1)
    ops.remove('sp',282,2)
    ops.remove('sp',282,3)
if pid == 0:
    ops.remove("sp",282,1)
    ops.remove("sp",282,2)
    ops.remove("sp",282,3)
    ops.load(282, 58.579817549302916,2.297037307456087,183.29426177071213)
if pid == 6:
    ops.load(283, 12.358308270646225,-1.3383091630745743,40.63022147675744)
    ops.remove('sp',283,1)
    ops.remove('sp',283,2)
    ops.remove('sp',283,3)
if pid == 0:
    ops.remove("sp",283,1)
    ops.remove("sp",283,2)
    ops.remove("sp",283,3)
    ops.load(283, 12.358308270646225,-1.3383091630745743,40.63022147675744)
if pid == 7:
    ops.load(283, 12.358308270646225,-1.3383091630745743,40.63022147675744)
    ops.remove('sp',283,1)
    ops.remove('sp',283,2)
    ops.remove('sp',283,3)
if pid == 0:
    ops.remove("sp",283,1)
    ops.remove("sp",283,2)
    ops.remove("sp",283,3)
    ops.load(283, 12.358308270646225,-1.3383091630745743,40.63022147675744)
if pid == 7:
    ops.load(284, 57.990120254208804,42.42070164062335,154.24315651168678)
    ops.remove('sp',284,1)
    ops.remove('sp',284,2)
    ops.remove('sp',284,3)
if pid == 0:
    ops.remove("sp",284,1)
    ops.remove("sp",284,2)
    ops.remove("sp",284,3)
    ops.load(284, 57.990120254208804,42.42070164062335,154.24315651168678)
if pid == 6:
    ops.load(285, -19.255832969025256,124.51118413066331,1.6062678083977175)
    ops.remove('sp',285,1)
    ops.remove('sp',285,2)
    ops.remove('sp',285,3)
if pid == 0:
    ops.remove("sp",285,1)
    ops.remove("sp",285,2)
    ops.remove("sp",285,3)
    ops.load(285, -19.255832969025256,124.51118413066331,1.6062678083977175)
if pid == 7:
    ops.load(285, -19.255832969025256,124.51118413066331,1.6062678083977175)
    ops.remove('sp',285,1)
    ops.remove('sp',285,2)
    ops.remove('sp',285,3)
if pid == 0:
    ops.remove("sp",285,1)
    ops.remove("sp",285,2)
    ops.remove("sp",285,3)
    ops.load(285, -19.255832969025256,124.51118413066331,1.6062678083977175)
if pid == 3:
    ops.load(286, -16.93410260725762,-87.5563019775243,73.98338541481735)
    ops.remove('sp',286,1)
    ops.remove('sp',286,2)
    ops.remove('sp',286,3)
if pid == 0:
    ops.remove("sp",286,1)
    ops.remove("sp",286,2)
    ops.remove("sp",286,3)
    ops.load(286, -16.93410260725762,-87.5563019775243,73.98338541481735)
if pid == 5:
    ops.load(286, -16.93410260725762,-87.5563019775243,73.98338541481735)
    ops.remove('sp',286,1)
    ops.remove('sp',286,2)
    ops.remove('sp',286,3)
if pid == 0:
    ops.remove("sp",286,1)
    ops.remove("sp",286,2)
    ops.remove("sp",286,3)
    ops.load(286, -16.93410260725762,-87.5563019775243,73.98338541481735)
if pid == 5:
    ops.load(287, 0.5992228213425341,-35.45681970923645,49.29030566751068)
    ops.remove('sp',287,1)
    ops.remove('sp',287,2)
    ops.remove('sp',287,3)
if pid == 0:
    ops.remove("sp",287,1)
    ops.remove("sp",287,2)
    ops.remove("sp",287,3)
    ops.load(287, 0.5992228213425341,-35.45681970923645,49.29030566751068)
if pid == 4:
    ops.load(288, -0.1255334112915396,-3.1498906150305688,91.26744748837396)
    ops.remove('sp',288,1)
    ops.remove('sp',288,2)
    ops.remove('sp',288,3)
if pid == 0:
    ops.remove("sp",288,1)
    ops.remove("sp",288,2)
    ops.remove("sp",288,3)
    ops.load(288, -0.1255334112915396,-3.1498906150305688,91.26744748837396)
if pid == 5:
    ops.load(288, -0.1255334112915396,-3.1498906150305688,91.26744748837396)
    ops.remove('sp',288,1)
    ops.remove('sp',288,2)
    ops.remove('sp',288,3)
if pid == 0:
    ops.remove("sp",288,1)
    ops.remove("sp",288,2)
    ops.remove("sp",288,3)
    ops.load(288, -0.1255334112915396,-3.1498906150305688,91.26744748837396)
if pid == 5:
    ops.load(289, -1.1992702027183983,-1.865421551067157,90.88858379696038)
    ops.remove('sp',289,1)
    ops.remove('sp',289,2)
    ops.remove('sp',289,3)
if pid == 0:
    ops.remove("sp",289,1)
    ops.remove("sp",289,2)
    ops.remove("sp",289,3)
    ops.load(289, -1.1992702027183983,-1.865421551067157,90.88858379696038)
if pid == 4:
    ops.load(290, -0.3960369500509212,-0.24192005956834134,94.81409192478864)
    ops.remove('sp',290,1)
    ops.remove('sp',290,2)
    ops.remove('sp',290,3)
if pid == 0:
    ops.remove("sp",290,1)
    ops.remove("sp",290,2)
    ops.remove("sp",290,3)
    ops.load(290, -0.3960369500509212,-0.24192005956834134,94.81409192478864)
if pid == 5:
    ops.load(290, -0.3960369500509212,-0.24192005956834134,94.81409192478864)
    ops.remove('sp',290,1)
    ops.remove('sp',290,2)
    ops.remove('sp',290,3)
if pid == 0:
    ops.remove("sp",290,1)
    ops.remove("sp",290,2)
    ops.remove("sp",290,3)
    ops.load(290, -0.3960369500509212,-0.24192005956834134,94.81409192478864)
if pid == 5:
    ops.load(291, -0.41229081377531385,-0.4180872903304735,94.5256932791331)
    ops.remove('sp',291,1)
    ops.remove('sp',291,2)
    ops.remove('sp',291,3)
if pid == 0:
    ops.remove("sp",291,1)
    ops.remove("sp",291,2)
    ops.remove("sp",291,3)
    ops.load(291, -0.41229081377531385,-0.4180872903304735,94.5256932791331)
if pid == 6:
    ops.load(291, -0.41229081377531385,-0.4180872903304735,94.5256932791331)
    ops.remove('sp',291,1)
    ops.remove('sp',291,2)
    ops.remove('sp',291,3)
if pid == 0:
    ops.remove("sp",291,1)
    ops.remove("sp",291,2)
    ops.remove("sp",291,3)
    ops.load(291, -0.41229081377531385,-0.4180872903304735,94.5256932791331)
if pid == 4:
    ops.load(292, -0.18835473724830018,0.5553617689593808,96.06952712462123)
    ops.remove('sp',292,1)
    ops.remove('sp',292,2)
    ops.remove('sp',292,3)
if pid == 0:
    ops.remove("sp",292,1)
    ops.remove("sp",292,2)
    ops.remove("sp",292,3)
    ops.load(292, -0.18835473724830018,0.5553617689593808,96.06952712462123)
if pid == 6:
    ops.load(292, -0.18835473724830018,0.5553617689593808,96.06952712462123)
    ops.remove('sp',292,1)
    ops.remove('sp',292,2)
    ops.remove('sp',292,3)
if pid == 0:
    ops.remove("sp",292,1)
    ops.remove("sp",292,2)
    ops.remove("sp",292,3)
    ops.load(292, -0.18835473724830018,0.5553617689593808,96.06952712462123)
if pid == 6:
    ops.load(293, 3.009865529082971,44.50948630981955,64.18349906530686)
    ops.remove('sp',293,1)
    ops.remove('sp',293,2)
    ops.remove('sp',293,3)
if pid == 0:
    ops.remove("sp",293,1)
    ops.remove("sp",293,2)
    ops.remove("sp",293,3)
    ops.load(293, 3.009865529082971,44.50948630981955,64.18349906530686)
if pid == 4:
    ops.load(294, -22.449312098721872,106.33984024622625,72.49669378138492)
    ops.remove('sp',294,1)
    ops.remove('sp',294,2)
    ops.remove('sp',294,3)
if pid == 0:
    ops.remove("sp",294,1)
    ops.remove("sp",294,2)
    ops.remove("sp",294,3)
    ops.load(294, -22.449312098721872,106.33984024622625,72.49669378138492)
if pid == 6:
    ops.load(294, -22.449312098721872,106.33984024622625,72.49669378138492)
    ops.remove('sp',294,1)
    ops.remove('sp',294,2)
    ops.remove('sp',294,3)
if pid == 0:
    ops.remove("sp",294,1)
    ops.remove("sp",294,2)
    ops.remove("sp",294,3)
    ops.load(294, -22.449312098721872,106.33984024622625,72.49669378138492)
if pid == 2:
    ops.load(295, -14.861914871235243,-75.05443263782914,78.03784055704887)
    ops.remove('sp',295,1)
    ops.remove('sp',295,2)
    ops.remove('sp',295,3)
if pid == 0:
    ops.remove("sp",295,1)
    ops.remove("sp",295,2)
    ops.remove("sp",295,3)
    ops.load(295, -14.861914871235243,-75.05443263782914,78.03784055704887)
if pid == 3:
    ops.load(295, -14.861914871235243,-75.05443263782914,78.03784055704887)
    ops.remove('sp',295,1)
    ops.remove('sp',295,2)
    ops.remove('sp',295,3)
if pid == 0:
    ops.remove("sp",295,1)
    ops.remove("sp",295,2)
    ops.remove("sp",295,3)
    ops.load(295, -14.861914871235243,-75.05443263782914,78.03784055704887)
if pid == 3:
    ops.load(296, 2.027627667326246,-27.12182806940738,85.73279122503753)
    ops.remove('sp',296,1)
    ops.remove('sp',296,2)
    ops.remove('sp',296,3)
if pid == 0:
    ops.remove("sp",296,1)
    ops.remove("sp",296,2)
    ops.remove("sp",296,3)
    ops.load(296, 2.027627667326246,-27.12182806940738,85.73279122503753)
if pid == 4:
    ops.load(296, 2.027627667326246,-27.12182806940738,85.73279122503753)
    ops.remove('sp',296,1)
    ops.remove('sp',296,2)
    ops.remove('sp',296,3)
if pid == 0:
    ops.remove("sp",296,1)
    ops.remove("sp",296,2)
    ops.remove("sp",296,3)
    ops.load(296, 2.027627667326246,-27.12182806940738,85.73279122503753)
if pid == 2:
    ops.load(297, -0.15736561979278219,-0.4924194570814623,95.71543164870467)
    ops.remove('sp',297,1)
    ops.remove('sp',297,2)
    ops.remove('sp',297,3)
if pid == 0:
    ops.remove("sp",297,1)
    ops.remove("sp",297,2)
    ops.remove("sp",297,3)
    ops.load(297, -0.15736561979278219,-0.4924194570814623,95.71543164870467)
if pid == 4:
    ops.load(297, -0.15736561979278219,-0.4924194570814623,95.71543164870467)
    ops.remove('sp',297,1)
    ops.remove('sp',297,2)
    ops.remove('sp',297,3)
if pid == 0:
    ops.remove("sp",297,1)
    ops.remove("sp",297,2)
    ops.remove("sp",297,3)
    ops.load(297, -0.15736561979278219,-0.4924194570814623,95.71543164870467)
if pid == 4:
    ops.load(298, -0.29551466747062993,-0.07469969128869489,95.96490355924932)
    ops.remove('sp',298,1)
    ops.remove('sp',298,2)
    ops.remove('sp',298,3)
if pid == 0:
    ops.remove("sp",298,1)
    ops.remove("sp",298,2)
    ops.remove("sp",298,3)
    ops.load(298, -0.29551466747062993,-0.07469969128869489,95.96490355924932)
if pid == 2:
    ops.load(299, -0.2981300927241639,0.002866057511217798,95.95765905669842)
    ops.remove('sp',299,1)
    ops.remove('sp',299,2)
    ops.remove('sp',299,3)
if pid == 0:
    ops.remove("sp",299,1)
    ops.remove("sp",299,2)
    ops.remove("sp",299,3)
    ops.load(299, -0.2981300927241639,0.002866057511217798,95.95765905669842)
if pid == 4:
    ops.load(299, -0.2981300927241639,0.002866057511217798,95.95765905669842)
    ops.remove('sp',299,1)
    ops.remove('sp',299,2)
    ops.remove('sp',299,3)
if pid == 0:
    ops.remove("sp",299,1)
    ops.remove("sp",299,2)
    ops.remove("sp",299,3)
    ops.load(299, -0.2981300927241639,0.002866057511217798,95.95765905669842)
if pid == 4:
    ops.load(300, -0.2796087360070548,0.16453032334845433,95.85369426869981)
    ops.remove('sp',300,1)
    ops.remove('sp',300,2)
    ops.remove('sp',300,3)
if pid == 0:
    ops.remove("sp",300,1)
    ops.remove("sp",300,2)
    ops.remove("sp",300,3)
    ops.load(300, -0.2796087360070548,0.16453032334845433,95.85369426869981)
if pid == 3:
    ops.load(301, -0.1799476714039358,0.5264514708780713,95.62032306813657)
    ops.remove('sp',301,1)
    ops.remove('sp',301,2)
    ops.remove('sp',301,3)
if pid == 0:
    ops.remove("sp",301,1)
    ops.remove("sp",301,2)
    ops.remove("sp",301,3)
    ops.load(301, -0.1799476714039358,0.5264514708780713,95.62032306813657)
if pid == 4:
    ops.load(301, -0.1799476714039358,0.5264514708780713,95.62032306813657)
    ops.remove('sp',301,1)
    ops.remove('sp',301,2)
    ops.remove('sp',301,3)
if pid == 0:
    ops.remove("sp",301,1)
    ops.remove("sp",301,2)
    ops.remove("sp",301,3)
    ops.load(301, -0.1799476714039358,0.5264514708780713,95.62032306813657)
if pid == 4:
    ops.load(302, 1.8051108155238833,28.325281824752224,87.78646890032107)
    ops.remove('sp',302,1)
    ops.remove('sp',302,2)
    ops.remove('sp',302,3)
if pid == 0:
    ops.remove("sp",302,1)
    ops.remove("sp",302,2)
    ops.remove("sp",302,3)
    ops.load(302, 1.8051108155238833,28.325281824752224,87.78646890032107)
if pid == 3:
    ops.load(303, -16.42715087406005,79.07627848415197,78.55132021045708)
    ops.remove('sp',303,1)
    ops.remove('sp',303,2)
    ops.remove('sp',303,3)
if pid == 0:
    ops.remove("sp",303,1)
    ops.remove("sp",303,2)
    ops.remove("sp",303,3)
    ops.load(303, -16.42715087406005,79.07627848415197,78.55132021045708)
if pid == 4:
    ops.load(303, -16.42715087406005,79.07627848415197,78.55132021045708)
    ops.remove('sp',303,1)
    ops.remove('sp',303,2)
    ops.remove('sp',303,3)
if pid == 0:
    ops.remove("sp",303,1)
    ops.remove("sp",303,2)
    ops.remove("sp",303,3)
    ops.load(303, -16.42715087406005,79.07627848415197,78.55132021045708)
if pid == 1:
    ops.load(304, -7.910784193043417,-44.24744413180601,82.68210639392453)
    ops.remove('sp',304,1)
    ops.remove('sp',304,2)
    ops.remove('sp',304,3)
if pid == 0:
    ops.remove("sp",304,1)
    ops.remove("sp",304,2)
    ops.remove("sp",304,3)
    ops.load(304, -7.910784193043417,-44.24744413180601,82.68210639392453)
if pid == 2:
    ops.load(304, -7.910784193043417,-44.24744413180601,82.68210639392453)
    ops.remove('sp',304,1)
    ops.remove('sp',304,2)
    ops.remove('sp',304,3)
if pid == 0:
    ops.remove("sp",304,1)
    ops.remove("sp",304,2)
    ops.remove("sp",304,3)
    ops.load(304, -7.910784193043417,-44.24744413180601,82.68210639392453)
if pid == 2:
    ops.load(305, 0.3925327721027283,-16.779764105853943,85.77006182870294)
    ops.remove('sp',305,1)
    ops.remove('sp',305,2)
    ops.remove('sp',305,3)
if pid == 0:
    ops.remove("sp",305,1)
    ops.remove("sp",305,2)
    ops.remove("sp",305,3)
    ops.load(305, 0.3925327721027283,-16.779764105853943,85.77006182870294)
if pid == 1:
    ops.load(306, 0.37495541087973383,0.10790164498392102,99.61095954188764)
    ops.remove('sp',306,1)
    ops.remove('sp',306,2)
    ops.remove('sp',306,3)
if pid == 0:
    ops.remove("sp",306,1)
    ops.remove("sp",306,2)
    ops.remove("sp",306,3)
    ops.load(306, 0.37495541087973383,0.10790164498392102,99.61095954188764)
if pid == 2:
    ops.load(306, 0.37495541087973383,0.10790164498392102,99.61095954188764)
    ops.remove('sp',306,1)
    ops.remove('sp',306,2)
    ops.remove('sp',306,3)
if pid == 0:
    ops.remove("sp",306,1)
    ops.remove("sp",306,2)
    ops.remove("sp",306,3)
    ops.load(306, 0.37495541087973383,0.10790164498392102,99.61095954188764)
if pid == 2:
    ops.load(307, -0.2844930043432431,-0.046771389061485015,95.91948358035364)
    ops.remove('sp',307,1)
    ops.remove('sp',307,2)
    ops.remove('sp',307,3)
if pid == 0:
    ops.remove("sp",307,1)
    ops.remove("sp",307,2)
    ops.remove("sp",307,3)
    ops.load(307, -0.2844930043432431,-0.046771389061485015,95.91948358035364)
if pid == 1:
    ops.load(308, 0.8830357936456464,0.09489998624725215,100.44984897552662)
    ops.remove('sp',308,1)
    ops.remove('sp',308,2)
    ops.remove('sp',308,3)
if pid == 0:
    ops.remove("sp",308,1)
    ops.remove("sp",308,2)
    ops.remove("sp",308,3)
    ops.load(308, 0.8830357936456464,0.09489998624725215,100.44984897552662)
if pid == 2:
    ops.load(308, 0.8830357936456464,0.09489998624725215,100.44984897552662)
    ops.remove('sp',308,1)
    ops.remove('sp',308,2)
    ops.remove('sp',308,3)
if pid == 0:
    ops.remove("sp",308,1)
    ops.remove("sp",308,2)
    ops.remove("sp",308,3)
    ops.load(308, 0.8830357936456464,0.09489998624725215,100.44984897552662)
if pid == 2:
    ops.load(309, -0.2906555688319368,0.05106180621750512,95.93607439347555)
    ops.remove('sp',309,1)
    ops.remove('sp',309,2)
    ops.remove('sp',309,3)
if pid == 0:
    ops.remove("sp",309,1)
    ops.remove("sp",309,2)
    ops.remove("sp",309,3)
    ops.load(309, -0.2906555688319368,0.05106180621750512,95.93607439347555)
if pid == 3:
    ops.load(309, -0.2906555688319368,0.05106180621750512,95.93607439347555)
    ops.remove('sp',309,1)
    ops.remove('sp',309,2)
    ops.remove('sp',309,3)
if pid == 0:
    ops.remove("sp",309,1)
    ops.remove("sp",309,2)
    ops.remove("sp",309,3)
    ops.load(309, -0.2906555688319368,0.05106180621750512,95.93607439347555)
if pid == 1:
    ops.load(310, 0.5026788456866234,-0.03444145055471698,99.75222250099631)
    ops.remove('sp',310,1)
    ops.remove('sp',310,2)
    ops.remove('sp',310,3)
if pid == 0:
    ops.remove("sp",310,1)
    ops.remove("sp",310,2)
    ops.remove("sp",310,3)
    ops.load(310, 0.5026788456866234,-0.03444145055471698,99.75222250099631)
if pid == 3:
    ops.load(310, 0.5026788456866234,-0.03444145055471698,99.75222250099631)
    ops.remove('sp',310,1)
    ops.remove('sp',310,2)
    ops.remove('sp',310,3)
if pid == 0:
    ops.remove("sp",310,1)
    ops.remove("sp",310,2)
    ops.remove("sp",310,3)
    ops.load(310, 0.5026788456866234,-0.03444145055471698,99.75222250099631)
if pid == 3:
    ops.load(311, 0.9377670078164281,19.111645601194493,84.31875528911314)
    ops.remove('sp',311,1)
    ops.remove('sp',311,2)
    ops.remove('sp',311,3)
if pid == 0:
    ops.remove("sp",311,1)
    ops.remove("sp",311,2)
    ops.remove("sp",311,3)
    ops.load(311, 0.9377670078164281,19.111645601194493,84.31875528911314)
if pid == 2:
    ops.load(312, -6.638812619333585,46.022235374647124,81.62674349742584)
    ops.remove('sp',312,1)
    ops.remove('sp',312,2)
    ops.remove('sp',312,3)
if pid == 0:
    ops.remove("sp",312,1)
    ops.remove("sp",312,2)
    ops.remove("sp",312,3)
    ops.load(312, -6.638812619333585,46.022235374647124,81.62674349742584)
if pid == 3:
    ops.load(312, -6.638812619333585,46.022235374647124,81.62674349742584)
    ops.remove('sp',312,1)
    ops.remove('sp',312,2)
    ops.remove('sp',312,3)
if pid == 0:
    ops.remove("sp",312,1)
    ops.remove("sp",312,2)
    ops.remove("sp",312,3)
    ops.load(312, -6.638812619333585,46.022235374647124,81.62674349742584)
if pid == 1:
    ops.load(313, 0.6793322155645612,-5.568919645747057,105.40941817883596)
    ops.remove('sp',313,1)
    ops.remove('sp',313,2)
    ops.remove('sp',313,3)
if pid == 0:
    ops.remove("sp",313,1)
    ops.remove("sp",313,2)
    ops.remove("sp",313,3)
    ops.load(313, 0.6793322155645612,-5.568919645747057,105.40941817883596)
if pid == 1:
    ops.load(314, 3.301005566395015,1.3989312853109446,112.28207763146395)
    ops.remove('sp',314,1)
    ops.remove('sp',314,2)
    ops.remove('sp',314,3)
if pid == 0:
    ops.remove("sp",314,1)
    ops.remove("sp",314,2)
    ops.remove("sp",314,3)
    ops.load(314, 3.301005566395015,1.3989312853109446,112.28207763146395)
if pid == 1:
    ops.load(315, 3.5384379006800195,-0.7661022018584327,112.72080961606451)
    ops.remove('sp',315,1)
    ops.remove('sp',315,2)
    ops.remove('sp',315,3)
if pid == 0:
    ops.remove("sp",315,1)
    ops.remove("sp",315,2)
    ops.remove("sp",315,3)
    ops.load(315, 3.5384379006800195,-0.7661022018584327,112.72080961606451)
if pid == 1:
    ops.load(316, 0.11588033263471509,6.7417693286375435,104.48314777843399)
    ops.remove('sp',316,1)
    ops.remove('sp',316,2)
    ops.remove('sp',316,3)
if pid == 0:
    ops.remove("sp",316,1)
    ops.remove("sp",316,2)
    ops.remove("sp",316,3)
    ops.load(316, 0.11588033263471509,6.7417693286375435,104.48314777843399)
if pid == 2:
    ops.load(316, 0.11588033263471509,6.7417693286375435,104.48314777843399)
    ops.remove('sp',316,1)
    ops.remove('sp',316,2)
    ops.remove('sp',316,3)
if pid == 0:
    ops.remove("sp",316,1)
    ops.remove("sp",316,2)
    ops.remove("sp",316,3)
    ops.load(316, 0.11588033263471509,6.7417693286375435,104.48314777843399)
if pid == 1:
    ops.load(317, 0.8707445521419727,0.6358061887270539,82.47856384667661)
    ops.remove('sp',317,1)
    ops.remove('sp',317,2)
    ops.remove('sp',317,3)
if pid == 0:
    ops.remove("sp",317,1)
    ops.remove("sp",317,2)
    ops.remove("sp",317,3)
    ops.load(317, 0.8707445521419727,0.6358061887270539,82.47856384667661)
if pid == 2:
    ops.load(317, 0.8707445521419727,0.6358061887270539,82.47856384667661)
    ops.remove('sp',317,1)
    ops.remove('sp',317,2)
    ops.remove('sp',317,3)
if pid == 0:
    ops.remove("sp",317,1)
    ops.remove("sp",317,2)
    ops.remove("sp",317,3)
    ops.load(317, 0.8707445521419727,0.6358061887270539,82.47856384667661)
if pid == 1:
    ops.load(318, 0.4015613911587238,0.019188177257983795,95.90826835181582)
    ops.remove('sp',318,1)
    ops.remove('sp',318,2)
    ops.remove('sp',318,3)
if pid == 0:
    ops.remove("sp",318,1)
    ops.remove("sp",318,2)
    ops.remove("sp",318,3)
    ops.load(318, 0.4015613911587238,0.019188177257983795,95.90826835181582)
if pid == 1:
    ops.load(319, -0.6116180689803914,-0.45590719020750214,85.12328654895516)
    ops.remove('sp',319,1)
    ops.remove('sp',319,2)
    ops.remove('sp',319,3)
if pid == 0:
    ops.remove("sp",319,1)
    ops.remove("sp",319,2)
    ops.remove("sp",319,3)
    ops.load(319, -0.6116180689803914,-0.45590719020750214,85.12328654895516)
if pid == 2:
    ops.load(319, -0.6116180689803914,-0.45590719020750214,85.12328654895516)
    ops.remove('sp',319,1)
    ops.remove('sp',319,2)
    ops.remove('sp',319,3)
if pid == 0:
    ops.remove("sp",319,1)
    ops.remove("sp",319,2)
    ops.remove("sp",319,3)
    ops.load(319, -0.6116180689803914,-0.45590719020750214,85.12328654895516)
if pid == 1:
    ops.load(320, 0.42316559081328753,0.005628633593908573,95.91709579976344)
    ops.remove('sp',320,1)
    ops.remove('sp',320,2)
    ops.remove('sp',320,3)
if pid == 0:
    ops.remove("sp",320,1)
    ops.remove("sp",320,2)
    ops.remove("sp",320,3)
    ops.load(320, 0.42316559081328753,0.005628633593908573,95.91709579976344)
if pid == 1:
    ops.load(321, -0.3397686007675562,-0.43516553137612646,85.92200645977687)
    ops.remove('sp',321,1)
    ops.remove('sp',321,2)
    ops.remove('sp',321,3)
if pid == 0:
    ops.remove("sp",321,1)
    ops.remove("sp",321,2)
    ops.remove("sp",321,3)
    ops.load(321, -0.3397686007675562,-0.43516553137612646,85.92200645977687)
if pid == 3:
    ops.load(321, -0.3397686007675562,-0.43516553137612646,85.92200645977687)
    ops.remove('sp',321,1)
    ops.remove('sp',321,2)
    ops.remove('sp',321,3)
if pid == 0:
    ops.remove("sp",321,1)
    ops.remove("sp",321,2)
    ops.remove("sp",321,3)
    ops.load(321, -0.3397686007675562,-0.43516553137612646,85.92200645977687)
if pid == 1:
    ops.load(322, 0.43892180011705934,0.015576822702355112,95.94387396068639)
    ops.remove('sp',322,1)
    ops.remove('sp',322,2)
    ops.remove('sp',322,3)
if pid == 0:
    ops.remove("sp",322,1)
    ops.remove("sp",322,2)
    ops.remove("sp",322,3)
    ops.load(322, 0.43892180011705934,0.015576822702355112,95.94387396068639)
if pid == 2:
    ops.load(322, 0.43892180011705934,0.015576822702355112,95.94387396068639)
    ops.remove('sp',322,1)
    ops.remove('sp',322,2)
    ops.remove('sp',322,3)
if pid == 0:
    ops.remove("sp",322,1)
    ops.remove("sp",322,2)
    ops.remove("sp",322,3)
    ops.load(322, 0.43892180011705934,0.015576822702355112,95.94387396068639)
if pid == 2:
    ops.load(323, -0.4175443514698859,0.43586349190902185,84.40371338824087)
    ops.remove('sp',323,1)
    ops.remove('sp',323,2)
    ops.remove('sp',323,3)
if pid == 0:
    ops.remove("sp",323,1)
    ops.remove("sp",323,2)
    ops.remove("sp",323,3)
    ops.load(323, -0.4175443514698859,0.43586349190902185,84.40371338824087)
if pid == 3:
    ops.load(323, -0.4175443514698859,0.43586349190902185,84.40371338824087)
    ops.remove('sp',323,1)
    ops.remove('sp',323,2)
    ops.remove('sp',323,3)
if pid == 0:
    ops.remove("sp",323,1)
    ops.remove("sp",323,2)
    ops.remove("sp",323,3)
    ops.load(323, -0.4175443514698859,0.43586349190902185,84.40371338824087)
if pid == 2:
    ops.load(324, 0.396593326824428,0.09980912908672647,95.55080236334537)
    ops.remove('sp',324,1)
    ops.remove('sp',324,2)
    ops.remove('sp',324,3)
if pid == 0:
    ops.remove("sp",324,1)
    ops.remove("sp",324,2)
    ops.remove("sp",324,3)
    ops.load(324, 0.396593326824428,0.09980912908672647,95.55080236334537)
if pid == 2:
    ops.load(325, 0.02912295853691349,-0.7630149904887413,86.73593494974472)
    ops.remove('sp',325,1)
    ops.remove('sp',325,2)
    ops.remove('sp',325,3)
if pid == 0:
    ops.remove("sp",325,1)
    ops.remove("sp",325,2)
    ops.remove("sp",325,3)
    ops.load(325, 0.02912295853691349,-0.7630149904887413,86.73593494974472)
if pid == 3:
    ops.load(325, 0.02912295853691349,-0.7630149904887413,86.73593494974472)
    ops.remove('sp',325,1)
    ops.remove('sp',325,2)
    ops.remove('sp',325,3)
if pid == 0:
    ops.remove("sp",325,1)
    ops.remove("sp",325,2)
    ops.remove("sp",325,3)
    ops.load(325, 0.02912295853691349,-0.7630149904887413,86.73593494974472)
if pid == 2:
    ops.load(326, -11.042976018026504,2.7246985470334475,68.788257123952)
    ops.remove('sp',326,1)
    ops.remove('sp',326,2)
    ops.remove('sp',326,3)
if pid == 0:
    ops.remove("sp",326,1)
    ops.remove("sp",326,2)
    ops.remove("sp",326,3)
    ops.load(326, -11.042976018026504,2.7246985470334475,68.788257123952)
if pid == 4:
    ops.load(326, -11.042976018026504,2.7246985470334475,68.788257123952)
    ops.remove('sp',326,1)
    ops.remove('sp',326,2)
    ops.remove('sp',326,3)
if pid == 0:
    ops.remove("sp",326,1)
    ops.remove("sp",326,2)
    ops.remove("sp",326,3)
    ops.load(326, -11.042976018026504,2.7246985470334475,68.788257123952)
if pid == 2:
    ops.load(327, -1.6438183903667865,-0.7747553357705996,53.341758870057134)
    ops.remove('sp',327,1)
    ops.remove('sp',327,2)
    ops.remove('sp',327,3)
if pid == 0:
    ops.remove("sp",327,1)
    ops.remove("sp",327,2)
    ops.remove("sp",327,3)
    ops.load(327, -1.6438183903667865,-0.7747553357705996,53.341758870057134)
if pid == 2:
    ops.load(328, -10.239214948067676,-3.1886249073778314,54.37079636348311)
    ops.remove('sp',328,1)
    ops.remove('sp',328,2)
    ops.remove('sp',328,3)
if pid == 0:
    ops.remove("sp",328,1)
    ops.remove("sp",328,2)
    ops.remove("sp",328,3)
    ops.load(328, -10.239214948067676,-3.1886249073778314,54.37079636348311)
if pid == 4:
    ops.load(328, -10.239214948067676,-3.1886249073778314,54.37079636348311)
    ops.remove('sp',328,1)
    ops.remove('sp',328,2)
    ops.remove('sp',328,3)
if pid == 0:
    ops.remove("sp",328,1)
    ops.remove("sp",328,2)
    ops.remove("sp",328,3)
    ops.load(328, -10.239214948067676,-3.1886249073778314,54.37079636348311)
if pid == 2:
    ops.load(329, -2.857814263527625,-2.129281732727624,66.2040977169234)
    ops.remove('sp',329,1)
    ops.remove('sp',329,2)
    ops.remove('sp',329,3)
if pid == 0:
    ops.remove("sp",329,1)
    ops.remove("sp",329,2)
    ops.remove("sp",329,3)
    ops.load(329, -2.857814263527625,-2.129281732727624,66.2040977169234)
if pid == 3:
    ops.load(329, -2.857814263527625,-2.129281732727624,66.2040977169234)
    ops.remove('sp',329,1)
    ops.remove('sp',329,2)
    ops.remove('sp',329,3)
if pid == 0:
    ops.remove("sp",329,1)
    ops.remove("sp",329,2)
    ops.remove("sp",329,3)
    ops.load(329, -2.857814263527625,-2.129281732727624,66.2040977169234)
if pid == 3:
    ops.load(330, -8.30369581898449,-1.3069743275854249,60.908982292606865)
    ops.remove('sp',330,1)
    ops.remove('sp',330,2)
    ops.remove('sp',330,3)
if pid == 0:
    ops.remove("sp",330,1)
    ops.remove("sp",330,2)
    ops.remove("sp",330,3)
    ops.load(330, -8.30369581898449,-1.3069743275854249,60.908982292606865)
if pid == 4:
    ops.load(330, -8.30369581898449,-1.3069743275854249,60.908982292606865)
    ops.remove('sp',330,1)
    ops.remove('sp',330,2)
    ops.remove('sp',330,3)
if pid == 0:
    ops.remove("sp",330,1)
    ops.remove("sp",330,2)
    ops.remove("sp",330,3)
    ops.load(330, -8.30369581898449,-1.3069743275854249,60.908982292606865)
if pid == 3:
    ops.load(331, -2.477977052893494,0.3863205506569791,65.85120261812267)
    ops.remove('sp',331,1)
    ops.remove('sp',331,2)
    ops.remove('sp',331,3)
if pid == 0:
    ops.remove("sp",331,1)
    ops.remove("sp",331,2)
    ops.remove("sp",331,3)
    ops.load(331, -2.477977052893494,0.3863205506569791,65.85120261812267)
if pid == 3:
    ops.load(332, -7.898812558555083,2.171804450791853,58.90401227671683)
    ops.remove('sp',332,1)
    ops.remove('sp',332,2)
    ops.remove('sp',332,3)
if pid == 0:
    ops.remove("sp",332,1)
    ops.remove("sp",332,2)
    ops.remove("sp",332,3)
    ops.load(332, -7.898812558555083,2.171804450791853,58.90401227671683)
if pid == 4:
    ops.load(332, -7.898812558555083,2.171804450791853,58.90401227671683)
    ops.remove('sp',332,1)
    ops.remove('sp',332,2)
    ops.remove('sp',332,3)
if pid == 0:
    ops.remove("sp",332,1)
    ops.remove("sp",332,2)
    ops.remove("sp",332,3)
    ops.load(332, -7.898812558555083,2.171804450791853,58.90401227671683)
if pid == 3:
    ops.load(333, -1.253496755320053,-2.682941213722291,58.33439849891144)
    ops.remove('sp',333,1)
    ops.remove('sp',333,2)
    ops.remove('sp',333,3)
if pid == 0:
    ops.remove("sp",333,1)
    ops.remove("sp",333,2)
    ops.remove("sp",333,3)
    ops.load(333, -1.253496755320053,-2.682941213722291,58.33439849891144)
if pid == 3:
    ops.load(334, -7.468307420581652,-11.966425673650441,71.13524174364949)
    ops.remove('sp',334,1)
    ops.remove('sp',334,2)
    ops.remove('sp',334,3)
if pid == 0:
    ops.remove("sp",334,1)
    ops.remove("sp",334,2)
    ops.remove("sp",334,3)
    ops.load(334, -7.468307420581652,-11.966425673650441,71.13524174364949)
if pid == 5:
    ops.load(334, -7.468307420581652,-11.966425673650441,71.13524174364949)
    ops.remove('sp',334,1)
    ops.remove('sp',334,2)
    ops.remove('sp',334,3)
if pid == 0:
    ops.remove("sp",334,1)
    ops.remove("sp",334,2)
    ops.remove("sp",334,3)
    ops.load(334, -7.468307420581652,-11.966425673650441,71.13524174364949)
if pid == 4:
    ops.load(335, -35.48475346079242,-3.1488430924960484,44.22162517638373)
    ops.remove('sp',335,1)
    ops.remove('sp',335,2)
    ops.remove('sp',335,3)
if pid == 0:
    ops.remove("sp",335,1)
    ops.remove("sp",335,2)
    ops.remove("sp",335,3)
    ops.load(335, -35.48475346079242,-3.1488430924960484,44.22162517638373)
if pid == 5:
    ops.load(335, -35.48475346079242,-3.1488430924960484,44.22162517638373)
    ops.remove('sp',335,1)
    ops.remove('sp',335,2)
    ops.remove('sp',335,3)
if pid == 0:
    ops.remove("sp",335,1)
    ops.remove("sp",335,2)
    ops.remove("sp",335,3)
    ops.load(335, -35.48475346079242,-3.1488430924960484,44.22162517638373)
if pid == 4:
    ops.load(336, -11.64584994120801,2.251297519711013,49.10653747903)
    ops.remove('sp',336,1)
    ops.remove('sp',336,2)
    ops.remove('sp',336,3)
if pid == 0:
    ops.remove("sp",336,1)
    ops.remove("sp",336,2)
    ops.remove("sp",336,3)
    ops.load(336, -11.64584994120801,2.251297519711013,49.10653747903)
if pid == 4:
    ops.load(337, -39.718048286099716,-6.300828083536809,31.354328419161376)
    ops.remove('sp',337,1)
    ops.remove('sp',337,2)
    ops.remove('sp',337,3)
if pid == 0:
    ops.remove("sp",337,1)
    ops.remove("sp",337,2)
    ops.remove("sp",337,3)
    ops.load(337, -39.718048286099716,-6.300828083536809,31.354328419161376)
if pid == 5:
    ops.load(337, -39.718048286099716,-6.300828083536809,31.354328419161376)
    ops.remove('sp',337,1)
    ops.remove('sp',337,2)
    ops.remove('sp',337,3)
if pid == 0:
    ops.remove("sp",337,1)
    ops.remove("sp",337,2)
    ops.remove("sp",337,3)
    ops.load(337, -39.718048286099716,-6.300828083536809,31.354328419161376)
if pid == 4:
    ops.load(338, -17.003195512613765,-4.213046305495439,55.27188084446914)
    ops.remove('sp',338,1)
    ops.remove('sp',338,2)
    ops.remove('sp',338,3)
if pid == 0:
    ops.remove("sp",338,1)
    ops.remove("sp",338,2)
    ops.remove("sp",338,3)
    ops.load(338, -17.003195512613765,-4.213046305495439,55.27188084446914)
if pid == 4:
    ops.load(339, -31.279353023627973,-1.670755494244121,36.270961835930244)
    ops.remove('sp',339,1)
    ops.remove('sp',339,2)
    ops.remove('sp',339,3)
if pid == 0:
    ops.remove("sp",339,1)
    ops.remove("sp",339,2)
    ops.remove("sp",339,3)
    ops.load(339, -31.279353023627973,-1.670755494244121,36.270961835930244)
if pid == 5:
    ops.load(339, -31.279353023627973,-1.670755494244121,36.270961835930244)
    ops.remove('sp',339,1)
    ops.remove('sp',339,2)
    ops.remove('sp',339,3)
if pid == 0:
    ops.remove("sp",339,1)
    ops.remove("sp",339,2)
    ops.remove("sp",339,3)
    ops.load(339, -31.279353023627973,-1.670755494244121,36.270961835930244)
if pid == 4:
    ops.load(340, -14.670965058804917,1.1030230969640797,56.49077434897421)
    ops.remove('sp',340,1)
    ops.remove('sp',340,2)
    ops.remove('sp',340,3)
if pid == 0:
    ops.remove("sp",340,1)
    ops.remove("sp",340,2)
    ops.remove("sp",340,3)
    ops.load(340, -14.670965058804917,1.1030230969640797,56.49077434897421)
if pid == 4:
    ops.load(341, -32.339239636138174,3.5738134991897295,34.15053847514329)
    ops.remove('sp',341,1)
    ops.remove('sp',341,2)
    ops.remove('sp',341,3)
if pid == 0:
    ops.remove("sp",341,1)
    ops.remove("sp",341,2)
    ops.remove("sp",341,3)
    ops.load(341, -32.339239636138174,3.5738134991897295,34.15053847514329)
if pid == 6:
    ops.load(341, -32.339239636138174,3.5738134991897295,34.15053847514329)
    ops.remove('sp',341,1)
    ops.remove('sp',341,2)
    ops.remove('sp',341,3)
if pid == 0:
    ops.remove("sp",341,1)
    ops.remove("sp",341,2)
    ops.remove("sp",341,3)
    ops.load(341, -32.339239636138174,3.5738134991897295,34.15053847514329)
if pid == 4:
    ops.load(342, -9.050780122146914,-9.422656499843232,53.08120721620925)
    ops.remove('sp',342,1)
    ops.remove('sp',342,2)
    ops.remove('sp',342,3)
if pid == 0:
    ops.remove("sp",342,1)
    ops.remove("sp",342,2)
    ops.remove("sp",342,3)
    ops.load(342, -9.050780122146914,-9.422656499843232,53.08120721620925)
if pid == 5:
    ops.load(342, -9.050780122146914,-9.422656499843232,53.08120721620925)
    ops.remove('sp',342,1)
    ops.remove('sp',342,2)
    ops.remove('sp',342,3)
if pid == 0:
    ops.remove("sp",342,1)
    ops.remove("sp",342,2)
    ops.remove("sp",342,3)
    ops.load(342, -9.050780122146914,-9.422656499843232,53.08120721620925)
if pid == 5:
    ops.load(343, -26.07342419001266,-21.352520101912702,46.73428394191619)
    ops.remove('sp',343,1)
    ops.remove('sp',343,2)
    ops.remove('sp',343,3)
if pid == 0:
    ops.remove("sp",343,1)
    ops.remove("sp",343,2)
    ops.remove("sp",343,3)
    ops.load(343, -26.07342419001266,-21.352520101912702,46.73428394191619)
if pid == 6:
    ops.load(343, -26.07342419001266,-21.352520101912702,46.73428394191619)
    ops.remove('sp',343,1)
    ops.remove('sp',343,2)
    ops.remove('sp',343,3)
if pid == 0:
    ops.remove("sp",343,1)
    ops.remove("sp",343,2)
    ops.remove("sp",343,3)
    ops.load(343, -26.07342419001266,-21.352520101912702,46.73428394191619)
if pid == 5:
    ops.load(344, -87.77827398948452,30.896934252200733,103.43206567940375)
    ops.remove('sp',344,1)
    ops.remove('sp',344,2)
    ops.remove('sp',344,3)
if pid == 0:
    ops.remove("sp",344,1)
    ops.remove("sp",344,2)
    ops.remove("sp",344,3)
    ops.load(344, -87.77827398948452,30.896934252200733,103.43206567940375)
if pid == 6:
    ops.load(344, -87.77827398948452,30.896934252200733,103.43206567940375)
    ops.remove('sp',344,1)
    ops.remove('sp',344,2)
    ops.remove('sp',344,3)
if pid == 0:
    ops.remove("sp",344,1)
    ops.remove("sp",344,2)
    ops.remove("sp",344,3)
    ops.load(344, -87.77827398948452,30.896934252200733,103.43206567940375)
if pid == 5:
    ops.load(345, -43.89954199399177,-15.009317608369926,-7.694009229800651)
    ops.remove('sp',345,1)
    ops.remove('sp',345,2)
    ops.remove('sp',345,3)
if pid == 0:
    ops.remove("sp",345,1)
    ops.remove("sp",345,2)
    ops.remove("sp",345,3)
    ops.load(345, -43.89954199399177,-15.009317608369926,-7.694009229800651)
if pid == 5:
    ops.load(346, -32.160954956714434,-3.5054997320388996,16.525435220866484)
    ops.remove('sp',346,1)
    ops.remove('sp',346,2)
    ops.remove('sp',346,3)
if pid == 0:
    ops.remove("sp",346,1)
    ops.remove("sp",346,2)
    ops.remove("sp",346,3)
    ops.load(346, -32.160954956714434,-3.5054997320388996,16.525435220866484)
if pid == 7:
    ops.load(346, -32.160954956714434,-3.5054997320388996,16.525435220866484)
    ops.remove('sp',346,1)
    ops.remove('sp',346,2)
    ops.remove('sp',346,3)
if pid == 0:
    ops.remove("sp",346,1)
    ops.remove("sp",346,2)
    ops.remove("sp",346,3)
    ops.load(346, -32.160954956714434,-3.5054997320388996,16.525435220866484)
if pid == 5:
    ops.load(347, -51.573753841436755,-2.8355446796095407,10.68391676377301)
    ops.remove('sp',347,1)
    ops.remove('sp',347,2)
    ops.remove('sp',347,3)
if pid == 0:
    ops.remove("sp",347,1)
    ops.remove("sp",347,2)
    ops.remove("sp",347,3)
    ops.load(347, -51.573753841436755,-2.8355446796095407,10.68391676377301)
if pid == 5:
    ops.load(348, -26.333280733704825,1.4847478555443854,31.402772117034885)
    ops.remove('sp',348,1)
    ops.remove('sp',348,2)
    ops.remove('sp',348,3)
if pid == 0:
    ops.remove("sp",348,1)
    ops.remove("sp",348,2)
    ops.remove("sp",348,3)
    ops.load(348, -26.333280733704825,1.4847478555443854,31.402772117034885)
if pid == 7:
    ops.load(348, -26.333280733704825,1.4847478555443854,31.402772117034885)
    ops.remove('sp',348,1)
    ops.remove('sp',348,2)
    ops.remove('sp',348,3)
if pid == 0:
    ops.remove("sp",348,1)
    ops.remove("sp",348,2)
    ops.remove("sp",348,3)
    ops.load(348, -26.333280733704825,1.4847478555443854,31.402772117034885)
if pid == 5:
    ops.load(349, -47.59026032784793,1.6942826631646213,11.832991921800495)
    ops.remove('sp',349,1)
    ops.remove('sp',349,2)
    ops.remove('sp',349,3)
if pid == 0:
    ops.remove("sp",349,1)
    ops.remove("sp",349,2)
    ops.remove("sp",349,3)
    ops.load(349, -47.59026032784793,1.6942826631646213,11.832991921800495)
if pid == 6:
    ops.load(349, -47.59026032784793,1.6942826631646213,11.832991921800495)
    ops.remove('sp',349,1)
    ops.remove('sp',349,2)
    ops.remove('sp',349,3)
if pid == 0:
    ops.remove("sp",349,1)
    ops.remove("sp",349,2)
    ops.remove("sp",349,3)
    ops.load(349, -47.59026032784793,1.6942826631646213,11.832991921800495)
if pid == 6:
    ops.load(350, -25.662859639022336,4.339880793018994,21.31398342839165)
    ops.remove('sp',350,1)
    ops.remove('sp',350,2)
    ops.remove('sp',350,3)
if pid == 0:
    ops.remove("sp",350,1)
    ops.remove("sp",350,2)
    ops.remove("sp",350,3)
    ops.load(350, -25.662859639022336,4.339880793018994,21.31398342839165)
if pid == 7:
    ops.load(350, -25.662859639022336,4.339880793018994,21.31398342839165)
    ops.remove('sp',350,1)
    ops.remove('sp',350,2)
    ops.remove('sp',350,3)
if pid == 0:
    ops.remove("sp",350,1)
    ops.remove("sp",350,2)
    ops.remove("sp",350,3)
    ops.load(350, -25.662859639022336,4.339880793018994,21.31398342839165)
if pid == 6:
    ops.load(351, -38.13106355062108,-12.230697419840226,0.2237144504464954)
    ops.remove('sp',351,1)
    ops.remove('sp',351,2)
    ops.remove('sp',351,3)
if pid == 0:
    ops.remove("sp",351,1)
    ops.remove("sp",351,2)
    ops.remove("sp",351,3)
    ops.load(351, -38.13106355062108,-12.230697419840226,0.2237144504464954)
if pid == 6:
    ops.load(352, -58.19896033172557,-34.945232733482094,27.760006069971382)
    ops.remove('sp',352,1)
    ops.remove('sp',352,2)
    ops.remove('sp',352,3)
if pid == 0:
    ops.remove("sp",352,1)
    ops.remove("sp",352,2)
    ops.remove("sp",352,3)
    ops.load(352, -58.19896033172557,-34.945232733482094,27.760006069971382)
if pid == 7:
    ops.load(352, -58.19896033172557,-34.945232733482094,27.760006069971382)
    ops.remove('sp',352,1)
    ops.remove('sp',352,2)
    ops.remove('sp',352,3)
if pid == 0:
    ops.remove("sp",352,1)
    ops.remove("sp",352,2)
    ops.remove("sp",352,3)
    ops.load(352, -58.19896033172557,-34.945232733482094,27.760006069971382)
if pid == 6:
    ops.load(353, -210.56630119070792,63.62100132641757,372.0553491129581)
    ops.remove('sp',353,1)
    ops.remove('sp',353,2)
    ops.remove('sp',353,3)
if pid == 0:
    ops.remove("sp",353,1)
    ops.remove("sp",353,2)
    ops.remove("sp",353,3)
    ops.load(353, -210.56630119070792,63.62100132641757,372.0553491129581)
if pid == 7:
    ops.load(353, -210.56630119070792,63.62100132641757,372.0553491129581)
    ops.remove('sp',353,1)
    ops.remove('sp',353,2)
    ops.remove('sp',353,3)
if pid == 0:
    ops.remove("sp",353,1)
    ops.remove("sp",353,2)
    ops.remove("sp",353,3)
    ops.load(353, -210.56630119070792,63.62100132641757,372.0553491129581)
if pid == 7:
    ops.load(354, -225.08281757154725,-5.786008148083013,361.7877536351066)
    ops.remove('sp',354,1)
    ops.remove('sp',354,2)
    ops.remove('sp',354,3)
if pid == 0:
    ops.remove("sp",354,1)
    ops.remove("sp",354,2)
    ops.remove("sp",354,3)
    ops.load(354, -225.08281757154725,-5.786008148083013,361.7877536351066)
if pid == 7:
    ops.load(355, -219.21037448784568,5.247044967857121,369.7372606001893)
    ops.remove('sp',355,1)
    ops.remove('sp',355,2)
    ops.remove('sp',355,3)
if pid == 0:
    ops.remove("sp",355,1)
    ops.remove("sp",355,2)
    ops.remove("sp",355,3)
    ops.load(355, -219.21037448784568,5.247044967857121,369.7372606001893)
if pid == 7:
    ops.load(356, -229.3794617402766,-19.785336495140342,387.22518855059263)
    ops.remove('sp',356,1)
    ops.remove('sp',356,2)
    ops.remove('sp',356,3)
if pid == 0:
    ops.remove("sp",356,1)
    ops.remove("sp",356,2)
    ops.remove("sp",356,3)
    ops.load(356, -229.3794617402766,-19.785336495140342,387.22518855059263)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(1, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(2, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(3, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(4, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(5, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(6, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(7, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(8, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(9, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(10, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(11, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(12, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(13, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(14, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(15, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(16, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(17, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(18, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(19, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(20, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(21, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(22, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(23, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(24, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(25, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(26, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(27, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(28, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(29, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(30, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(31, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 1, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 3, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 5, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 7, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 13, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 14, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 15, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 16, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 29, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 30, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 31, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(32, 32, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(33, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(34, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(35, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(36, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(37, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(38, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(39, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 2, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 4, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 6, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 8, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 21, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 22, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 23, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 24, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 37, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 38, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 39, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(40, 40, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(57, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(58, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(59, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(60, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(61, 61, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(61, 81, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(62, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(63, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(64, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(65, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(66, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(67, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(68, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(69, 69, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(69, 73, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(70, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(71, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(72, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(73, 69, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(73, 73, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(74, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(75, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 12, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 20, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 28, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 36, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 70, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 71, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 72, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 74, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 75, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(76, 76, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(77, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(78, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(79, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 11, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 19, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 27, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 35, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 65, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 66, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 67, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 68, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 77, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 78, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 79, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(80, 80, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(81, 61, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(81, 81, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(82, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(83, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 10, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 18, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 26, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 34, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 62, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 63, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 64, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 82, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 83, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(84, 84, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(85, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(86, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(87, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 9, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 17, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 25, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 33, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 57, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 58, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 59, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 60, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 85, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 86, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 87, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(88, 88, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(217, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(218, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(219, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(220, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(221, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(222, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(223, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(224, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(225, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(226, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(227, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(228, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(229, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(230, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(231, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(232, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(233, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(234, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(235, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(236, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(237, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(238, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(239, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(240, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(241, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(242, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(243, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(244, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(245, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 222, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 223, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 224, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 225, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 226, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 242, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 243, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 244, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 245, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(246, 246, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(247, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(248, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(249, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(250, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(251, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(252, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(253, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(254, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(255, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 232, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 233, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 234, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 235, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 236, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 252, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 253, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 254, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 255, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(256, 256, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(277, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(278, 278, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(279, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(280, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(281, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(282, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(283, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(284, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(285, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(286, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(287, 287, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(288, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(289, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(290, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(291, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(292, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(293, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(294, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(295, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(296, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(297, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(298, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(299, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(300, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(301, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(302, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(303, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(304, 304, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(304, 306, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(304, 317, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(304, 319, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(305, 305, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(305, 327, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(306, 304, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(306, 306, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(306, 317, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(306, 319, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(307, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(308, 308, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(308, 310, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(308, 312, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(308, 321, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(308, 323, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(308, 325, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(309, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(310, 308, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(310, 310, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(310, 312, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(310, 321, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(310, 323, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(310, 325, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(311, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(312, 308, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(312, 310, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(312, 312, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(312, 321, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(312, 323, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(312, 325, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(313, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(314, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(315, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(316, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(317, 304, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(317, 306, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(317, 317, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(317, 319, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(318, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(319, 304, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(319, 306, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(319, 317, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(319, 319, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(320, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(321, 308, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(321, 310, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(321, 312, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(321, 321, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(321, 323, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(321, 325, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(322, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(323, 308, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(323, 310, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(323, 312, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(323, 321, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(323, 323, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(323, 325, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 221, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 231, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 241, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 251, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 313, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 314, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 315, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 316, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 318, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 320, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 322, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(324, 324, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(325, 308, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(325, 310, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(325, 312, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(325, 321, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(325, 323, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(325, 325, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(326, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(327, 305, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(327, 327, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(328, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(329, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(330, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(331, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(332, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 220, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 230, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 240, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 250, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 307, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 309, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 311, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 329, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 331, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(333, 333, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 295, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 297, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 299, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 301, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 303, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 326, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 328, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 330, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 332, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(334, 334, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(335, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(336, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(337, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(338, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(339, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(340, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(341, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 219, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 229, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 239, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 249, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 296, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 298, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 300, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 302, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 336, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 338, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 340, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(342, 342, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 286, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 288, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 290, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 292, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 294, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 335, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 337, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 339, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 341, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(343, 343, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(344, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(345, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(346, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(347, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(348, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(349, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(350, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 218, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 228, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 238, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 248, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 289, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 291, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 293, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 345, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 347, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 349, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(351, 351, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 277, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 279, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 281, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 283, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 285, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 344, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 346, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 348, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 350, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(352, 352, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(353, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(354, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(355, 356, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 217, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 227, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 237, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 247, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 280, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 282, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 284, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 353, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 354, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 355, *DOF)
if pid == 0:
    DOF = [1, 2]
    ops.equalDOF(356, 356, *DOF)
cFactor = 22500000.0
ops.model('basic', '-ndm', 3, '-ndf', 4)
ops.setTime(0.0)
ops.wipeAnalysis()
ops.remove('recorders')
velocityFile = 'yerbaNSvelocity'
data_gm = nup.loadtxt('yerbaNSvelocity.out')
ops.timeSeries('Path', 2, '-dt', 0.005, '-filePath', velocityFile +'.out', '-factor', 22500000.0)
ops.pattern('Plain', 10, 2)
if pid == 7:
    ops.load(458, 1.0,0.0, 0.0)
if pid == 1:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',1,519,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',1,519,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',1,519,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',45,522,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',45,522,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',45,522,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',46,525,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',46,525,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',46,525,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',47,528,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',47,528,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',47,528,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',5,529,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',5,529,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',5,529,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',13,532,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',13,532,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',13,532,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',145,535,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',145,535,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',145,535,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',146,538,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',146,538,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',146,538,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',147,541,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',147,541,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',147,541,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',29,542,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',29,542,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',29,542,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',14,545,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',14,545,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',14,545,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',141,548,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',141,548,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',141,548,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',142,551,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',142,551,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',142,551,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',143,554,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',143,554,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',143,554,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',30,555,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',30,555,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',30,555,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',15,558,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',15,558,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',15,558,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',137,561,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',137,561,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',137,561,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',138,564,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',138,564,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',138,564,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 211,228,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 211,228,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 211,228,'material','1','strain')
if pid == 2:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',139,567,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',139,567,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',139,567,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',31,568,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',31,568,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',31,568,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',3,569,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',3,569,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',3,569,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',53,570,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',53,570,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',53,570,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',54,571,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',54,571,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',54,571,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',55,572,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',55,572,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',55,572,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',7,572,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',7,572,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',7,572,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',11,575,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',11,575,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',11,575,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',91,578,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',91,578,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',91,578,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',95,581,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',95,581,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',95,581,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',99,584,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',99,584,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',99,584,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',27,585,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',27,585,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',27,585,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',65,588,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',65,588,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',65,588,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',153,591,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',153,591,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',153,591,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',154,594,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',154,594,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',154,594,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',155,597,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',155,597,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',155,597,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',73,598,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',73,598,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',73,598,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',66,601,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',66,601,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',66,601,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 229,246,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 229,246,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 229,246,'material','1','strain')
if pid == 3:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',157,604,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',157,604,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',157,604,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',158,607,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',158,607,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',158,607,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',159,610,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',159,610,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',159,610,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',74,611,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',74,611,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',74,611,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',67,614,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',67,614,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',67,614,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',161,617,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',161,617,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',161,617,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',162,620,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',162,620,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',162,620,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',163,623,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',163,623,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',163,623,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',75,624,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',75,624,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',75,624,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',19,625,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',19,625,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',19,625,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',115,626,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',115,626,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',115,626,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',111,627,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',111,627,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',111,627,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',107,628,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',107,628,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',107,628,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',35,628,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',35,628,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',35,628,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',10,631,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',10,631,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',10,631,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',90,634,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',90,634,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',90,634,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',94,637,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',94,637,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',94,637,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',98,640,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',98,640,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',98,640,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 247,264,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 247,264,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 247,264,'material','1','strain')
if pid == 4:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',26,641,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',26,641,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',26,641,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',61,644,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',61,644,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',61,644,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',169,647,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',169,647,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',169,647,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',170,650,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',170,650,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',170,650,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',171,653,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',171,653,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',171,653,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',77,654,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',77,654,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',77,654,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',62,657,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',62,657,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',62,657,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',173,660,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',173,660,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',173,660,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',174,663,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',174,663,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',174,663,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',175,666,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',175,666,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',175,666,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',78,667,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',78,667,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',78,667,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',63,670,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',63,670,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',63,670,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',177,673,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',177,673,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',177,673,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',178,676,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',178,676,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',178,676,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',179,679,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',179,679,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',179,679,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',79,680,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',79,680,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',79,680,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',18,681,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',18,681,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',18,681,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',114,682,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',114,682,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',114,682,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 265,282,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 265,282,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 265,282,'material','1','strain')
if pid == 5:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',110,683,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',110,683,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',110,683,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',106,684,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',106,684,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',106,684,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',34,684,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',34,684,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',34,684,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',9,687,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',9,687,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',9,687,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',89,690,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',89,690,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',89,690,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',93,693,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',93,693,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',93,693,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',97,696,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',97,696,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',97,696,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',25,697,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',25,697,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',25,697,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',57,700,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',57,700,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',57,700,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',185,703,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',185,703,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',185,703,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',186,706,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',186,706,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',186,706,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',187,709,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',187,709,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',187,709,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',81,710,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',81,710,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',81,710,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',58,713,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',58,713,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',58,713,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',189,716,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',189,716,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',189,716,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',190,719,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',190,719,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',190,719,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',191,722,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',191,722,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',191,722,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',82,723,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',82,723,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',82,723,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 283,300,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 283,300,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 283,300,'material','1','strain')
if pid == 6:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',59,726,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',59,726,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',59,726,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',193,729,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',193,729,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',193,729,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',194,732,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',194,732,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',194,732,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',195,735,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',195,735,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',195,735,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',83,736,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',83,736,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',83,736,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',17,737,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',17,737,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',17,737,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',113,738,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',113,738,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',113,738,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',109,739,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',109,739,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',109,739,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',105,740,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',105,740,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',105,740,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',33,740,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',33,740,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',33,740,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',2,741,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',2,741,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',2,741,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',41,742,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',41,742,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',41,742,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',42,743,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',42,743,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',42,743,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',43,744,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',43,744,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',43,744,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',6,744,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',6,744,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',6,744,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',21,745,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',21,745,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',21,745,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',121,746,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',121,746,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',121,746,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',122,747,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',122,747,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',122,747,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 301,318,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 301,318,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 301,318,'material','1','strain')
if pid == 7:
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',123,748,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',123,748,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',123,748,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',37,748,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',37,748,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',37,748,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',22,749,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',22,749,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',22,749,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',125,750,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',125,750,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',125,750,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',126,751,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',126,751,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',126,751,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',127,752,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',127,752,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',127,752,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',38,752,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',38,752,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',38,752,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',23,753,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',23,753,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',23,753,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',129,754,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',129,754,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',129,754,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',130,755,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',130,755,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',130,755,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',131,756,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',131,756,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',131,756,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',39,756,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',39,756,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',39,756,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',4,753,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',4,753,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',4,753,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',49,754,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',49,754,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',49,754,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',50,755,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',50,755,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',50,755,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',51,756,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',51,756,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',51,756,'-dof', 4, 'vel')
    ops.recorder('Node','-file','displacement.out','-time', '-dT',recDT,'-nodeRange',8,756,'-dof', 1, 2,3, 'disp')
    ops.recorder('Node','-file','acceleration.out','-time', '-dT',recDT,'-nodeRange',8,756,'-dof', 1, 2,3, 'accel')
    ops.recorder('Node','-file','porePressure.out','-time', '-dT',recDT,'-nodeRange',8,756,'-dof', 4, 'vel')
    ops.recorder('Element','-file','stress.out','-time','-eleRange', 319,335,'material','1','stress')
    ops.recorder('Element','-file','gauss.out','-time','-eleRange', 319,335,'material','1','gausspoint')
    ops.recorder('Element','-file','strain.out','-time','-eleRange', 319,335,'material','1','strain')
ops.barrier()
print('dynamic phase')
#ops.partition('-ncuts',8)
ops.constraints('Penalty', 1.0E16, 1.0E16)
ops.test('NormDispIncr', 1e-3, 100, 1)
ops.algorithm('KrylovNewton')
ops.numberer('ParallelRCM')
ops.system('Mumps')
ops.integrator('Newmark', 1.5, 1.0)
ops.rayleigh(0.049767804413303654, 0.000315158303152268, 0.0, 0.0)
ops.analysis('Transient')
ok = ops.analyze(nSteps, dT)
if ok != 0:
    print('did not converge, reducing time step')
    curTime = ops.getTime()
    mTime = curTime
    print('curTime: ', curTime)
    curStep = curTime / dT
    print('curStep: ', curStep)
    rStep = (nSteps - curStep) * 2.0
    remStep = int((nSteps - curStep) * 2.0)
    print('remStep: ', remStep)
    dT = dT / 2.0
    print('dT: ', dT)
    ok = ops.analyze(remStep, dT)
    # if analysis fails again, reduce timestep and continue with analysis
    if ok != 0:
        print('did not converge, reducing time step')
        curTime = ops.getTime()
        print('curTime: ', curTime)
        curStep = (curTime - mTime) / dT
        print('curStep: ', curStep)
        remStep = int((rStep - curStep) * 2.0)
        print('remStep: ', remStep)
        dT = dT / 2.0
        print('dT: ', dT)
        ok = ops.analyze(remStep, dT)
endT = tt.time()
