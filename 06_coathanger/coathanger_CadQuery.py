import math
import cadquery as cq

def coathanger(dia):
    p0x = 20 * math.cos(-math.pi / 4)
    p0y = 20 * math.sin(-math.pi / 4)
    p1x = p0x - (40 * math.cos(-math.pi / 4))
    p1y = p0y + (40 * math.sin(-math.pi / 4))
    pix = (p1x + p0x) / 2
    piy = (p1y + p0y) / 2
    pmx = pix + p0x
    pmy = piy + p0y
    slopeL = 220 / math.cos(math.pi / 180 * 15)
    bottomL = 2 * slopeL + dia - p0x
    prbx = (p1x - p0x - 20) - (slopeL * math.sin(math.pi / 180 * 15))
    prby = (p1y - p0y - 220)
    circ = cq.Workplane("XZ").circle(dia / 2)
    sketch = (
        cq.Workplane("XY")
        .moveTo(0, 0)
        .lineTo(p0x, p0y)
        .threePointArc((pmx, pmy), (p1x, p1y))
        .line(-p0x, -p0y)
        .line(-20, 0)
        .lineTo(prbx, prby)
        .line(0, -0.5) #Small offset to prevent errors in STL generation
        .threePointArc((prbx - 20, prby - 20 - 0.5), (prbx - 40, prby - 0.5))
        .line(0, bottomL + 1) #Small offset to prevent errors in STL generation
        .threePointArc((prbx - 20, prby + 20 + 0.5 + bottomL), (prbx, prby + bottomL + 0.5))
        .line(0, -0.5) #Small offset to prevent errors in STL generation
        .polarLine(slopeL, -75)
        .wire()).rotate((0, 0, 0), (0, 0, 1), 135)
    shape = circ.sweep(sketch)
    assy = cq.Assembly()
    assy.add(shape)
    return assy

if __name__ == "__main__":
    ch = coathanger(6)
    ch.export("coathanger.stl", "STL")
