<!-- COMMANDS TO RUN  -->
conda create -n env39 python=3.9
conda activate env39

rasa train
rasa run actions
rasa shell

