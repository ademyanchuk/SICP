(define (memq item x)
    (cond ((null? x) false)
         ((eq? item (car x)) x)
         (else (memq item (cdr x)))))


(define (deriv exp var)
    (cond ((number? exp) 0)
          ((variable? exp)
            (if (same-variable? exp var) 1 0))
          ((sum? exp)
            (make-sum (deriv (addend exp) var)
                      (deriv (augend exp) var)))
          ((product? exp)
           (make-sum
             (make-product (multiplier exp)
                           (deriv (multiplicand exp) var))
             (make-product (deriv (multiplier exp) var)
                            (multiplicand exp))))
          (else
            (error "неизвестный тип выражения -- DERIV" exp))))

(display 
    ())
(newline)
