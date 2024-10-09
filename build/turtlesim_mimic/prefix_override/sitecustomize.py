import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/shaqiloheal/ros2_ws/install/turtlesim_mimic'
