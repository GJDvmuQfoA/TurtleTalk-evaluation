import math
import cadquery as cq

def paperclip(l, w, dia, diff):
    upperSL = (w - dia) / (2 * math.cos(math.pi / 4))
    lowerSL = ((w - dia)/2 - dia -1) / math.cos(math.pi / 4)
    innerL = l-diff-upperSL*math.cos(math.pi / 4)
    circ = cq.Workplane("XZ").circle(dia/2)
    sketch = (cq.Workplane("XY")
              .line(0, innerL)
              .polarLine(upperSL, 45)
              .polarLine(upperSL, -45)
              .line(0, -(innerL+diff))
              .lineTo(dia+1, -diff)
              .line(0, innerL)
              .polarLine(lowerSL, 45)
              .polarLine(lowerSL, -45)
              .line(0, -innerL+diff)
              .wire())
    shape = circ.sweep(sketch)
    assy = cq.Assembly()
    assy.add(shape)
    return assy

if __name__ == "__main__":
    pc = paperclip(65, 25, 3, 7)
    pc.export("paperclip.stl", "STL")