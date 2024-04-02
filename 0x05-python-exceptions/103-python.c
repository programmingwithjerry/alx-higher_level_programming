#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <floatobject.h>
#include <string.h>



/**
 * print_python_list - This function prints information
 * about Python list objects.
 * @p: A pointer to the PyObject p
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t list_size, allocated_size, index;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	list_size = var->ob_size;
	allocated_size = list->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", allocated_size);

	for (index = 0; index < size; index++)
	{
		type = list->ob_item[index]->ob_type->tp_name;
		printf("Element %ld: %s\n", index, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[index]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[index]);
	}
}




/**
 * print_python_bytes - This function prints information
 * about Python bytes objects.
 * @p: Pointer to the PyObject p
 */

void print_python_bytes(PyObject *p)
{
	size_t byte_count, index;
	char *byte_str;

	/* Disables buffering of stdout */
	setbuf(stdout, NULL);

	/* Prints information about bytes object */
	printf("[.] bytes object info\n");

	/* Checks if the object is a valid bytes object */
	if (PyBytes_Check(p) == 0)
	{
		printf("\t[ERROR] Invalid Bytes Object\n");
		return;
	}

	/* Extracts byte string and its size */
	byte_str = ((PyBytesObject *)(p))->ob_sval;
	byte_count = PyBytes_Size(p);

	/* Prints the size and a portion of the byte string */
	printf("\tsize: %ld\n\ttrying string: %s\n", byte_count, byte_str);

	/* Adjusts byte count for display */
	byte_count >= 10 ? byte_count = 10 : byte_count++;

	/* Prints the first portion of byte string */
	printf("\tfirst %ld bytes: ", byte_count);
	for (index = 0; index < byte_count - 1; index++)
		printf("%02hhx ", byte_str[index]);
	printf("%02hhx\n", byte_str[index]);
}



/**
 * print_python_float - Prints information about Python float objects.
 * @p: Pointer to the PyObject p
 */

void print_python_float(PyObject *p)
{
	char *float_str;
	double float_v;

	/* Disables buffering of stdout */
	setbuf(stdout, NULL);

	/* Prints information about float object */
	printf("[.] float object info\n");

	/* Checks if the object is a valid float object */
	if (PyFloat_Check(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	/* Extracts float value */
	float_v = ((PyFloatObject *)(p))->ob_fval;

	/* Converts float value to string */
	float_str = PyOS_double_to_string(float_v, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	/* Prints the float value */
	printf("  value: %s\n", float_str);
}





