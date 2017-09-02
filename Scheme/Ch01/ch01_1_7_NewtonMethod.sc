(define (sqrt-iter guess x)
    (if (good-enough? guess (improve guess x))
         guess
         (sqrt-iter (improve guess x)
                    x)))

(define (improve guess x)
  (average guess (/ x guess) 2))

(define (average x y n)
  (/ (+ x y) n))

(define (good-enough? guess new-guess)
  (< (abs (- guess new-guess)) (abs (* guess 0.001))))

(define (sqrt x)
  (sqrt-iter 1.0 x))

(define (new-if predicate then-clause else-clause)
  (cond (predicate then-clause)
        (else else-clause)))

(define (qube-iter guess x)
    (if (good-enough? guess (improve_qube guess x))
         guess
         (sqrt-iter (improve_qube guess x)
                    x)))

(define (improve_qube guess x)
  (average (/ x (square guess)) (* 2 guess) 3))

(define (qubert x)
  (qube-iter 1.0 x))

(display (qubert 0.81))
