(define (trib n)
  (if (< n 3)
      n
      (+ (trib (- n 1))
	 (trib (- n 2))
	 (trib (- n 3)))))

(define (tribonaci n)
  (trib-iter 2 1 0 n))

(define (trib-iter a b c count)
  (if (= count 0)
      c
      (trib-iter (+ a b c)
		 a
		 b
		 (- count 1))))
(trib 4)

(define (pascal r c) 
   (if (or (= c 1) (= c r)) 
       1 
       (+ (pascal (- r 1) (- c 1)) (pascal (- r 1) c)))) 
(pascal 5 3)