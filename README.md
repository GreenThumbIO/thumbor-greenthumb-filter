# Calibrate Leaf and Bud Area Functions

## HSV Range Detector Calibration
```
open -a XQuartz
ip=$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')
display_number=`ps -ef | grep "Xquartz :\d" | grep -v xinit | awk '{ print $9; }'`
/opt/X11/bin/xhost + $ip
```
### Run bash into container
`docker run -it --rm -e DISPLAY=$ip:0 -v /tmp/.X11-unix:/tmp/.X11-unix tensorflow-notebook /bin/bash`
### Run the detector
`range-detector --filter HSV --image work/test3.png --preview`
