(shape: pillar (h baseH outerD innerD angle innerH)
 (script:
  (revolve-z: 360 (named: tr (turtle:
    (forward (/ outerD 2))
    (up 90)
    (forward baseH)
    (up angle)
    (forward-until-x (/ innerD 2))
    (down angle)
    (forward innerH)
    (down angle)
    (forward-until-x (/ outerD 2))
    (up angle)
    (forward baseH)
    (tag! top)
    (up 90)
    (forward (/ outerD 2))
    (close)))))
 (constraints:
  (assert: (= tr.top.z h))))

(print: (pillar #:h 100 #:baseH 15 #:outerD 50 #:innerD 30 #:angle 45) "pillar.stl")