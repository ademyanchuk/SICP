(define (double x) (+ x x))

(define (iseven? x)
  (= (remainder x 2) 0))

(define (halve evenNumber)
  (/ evenNumber 2))

;;; iterative process log time, const space
(define (iter a b prod)
  (cond ((= b 0) prod)
	((iseven? b) (iter (double a)
			   (halve b)
			   prod))
	(else (iter a
		    (- b 1)
		    (+ a prod)))))

(define (* a b)
  (iter a b 0))

(* 7 5)
