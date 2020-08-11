all:
	rm -rf ./__pycache__ ./gui/__pycache__
	buildozer android debug deploy run

