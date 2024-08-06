# End-to-end-Cell-Segmentation-Using-Yolo-v8

## Workflows

1. constants
2. entity
3. components
4. pipelines
5. app.py

## STEPS TO RUN
```bash
conda create -n cellseg python=3.10 -y
```

```bash
conda activate cellseg
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```

## Run from terminal:

docker build -t cellseg1.azurecr.io/cell:latest . (Replace cellseg1.azurecr.io with your own Azure Container Registry (ACR) domain to correctly tag and push Docker images to your registry.)

docker login cellseg1.azurecr.io ( provide credentails)

docker push cellseg1.azurecr.io/cell:latest


