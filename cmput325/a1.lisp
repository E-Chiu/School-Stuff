#|
Ethan Chiu
1621615
CMPUT 325 LEC B1
Assignment 1
|#


#| Question 1.
This function returns the number of atoms appearing in a possibly nested list L.
Nil is treated as an empty list and not counted as an atom
|#
(defun xcount (L)
	(cond
	((null L) 0)
	((listp (car L)) (+ (xcount (car L)) (xcount (cdr L))))
	(t (+ 1 (xcount (cdr L))))
	)
)

#| Question 2.
flatten is a function where the argument x is a list of sublists nested to any depth, such that the result of (flatten x) is just a list of atoms with the property that all the atoms appearing in x also appear in (flatten x) and in the same order.

(Comment: this was not too easy for me to understand. My assumption is that all this function does is take a nested list and "unnests" them)

Test cases:
(flatten '(1 (2) 3 (4 5)) => (1 2 3 4 5)
(flatten '((1) (2 3 (4 5) 6) 7)) => (1 2 3 4 5 6 7)
|#

(defun flatten (L)
	(cond
	((null L) nil)
	((atom (car L)) (cons (car L) (flatten (cdr L))))
	(t (append (flatten (car L)) (flatten (cdr L))))
	)
)

#| Question 3.
remove-ducplicate takes x as a list of atoms and removes the repeated ones in x. The order of the elements in the resulting list should preserve the order in the given list

(Comment: The has-dup function I made checks a list x for the atom i and returns the second it finds it)

Test cases:
(remove-duplicate '(1 1 2 3 4 3 5 5)) => (1 2 3 4 5)
(remove-duplicate '(1 2 1 3 2 3 4 5 5 5 5 3 3 3 5 5 5)) => (1 2 3 4 5)
|#

(defun remove-duplicate (x)
  	(if (null x)
		nil
		(if (has-dup (cdr x) (car x))
			(remove-duplicate (cdr x))
				(cons (car x) (remove-duplicate (cdr x)))
		)
	)
)
	  
(defun has-dup (x i)
  	(cond
	((null x) nil)
	((equal (car x) i) 1)
	(t (has-dup (cdr x) i))
	)
)

#| Question 4a.
mix mixes the elements of L1 and L2 into a single, by choosing elements from L1 and L2 alternatingly. If one list is shorter than the other, then it appands all remaining elements from the longer list at the end.
|#

(defun mix (L1 L2)
	(cond
	((null L1) (if (null L2) nil (cons (car L2) (mix (cdr L2) L1))))
	(t (cons (car L1) (mix L2 (cdr L1))))
	)
)

#| Question 4b.
split returns a list of two sublists, first one is the list of elements in L at odd positions and second is the list of elements in L at even positions. If L is empty then a list of two empty lists is returned
|#

(defun split (L)
	(if (null L) '(() ())
		(let ((L2 (split (cdr L))))
			(list (cons (car L) (cadr L2)) (car L2))
		)
	)
)

#| Question 5.
allsubsets returns a list of all subsets of L

(Comment: there is a lot of nesting when creating the subsets that I could not figure out)
|#

(defun allsubsets (L)
  (gen-subsets '() L)
)

(defun gen-subsets (L1 L2)
  (if (null L2) (list L1)
    (append (gen-subsets (append L1 (list (car L2))) (cdr L2)) (gen-subsets L1 (cdr L2)))
    )
)

#| Question 6a.
reached takes in a webpage x and a list of pairs L and returns a list of all webpages that can be reached from x

(Comment: unfortunatley i was unable to figure out a solution that allowed me to not include the original x entry, but the entry is not a result of a pair such as '(google google) and i have checked for that)
|#

(defun reached (x L)
	(cond
	((null L) x)
	((and 
	   (equal (caar L) x)
	   (not (equal (caar L) (cadar L))) (remove-duplicate (flatten (list (reached x (cdr L)) (reached (cadar L) L))))))
	(t (reached x (cdr L)))
	)
)

#| Question 6b.
rank takes a list of atoms naming web pages and another list of pairs representing links and returns S such that they are ordered by the number of pages that refrence them

(Comment: the mySort function was borrowed from the assignment example)
|#

(defun rank (S L)
  (removeNum (mySort (make-count-list S L)))
)

(defun removeNum (L)
  (if (null L) nil
    (cons (caar L) (removeNum (cdr L)))
  )
)

(defun make-count-list (S L)
  (if (null S) nil
    (cons (list (car S) (count-references (car S) L)) (make-count-list (cdr S) L))
  )
)

(defun count-references (s L)
  (cond
  ((null L) 0)
  ((and 
     (equal s (cadar L))
     (not (equal s (caar L)))) (+ 1 (count-references s (cdr L))))
  (t (count-references s (cdr L)))
  )
)

(defun mySort (L)
  (sort L 'greaterthan))

(defun greaterThan (L1 L2)
  (> (cadr L1) (cadr L2)))
