;From http://programmingpraxis.com/2009/02/19/rpn-calculator/
;
;Implement an RPN calculator that takes an expression like 19 2.14 + 4.5 2 4.3 / - *
;which is usually expressed as (19 + 2.14) * (4.5 - 2 / 4.3) and responds with
;85.2974. The program should read expressions from standard input and print the top
;of the stack to standard output when a newline is encountered. The program should
;retain the state of the operand stack between expressions.

(define rpn
  (lambda (exp)
    (define iter-rpn
      (lambda (exp stack)
        (cond ((null? exp) ;everything processed
               (car stack))
              ((eq? (car exp) '+)
               (iter-rpn (cdr exp)
                         (cons (+ (cadr stack) (car stack))
                               (cddr stack))))
              ((eq? (car exp) '-)
               (iter-rpn (cdr exp)
                         (cons (- (cadr stack) (car stack))
                               (cddr stack))))
              ((eq? (car exp) '*)
               (iter-rpn (cdr exp)
                         (cons (* (cadr stack) (car stack))
                               (cddr stack))))
              ((eq? (car exp) '/)
               (iter-rpn (cdr exp)
                         (cons (/ (cadr stack) (car stack))
                               (cddr stack))))
              (else (iter-rpn (cdr exp)
                              (cons (car exp) stack))))))
    (iter-rpn exp '())))

; Test
; > (rpn '(19 2.14 -))
; 16.86
; > (rpn '(19 2.14 + 4.5 2 4.3 / - *))
; 85.29744186046511
