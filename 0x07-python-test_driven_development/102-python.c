#include "Python.h"
/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */

void print_python_string(PyObject *p)
{
	Py_ssize_t length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("\t[ERROR] Invalid String Object\n");
		return;
	}

	length = PyUnicode_GET_LENGTH(p);

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("\ttype: compact ascii\n");
	else
		printf("\ttype: compact unicode object\n");
	printf("\tlength: %ld\n", length);
	printf("\tvalue: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

