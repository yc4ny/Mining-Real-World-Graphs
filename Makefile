run:
	python label_propagation/label_propagation.py --input data/git_web_ml/musae_git_edges.csv --assignment-output output/musae_git.json --rounds 30
	python preprocess/preprocess_kl.py --input_dir output/musae_git.json --original_edges data/git_web_ml/musae_git_edges.csv --output_dir data/processed_communityDetection/processed_musae_git.txt
	python baselines/Kl_partitioning/kl.py --input data/processed_communityDetection/processed_musae_git.txt
	