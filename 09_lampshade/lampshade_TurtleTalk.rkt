(shape: lampshade (bottomDia topDia H th)
 (script:
  (revolve-z: 360
   (turtle:
    (pen-off!)
    (left 90)
    (forward (/ bottomDia 2))
    (pen-on!)
    (tag! CP1)
    (curve:
     (up 45)
     (forward-until-z (/ H 6))
     (tag! CP2)
     (up 45)
     (forward-until-z (* H (/ 1 3)))
     (tag! CP3)
     (up 60)
     (forward-until-z (* H (/ 1 2)))
     (tag! CP4)
     (down 60)
     (forward-until-z H)
     (tag! CP5)
     (move-to 0 (/ topDia 2) H))
    (tag! CP6)
    (move-to CP6.x (- CP6.y th) CP6.z)
    (curve:
     (move-to CP5.x (- CP5.y th) CP5.z)
     (move-to CP4.x (- CP4.y th) CP4.z)
     (move-to CP3.x (- CP3.y th) CP3.z)
     (move-to CP2.x (- CP2.y th) CP2.z)
     (move-to CP1.x (- CP1.y th) CP1.z))
    (move-to CP1.x CP1.y CP1.z)))))

(shape: stripped (!base !nr-of-strips stripW)
 (script:
  (named: strips ((shape: (strip)
                  (script:
                   (for i in (range nr-of-strips)
                     ((shape: () (script: strip)) #:rot-z (* i (/ 360 nr-of-strips))))))
                  #:strip ((shape: () (script:
                            base
                            (intersect: (cuboid #:length stripW #:width 300 #:height 300
                                                #:z 75 #:rot-y 37.5)))))))))

(shape: complete-lampshade (!base stripH stripZ)
 (script:
  (named: bottom ((shape: () (script: base (intersect: (cuboid #:length 300
                                                               #:width 300
                                                               #:height stripZ))))))
  (named: top ((shape: () (script: base (intersect: (cuboid #:length 300
                                                            #:width 300
                                                            #:height stripZ
                                                            #:z (+ stripH stripZ)))))))
  (named: middle (stripped #:base ((shape: () (script: base (cut: bottom) (cut: top))))
                           #:nr-of-strips 16
                           #:stripW 15))))

(print: (complete-lampshade #:base (lampshade #:bottomDia 180 #:topDia 45 #:H 170 #:th 3.5)
                            #:stripH 120
                            #:stripZ 30)
        "lampshade.stl")