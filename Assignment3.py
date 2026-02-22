from ast import Store
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput
import jetson_inference
import jetson_utils

#change video input to one image input
# choose one class output

net = detectNet("ssd-mobilenet-v2", threshold=0.5)
camera = videoSource("~/Pictures/horse_0.jpg") # '/dev/video0' for V4L2
display = videoOutput("display://") # 'my_video.mp4' for file

while display.IsStreaming():
  img = camera.Capture()

  if img is None: # capture timeout
    continue

  detections = net.Detect(img)
  print(detections)

  display.Render(img)
  display.SetStatus("Object Detection | Network {:.100f} FPS".format(net.GetNetworkFPS()))
  
