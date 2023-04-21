python -u demo.py \
        --config config/nemo-256.yaml \
        --checkpoint "log/nemo-256 16_04_23_16.32.22/00000004-checkpoint.pth.tar" \
		--source_image assets/source_nemo_advait.jpg \
		--driving_video assets/driving_nemo_smile1.gif \
        --result_video results/result_nemo_1_advait_5.gif \
        --img_shape '256,256'

exit 0