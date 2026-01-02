module glass(baseR, H, th, glassR){
 stemH = H-glassR-th;
 rotate_extrude()
  polygon([
   [0, 0],
   [baseR, 0],
   [baseR, th],
   [th, th],
   [th, stemH],
   [glassR, H],
   [glassR-th, H],
   [0, stemH]]);
}

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

//glass(baseR=35, H=150, th=3, glassR=70);
glassV(baseR=35, H=150, th=3, volume=200000);
