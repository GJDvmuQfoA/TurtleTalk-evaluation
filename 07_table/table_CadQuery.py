import math
import cadquery as cq

def leg(h):
    sketch = (cq.Workplane("XZ")
              .line(80/math.tan(math.pi/180*80), 80)
              .line(20, 0)
              .line(0, -4)
              .line(-10, 0)
              .lineTo(4, 0)
              .close()
              .wire())
    return (sketch.extrude(6)
    .translate((0, 3, 0))
    .rotate((0, 0, 0), (0, 0, 1), 180))

def table(dia, legH):
    assy = cq.Assembly()
    tabletop = (cq.Workplane("XY")
                .cylinder(4, dia/2)
                .translate((0, 0, legH+2)))
    assy.add(tabletop)
    for i in range(4):
        lg = (leg(h=legH)
              .rotate((0, 0, 0), (0, 0, 1), 90*i)
              .translate((math.cos(math.radians(90*i))*dia/2,
                          math.sin(math.radians(90*i))*dia/2,
                          0)))
        assy.add(lg)
    return assy

if __name__ == "__main__":
    tb = table(dia=100, legH=80)
    tb.export("table.stl", "STL")