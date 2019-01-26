"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"8","name":"flipper","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":0},{"hwid":"9","name":"flywheel_","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":1},{"hwid":"10","name":"flywheel2","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":2},{"hwid":"11","name":"rightFront_","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":3},{"hwid":"12","name":"rightBack","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":4},{"hwid":"13","name":"leftFront","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":5},{"hwid":"14","name":"intake","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":6},{"hwid":"15","name":"leftBack","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":7},{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":8},{"hwid":"drivetrain","name":"DRC","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"12","rightMotorHwId":"15","wheelTravel":319.1764,"trackWidth":292.1},"bufferIndex":9},{"hwid":"controller","name":"DRC_Controler","typeName":"controller_one","extraConfig":null,"bufferIndex":10},{"hwid":"Axis1","name":"axis1","typeName":"controller_axis","extraConfig":null,"bufferIndex":11},{"hwid":"Axis2","name":"axis2","typeName":"controller_axis","extraConfig":null,"bufferIndex":12},{"hwid":"Axis3","name":"axis3","typeName":"controller_axis","extraConfig":null,"bufferIndex":13},{"hwid":"Axis4","name":"axis4","typeName":"controller_axis","extraConfig":null,"bufferIndex":14},{"hwid":"ButtonL1","name":"buttonL1","typeName":"controller_button","extraConfig":null,"bufferIndex":15},{"hwid":"ButtonL2","name":"buttonL2","typeName":"controller_button","extraConfig":null,"bufferIndex":16},{"hwid":"ButtonR1","name":"buttonR1","typeName":"controller_button","extraConfig":null,"bufferIndex":17},{"hwid":"ButtonR2","name":"buttonR2","typeName":"controller_button","extraConfig":null,"bufferIndex":18},{"hwid":"ButtonUp","name":"buttonUp","typeName":"controller_button","extraConfig":null,"bufferIndex":19},{"hwid":"ButtonDown","name":"buttonDown","typeName":"controller_button","extraConfig":null,"bufferIndex":20},{"hwid":"ButtonLeft","name":"buttonLeft","typeName":"controller_button","extraConfig":null,"bufferIndex":21},{"hwid":"ButtonRight","name":"buttonRight","typeName":"controller_button","extraConfig":null,"bufferIndex":22},{"hwid":"ButtonX","name":"buttonX","typeName":"controller_button","extraConfig":null,"bufferIndex":23},{"hwid":"ButtonB","name":"buttonB","typeName":"controller_button","extraConfig":null,"bufferIndex":24},{"hwid":"ButtonY","name":"buttonY","typeName":"controller_button","extraConfig":null,"bufferIndex":25},{"hwid":"ButtonA","name":"buttonA","typeName":"controller_button","extraConfig":null,"bufferIndex":26}]}"""
"""__BLOCKLY__
<xml xmlns="http://www.w3.org/1999/xhtml"><block id="1" type="vexv5_start_autonomous" y="-304" x="-651"><next><block id="#3*x1RAj!kl?=+XhIqCi" type="variables_set"><field name="VAR">on</field><value name="VALUE"><block id="C@PRF5Vii]EY_w-cn~0L" type="math_number"><field name="NUM">1</field></block></value><next><block id="ypT#5^o4}uYK1hh5zJ07" type="variables_set"><field name="VAR">direction</field><value name="VALUE"><block id="yh;fH|LQ#ItYdoIlO[W1" type="math_number"><field name="NUM">1</field></block></value></block></next></block></next></block><block id="!Fu=)cfMVTDEPrhZQ;M[" type="procedures_defnoreturn" y="-170" x="588"><field name="NAME">flyWheelControl</field><statement name="STACK"><block id="WcNUrBCS`+~=2@0Jz2a^" type="controls_if"><value name="IF0"><block id="ew%`5BSA9hk:15I[b3dH" type="vexv5_controller_button_pressing"><field name="WIDGET_ID">ButtonX</field></block></value><statement name="DO0"><block id="dJe#R!Sx]dB[W_caUT86" type="variables_set"><field name="VAR">on</field><value name="VALUE"><block id="/!3;Dn`;H?,,kaR^)6jF" type="math_arithmetic"><field name="OP">MULTIPLY</field><value name="A"><block id="4tU`Ru0kQ;6NbA#JYx4;" type="variables_get"><field name="VAR">on</field></block></value><value name="B"><block id="Jjk6W][/,5BLLkHOTHr1" type="math_number"><field name="NUM">-1</field></block></value></block></value><next><block id="(8JhzU_PEyW6waJ2?aoB" type="sleep"><value name="seconds"><block id="_FM6eRf?j]w-k1,c~YsE" type="math_number"><field name="NUM">0.3</field></block></value></block></next></block></statement><next><block id="ogercc)`@[q:Std:XoG)" type="controls_if"><mutation else="1"></mutation><value name="IF0"><block id="6[XNH}]I{C)vC)r7N-)@" type="logic_compare"><field name="OP">EQ</field><value name="A"><block id="Wxz^NR)9I0I^Zt^olouZ" type="variables_get"><field name="VAR">on</field></block></value><value name="B"><block id="+kqhREJjMwz~~%V%@nu*" type="math_number"><field name="NUM">-1</field></block></value></block></value><statement name="DO0"><block id="M7v,i|Bhj:)0JteBwze^" type="vexv5_motor_spin"><field name="WIDGET_ID">9</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="%5ftboWW-fRsRuo1HqMt" type="math_number"><field name="NUM">100</field></block></value><next><block id="iGfRlI]rh4IM+`k^dak:" type="vexv5_motor_spin"><field name="WIDGET_ID">10</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="2*HNvS0Rvlp{4Ljg}!0p" type="math_number"><field name="NUM">100</field></block></value></block></next></block></statement><statement name="ELSE"><block id="Cj*@4IRx0jkdE]dt^hkl" type="vexv5_motor_stop"><field name="WIDGET_ID">9</field><field name="p0">COAST</field><next><block id="z,8Z|qs1:ylINFLw9NkO" type="vexv5_motor_stop"><field name="WIDGET_ID">10</field><field name="p0">COAST</field></block></next></block></statement></block></next></block></statement></block><block id="rUpS9gAb;7OYNQ}!xg6w" type="procedures_defnoreturn" y="-101" x="-79"><field name="NAME">driveControl</field><statement name="STACK"><block id="|-T7GE9Jv;`?-v[)y?}5" type="controls_if"><mutation else="1"></mutation><value name="IF0"><block id="X}prQHkPE=#MuFpt8HSN" type="logic_compare"><field name="OP">EQ</field><value name="A"><block id="[3g:aJ6I`E9H6XFq2vVs" type="variables_get"><field name="VAR">direction</field></block></value><value name="B"><block id="bJ,uL+EE%JWyl9SVoZ3h" type="math_number"><field name="NUM">-1</field></block></value></block></value><statement name="DO0"><block id="Ib!@SU[aGebSxw8BgS%`" type="vexv5_motor_spin"><field name="WIDGET_ID">11</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id=",{nN@Mpi4Z2T+1-tBu.b" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis2</field></block></value><next><block id="by3;J[ZcJj/heY6)wpe2" type="vexv5_motor_spin"><field name="WIDGET_ID">12</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="Ej:c`;eGGN;mJnf0}z[P" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis2</field></block></value><next><block id="~TxGT}Bmwibc51X@{ZLS" type="vexv5_motor_spin"><field name="WIDGET_ID">13</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="#.5{Q,:%nkE!-C5lT#Aq" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis3</field></block></value><next><block id="}xrH8Eg:SMg@#xM=ScQ1" type="vexv5_motor_spin"><field name="WIDGET_ID">15</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="jI*NV~;3OUzMm_)NF8_;" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis3</field></block></value></block></next></block></next></block></next></block></statement><statement name="ELSE"><block id="b?,)b#`7+Xc1~u=tkF7c" type="vexv5_motor_spin"><field name="WIDGET_ID">15</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block id="!mpX%rerW).w:k)ppzV0" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis2</field></block></value><next><block id="3otNKZ+,5BzV5E12YhDK" type="vexv5_motor_spin"><field name="WIDGET_ID">13</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block id="q[0N-xHd):|fnU;_Lo;6" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis2</field></block></value><next><block id="TmJ{A[e12h+^*pu91v*F" type="vexv5_motor_spin"><field name="WIDGET_ID">12</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block id="bL|s4sUDQb7yd0(+i;^e" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis3</field></block></value><next><block id="EyUpU@Rv}4Xexia|s`i~" type="vexv5_motor_spin"><field name="WIDGET_ID">11</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block id="|oPY/;](2DWnCn~BPWp+" type="vexv5_controller_axis_position"><field name="WIDGET_ID">Axis3</field></block></value></block></next></block></next></block></next></block></statement></block></statement></block><block id="3" type="vexv5_start_drivercontrol" y="-93" x="1119"><next><block id="[;/D2g78w0t}NfUXLJEh" type="sleep"><value name="seconds"><block id="L.J||N:|yPCEOD4jVQ53" type="math_number"><field name="NUM">0.2</field></block></value><next><block id="5" type="controls_forever"><statement name="DO"><block id="9s*sBg6YV+L]I27xi1ze" type="procedures_callnoreturn"><mutation name="DriverSwitch"></mutation><next><block id="j3d,2`yJWDc7i+x+t(9~" type="procedures_callnoreturn"><mutation name="ballController"></mutation><next><block id="q-*]ME.:YaFdf9c%%_L^" type="procedures_callnoreturn"><mutation name="driveControl"></mutation><next><block id="N2%7`Lu,3y_#j98?37`;" type="procedures_callnoreturn"><mutation name="flyWheelControl"></mutation><next><block id="50H~4/}Uo2yQ?:.r3BKT" type="procedures_callnoreturn"><mutation name="flip"></mutation></block></next></block></next></block></next></block></next></block></statement></block></next></block></next></block><block id="oZ-r]53NJdE`OS/hw^5B" type="procedures_defnoreturn" y="202" x="596"><field name="NAME">DriverSwitch</field><statement name="STACK"><block id="%bnqH!RONZGKwCjgo_F%" type="controls_if"><value name="IF0"><block id="){#YaT/.}bxsr{mg#]+4" type="vexv5_controller_button_pressing"><field name="WIDGET_ID">ButtonLeft</field></block></value><statement name="DO0"><block id="7il}5+8b-1}g=F:Il2c;" type="variables_set"><field name="VAR">direction</field><value name="VALUE"><block id="n*A!X,]Oa]AYV~XCLH?J" type="math_arithmetic"><field name="OP">MULTIPLY</field><value name="A"><block id="aWz_G|a`^dsP@:Q4u?x^" type="variables_get"><field name="VAR">direction</field></block></value><value name="B"><block id="pH]bI5cDIO4Xo-]t.9wz" type="math_number"><field name="NUM">-1</field></block></value></block></value><next><block id="KnaJ;(;m6Q1NMU)iCoZK" type="sleep"><value name="seconds"><block id="~Z`Y[;/@B?F-:!(?X(Tc" type="math_number"><field name="NUM">0.25</field></block></value></block></next></block></statement></block></statement></block><block id="K-9)Le26Q12nPXD4~9-S" type="procedures_defnoreturn" y="368" x="593"><field name="NAME">ballController</field><statement name="STACK"><block id="r/WnDinTw|k@FFr`Pw1u" type="controls_if"><mutation else="1" elseif="1"></mutation><value name="IF0"><block id="k~lowos3sGf/_SY[t@}4" type="vexv5_controller_button_pressing"><field name="WIDGET_ID">ButtonL1</field></block></value><statement name="DO0"><block id="NF5}M5tGYUmO.v17V@xF" type="vexv5_motor_spin"><field name="WIDGET_ID">14</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="@X@u/Znyt!#`o.?@Zi5q" type="math_number"><field name="NUM">100</field></block></value></block></statement><value name="IF1"><block id="wc:H9]1McSFpTo#|jXZ/" type="vexv5_controller_button_pressing"><field name="WIDGET_ID">ButtonL2</field></block></value><statement name="DO1"><block id="q@cO(n[t?A~lo=%CUD.N" type="vexv5_motor_spin"><field name="WIDGET_ID">14</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block id="@/uM:y?2*vm6=*X0_0w8" type="math_number"><field name="NUM">100</field></block></value></block></statement><statement name="ELSE"><block id="wz;[zOxfX0j3(kFj}DPJ" type="vexv5_motor_stop"><field name="WIDGET_ID">14</field><field name="p0">BRAKE</field></block></statement></block></statement></block><block id="e[~]K_+TpT%7B6)#8o^K" type="procedures_defnoreturn" y="635" x="573"><field name="NAME">flip</field><statement name="STACK"><block id="loow;+,SCcP6!+}`2+[A" type="controls_if"><mutation else="1" elseif="1"></mutation><value name="IF0"><block id=",N]hNzoLQMyU#jlh%@H{" type="vexv5_controller_button_pressing"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO0"><block id="ATSedODTkqf2/f+=Q]t?" type="vexv5_motor_spin"><field name="WIDGET_ID">8</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block id="r%A6JjvUl;3vVlT.NuYd" type="math_number"><field name="NUM">25</field></block></value></block></statement><value name="IF1"><block id="#X/,yJ.[@~aMPQ`5iEgz" type="vexv5_controller_button_pressing"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO1"><block id="G)o7b*hE^Y|.|rr+MO:T" type="vexv5_motor_spin"><field name="WIDGET_ID">8</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block id="#~V2tsmL_}n3NG=7h}Ge" type="math_number"><field name="NUM">25</field></block></value></block></statement><statement name="ELSE"><block id="Q^-U7NmXm.QIx/UXL8)8" type="vexv5_motor_stop"><field name="WIDGET_ID">8</field><field name="p0">BRAKE</field></block></statement></block></statement></block></xml>
"""

import vex
import sys

#region config
brain         = vex.Brain()
flipper       = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, False)
flywheel_     = vex.Motor(vex.Ports.PORT9, vex.GearSetting.RATIO18_1, False)
flywheel2     = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
rightFront_   = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)
rightBack     = vex.Motor(vex.Ports.PORT12, vex.GearSetting.RATIO18_1, True)
leftFront     = vex.Motor(vex.Ports.PORT13, vex.GearSetting.RATIO18_1, False)
intake        = vex.Motor(vex.Ports.PORT14, vex.GearSetting.RATIO18_1, False)
leftBack      = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)
DRC           = vex.Drivetrain(rightBack, leftBack, 319.1764, 292.1, vex.DistanceUnits.MM)
DRC_Controler = vex.Controller(vex.ControllerType.PRIMARY)
#endregion config

