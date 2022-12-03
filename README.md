# Partitioning Real World Graphs with <br/> Label Propagation for Community Detection
Implementation of the term project for the course M2177.003000 Advanced Data Mining Course at SNU.<br/> 

![Real World Graph Partitioning](readme_img/intro.png)<br/>
> - Left image indicates a poor partitioned graph. There are many inter-partition links <br/>
> - Right image indicates a good partitoned graph. Vertices that are highly connected are assigned to the same partition.<br/>
> - Our method aims to reduce the number of vertex-cuts in the final partitioned graph. 


## Environment Setup
> Note: This code was developed on Ubuntu 20.04 with Python 3.5. Later versions should work, but have not been tested.
Create and activate a virtual environment to work in, e.g. using Conda: <br>

conda create -n venv_graph python=3.5
conda activate venv_graph

The codebase is implemented in Python 3.5.2 | Anaconda 4.2.0 (64-bit). Package versions used for development are just below.
```
networkx          2.4
tqdm              4.28.1
numpy             1.15.4
pandas            0.23.4
jsonschema        2.6.0
python-louvain    0.11
texttable         0.15.0
```

Install the remaining requirements with pip:
```
pip install -r requirements.txt
```

You must also have _ffmpeg_ installed on your system to save visualizations. <br/><br/>
I have used 5 _GOPRO10_ cameras for this task. If you are using more or less cameras, you need to modify the DLT, optimization code. 





