(define (abs x)
    (cond ((> x 0) x)
          ((= x 0) 0)
          ((< x 0) (- x))))

(define (abs1 x)
    (cond ((< x 0) (- x))
          (else x)))

(define (abs2 x)
    (if (< x 0)
        (- x)
        x))

(display (abs2 0))
