(define (square x) (* x x))

(define (sum-of-square x y)
    (+ (square x) (square y)))

(define (max-to-sum-of-square a b c)
  (cond ((and (>= a c) (>= b c)) (sum-of-square a b))
        ((and (>= a b) (>= c b)) (sum-of-square a c))
        (else (sum-of-square b c))))

(display (max-to-sum-of-square 1 2 3))
