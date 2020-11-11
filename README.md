# README file for project

This project contains code for building an containerized application for my
raspberry pi k8s cluster. The application assues each node in the cluster has
some neopixels attached to the gpio pins and visualizes the number of pods
running on each node.

(for the time being, the application actually just shows a rainbow visualization
of the neopixels.... work in progress)

## Files

* src/ - the source python files
* Dockerfile - to build the container
* cloudbuild.yaml - to use GCP's cloud build that uses the dockerfile to build the 
   container
* README.md - this file

## To Build

try these commands:
*  `% gcloud builds submit --config cloudbuild.yaml` : to use GCP to build the container and store in GCR
* `% docker pull gcr.io/western-reason-281919/quickstart-image` : on an RPI with docker to pull the image
* `% docker run --privileged gcr.io/western-reason-281919/quickstart-image` : to run the image.  if you have
   the neopixels plugged in, then they should start oscilating in color.

## References

* https://www.balena.io/docs/reference/base-images/base-images/  - where i got my base images from
* https://blog.hypriot.com/post/setup-simple-ci-pipeline-for-arm-images/ - how to use QEMU for building arm containers
  * https://github.com/multiarch/qemu-user-static : more details on this
* https://cloud.google.com/cloud-build/docs/quickstart-build - cloud build quickstart
* https://learn.adafruit.com/adafruit-neopixel-uberguide/python-circuitpython - neopixel library for raspberry pi
* https://www.docker.com/blog/containerized-python-development-part-1/ - containerizing python
* https://shop.pimoroni.com/products/blinkt - blinkt product that does what i'm trying to do
* https://github.com/apprenda/blinkt-k8s-controller - blinked container for k8s
* https://pleasereleaseme.net/setting-up-a-raspberry-pi-kubernetes-cluster-with-blinkt-strips-that-show-number-of-pods-per-node-using-k3sup/ - writeup for using blinkt in k8s
* https://circuitpython.readthedocs.io/projects/neopixel/en/latest/api.html#neopixel.NeoPixel.show - more neopixel docs
* https://docs.openfaas.com/deployment/kubernetes/#notes-for-raspberry-pi-32-bit-arm-armhf - k3s deployment guide
* https://github.com/openfaas/faas - openfaas quickstart on k3s
* https://opensource.com/article/20/3/kubernetes-raspberry-pi-k3s - more k3s on rpi stuff
* 


