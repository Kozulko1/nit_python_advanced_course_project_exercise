#include <Python.h>
#include <string.h>

static char *hash_value(char *key, char *value)
{
    char *hashed_value;
    // implement hashing
    hashed_value = value;
    // implement hashing above

    return hashed_value;
}

static PyObject *hash_password(PyObject *self, PyObject *args)
{
    char *password;

    if (!PyArg_ParseTuple(args, "s", &password))
    {
        Py_RETURN_NONE;
    }
    char *key = "some_key";
    char *hashed_value = hash_value(key, password);
    return Py_BuildValue("s", hashed_value);
}

static char hash_password_docs[] =
    "hash_password(password: str): Function which returns hashed value of an param password\n";

static PyObject *check_hash(PyObject *self, PyObject *args)
{
    char *hash;
    char *password;

    if (!PyArg_ParseTuple(args, "ss", &hash, &password))
    {
        Py_RETURN_NONE;
    }
    char *key = "some_key";
    char *hashed_value = hash_value(key, password);
    if (strcmp(hash, hashed_value) == 0)
    {
        return Py_BuildValue("O", Py_True);
    }
    else
    {
        return Py_BuildValue("O", Py_False);
    }
}

static char check_hash_docs[] =
    "check_hash(hash: str, password: str): Function which returns bool\n";

static PyMethodDef hash_module_funcs[] = {
    {"hash_password", (PyCFunction)hash_password, METH_VARARGS, hash_password_docs},
    {"check_hash", (PyCFunction)check_hash, METH_VARARGS, check_hash_docs},
    {NULL}};

static PyModuleDef hash_module = {PyModuleDef_HEAD_INIT, "hash_module", "Extension module example", 0, hash_module_funcs};

void PyInit_hash_module(void)
{
    PyModule_Create(&hash_module);
}
