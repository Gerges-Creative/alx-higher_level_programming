#include <Python.h>

/**
 * print_python_list_info - a C function that prints some basic info about
 * Python lists.
 * @p: pointer to python object list
 * Return: No return needed
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
