CUDA_VISIBLE_DEVICES=0,1 python run.py --config config/nemo-256.yaml --log_dir "log/nemo-256 16_04_23_16.32.22" \
                    --checkpoint "log/nemo-256 16_04_23_16.32.22/00000009-checkpoint.pth.tar" --device_ids 0,1

exit 0