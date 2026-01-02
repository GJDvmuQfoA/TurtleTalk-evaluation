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

(print: (glass #:baseR 35 #:th 3 #:H 150 #:vol 200000) "glass.stl")