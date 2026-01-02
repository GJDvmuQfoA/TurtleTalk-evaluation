from math import tan, radians
import cadquery as cq

def pillar(h, baseH, outerD, innerD, angle):
    chamferH = tan(radians(angle)) * (outerD - innerD) / 2
    innerH = h - 2*(baseH + chamferH)
    sketch = (
    cq.Workplane("XZ")
    .line(outerD / 2, 0)
    .line(0, baseH)
    .lineTo(innerD/2, baseH + chamferH)
    .line(0, innerH)
    .lineTo(outerD/2, h - baseH)
    .lineTo(outerD/2, h)
    .lineTo(0, h)
    .close())
    pil = sketch.revolve(360, (0, 0, 0), (0, 1, 0))
    assy = cq.Assembly()
    assy.add(pil)
    return assy

if __name__ == "__main__":
    pil = pillar(h=100, baseH=15, outerD=50, innerD=30, angle=45)
    pil.export("pillar.stl", "STL")
