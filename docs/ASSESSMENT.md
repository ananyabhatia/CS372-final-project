# Self Assessment

## Machine Learning Category:

### Core ML Fundamentals
**Modular code design with reusable functions and classes rather than monolithic scripts (3 pts):** See entire codebase, most notably the src folder with functions and classes only. All functions are put together cleanly in notebooks. 
**Implemented proper train/validation/test split with documented split ratios (3 pts):** See src/data.py/build_records function with splits and notebooks/FullPipeline.ipynb cell 2 for split ratios (sizes) 
**Used appropriate data loading with batching and shuffling (PyTorch DataLoader or equivalent) (3 pts):** See src/data/get_dataloaders function with DataLoaders, batch sizes, and shuffling. See notebooks/FullPipeline.ipynb cell 4 to see this function being called. 
**Created baseline model for comparison (e.g., constant prediction, random, simple heuristic) (3 pts):** See notebooks/FullPipeline.ipynb cell 5 to train and build the TinyCNN baseline model for comparison. See notebooks/Inference.ipynb cells 7 and 8 to see loading pretrained weights and using the baseline model. 

### Data Collection, Preprocessing, & Feature Engineering
**Properly normalized or standardized input features/data appropriate to your modality (3 pts):** See src/data.py/get_dataloaders function to see the transforms to see how I have Normalized the features. The numbers used for these come from ImageNet and are therefore appropriate to my modality of trying to understand images. 

### Model Training & Optimization
**Trained model using GPU/TPU/CUDA acceleration (5 pts):** See notebooks/Inference.ipynb and notebooks/FullPipeline.ipynb cell 1 to find the torch.device. To actually train the model weights in models/baseline_weights.pth and models/resnet_finetuned_weights.pth I used GPU acceleration on Google CoLab since they have a free student version of Pro. 

**Defined and trained a custom (substantially designed by you, not a pretrained model) neural network architecture using PyTorch or similar framework (5 pts):** See src/model.py/TinyCNN class to see the definition of the custom NN architecture using PyTorch and src/model.py/build_baseline_model function to see building function. See src/train.py/train_baseline_model function to see training function. See notebooks/FullPipeline.ipynb cell 5 to see the training of this NN model. 

### Transfer Learning & Pretrained Models
**Fine-tuned pretrained model on your dataset (ResNet, BERT, GPT, Llama, etc.) with appropriate adaptation (5 pts):** See src/train.py/train_resnet_model function to see fine tuning function. See src/model.py/build_resnet_model function to see building function. This is where appropriate adaptation can be seen (replacing final layer with the number of classes needed). See notebooks/FullPipeline.ipynb cell 7 to see building and fine tuning ResNet. 

### Computer Vision
**Used or fine-tuned vision convolutional neural network architecture (5 pts):** See src/train.py/train_resnet_model function to see fine tuning function. See src/model.py/build_resnet_model function to see building function. See notebooks/FullPipeline.ipynb cell 7 to see building and fine tuning ResNet. 

### Natural Language Processing
**Used or fine-tuned a transformer language model (7 pts):** See src/inference.py/load_text_generator to see loading function. See notebooks/FullPipeline.ipynb cell 10 and notebooks/Inference.ipynb cells 7 and 9 to call this function with microsoft/phi-2 which is a transformer language model. 

### Advanced System Integration
**Built multi-stage ML pipeline connecting outputs of one model to inputs of another (e.g., vision model to a language model to a text-to-speech model) (7 pts):** See src/inference.py/generate_recipe_from_image function to see the full ML pipeline in action. This gets the outputs from the CNN and then turns it into a list of ingredients, then passes in that list of ingredients as a prompt into the pipe which is an LLM. See notebooks/FullPipeline.ipynb cell 10 and notebooks/Inference.ipynb cells 7 and 9 to see calls to this function. 


### Solo Project Credit
**Completed project individually without a partner (10 pts):** See whole project. 

## Following Directions Category

### Submission and Self-Assessment (3 points each)
**Ontime submission by 5 pm on Friday, December 5th Tuesday, December 9th (note that late submissions will be accepted but only for the normal 72 hour late period, and will not qualify for this rubric item):** See submission time. 
**Self-assessment submitted that follows guidelines for at most 15 selections in Machine Learning with evidence (note that failing to submit a self-assessment may result in a loss of credit for some overlooked rubric items during grading):** Well, if you're reading this document I think you know where to find this. 

### Basic Documentation (2 points each)
**SETUP.md exists with clear, step-by-step installation instructions:** See SETUP.md file. 
**ATTRIBUTION.md exists with detailed attributions of all sources including AI-generation information:**  See ATTRIBUTION.md file.
**requirements.txt or environment.yml file is included and accurate:** See requirements.txt file.

### README.md (1 point each)
**README.md has What it Does section that describes in one paragraph what your project does:** See README.md.
**README.md has Quick Start section that concisely explains how to run your project:** See README.md.
**README.md has Video Links section with direct links to your demo and technical walkthrough videos:** See README.md.
**README.md has Evaluation section that presents any quantitative results, accuracy metrics, or qualitative outcomes from testing:** See README.md for qualitative outcomes from testing.
**README.md has Individual Contributions section for group projects that describes who did what:** See README.md.

### Video Submissions (2 points each)
Demo video is of the correct length and appropriate for non-specialist audience with no code shown
Technical walkthrough is of the correct length and clearly explains code structure, ML techniques, and key contributions

### Project Workshop Days (1 points each)
**Attended 1-2 project workshop days:** See attendance.
**Attended 3-4 project workshop days:** See attendance.
**Attended 5-6 project workshop days:** See attendance.

## Project Cohesion Category
### Project Purpose and Motivation (3 points each)
**README clearly articulates a single, unified project goal or research question:** See README.md and What It Does section. 
**Project demo video effectively communicates why the project matters to a non-technical audience in non-technical terms:** See demo video. 
**Project addresses a real-world problem or explores a meaningful research question:** See README.md and What It Does section.

### Technical Coherence (3 points each)
**Technical walkthrough demonstrates how components work together synergistically (not just isolated experiments):** See technical walkthrough. 
**Project shows clear progression from problem → approach → solution → evaluation:** See technical walkthrough. 
**Design choices are explicitly justified in videos or documentation:** See technical walkthrough. 
**None of the major components awarded rubric item credit in the machine learning category are superfluous to the larger goals of the project (no unrelated "point collecting"):** See this document. 
**Clean codebase with readable code and no extraneous, stale, or unused files:** See codebase. 