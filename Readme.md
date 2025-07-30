<!-- COMMANDS TO RUN  -->
```
cd rasa_project
pip install -r requirements.txt
conda create -n env39 python=3.9
conda activate env39
rasa init --no-prompt
rasa train
rasa run actions
rasa shell
```

