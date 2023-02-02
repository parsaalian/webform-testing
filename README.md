# webform-testing
Source code for webform testing automation project

# Setup environment
- Install conda package manager.
- Create python environment with required dependencies

```
Create The following steps create an isolated environment webform-env and install required dependencies.
conda create --name webform-env python=3.9 # creates the webform-env environment
conda activate webform-env                 # activates the codex-env environment
conda install openai                       # installs dependency - openai
```

# Models
- [BLIP]() for get context from image to text 
- [MarkupLM](https://github.com/microsoft/unilm/tree/master/markuplm) to understand the web page layout better