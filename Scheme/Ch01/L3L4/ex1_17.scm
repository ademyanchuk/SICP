(define (double x) (+ x x))

(define (iseven? x)
  (= (remainder x 2) 0))

(define (halve evenNumber)
  (/ evenNumber 2))

;;; recursive process log time and linear space
(define (* a b)
  (cond ((= b 0)
	 0)
	((iseven? b)
	 (* (double a) (halve b)))
	(else
	 (+ a (* a (- b 1))))))











