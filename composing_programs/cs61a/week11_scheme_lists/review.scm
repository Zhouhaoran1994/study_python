;1. all the even subsets of the rest  of s
;2. the first element of s followed by an (even/odd) subset of the rest
;3. just the first element of s if it is even

;> (even-subsets ' (3 4 5 7))
;((5 7) (4 5 7) (4) (3 7) (3 5) (3 4 7) (3 4 5))

;solution
(define (even-subsets s)
  (if (null? s)
    nil
    (append (even-subsets (cdr s))
      (map (lambda (t) (cons (car s) t))
        (if (even? (car s))
           (even-subsets (cdr s)) ;偶数+偶数=偶数
           (odd-subsets (cdr s)) ;偶数+奇数=奇数
          ))
      (if (even? (car s))
        (list (list (car s)))
        nil
        )
      )
    )
  )

(define (odd-subsets s)
  (if (null? s)
    nil
    (append (odd-subsets (cdr s))
      (map (lambda (t) (cons (car s) t))
        (if (odd? (car s))
           (even-subsets (cdr s)) ;奇数+偶数=奇数
           (odd-subsets (cdr s)) ;奇数+奇数=偶数
          ))
      (if (odd? (car s))
        (list (list (car s)))
        nil
        )
      )
    )
  )

(even-subsets '(3 4 5 7))

;high-order functions
(define (even-subsets s)
  (if (null? s)
    nil
    (append (even-subsets (cdr s))
      (subsets-helper even? s)
      )
    )
  )

(define (odd-subsets s)
  (if (null? s)
    nil
    (append (odd-subsets (cdr s))
      (subsets-helper odd? s)
      )
    )
  )

(define (subsets-helper f s)
  (append
    (map (lambda (t) (cons (car s) t))
          (if (f (car s))
             (even-subsets (cdr s))
             (odd-subsets (cdr s))
            ))
    (if (f (car s))
      (list (list (car s)))
      nil
      )
    )
  )

(even-subsets '(3 4 5 7))

(define s '(2 3))

(append s s s) ; (2 3 2 3 2 3)
(append s (append s s)) ; (2 3 2 3 2 3)，append会把每个元素加在链表末尾

(list s s s) ; ((2 3) (2 3) (2 3))
(list s (list s s)) ; ((2 3) ((2 3) (2 3)))，list会把每个元素当做独立元素

;filter改写
(define (nonempty-subsets s)
  (if (null? s)
    nil
    (let ((rest (nonempty-subsets (cdr s))))
      (append rest
        (map (lambda (t) (cons (car s) t))
          rest
          )
        (list (list (car s)))
        )
      )
    )
  )

(nonempty-subsets '(3 4 5))

(let ((x (+ 1 3))) (* x 2)) ; 8

(define (even-subsets s)
  (filter (lambda (s) (even? (apply + s))) (nonempty-subsets s))
  )

(even-subsets '(3 4 5 7))