on = None
direction = None

competition = vex.Competition()

def auto():
  global on, direction
  on = 1
  direction = 1
competition.autonomous(auto)

def flyWheelControl():
  global on
  if DRC_Controler.buttonX.pressing():
    on = on * -1
    sys.sleep(0.3)
  if on == -1:
    flywheel_.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
    flywheel2.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
  else:
    flywheel_.stop(vex.BrakeType.COAST)
    flywheel2.stop(vex.BrakeType.COAST)

def driveControl():
  global direction
  if direction == -1:
    rightFront_.spin(vex.DirectionType.FWD, (DRC_Controler.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    rightBack.spin(vex.DirectionType.FWD, (DRC_Controler.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    leftFront.spin(vex.DirectionType.FWD, (DRC_Controler.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    leftBack.spin(vex.DirectionType.FWD, (DRC_Controler.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
  else:
    leftBack.spin(vex.DirectionType.REV, (DRC_Controler.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    leftFront.spin(vex.DirectionType.REV, (DRC_Controler.axis2.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    rightBack.spin(vex.DirectionType.REV, (DRC_Controler.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)
    rightFront_.spin(vex.DirectionType.REV, (DRC_Controler.axis3.position(vex.PercentUnits.PCT)), vex.VelocityUnits.PCT)

def driver():
  sys.sleep(0.2)
  while True:
    DriverSwitch()
    ballController()
    driveControl()
    flyWheelControl()
    flip()
competition.drivercontrol(driver)

def DriverSwitch():
  global direction
  if DRC_Controler.buttonLeft.pressing():
    direction = direction * -1
    sys.sleep(0.25)

def ballController():
  if DRC_Controler.buttonL1.pressing():
    intake.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
  elif DRC_Controler.buttonL2.pressing():
    intake.spin(vex.DirectionType.REV, 100, vex.VelocityUnits.PCT)
  else:
    intake.stop(vex.BrakeType.BRAKE)

def flip():
  if DRC_Controler.buttonR1.pressing():
    flipper.spin(vex.DirectionType.FWD, 25, vex.VelocityUnits.PCT)
  elif DRC_Controler.buttonR2.pressing():
    flipper.spin(vex.DirectionType.REV, 25, vex.VelocityUnits.PCT)
  else:
    flipper.stop(vex.BrakeType.BRAKE)

