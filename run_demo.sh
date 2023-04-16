BASE_DIR="."
MODEL_NAME="model1"
LOG_FOLDER=${BASE_DIR}/models/training_logs
LOG_FILE_NAME=${LOG_FOLDER}/log_training_${MODEL_NAME}.txt

python -u demo.py \
        --config config/nemo-64.yaml \
        --checkpoint checkpoints/nemo.pth.tar \
		--source_image assets/source_priyavrat.png\
		--driving_video assets/driving_int_biswas.mp4 \
        --result_video results/result_int_bis_p.mp4 \
        --img_shape '128,128'

exit 0