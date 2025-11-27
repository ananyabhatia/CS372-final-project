# SETUP.md

## Overview
1. You will need to create a Python environment (ex. conda)
2. Activate the environment
3. Install dependencies from requirements.txt
4. Choose that environment when running the notebooks
5. Run the notebooks

### Environment
Actually create environment with: 
```conda create -n cs372 python=3.10```
Activate environment with:
```conda activate cs372```
Install dependencies with: 
```pip install -r requirements.txt```


### Running Notebooks
Go to the notebook you want to run under notebooks/
In the top left of the notebook you should see an icon that asks you to choose your kernel / environment.
Choose the environment you just created. 
Run any cells you want to run!

### Recommended things to try
You can quickly run inference by going to notebooks/Inference.ipynb and running all the cells (assuming you have the weights in the models folder) Cells 7 and 9 are the cells that actually run inference. Cell 7 uses the fine tuned ResNet and cell 9 uses the baseline CNN model. Line 2 of both cell 7 and cell 9 can be changed to try different images of food from the test set. Simply change the number in the square brackets.
If you want to create your own model weights you should go to notebooks/FullPipeline.ipynb. You can see multiple cells for training of the models if you would like to do hyperparameter tuning, and you can test on the validation set in the last cell in this file. 


