python -u demo.py \
        --config config/vox-256.yaml \
        --checkpoint checkpoints/vox.pth.tar \
		--source_image assets/source_vox_shreyansh.jpg \
		--driving_video assets/driving_vox_chan.mp4 \
        --result_video results/result_nemo_chan_shreyansh.gif \
        --img_shape '256,256'

exit 0