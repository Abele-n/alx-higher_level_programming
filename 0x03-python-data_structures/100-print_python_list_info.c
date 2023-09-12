#include <Python.h>

/**
 * print_python_list_info - gets basic python lists information
 * @p: PyObject list
 */

void print_python_list_info(PyObject *p)
{
	int m, my_size, alloc;
	PyObject *my_object;

	alloc = (PyListObject *)p->allocated;
	my_size = Py_SIZE(p);

	printf("[*] Size of python list = %d\n", my_size);
	printf("[*] Alloccated = %d\n", alloc);

	for (m = 0; m < my_size; m++)
	{
		printf("Element %d", m);
		my_object = PyList_GetItem(p, m);
		printf("%s\n", Py_TYPE(list->my_object[m])->tp_name);
	}
}
