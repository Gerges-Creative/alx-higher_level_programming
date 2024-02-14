#include <Python.h>

/*
includes listobject.h
VIEW HEADER-> https://github.com/python/cpython/blob/master/Include/listobject.h
VIEW MANUAL-> https://docs.python.org/3.4/c-api/list.html

includes object.h
VIEW HEADER-> https://docs.python.org/3.4/c-api/structures.html
VIEW MANUAL-> https://github.com/python/cpython/blob/master/Include/object.h
*/

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size_list, allocate, index;

	size_list = PyList_Size(p);
	allocate = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld\n", size_list);
	printf("[*] Allocated = %ld\n", allocate);
	for (index = 0; index < size_list; index++)
	{
		printf("Element %ld: %s\n",
		       index,
		       (PY_TYPE(PyList_GetItem(p, index)))->tp_name);
	}
}
