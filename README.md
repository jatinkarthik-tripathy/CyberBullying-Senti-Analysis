# CyberBullying Analysis

  

dataset: Formspring Dataset from Kaggle

> https://www.kaggle.com/swetaagrawal/formspring-data-for-cyberbullying-detection

  

Implementation of AlBert finetuning for sentimental analysis of cyber bullying

  
  

## Instructions for training

  

1. Clone the Albert Library
> https://github.com/google-research/albert
 2. Download the pre-trained weights (this implementation uses the base weights)
 3. Ready the data to be formatted in way AlBert uses.
 4. Use the following command to run the fine-tuning script present in the AlBert library
>python -m albert.run_classifier --data_dir="data/" --output_dir="outputs/" --spm_model_file="albert_base/30k-clean.model" --init_checkpoint="albert_base/model.ckpt-best" --albert_config_file="albert_base/albert_config.json" --do_train --do_eval --task_name=CoLA --max_seq_length=512 --optimizer=adamw --warmup_step=320 --learning_rate=1e-5 --train_step=5336 --save_checkpoints_steps=100 --vocab_file="albert_base/30k-clean.vocab" --train_batch_size=4

#### Important args
- data_dir -> Dir where the train.tsv file is present (Note: the .tsv files must be in subdir CoLA as we are using CoLA for the training method)
- output_dir -> Where you store the outputs.
- spm_model_file -> The model.
- init_checkpoint -> Initial checkpoint to start fine-tuning from.
- vocab_file -> AlBert vocab file
- do_train -> Flag to start training.
- do_eval -> Flag to eval at each ckpt.
- train_batch_size -> batch size whilst training, if mem error occurs reduce this value


## Instructions for testing 
1. Use the following command
> python run_classifier.py --task_name=cola  --do_predict=true  --data_dir="data/" --vocab_file="albert_base/30k-clean.vocab" --albert_config_file="albert_base/albert_config.json" --init_checkpoint=\BERT\bert_output\model.ckpt-1085250 --max_seq_length=512  --output_dir="outputs"