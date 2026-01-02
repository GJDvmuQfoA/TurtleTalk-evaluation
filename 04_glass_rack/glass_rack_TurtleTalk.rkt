(shape: glass (baseR stemH glassR H th vol)
 (script:
  (revolve-z: 360
   (named: tr (turtle:
    (forward baseR)
    (up 90)
    (forward th)
    (up 90)
    (forward-until-x th)
    (down 90)
    (forward stemH)
    (down 45)
    (forward-until-x glassR)
    (up 135)
    (forward th)
    (tag! outer)
    (up 45)
    (forward-until-x 0)
    (tag! inner)
    (up 45)
    (close)))))
 (constraints:
  (assert: (= tr.outer.z H))
  (assert: (= vol (/ (* 3.14 tr.outer.x tr.outer.x (- tr.outer.z tr.inner.z)) 3)))))

(shape: hangerRail (L H offset wireD railL)
 (script:
  (sweep: (circle #:plane "XY" #:d wireD)
   (named: tr (turtle:
    (up 90)
    (forward H)
    (down 90)
    (forward railL)
    (left 45)
    (forward-until-y offset)
    (tag! end)
    (down 90)
    (forward H)))))
  (constraints:
   (assert: (= L tr.end.x))))

(shape: hanger (L innerW outerW H wireD wireZ)
 (script:
  (named: shelve (cuboid #:length (+ L wireD) #:width (+ outerW wireD) #:height 5))
  (named: wireL (hangerRail #:L L #:H H #:offset (/ (- outerW innerW) 2) #:wireD 5
                            #:x (/ L -2) #:y (/ innerW 2) #:z (/ shelve.height 2)))
  (named: wireR (mirror-xz:
                 (hangerRail #:L L #:H H #:offset (/ (- outerW innerW) 2) #:wireD 5
                             #:x (/ L -2) #:y (/ innerW 2) #:z (/ shelve.height 2)))))
 (constraints:
  (assert: (= wireZ (+ wireL.z H (/ wireD -2))))))

(shape: glassRack (glassVcl glassR glassBaseR glassTh !glassesN L glassZ)
 (script:
  (named: rack (hanger #:L L #:wireD 5))
  (named: glasses ((shape: ()
                    (script:
                     (for _ in (range glassesN)
                      (glass #:vol (* 10000 glassVcl) #:glassR glassR
                             #:baseR glassBaseR #:H 130 #:th glassTh #:z glassZ)))))))
 (constraints:
  (assert: (= L (* (+ (* glassR 2) 5) glassesN)))
  (assert: (= rack.outerW (+ (* 2 glassR) 10)))
  (assert: (> rack.outerW (+ (* 2 glassBaseR) rack.wireD)))
  (assert: (>= rack.innerW (+ (* 2 glassTh) 10)))
  (assert: (<= rack.innerW (- (* 2 glassBaseR) 10)))
  (assert: (>= rack.H (+ glassTh 10)))
  (assert: (= rack.wireZ (+ glassZ glassTh)))
  (assert: (linear #:shapes glasses
                   #:x0 (- (- (/ L 2) glassR))
                   #:xn    (- (/ L 2) glassR)))))

(print: (glassRack #:glassesN 3 #:glassVcl 20 #:glassBaseR 35 #:glassTh 4) "glass_rack.stl")