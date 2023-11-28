import cv2
import numpy as np

# https://www.pauldebevec.com/Research/HDR/
hdr_image = cv2.imread('/Users/gefeishen/Developer/Research/Playground/CV-Playground/ComputationPhotography/vinesunset.hdr',
                       cv2.IMREAD_ANYDEPTH | cv2.IMREAD_COLOR)

tonemapRein = cv2.createTonemapReinhard(gamma=2.2, intensity=2.0)
tonemapMan = cv2.createTonemapMantiuk(gamma=2.2, saturation=2)
tonemapDra = cv2.createTonemapDrago(gamma=2.2)

ldr_Reinhard = tonemapRein.process(hdr_image.copy())
ldr_Mantiuk = tonemapMan.process(hdr_image.copy())
ldr_Drago = tonemapDra.process(hdr_image.copy())

# Combine images for side by side comparison
combined = np.hstack((ldr_Reinhard,
                     ldr_Mantiuk, ldr_Drago))

# Display the images
cv2.imshow('Tone Mapping Comparison', combined)
cv2.waitKey(0)
cv2.destroyAllWindows()
