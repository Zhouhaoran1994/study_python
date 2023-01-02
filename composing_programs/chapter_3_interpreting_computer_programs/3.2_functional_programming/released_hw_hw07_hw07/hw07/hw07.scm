(define (cddr s) (cdr (cdr s)))

(define (cadr s) (cdr s))

(define (caddr s) (cdr (cdr s)))

(define (ascending? asc-lst) (whos-bigger asc-lst))

(define (whos-bigger rest)
    (display rest)
    (cond ((null? (cdr rest)) #t)
          ((<= (car rest) (car (cdr rest))) (whos-bigger (cdr rest)))
          (else #f)
    )
)

(ascending? (cons 1 (cons 2 (cons 3 (cons 3 (cons 4 nil))))))
(ascending? (cons 1 (cons 2 (cons 3 (cons 3 (cons 1 nil))))))

(define (square n) (* n n))

(define (pow base exp) 'YOUR-CODE-HERE)
