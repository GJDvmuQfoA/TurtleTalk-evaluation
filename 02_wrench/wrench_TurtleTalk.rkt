(shape: half-wrench (size L handleL sideL lowerangL)
 (script:
  (extrude: (/ size 4)
   (named: tr (turtle:
    (curve:
     (right 90)
     (forward (* size 0.33))
     (left 90)
     (forward (* size 2)))
    (forward handleL)
    (curve:
     (forward (* size 2))
     (right 45)
     (forward (* size 0.2)))
    (curve:
     (forward lowerangL)
     (left 45)
     (forward (/ size 2))
     (left 45)
     (forward (/ size 2))
     (left 45))
    (forward 1)
    (tag! upper)
    (left 90)
    (forward sideL)
    (right 60)
    (forward sideL)
    (tag! middle)
    (close)))))
 (constraints:
  (assert: (< handleL (- L (* 2 size))))
  (assert: (= tr.middle.y 0))
  (assert: (= tr.upper.x L))
  (assert: (= tr.upper.y (/ size -2)))))

(shape: wrench (size length)
 (script:
  (named: right-side (half-wrench #:size size #:L length))
  (mirror-xz: (named: left-side (half-wrench #:size size #:L length)))
  (cut: (cylinder #:diameter (* size 0.3) #:height (/ size 4) #:x (* size 0.6)))))

(print: (wrench #:size 18.2 #:length 100) "wrench.stl")
