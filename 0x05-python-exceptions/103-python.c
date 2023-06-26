#include <Python.h>
#include <float.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("Invalid PyListObject\n");
        return;
    }
    
    Py_ssize_t size = PyList_Size(p);
    PyObject *item;
    PyTypeObject *type;
    Py_ssize_t i;
    
    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
    
    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        type = Py_TYPE(item);
        printf("Element %ld: %s\n", i, type->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("Invalid PyBytesObject\n");
        return;
    }
    
    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    unsigned char *data = (unsigned char *)PyBytes_AsString(p);
    
    printf("[.] bytes object info\n");
    printf("size: %ld\n", size);
    printf("trying string: %s\n", data);
    
    printf("first %ld bytes:", (size + 1 < 10) ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++) {
        printf(" %02x", data[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("Invalid PyFloatObject\n");
        return;
    }
    
    double value = PyFloat_AsDouble(p);
    PyObject *repr = PyObject_Repr(p);
    const char *str_value = PyUnicode_AsUTF8(repr);
    
    printf("[.] float object info\n");
    printf("value: %f\n", value);
    printf("string: %s\n", str_value);
}


