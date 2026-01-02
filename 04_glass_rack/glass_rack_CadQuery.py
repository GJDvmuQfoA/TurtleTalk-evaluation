import cadquery as cq
import math

def glassV(baseR, H, th, volume):
    innerR = ((3 * volume) / 3.14) ** (1 / 3)
    stemH = H - innerR
    glassR = innerR + th
    sketch = (cq.Workplane("XZ")
              .lineTo(baseR, 0)
              .line(0, th)
              .lineTo(th, th)
              .lineTo(th, stemH)
              .lineTo(glassR, H)
              .lineTo(innerR, H)
              .line(-innerR, -innerR)
              .close())
    glass = sketch.revolve(axisStart=(0, 0, 0), axisEnd=(0, 1, 0))
    assy = cq.Assembly()
    assy.add(glass)
    return assy

def hangerRail(L, H, offset, wireD):
    railL = L-(offset*math.tan(45*math.pi/180))
    angledLineLength = math.sqrt((L-railL)**2 + offset**2)
    sketch1 = (cq.Workplane("XZ")
               .lineTo(0, H)
               .lineTo(railL/2, H)
               .wire())
    base1 = cq.Workplane("XY").circle(radius=wireD/2)
    wire1 = base1.sweep(sketch1)
    sketch2 = (cq.Workplane("XY")
               .lineTo(railL / 2, 0)
               .line((L-railL)/2, offset/2)
               .wire())
    base2 = cq.Workplane("YZ").circle(radius=wireD / 2)
    wire2 = base2.sweep(sketch2)
    wire2 = wire2.translate((railL/2, 0, H))
    sketch3 = (cq.Workplane("XZ")
               .lineTo(0, H)
               .lineTo(angledLineLength/2, H)
               .wire())
    base3 = cq.Workplane("XY").circle(radius=wireD / 2)
    wire3 = base3.sweep(sketch3)
    wire3 = wire3.rotate((0, 0, 0), (0, 0, 1), -135)
    wire3 = wire3.translate((L, offset, 0))
    assy = cq.Assembly()
    assy.add(wire1)
    assy.add(wire2)
    assy.add(wire3)
    return assy

def hanger(L, innerW, outerW, H, wireD):
    shelveH = 5
    shelve = (cq.Workplane("XY", origin=(0, 0, -shelveH/2)).rect(L+wireD,outerW+wireD)).extrude(shelveH)
    wireL = hangerRail(L=L, H=H, offset=(outerW-innerW)/2, wireD=5).toCompound().translate((L/-2, innerW/2, shelveH/2))
    wireR = hangerRail(L=L, H=H, offset=(outerW-innerW)/2, wireD=5).toCompound().mirror("XZ").translate((L / -2, innerW / -2, shelveH/2))
    assy = cq.Assembly()
    assy.add(shelve)
    assy.add(wireL)
    assy.add(wireR)
    return assy

def glassRack(glassVcl, glassBaseR, glassTh, glassesN):
    glassR = ((3 * (10000*glassVcl) / 3.14) ** (1 / 3)) + glassTh #Calculation retrieved from glassV shape
    L = ((glassR*2)+5)*glassesN
    innerW = (glassTh*2) + 20 #Hard coded
    outerW = (glassR*2) + 10 #Hard coded
    H = glassTh + 10 #Hard coded
    shelveH = 5 #Value retrieved from hanger shape
    wireD=5
    wireZ = shelveH/2+H+(wireD/-2) # Calculation retrieved from hanger shape
    gZ = wireZ-glassTh
    rack = hanger(L=L, innerW=innerW, outerW=outerW, H=H, wireD=wireD)
    assy = cq.Assembly()
    assy.add(rack)
    gsX0 = -(L/2)+glassR
    glassesD = ((L/2)-glassR)*2/(glassesN-1)
    for i in range(glassesN):
        glass = glassV(baseR=glassBaseR, H=130, th=glassTh, volume=10000*glassVcl)
        gX = gsX0 + (i * glassesD)
        glass = glass.toCompound().translate((gX, 0, gZ))
        assy.add(glass)
    return assy

if __name__ == "__main__":
    gr = glassRack(glassVcl=20, glassBaseR=35, glassTh=4, glassesN=3)
    gr.export("glass_rack.stl", "STL")
