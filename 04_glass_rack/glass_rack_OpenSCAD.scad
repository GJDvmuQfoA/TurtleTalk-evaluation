module glassV(baseR, H, th, volume){
 innerR = ((3*volume)/3.14)^(1/3);
 stemH = H-innerR;
 glassR = innerR+th;
 rotate_extrude()
  polygon([
   [0, 0],
   [baseR, 0],
   [baseR, th],
   [th, th],
   [th, stemH],
   [glassR, H],
   [innerR, H],
   [0, stemH]]);
}

module hangerRail(L, H, offset, wireD){
 railL = L-(offset*tan(45));
 angledLineLength = sqrt((L-railL)^2 + offset^2);
 union(){
  cylinder(h=H, r=wireD/2);
  translate([0, 0, H])
   rotate([0, 90, 0])
    cylinder(h=railL, r=wireD/2);
  translate([railL, 0, H])
   rotate([0, 90, 45])
    cylinder(h=angledLineLength, r=wireD/2);
  translate([L, offset, 0])
   cylinder(h=H, r=wireD/2);
}}

module hanger(L, innerW, outerW, H, wireD){
 shelveH = 5;
 union(){
  cube([L+wireD, outerW+wireD, shelveH], center=true);
  translate([L/-2, innerW/2, shelveH/2])
   hangerRail(L=L, H=H, offset=(outerW-innerW)/2, wireD=5);
  translate([L/-2, innerW/-2, shelveH/2])
   mirror([0,1,0])
    hangerRail(L=L, H=H, offset=(outerW-innerW)/2, wireD=5);
}}

module glassRack(glassVcl, glassBaseR, glassTh, glassesN){
 glassR = ((3*(10000*glassVcl)/3.14)^(1/3))+glassTh; //Calculation retrieved from glassV shape
 L = ((glassR*2)+5)*glassesN;
 innerW = (glassTh*2)+20; //Hardcoded: no way to derive value using constraints
 outerW = (glassR*2)+10; //Hardcoded: no way to derive value using constraints
 H = glassTh+10; //Hardcoded: no way to derive value using constraints
 shelveH = 5; //Value retrieved from hanger shape
 wireD = 5;
 wireZ = shelveH/2+H+(wireD/-2); //Calculation retrieved from hanger shape
 glassZ = wireZ-glassTh;
 glassesX0 = -(L/2)+glassR;
 glassesD = ((L/2)-glassR)*2/(glassesN-1);
 union(){
  hanger(L=L, innerW=innerW, outerW=outerW, H=H, wireD=wireD);
  for (i = [0:glassesN-1]){
   glassX = glassesX0 + (i * glassesD);
   translate([glassX, 0, glassZ])
    glassV(baseR=glassBaseR, H=130, th=glassTh, volume=10000*glassVcl);
}}}

glassRack(glassVcl=20, glassBaseR=35, glassTh=4, glassesN=3);