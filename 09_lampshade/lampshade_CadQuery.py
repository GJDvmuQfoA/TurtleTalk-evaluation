import math
import cadquery as cq

def lampshade(bottomDia, topDia, H, th):
    sketch = (cq.Workplane("XZ")
              .lineTo(bottomDia/2, 0, True)
              .bezier([(bottomDia/2, 0),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4), (H / 6)),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4), (H / 3)),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4) - ((H / 2)-(H / 3))*math.tan(math.pi/3) , (H / 2)),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4) - ((H / 2) - (H / 3)) * math.tan(math.pi / 3), H),
                       (topDia / 2 , H)])
              .line(-th, 0)
              .bezier([(topDia / 2 -th, H),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4) - ((H / 2) - (H / 3)) * math.tan(math.pi / 3) - th, H),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4) - ((H / 2) - (H / 3)) * math.tan(math.pi / 3) - th, (H / 2)),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4) - th, (H / 3)),
                       (bottomDia / 2 + (H / 6) / math.tan(math.pi / 4) - th, (H / 6)),
                       (bottomDia / 2 -th, 0)])
              .close()
              .wire())
    return sketch.revolve()

def stripped(base, nr_of_strips, stripW):
    assy = cq.Assembly()
    for i in range(nr_of_strips):
        intersect_cbe = ((cq.Workplane("XY").box(stripW, 300, 300)
                         .rotate((0, 0, 0), (0, 1, 0), 37.5))
                         .translate((0, 0, 75)))
        strip = base.intersect(intersect_cbe).rotate((0, 0, 0), (0, 0, 1), (360/nr_of_strips)*i)
        assy.add(strip)
    return assy

def complete_lampshade(base, stripH, stripZ):
    bottom = base.intersect(cq.Workplane("XY").box(300, 300, stripZ))
    top = base.intersect(cq.Workplane("XY").box(300, 300, stripZ).translate((0, 0, stripH+stripZ)))
    middle = stripped(base.cut(bottom).cut(top), 16, 15)

    assy = cq.Assembly()
    assy.add(bottom)
    assy.add(middle)
    assy.add(top)
    return assy

if __name__ == "__main__":
    ls = complete_lampshade(lampshade(180, 45, 170, 3.5), 120, 30)
    ls.export("lampshade.stl", "STL")
    