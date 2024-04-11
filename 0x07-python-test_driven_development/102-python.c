#include "Python.h"

/**
 * print_python_string - This Prints information about Python strings.
 * @p: A pointer to a PyObject string object.
 */
void print_python_string(PyObject *p)
{
	/* Declare a variable to store the length of the string */
	long int length;

	/* Flush the standard output buffer */
	fflush(stdout);

	/* Print information about the string object */
	printf("[.] string object info\n");

	/* Check if the object is a string */
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		/* Print an error message if the object is not a string */
		printf("  [ERROR] Invalid String Object\n");
		return; /* Return from the function */
	}

	/* Get the length of the string */
	length = ((PyASCIIObject *)(p))->length;

	/* Check if the string is a compact ASCII string */
	if (PyUnicode_IS_COMPACT_ASCII(p))
		/* Print the type of the string (compact ASCII) */
		printf("  type: compact ascii\n");
	else
		/* Print the type of the string (compact Unicode) */
		printf("  type: compact unicode object\n");

	/* Print the length of the string */
	printf("  length: %ld\n", length);

	/* Print the value of the string as wide characters */
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
