import numpy as np
import cv2
import time
import random
import sys

class Freak:
   def __init__(self, _threshold=10):     
      self.threshold = _threshold

   def computeDes(self, img, kp):
      
      len_kp_before = len(kp)
      
      kp_before = kp
      
      brief = cv2.DescriptorExtractor_create("FREAK")
      kp, des = brief.compute(img, kp)
      
      len_kp_after = len(kp)
      
      if len_kp_before != len_kp_after:
         print "Before: " + str(len_kp_before)
         print "After: " + str(len_kp_after)
         print "ERROR: NUMBER OF KP DIFFERENT AFTER DESCRIPTOR"
         sys.exit()        
      
      return des
   
   def writeParametersDes(self, f):
      f.write("Keypoint Descriptor FREAK with parameters: ")
      f.write("DEFAULT")
      f.write('\n')     
   