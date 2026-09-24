import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:

	a = np.array(A)
	t = np.array(T)
	s = np.array(S)


	det_t = np.linalg.det(t)
	det_s = np.linalg.det(s)

	if det_s==0 or det_t==0:
		return -1
	else:
		t_inv = np.linalg.inv(t)
		transformed_matrix = t_inv.dot(a).dot(s) 
		return transformed_matrix.tolist()