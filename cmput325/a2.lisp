(defun fl-interp (E P)
  (cond 
	((atom E) E)   ;this includes the case where E is nil or a number
        (t
           (let ( (f (car E))  (arg (cdr E)) ) 
	      (cond 
                ; handle built-in functions
                ((eq f 'if) (if (fl-interp (car arg) P) (fl-interp (cadr arg) P) (fl-interp (caddr arg) P)))
                ((eq f 'null) (null (fl-interp (car arg) P)))
                ((eq f 'atom) (atom (fl-interp (car arg) P)))
                ((eq f 'eq) (eq (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f 'first) (car (fl-interp (car arg) P)))
                ((eq f 'rest) (cdr (fl-interp (car arg) P)))
                ((eq f 'cons) (cons (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f 'equal) (equal (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f 'number) (numberp (fl-interp (car arg) P)))
                ((eq f '+) (+ (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f '-) (- (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f '*) (* (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f '>) (> (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f '<) (< (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f '=) (= (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f 'and) (and (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f 'or) (or (fl-interp (car arg) P) (fl-interp (cadr arg) P)))
                ((eq f 'not) (not (fl-interp (car arg) P)))
                ; if f is a user-defined function,
                ;    then evaluate the arguments 
                ;         and apply f to the evaluated arguments 
                ;             (applicative order reduction) 
                ((eq f (caar P)) (fl-interp (replace-var arg (cadar P) (car (cdddar P))) P))
                ; otherwise f is undefined (not intended to be a function),
                ; the E is returned, as if it is quoted in lisp 
                (t E)
          )
           )
        )
  )
)

#|
this function goes through the list of atoms to replace the variables with and calls the helper each time
|#
(defun replace-var (V Y D)
  (if (null Y) D
    (let ((D (replace-var (cdr V) (cdr Y) D)))
      (replace-var-help V Y D)
    )
  )
)

#|
this helper recursively goes through the formal definition of the function and if there is a variable that matches
the variable to replace it will do so.
|#
(defun replace-var-help (V Y D)
  (cond
  ((null D) nil)
  ((atom (car D)) (if (equal (car Y) (car D)) (cons (car V) (replace-var-help V Y (cdr D)))
    (cons (car D) (replace-var-help V Y (cdr D))))
  )
  (t (cons (replace-var-help V Y (car D)) (replace-var-help V Y (cdr D))))
  )
)