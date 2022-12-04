run:
	python label_propagation/label_propagation.py --input datasets/facebook_clean_data/artist_edges.csv --output outputs/output_LP/artist.json
	python preprocess/preprocess_LP.py --input outputs/output_LP/artist.json --output outputs/output_preprocess/processed_artist.txt --original_edges datasets/facebook_clean_data/artist_edges.csv
	python baseline/kl_partitioning/kl.py --input outputs/output_preprocess/processed_artist.txt --output outputs/output_KL/partitioned_artist.txt
	