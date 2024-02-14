#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - a C function that prints some basic info about
 * Python lists.
 * @p: pointer to python object list
 * Return: No return needed
 */

void print_python_list_info(PyObject *p)
{
	long int size_list, i;
	PyListObject *py_list;
	PyObject *element;

	size_list = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size_list);

	py_list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", py_list->allocated);

	for (i = 0; i < size_list; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
