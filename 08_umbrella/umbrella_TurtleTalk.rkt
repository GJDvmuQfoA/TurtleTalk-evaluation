(shape: canopy (radius)
 (script:
  (revolve-z: 360
   (turtle:
    (curve:
     (forward (* radius 0.80))
     (down 65)
     (forward-until-x radius))
    (down 25)
    (forward 1)
    (down 155)
    (curve:
     (forward-until-x (* radius 0.80))
     (up 65)
     (forward-until-x 0))
    (close)))
   (cut: (named: spheres-to-cut ((shape: () (script:
                                     (for i in (range 8)
                                       (sphere #:diameter (* radius 2.75) #:z (* radius -1.7)))))))))
 (constraints:
  (assert: (circular #:shapes spheres-to-cut #:radius radius))))

(shape: stick (l)
 (script:
  (sweep:
   (circle #:plane plane-XY #:d 6)
   (turtle:
    (down 90)
    (forward l)
    (tag! p1)
    (up 90)
    (arc (/ l 10) (+ p1.x (/ l 20)) p1.y (- p1.z (/ l 20)))
    (up 90)
    (forward (/ l 40))))))
   
(shape: umbrella ()
 (script:
  (canopy #:radius 200)
  (stick #:l 300)
  (sphere #:diameter 10)))

(print: (umbrella) "umbrella.stl")