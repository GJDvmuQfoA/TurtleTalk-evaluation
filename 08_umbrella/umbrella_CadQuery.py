import math
import cadquery as cq

def canopy(radius):
    assy = cq.Assembly()
    sketch = (cq.Workplane("XZ")
              .bezier([(0, 0),
                       (radius*0.8, 0),
                       (radius, (radius*-0.2)/math.tan(math.pi/180*25))])
              .line(0, -1)
              .bezier([(radius, (radius*-0.2)/math.tan(math.pi/180*25)-1),
                       (radius*0.8, -1),
                       (0, -1)])
              .close()
              .wire())
    shape = sketch.revolve()
    for i in range(8):
        sphAs = cq.Assembly()
        sphere_to_cut = (cq.Workplane("XY").sphere(radius = radius*1.375)
                         .translate((radius*math.cos(math.pi/4*i), radius*math.sin(math.pi/4*i), radius*-1.7)))
        sphAs.add(sphere_to_cut)
        shape = shape.cut(sphAs.toCompound())
    assy.add(shape)
    return assy

def stick(l):
    circ = cq.Workplane("XY").circle(3)
    sketch = (cq.Workplane("XZ")
              .line(0, -l)
              .threePointArc((l/20, -l-l/20), (l/10, -l))
              .line(0, l/40)
              .wire())
    shape = circ.sweep(sketch)
    assy = cq.Assembly()
    assy.add(shape)
    return assy

def umbrella():
    assy = cq.Assembly()
    assy.add(canopy(200))
    assy.add(stick(300))
    assy.add(cq.Workplane("XY").sphere(radius=5))
    return assy

if __name__ == "__main__":
    um = umbrella()
    um.export("umbrella.stl", "STL")
