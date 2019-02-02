"""__CONFIG__
{"version":20,"widgetInfos":[{"hwid":"8","name":"flipper","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":0},{"hwid":"9","name":"flywheel_","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":1},{"hwid":"10","name":"flywheel2","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":2},{"hwid":"11","name":"rightFront_","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":3},{"hwid":"12","name":"rightBack","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":true},"bufferIndex":4},{"hwid":"13","name":"leftFront","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":5},{"hwid":"14","name":"intake","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":6},{"hwid":"15","name":"leftBack","typeName":"motor","extraConfig":{"gearSetting":1,"reverse":false},"bufferIndex":7},{"hwid":"triport_adi","name":"triport_22","typeName":"triport","extraConfig":null,"bufferIndex":8},{"hwid":"drivetrain","name":"DRC","typeName":"drivetrain","extraConfig":{"leftMotorHwId":"12","rightMotorHwId":"15","wheelTravel":319.1764,"trackWidth":292.1},"bufferIndex":9},{"hwid":"controller","name":"DRC_Controler","typeName":"controller_one","extraConfig":null,"bufferIndex":10},{"hwid":"Axis1","name":"axis1","typeName":"controller_axis","extraConfig":null,"bufferIndex":11},{"hwid":"Axis2","name":"axis2","typeName":"controller_axis","extraConfig":null,"bufferIndex":12},{"hwid":"Axis3","name":"axis3","typeName":"controller_axis","extraConfig":null,"bufferIndex":13},{"hwid":"Axis4","name":"axis4","typeName":"controller_axis","extraConfig":null,"bufferIndex":14},{"hwid":"ButtonL1","name":"buttonL1","typeName":"controller_button","extraConfig":null,"bufferIndex":15},{"hwid":"ButtonL2","name":"buttonL2","typeName":"controller_button","extraConfig":null,"bufferIndex":16},{"hwid":"ButtonR1","name":"buttonR1","typeName":"controller_button","extraConfig":null,"bufferIndex":17},{"hwid":"ButtonR2","name":"buttonR2","typeName":"controller_button","extraConfig":null,"bufferIndex":18},{"hwid":"ButtonUp","name":"buttonUp","typeName":"controller_button","extraConfig":null,"bufferIndex":19},{"hwid":"ButtonDown","name":"buttonDown","typeName":"controller_button","extraConfig":null,"bufferIndex":20},{"hwid":"ButtonLeft","name":"buttonLeft","typeName":"controller_button","extraConfig":null,"bufferIndex":21},{"hwid":"ButtonRight","name":"buttonRight","typeName":"controller_button","extraConfig":null,"bufferIndex":22},{"hwid":"ButtonX","name":"buttonX","typeName":"controller_button","extraConfig":null,"bufferIndex":23},{"hwid":"ButtonB","name":"buttonB","typeName":"controller_button","extraConfig":null,"bufferIndex":24},{"hwid":"ButtonY","name":"buttonY","typeName":"controller_button","extraConfig":null,"bufferIndex":25},{"hwid":"ButtonA","name":"buttonA","typeName":"controller_button","extraConfig":null,"bufferIndex":26}]}"""
"""__BLOCKLY__
<xml xmlns="http://www.w3.org/1999/xhtml"><block type="vexv5_start_autonomous" id="1" x="-651" y="-304"><next><block type="variables_set" id="#3*x1RAj!kl?=+XhIqCi"><field name="VAR">on</field><value name="VALUE"><block type="math_number" id="C@PRF5Vii]EY_w-cn~0L"><field name="NUM">1</field></block></value><next><block type="variables_set" id="ypT#5^o4}uYK1hh5zJ07"><field name="VAR">direction</field><value name="VALUE"><block type="math_number" id="yh;fH|LQ#ItYdoIlO[W1"><field name="NUM">1</field></block></value><next><block type="vexv5_drivetrain_set_velocity" id="@=SxN1{pxU+vhTg,bkVI"><field name="p1">PCT</field><value name="p0"><block type="math_number" id="sEW%CGrfa5QIL+P1zd%;"><field name="NUM">75</field></block></value><next><block type="vexv5_motor_spin" id="DErRi?|RHw/2y6m60`@A"><field name="WIDGET_ID">14</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="Tw3YG(7:F=@MN3t1pt{d"><field name="NUM">100</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="PE6PY9L%I]?ToJ`DKGr0"><field name="p0">REV</field><field name="p2">IN</field><value name="p1"><block type="math_number" id="B[j1pt+Ul)GpSCgP34x;"><field name="NUM">40</field></block></value><next><block type="vexv5_drivetrain_set_timeout" id="[vNNp`?srHBupkwSyb=7"><field name="p1">SEC</field><value name="p0"><block type="math_number" id="U+ErG3I7UpL%Fuu_=t-R"><field name="NUM">1</field></block></value><next><block type="vexv5_drivetrain_drive_for" id="%(i+#R|w,RiD0LxYE.W)"><field name="p0">FWD</field><field name="p2">IN</field><value name="p1"><block type="math_number" id="]t%v}s[/WoywPiY?Rzml"><field name="NUM">3</field></block></value><next><block type="vexv5_drivetrain_turn_for" id="3!me(J@o2f(j-lIygCM3"><field name="p0">LEFT</field><field name="p2">DEG</field><value name="p1"><block type="math_number" id="%.NsCESn4SsQN%H4a|Fa"><field name="NUM">125</field></block></value><next><block type="spin_without_velocity" id="Ji[;a`TR5#=zhRL!hp}G"><field name="WIDGET_ID">11</field><field name="p0">REV</field><next><block type="spin_without_velocity" id="|DU%~`?{xV+ov9Y`[w3~"><field name="WIDGET_ID">12</field><field name="p0">FWD</field><next><block type="spin_without_velocity" id="tJjDMSd0(erNUs|C)T.r"><field name="WIDGET_ID">13</field><field name="p0">REV</field><next><block type="spin_without_velocity" id="[N]`^^rM4Ne!9`L~Puig"><field name="WIDGET_ID">15</field><field name="p0">FWD</field><next><block type="timer_start" id="}N^F0Ygskk9E@tDNwTej"><next><block type="controls_if" id="?tqwS4ksga%ZWx=HVB}Y"><value name="IF0"><block type="logic_compare" id="*BeOLq[7ko|dU}!atvEt"><field name="OP">GT</field><value name="A"><block type="timer_elapsedTime" id="lxA-)A`A*}U?h%2t=etm"></block></value><value name="B"><block type="math_number" id="=qiDwRZesQRzK3If*8ew"><field name="NUM">2</field></block></value></block></value><statement name="DO0"><block type="timer_stop" id="^/)RGd42kNPw}e?s0:;`"><next><block type="vexv5_motor_stop" id="`Qv/-b%1qU9eqCGM9mp]"><field name="WIDGET_ID">15</field><field name="p0">HOLD</field><next><block type="vexv5_motor_stop" id="[xBK;:}C?-pzv:Cn=iIx"><field name="WIDGET_ID">13</field><field name="p0">HOLD</field><next><block type="vexv5_motor_stop" id="gqnY?N_b0,gqOK#(@V~e"><field name="WIDGET_ID">12</field><field name="p0">HOLD</field><next><block type="vexv5_motor_stop" id="9C_uvtvQqbnCcr2_W:NZ"><field name="WIDGET_ID">11</field><field name="p0">HOLD</field></block></next></block></next></block></next></block></next></block></statement></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><block type="procedures_defnoreturn" id="!Fu=)cfMVTDEPrhZQ;M[" x="588" y="-170"><field name="NAME">flyWheelControl</field><statement name="STACK"><block type="controls_if" id="WcNUrBCS`+~=2@0Jz2a^"><value name="IF0"><block type="vexv5_controller_button_pressing" id="ew%`5BSA9hk:15I[b3dH"><field name="WIDGET_ID">ButtonX</field></block></value><statement name="DO0"><block type="variables_set" id="dJe#R!Sx]dB[W_caUT86"><field name="VAR">on</field><value name="VALUE"><block type="math_arithmetic" id="/!3;Dn`;H?,,kaR^)6jF"><field name="OP">MULTIPLY</field><value name="A"><block type="variables_get" id="4tU`Ru0kQ;6NbA#JYx4;"><field name="VAR">on</field></block></value><value name="B"><block type="math_number" id="Jjk6W][/,5BLLkHOTHr1"><field name="NUM">-1</field></block></value></block></value><next><block type="sleep" id="(8JhzU_PEyW6waJ2?aoB"><value name="seconds"><block type="math_number" id="_FM6eRf?j]w-k1,c~YsE"><field name="NUM">0.3</field></block></value></block></next></block></statement><next><block type="controls_if" id="ogercc)`@[q:Std:XoG)"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="6[XNH}]I{C)vC)r7N-)@"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="Wxz^NR)9I0I^Zt^olouZ"><field name="VAR">on</field></block></value><value name="B"><block type="math_number" id="+kqhREJjMwz~~%V%@nu*"><field name="NUM">-1</field></block></value></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="M7v,i|Bhj:)0JteBwze^"><field name="WIDGET_ID">9</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="%5ftboWW-fRsRuo1HqMt"><field name="NUM">100</field></block></value><next><block type="vexv5_motor_spin" id="iGfRlI]rh4IM+`k^dak:"><field name="WIDGET_ID">10</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="2*HNvS0Rvlp{4Ljg}!0p"><field name="NUM">100</field></block></value></block></next></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="Cj*@4IRx0jkdE]dt^hkl"><field name="WIDGET_ID">9</field><field name="p0">COAST</field><next><block type="vexv5_motor_stop" id="z,8Z|qs1:ylINFLw9NkO"><field name="WIDGET_ID">10</field><field name="p0">COAST</field></block></next></block></statement></block></next></block></statement></block><block type="procedures_defnoreturn" id="rUpS9gAb;7OYNQ}!xg6w" x="-79" y="-101"><field name="NAME">driveControl</field><statement name="STACK"><block type="controls_if" id="|-T7GE9Jv;`?-v[)y?}5"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="X}prQHkPE=#MuFpt8HSN"><field name="OP">EQ</field><value name="A"><block type="variables_get" id="[3g:aJ6I`E9H6XFq2vVs"><field name="VAR">direction</field></block></value><value name="B"><block type="math_number" id="bJ,uL+EE%JWyl9SVoZ3h"><field name="NUM">-1</field></block></value></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="Ib!@SU[aGebSxw8BgS%`"><field name="WIDGET_ID">11</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id=",{nN@Mpi4Z2T+1-tBu.b"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="by3;J[ZcJj/heY6)wpe2"><field name="WIDGET_ID">12</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="Ej:c`;eGGN;mJnf0}z[P"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="~TxGT}Bmwibc51X@{ZLS"><field name="WIDGET_ID">13</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="#.5{Q,:%nkE!-C5lT#Aq"><field name="WIDGET_ID">Axis3</field></block></value><next><block type="vexv5_motor_spin" id="}xrH8Eg:SMg@#xM=ScQ1"><field name="WIDGET_ID">15</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="jI*NV~;3OUzMm_)NF8_;"><field name="WIDGET_ID">Axis3</field></block></value></block></next></block></next></block></next></block></statement><statement name="ELSE"><block type="vexv5_motor_spin" id="b?,)b#`7+Xc1~u=tkF7c"><field name="WIDGET_ID">15</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="!mpX%rerW).w:k)ppzV0"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="3otNKZ+,5BzV5E12YhDK"><field name="WIDGET_ID">13</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="q[0N-xHd):|fnU;_Lo;6"><field name="WIDGET_ID">Axis2</field></block></value><next><block type="vexv5_motor_spin" id="TmJ{A[e12h+^*pu91v*F"><field name="WIDGET_ID">12</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="bL|s4sUDQb7yd0(+i;^e"><field name="WIDGET_ID">Axis3</field></block></value><next><block type="vexv5_motor_spin" id="EyUpU@Rv}4Xexia|s`i~"><field name="WIDGET_ID">11</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="vexv5_controller_axis_position" id="|oPY/;](2DWnCn~BPWp+"><field name="WIDGET_ID">Axis3</field></block></value></block></next></block></next></block></next></block></statement></block></statement></block><block type="vexv5_start_drivercontrol" id="3" x="1119" y="-93"><next><block type="sleep" id="[;/D2g78w0t}NfUXLJEh"><value name="seconds"><block type="math_number" id="L.J||N:|yPCEOD4jVQ53"><field name="NUM">0.2</field></block></value><next><block type="controls_forever" id="5"><statement name="DO"><block type="procedures_callnoreturn" id="9s*sBg6YV+L]I27xi1ze"><mutation name="DriverSwitch"></mutation><next><block type="procedures_callnoreturn" id="j3d,2`yJWDc7i+x+t(9~"><mutation name="ballController"></mutation><next><block type="procedures_callnoreturn" id="q-*]ME.:YaFdf9c%%_L^"><mutation name="driveControl"></mutation><next><block type="procedures_callnoreturn" id="N2%7`Lu,3y_#j98?37`;"><mutation name="flyWheelControl"></mutation><next><block type="procedures_callnoreturn" id="50H~4/}Uo2yQ?:.r3BKT"><mutation name="flip"></mutation></block></next></block></next></block></next></block></next></block></statement></block></next></block></next></block><block type="procedures_defnoreturn" id="oZ-r]53NJdE`OS/hw^5B" x="596" y="202"><field name="NAME">DriverSwitch</field><statement name="STACK"><block type="controls_if" id="%bnqH!RONZGKwCjgo_F%"><value name="IF0"><block type="vexv5_controller_button_pressing" id="){#YaT/.}bxsr{mg#]+4"><field name="WIDGET_ID">ButtonLeft</field></block></value><statement name="DO0"><block type="variables_set" id="7il}5+8b-1}g=F:Il2c;"><field name="VAR">direction</field><value name="VALUE"><block type="math_arithmetic" id="n*A!X,]Oa]AYV~XCLH?J"><field name="OP">MULTIPLY</field><value name="A"><block type="variables_get" id="aWz_G|a`^dsP@:Q4u?x^"><field name="VAR">direction</field></block></value><value name="B"><block type="math_number" id="pH]bI5cDIO4Xo-]t.9wz"><field name="NUM">-1</field></block></value></block></value><next><block type="sleep" id="KnaJ;(;m6Q1NMU)iCoZK"><value name="seconds"><block type="math_number" id="~Z`Y[;/@B?F-:!(?X(Tc"><field name="NUM">0.25</field></block></value></block></next></block></statement></block></statement></block><block type="procedures_defnoreturn" id="K-9)Le26Q12nPXD4~9-S" x="593" y="368"><field name="NAME">ballController</field><statement name="STACK"><block type="controls_if" id="r/WnDinTw|k@FFr`Pw1u"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id="k~lowos3sGf/_SY[t@}4"><field name="WIDGET_ID">ButtonL1</field></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="NF5}M5tGYUmO.v17V@xF"><field name="WIDGET_ID">14</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="@X@u/Znyt!#`o.?@Zi5q"><field name="NUM">100</field></block></value></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="wc:H9]1McSFpTo#|jXZ/"><field name="WIDGET_ID">ButtonL2</field></block></value><statement name="DO1"><block type="vexv5_motor_spin" id="q@cO(n[t?A~lo=%CUD.N"><field name="WIDGET_ID">14</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="@/uM:y?2*vm6=*X0_0w8"><field name="NUM">100</field></block></value></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="wz;[zOxfX0j3(kFj}DPJ"><field name="WIDGET_ID">14</field><field name="p0">BRAKE</field></block></statement></block></statement></block><block type="procedures_defnoreturn" id="e[~]K_+TpT%7B6)#8o^K" x="573" y="635"><field name="NAME">flip</field><statement name="STACK"><block type="controls_if" id="loow;+,SCcP6!+}`2+[A"><mutation elseif="1" else="1"></mutation><value name="IF0"><block type="vexv5_controller_button_pressing" id=",N]hNzoLQMyU#jlh%@H{"><field name="WIDGET_ID">ButtonR1</field></block></value><statement name="DO0"><block type="vexv5_motor_spin" id="ATSedODTkqf2/f+=Q]t?"><field name="WIDGET_ID">8</field><field name="p0">FWD</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="r%A6JjvUl;3vVlT.NuYd"><field name="NUM">25</field></block></value></block></statement><value name="IF1"><block type="vexv5_controller_button_pressing" id="#X/,yJ.[@~aMPQ`5iEgz"><field name="WIDGET_ID">ButtonR2</field></block></value><statement name="DO1"><block type="vexv5_motor_spin" id="G)o7b*hE^Y|.|rr+MO:T"><field name="WIDGET_ID">8</field><field name="p0">REV</field><field name="p2">PCT</field><value name="p1"><block type="math_number" id="#~V2tsmL_}n3NG=7h}Ge"><field name="NUM">25</field></block></value></block></statement><statement name="ELSE"><block type="vexv5_motor_stop" id="Q^-U7NmXm.QIx/UXL8)8"><field name="WIDGET_ID">8</field><field name="p0">BRAKE</field></block></statement></block></statement></block></xml>
"""

import vex
import timer
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

timer_ = timer.Timer()

def auto():
  global on, direction
  on = 1
  direction = 1
  DRC.set_velocity(75, vex.VelocityUnits.PCT)
  intake.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
  DRC.drive_for(vex.DirectionType.REV, 40, vex.DistanceUnits.IN)
  DRC.set_timeout(1, vex.TimeUnits.SEC)
  DRC.drive_for(vex.DirectionType.FWD, 3, vex.DistanceUnits.IN)
  DRC.turn_for(vex.TurnType.LEFT, 125, vex.RotationUnits.DEG)
  rightFront_.spin(vex.DirectionType.REV)
  rightBack.spin(vex.DirectionType.FWD)
  leftFront.spin(vex.DirectionType.REV)
  leftBack.spin(vex.DirectionType.FWD)
  timer_.start()
  if timer_.elapsed_time() > 2:
    timer_.stop()
    leftBack.stop(vex.BrakeType.HOLD)
    leftFront.stop(vex.BrakeType.HOLD)
    rightBack.stop(vex.BrakeType.HOLD)
    rightFront_.stop(vex.BrakeType.HOLD)
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

