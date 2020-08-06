publish:
	rm -rf dist/
	python setup.py sdist
	twine upload dist/*

publish-test:
	rm -rf dist/
	python setup.py sdist
	twine upload --repository testpypi dist/*

..phony: publish publish-test
