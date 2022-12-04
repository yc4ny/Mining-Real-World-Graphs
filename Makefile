run:
	python label_propagation/label_propagation.py --input data/facebook_clean_data/artist_edges.csv --assignment-output output/artist.json --rounds 30
	python preprocess/preprocess_kl.py --input_dir output/artist.json --original_edges data/facebook_clean_data/artist_edges.csv --output_dir data/processed_communityDetection/processed_artist.txt
	python baselines/Kl_partitioning/kl.py --input data/processed_communityDetection/processed_artist.txt
	