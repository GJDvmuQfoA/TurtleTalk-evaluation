import math
import cadquery as cq

def half_wrench(size, L):
    sideL = (size/2)/math.sin(math.pi/3)
    begin_y = (size*0.33)+((size*0.2)*math.sin(math.pi/4))
    halfW = (size/2)+1+((size/2)*math.sin(math.pi/4))
    diff = (halfW-begin_y)/math.sin(math.pi/4)
    handleL = L - (size * 4 + (size * 0.2 * math.sin(math.pi / 4)) + diff * math.sin(math.pi / 4) + size / 2 + ((size / 2) * math.sin(math.pi / 4)))
    sketch = (
        cq.Workplane("XY")
        .bezier([(0, 0),
                 (0, -size*0.33),
                 (size*2, -size*0.33)])
        .line(handleL, 0)
        .bezier([(size * 2 + handleL, -size * 0.33),
                 (size * 4 + handleL, -size * 0.33),
                 (size * 4 + handleL + (size * 0.2 * math.sin(math.pi / 4)), -begin_y)])
        .bezier([(size * 4 + handleL + (size * 0.2 * math.sin(math.pi / 4)), -begin_y),
                 (size * 4 + handleL + (size * 0.2 * math.sin(math.pi / 4))+diff*math.sin(math.pi/4), -halfW),
                 (size * 4 + handleL + (size * 0.2 * math.sin(math.pi / 4)) + diff * math.sin(math.pi / 4) + size/2, -halfW),
                 (L, -halfW + ((size / 2) * math.sin(math.pi / 4)))])
        .line(0, 1)
        .line(-sideL, 0)
        .polarLine(sideL, 120)
        .close()
        .wire())
    shape = sketch.extrude(size/4)
    assy = cq.Assembly()
    assy.add(shape)
    return assy

def wrench(size, length):
    right = half_wrench(size, length).toCompound()
    left = half_wrench(size, length).toCompound().mirror("XZ")
    holeWp = cq.Workplane("XY").cylinder(size/4, size*0.15).translate((size*0.6, 0, size/8))
    holeAs = cq.Assembly()
    holeAs.add(holeWp)
    hole = holeAs.toCompound()
    assy = cq.Assembly()
    shape = right.fuse(left).cut(hole)
    assy.add(shape)
    return assy

if __name__ == "__main__":
    hl = wrench(18.2, 100)
    hl.export("wrench.stl", "STL")