# -*- coding: utf-8 -*-
from check_module import check
from check_in_module import check_in
from check_out_module import check_out
from face_compare_module import face_compare 
from face_catch_module import face_catch
import sys

def main():
#check_in()
#check()
#check_out()
#camera_module.show_webcam()
#face_compare(0)
#face_catch(0)
    if len(sys.argv) is 1:
        print("face_catch or face_compare");
    else:
        if(sys.argv[1] == "face_catch"):
            face_catch(0)
        if(sys.argv[1] == "face_compare"):
            face_compare(0)

if __name__ == '__main__':
    main()
