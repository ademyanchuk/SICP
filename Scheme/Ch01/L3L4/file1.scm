(define (factorial n)
  (if (= n 1)
      1
      (* n (factorial (- n 1)))))

(factorial 10)

(define (fact-iter product counter max-count)
  (if (> counter max-count)
      product
      (fact-iter (* counter product)
		 (+ counter 1)
		 max-count)))

(define (factoriali n)
  (fact-iter 1 1 n))

(factoriali 6)
