PYTHON_VENV=./.python_venv
PYTHON=${PYTHON_VENV}/bin/python
PIP=${PYTHON_VENV}/bin/pip
PYTHON_RUN_UNITTESTS=${PYTHON} -m unittest discover -p "test_*.py" -v

${PYTHON_VENV}/bin/activate:
	python3.10 -m venv ${PYTHON_VENV}


pyvenv_create: ${PYTHON_VENV}/bin/activate

pyvenv_remove:
	rm -rf ${PYTHON_VENV}

python_run_unit_tests:
	${PYTHON_RUN_UNITTESTS}

list_packages:
	${PIP} freeze
	${PIP} list

pip_reinstall_requirements:
	${PIP} install -r requirements.txt

pip_reinstall_packages: package_install


package_remove:
	${PIP} uninstall user-manager -y

package_install: package_remove
	${PYTHON} setup.py install


package_create_distribution:
	${PYTHON} setup.py bdist
