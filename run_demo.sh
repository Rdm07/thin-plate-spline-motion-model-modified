python -u demo.py \
        --config config/ted-384.yaml \
        --checkpoint checkpoints/ted.pth.tar \
		--source_image assets/source_ted_rohan.jpeg\
		--driving_video assets/driving_ted_biswas.mp4 \
        --result_video results/result_ted_biswas_rohan.mp4 \
        --img_shape '256,256'

exit 0