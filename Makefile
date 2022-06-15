clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 

dataset:
	env/bin/python src/data/make_dataset.py $(sql)

process:
	env/bin/python src/features/make_features.py