# HW 07:Scheme
# https://cs61a.org/hw/sol-hw07/

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

(define (pow base exp)
    (cond   ((= exp 1) base)
            ((even? exp) (pow (square base) (/ exp 2)))
            ((odd? exp) (* base (pow (square base) (/ (- exp 1) 2))))
    )
)

(define (sum x y)
    (define x 1)
    (+ x y)
)
