# OpenLLMs - Llama 2 

### Environment setup
```
conda create -n llama2 --file environment.txt
```

### Run 
SSH to bizon machine
```
ssh -A -t nashid@ssh.ece.ubc.ca ssh -t webtesting@bizon1.ece.ubc.ca
It will prompt for two passwords:
1. First the ECE password
2. Then the password for the Bizon machine i.e. for `webtesting`
```

Then run the following commands:
```
conda activate llama2
cd /home/webtesting/webform-testing/evaluation/opensource-llms/llama
python llama2.py
```