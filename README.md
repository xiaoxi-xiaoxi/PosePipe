# PosePipe
Blender Motion Capture using your camera!
![Screenshot](/screenshots/PosePipeScreenshot.png)
![GIF](/screenshots/PosePipeDemo4.gif)

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

## Install Manually python dependences
OSX:
- `/Applications/Blender.app/Contents/Resources/3.0/python/bin/pip3 install opencv-python mediapipe protobuf --target=/Applications/Blender.app/Contents/Resources/3.0/python/lib/python3.9`

## Troubles and solutions

Blender3 + Python3.10 on OSX: ***numpy.core._multiarray_umath***
- `/Applications/Blender.app/Contents/Resources/3.0/python/bin/pip3 install numpy --target=/Applications/Blender.app/Contents/Resources/3.0/python/lib/python3.9 --upgrade`

Blender3 + Python3.10 on OSX: ***mediapipe.python._framework_bindings***
- `/Applications/Blender.app/Contents/Resources/3.0/python/bin/pip3 install mediapipe --upgrade --target=/Applications/Blender.app/Contents/Resources/3.0/python/lib/python3.9`

## Credits

forked from [BlendyPose by Zonkosoft](https://github.com/zonkosoft/BlendyPose)

BlendyPose is made using [MediaPipe](https://github.com/google/mediapipe), [OpenCV](https://github.com/opencv/opencv-python)

[Nicholas Renotte](https://www.youtube.com/c/NicholasRenotte) provided some Mediapipe knowledge.

[Anton Sychev](https://github.com/klich3) contribute and update code for run on Mac OSX

weixin_44834086 demonstrated how to downgrade protobuf, which makes mediapipe compatible with Blender 3 and up!