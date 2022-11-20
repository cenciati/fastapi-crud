python -m black src/*/*.py
python -m isort src/*/*.py
python -m flake8 src/*/*.py
python -m autoflake src/*/*.py