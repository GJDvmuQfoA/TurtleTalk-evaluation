(shape: leg (h topZ)
 (script:
  (named: lg (extrude: 6
   (named: tr (turtle:
     (up 80)
     (forward-until-z h)
     (down 80)
     (forward 20)
     (tag! top)
     (down 90)
     (forward 4)
     (down 90)
     (forward 10)
     (move-to 4 0 0)
     (close))))))
 (constraints:
  (assert: (>= h 20))
  (assert: (= topZ tr.top.z))
  (assert: (= lg.rot-z 180))))

(shape: table (dia legH legTopZ)
 (script:
  (named: tabletop (cylinder #:diameter dia #:height 4))
  (named: legs ((shape: () (script:
                  (for _ in (range 4) 
                   (leg #:h legH #:topZ legTopZ)))))))
 (constraints:
  (assert: (circular #:shapes legs #:radius (/ dia 2)))
  (assert: (= tabletop.z (+ legTopZ 2)))
  (assert: (>= legH (/ dia 2)))))

(print: (table #:dia 100 #:legH 80) "table.stl")