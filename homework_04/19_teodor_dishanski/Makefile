make:
	echo "Run PyLint:"	&& (pylint *.py 	|| echo "PyLint did find problems!\n"; 		echo "PyLint did not find problems!\n")
	echo "Run PyLama:"	&& (pylama *.py 	|| echo "PyLama did find problems!\n"; 		echo "PyLama did not find problems!\n")
	echo "Run PyCodeStyle:"	&& (pycodestyle *.py 	|| echo "PyCodeStyle did find problems!\n"; 	echo "PyCodeStyle did not find problems!\n")
	echo "Run PyDocStyle:"	&& (pydocstyle *.py 	|| echo 'PyDocStyle did find problems!\n';	echo 'PyDocStyle did not find problems!\n')
	echo "Run PyFlakes:"	&& (pyflakes *.py 	|| echo 'PyFlakes did find problems\n';		echo 'PyFlakes did not find problems!\n')
	echo "Run MyPy:"	&& (mypy *.py 		|| echo 'MyPy did find problems!\n';		echo 'MyPy did not find problems!\n')
	echo "Run PyTest:"	&& (pytest 		|| echo 'PyTest did find problems!\n';		echo 'PyTest did not find problems!\n')

clean:
	rm -r __pycache__
	rm -r .mypy_cache
	rm -r .pytest_cache
