python -u demo.py \
        --config config/nemo-256.yaml \
        --checkpoint "log/nemo-256 16_04_23_16.32.22/00000009-checkpoint.pth.tar" \
		--source_image assets/source_vox_priyavrat.png \
		--driving_video assets/driving_vox_chan.mp4 \
        --result_video results/result_nemo_chan_priyavrat.gif \
        --img_shape '256,256'

exit 0