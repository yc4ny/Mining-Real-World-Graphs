# Partitioning Real World Graphs with <br/> Label Propagation for Community Detection
Implementation of the term project for the course M2177.003000 Advanced Data Mining Course at SNU.<br/> 

![Real World Graph Partitioning](readme_img/intro.png)<br/>
> - Left image indicates a poor partitioned graph. There are many inter-partition links <br/>
> - Right image indicates a good partitoned graph. Vertices that are highly connected are assigned to the same partition.<br/>
> - Our method aims to reduce the number of vertex-cuts in the final partitioned graph. 


## Environment Setup
> Note: This code was developed on Ubuntu 20.04 with Python 3.5. Later versions should work, but have not been tested.<br/>
> Create and activate a virtual environment to work in, e.g. using Conda: <br/>

```
conda create -n venv_graph python=3.5
conda activate venv_graph
```
> The codebase is implemented in Python 3.5.2 | Anaconda 4.2.0 (64-bit). Package versions used for development are just below.
```
networkx          2.4
tqdm              4.64.1
numpy             1.18.5
pandas            0.25.3        
python-louvain    0.11
texttable         1.6.7
```

> Install the requirements with pip:
```
pip install -r requirements.txt
```
## Datasets
The code takes an input graph in a csv/txt file. Each row of the file indicates an edge between the two nodes separated by a comma.<br/><br/>
For sample tests there are custom test graphs in the  ` data/custom ` folder. <br/><br/>
If you wish to test on real world graphs, please download the network data from Stanford Large Network Dataset Collection at `https://snap.stanford.edu/data/`, and place it in the ` data/`  folder. 

## Options

Creating a clustering is handled by the `src/label_propagation.py` script which provides the following command line arguments.

### Model options

```
  --input               STR    Input graph path.                          Default is `data/politician_edges.csv`.                                     
  --assignment-output   STR    Node-cluster assignment dictionary path.   Default is `output/politician.json`.
  --weighing            STR    Weighting strategy.                        Default is `overlap`.
  --rounds              INT    Number of iterations.                      Default is 30.
  --seed                INT    Initial seed           .                   Default is 42.
```







