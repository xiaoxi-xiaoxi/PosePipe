# PosePipe & Media Pipe
Blender Motion Capture using your camera or stream camera!

![Screenshot](/screenshots/PosePipeScreenshot.png)
![GIF](/screenshots/PosePipeDemo4.gif)
![Stream](/screenshots/PosePipeStream.png)

## Note
This will install to Blender's Python path, rather than your system's.

## Install
1 - Open Blender
2 - Download repo in zip file
3 - Go to Edit > Preferences > Add Ons > Install Add on, then select <zip> file
4 - Open the BlendyPose panel
    On Open is checks for dependencies for proper work, click Install
    ![Dependencies](/screenshots/PosePipeDependencies.png)

5 - Click Start Camera! or Load Video File

***Options Extra:***
    - Flip Horizontal for selfies
    - Mask background


## Install Manually python dependences
OSX:
- `/Applications/Blender.app/Contents/Resources/3.0/python/bin/pip3 install opencv-python mediapipe protobuf --target=/Applications/Blender.app/Contents/Resources/3.0/python/lib/python3.9`

## Troubles and solutions

Blender3 + Python3.10 on OSX: ***numpy.core._multiarray_umath***
- `/Applications/Blender.app/Contents/Resources/3.0/python/bin/pip3 install numpy --target=/Applications/Blender.app/Contents/Resources/3.0/python/lib/python3.9 --upgrade`

Blender3 + Python3.10 on OSX: ***mediapipe.python._framework_bindings***
- `/Applications/Blender.app/Contents/Resources/3.0/python/bin/pip3 install mediapipe --upgrade --target=/Applications/Blender.app/Contents/Resources/3.0/python/lib/python3.9`

Blender crash on connect to the camera:
- ![You need extra OSX permissions to use Camera](https://apple.stackexchange.com/questions/360851/add-access-to-the-macbook-camera-for-the-terminal-application)
- ![Add access to the macbook camera for the terminal application](https://apple.stackexchange.com/questions/360851/add-access-to-the-macbook-camera-for-the-terminal-application)

  Method 1: in Finder go to `/Applications/Blender.app/Contents/MacOS/` click right click and Open in Terminal
  Method 2: in Terminal run `/Applications/Blender.app/Contents/MacOS/Blender`

  ![This solution](https://blender.stackexchange.com/questions/248198/piping-blender-camera-to-python-opencv-webcam/284215#284215)


### Camera setup:
- -1 Linux
- 0 (Windows, Osx build-in "laptop", Linux)
- 1 (Osx iPhone)

### Docs

***Stream:***
Now you can connect to any stream camera using "JMPEG" format or RTSP stream.
For simple camera stream I recomend to use ESP32
    - Arduino > Examples > ESP32 > Camera > CameraWebServer
    - [esp32cam-rtsp](https://github.com/rzeldent/esp32cam-rtsp)
    - [esp32cam-example1](https://randomnerdtutorials.com/esp32-cam-video-streaming-web-server-camera-home-assistant/)
    - [esp32cam-example2](https://www.hackster.io/onedeadmatch/esp32-cam-python-stream-opencv-example-1cc205)

***MediaPipe:***
    - [MediaPipe Documentation](https://google.github.io/mediapipe/)


## Credits

forked from [BlendyPose by Zonkosoft](https://github.com/zonkosoft/BlendyPose)

BlendyPose is made using [MediaPipe](https://github.com/google/mediapipe), [OpenCV](https://github.com/opencv/opencv-python)

[Nicholas Renotte](https://www.youtube.com/c/NicholasRenotte) provided some Mediapipe knowledge.

[Anton Sychev](https://github.com/klich3) contribute and update code for run on Mac OSX

weixin_44834086 demonstrated how to downgrade protobuf, which makes mediapipe compatible with Blender 3 and up!

### TODO

    [x] modal notify of errors or no possibility to connect
    [] save processed data to file
    [] load data from processed file 

    [x] separate methods mediapipe to file
    [] add yolo engine
    [x] add selector for preview -> original size video input | 800x600 | other resize

### Knowledge of bugs
BUG: 
    [x] prevent crash on intent to connect to camera (osx)
    [x] prevent crash on intent to connect to stream
    [] capture is deformed on vertical axie