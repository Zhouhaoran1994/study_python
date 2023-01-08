(define (even-subsets s)
    (if (nill? s) nil
        (append (even-subsets (cdr s))
                (subset-helper even? s))))

(define (odd-subsets s)
    (if (nill? s) nil
        (append (odd-subsets (cdr s))
                (subset-helper even? s))))


(define (subset-helper f s)
    (append
        (map (lambda (t) (cons (car s) t))
            (if (f (car s))
                (even-subsets (cdr s))
                (odd-subsets (cdr s))))
            (if (f (car s)) (list (list (car s))) nil)))

(even-subsets '(3 4 5))

(map (lambda (t) (cons 4 t)) '((5 7)))

(define (nonempty-subsets s)
  (if (null? s)
    nil
    (let ((rest (nonempty-subsets (cdr s))))
      (append rest
        (map (lambda (t) (cons (car s) t)) rest)
        (list (list (car s)))
        )
      )
    )
  )

(nonempty-subsets '(3 4 5))

(define (even-subsets s)
  (filter even-sum? (nonempty-subsets s))
  )

(define (even-subsets s)
  (filter (lambda (s) (even? (apply + s))) (nonempty-subsets s))
  )

(define (even-sum? s)
  (if (even? (apply + s))
    #t
    #f
    )
  )

(even-subsets '(3 4 5))

(let ((x 2)) (* x 3))