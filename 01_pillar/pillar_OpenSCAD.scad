module pillar(h, baseH, outerD, innerD, angle){
 chamfer_h = tan(angle)*(outerD-innerD)/2;
 rotate_extrude()
  polygon([
   [0, 0], 
   [outerD/2, 0], 
   [outerD/2, baseH],
   [innerD/2, baseH+chamfer_h],
   [innerD/2, h-(baseH+chamfer_h)],
   [outerD/2, h-baseH],
   [outerD/2, h],
   [0, h]]);
}

pillar(h=100, baseH=15, outerD=50, innerD=30, angle=45);