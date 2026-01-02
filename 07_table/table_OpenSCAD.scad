module table_leg(height){
 length = 20+cos(80)*height;
 translate([length/2, -3, 0])
  rotate([90, 0, 180])
   linear_extrude(6){
    p0 = [0, 0];
    p1 = [height * cos(80), height];
    p2 = [height * cos(80) + 20, height];
    p3 = [height * cos(80) + 20, height-4];
    p4 = [height * cos(80) + 10, height-4];
    p5 = [4, 0];
    polygon(points = [p0, p1, p2, p3, p4, p5]);
}}

module table(dia, leg_h, nr_of_legs){
 leg_radius = dia/2 - 20;
 union(){
  translate([0, 0, leg_h+2])
   cylinder(d=dia, h=4, center=true);
  for(i=[0:nr_of_legs-1]){
   translate([leg_radius * cos(360*i/nr_of_legs), 
              leg_radius * sin(360*i/nr_of_legs), 
              0]){
    rotate([0, 0, 360/nr_of_legs*i]){
     table_leg(height=leg_h);
}}}}}

table(dia=100, leg_h=80, nr_of_legs=4);