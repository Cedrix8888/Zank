### positive_prompt for test: A marketing poster promoting Coca-Cola
## error logs
### 2025.7.31: UNet1024 missing keys: temb_channel
### version_3: first release implemented on mps but failed for some mps's restriction and memory insufficiency
### t2i: glass bottle, high quality
### iti: a handsome man with curly hair, high quality




## log in Colab
/content# git clone https://github.com/Cedrix8888/Zank.git
Cloning into 'Zank'...
remote: Enumerating objects: 138, done.
remote: Counting objects: 100% (138/138), done.
remote: Compressing objects: 100% (97/97), done.
remote: Total 138 (delta 46), reused 118 (delta 26), pack-reused 0 (from 0)
Receiving objects: 100% (138/138), 10.73 MiB | 50.85 MiB/s, done.
Resolving deltas: 100% (46/46), done.
Filtering content:                        
  100% (3/3), 1.97 GiB | 75.96 MiB/s, done.
/content# cd Zank
/content/Zank# git checkout cuda
Branch 'cuda' set up to track remote branch 'cuda' from 'origin'.
Switched to a new branch 'cuda'
/content/Zank# python t2i.py
2025-08-04 08:32:28.222365: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1754296348.242613    2141 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1754296348.248766    2141 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
2025-08-04 08:32:28.269658: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
tokenizer_config.json: 100%|█| 737/737 [00
vocab.json: 1.06MB [00:00, 23.0MB/s]
merges.txt: 525kB [00:00, 71.4MB/s]
special_tokens_map.json: 100%|█| 472/472 [
tokenizer_config.json: 100%|█| 725/725 [00
special_tokens_map.json: 100%|█| 460/460 [
config.json: 100%|█| 560/560 [00:00<00:00,
model.fp16.safetensors: 100%|█| 246M/246M 
config.json: 100%|█| 570/570 [00:00<00:00,
model.fp16.safetensors: 100%|█| 1.39G/1.39
config.json: 100%|█| 602/602 [00:00<00:00,
diffusion_pytorch_model.fp16.safetensors: 
config.json: 1.68kB [00:00, 7.55MB/s]
diffusion_pytorch_model.fp16.safetensors: 
Please enter positive prompt.A marketing poster promoting Coca-Cola
100%|█████| 25/25 [00:20<00:00,  1.20it/s]
100%|█████████████████████████████████████████████| 8/8 [00:02<00:00,  3.55it/s]