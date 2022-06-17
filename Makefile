clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 

populate:
	env/bin/python src/database/populate.py $(dir) $(pass) $(host) $(table)
	
dataset:
	env/bin/python src/dataset/make_dataset.py $(sql)

process:
	env/bin/python src/labels/make_labels.py

