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
<b>Format</b><br/> 
The code takes an input graph in a csv/txt file. Each row of the file indicates an edge between the two nodes separated by a comma.<br/><br/>
For small sample tests. there are custom test graphs in the  ` data/custom ` folder. <br/><br/>
If you wish to test on real world graphs, please download the network data from Stanford Large Network Dataset Collection here: <a href="https://snap.stanford.edu/data/" target="_blank">SNAP</a>, unzip and place the csv files in the ` data/`  folder.  <br/><br/>
To partition other graphs, please match the format of the input graph as stated above. 

## Community Detection - Label Propagation 
<p align= "center">
<img src="readme_img/cluster.png" width="300" height="300" alt="Clustering" class="center"/><br/><br/>
</p>
The Label Propagation algorithm is a fast algorithm for finding communities in a graph, while detecting these communites using the network structure alone as its guide and does not require a pre-defined objective function or prior informations about the communities. The quality of community detection is determined with the modularity value.

### Options

Clustering the input graph is done by the `label_propagation/label_propagation.py` script which provides the following command line arguments. <br/>

#### Model options

```
  --input               STR    Input graph path.                                     
  --assignment-output   STR    Node-cluster assignment dictionary path.                     
  --rounds              INT    Number of iterations.      
```
#### Example for running label propagation on the sample data
```
python label_propagation/label_propagation.py --input data/custom/sample_data.txt --assignment-output output/sample_data.json --rounds 20
```
Detected communities will be in the form of a `.json` file which can be found in  `output` folder. <br/>

## Graph Partitioning - Kernighan-Lin 
<p align= "center">
<img src="readme_img/kl.png" width="400" height="300" alt="KL" class="center" /><br/><br/>
</p>
The Kernighan-Lin (KL) algorithm takes an undirected graph as input and partitions the vertices into two disjoint subsets A,B of equal(or nearly equal) size, in a way that minimizes the sum of the weights of the subsets of edges that cross from A,B.


