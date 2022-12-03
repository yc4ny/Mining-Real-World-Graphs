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
The codebase is implemented in Python 3.5.2 | Anaconda 4.2.0 (64-bit). Package versions used for development are just below.
```
networkx          2.4
tqdm              4.64.1
numpy             1.18.5
pandas            0.25.3        
python-louvain    0.11
texttable         1.6.7
```

Install the remaining requirements with pip:
```
pip install -r requirements.txt
```








