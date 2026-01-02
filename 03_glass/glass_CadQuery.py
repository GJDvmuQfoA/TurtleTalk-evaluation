import cadquery as cq

def glass(baseR, H, th, glassR):
    stemH = H - glassR - th
    sketch = (cq.Workplane("XZ")
              .lineTo(baseR, 0)
              .lineTo(baseR, th)
              .lineTo(th, th)
              .lineTo(th, stemH)
              .lineTo(glassR, H)
              .lineTo(glassR-th, H)
              .lineTo(0, stemH)
              .lineTo(0, H)
              .wire())
    glass = sketch.revolve(axisStart=(0, 0, 0), axisEnd=(0, 1, 0))
    assy = cq.Assembly()
    assy.add(glass)
    return assy


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

if __name__ == "__main__":
    #g = glass(baseR=35, H=150, th=3, glassR=70)
    g = glassV(baseR=35, H=150, th=3, volume=200000)
    g.export("glass.stl", "STL")