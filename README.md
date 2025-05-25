# Ultrasonic RViz2 Visualization

**Clone & Build**

cd ultrasonic_sensor_data_visualization_using_Rviz2/ros2_ws
colcon build
source ./install/setup.bash
Upload arduino/ultrasonic_sensor.ino to your Arduino using arduino ide and set the suitable baud rate in my project i have used **115200** if you prefer to use the same ensure you set **Serial.begin(11200)**.

Launch publisher:
ros2 run wall_distance_publisher sensor_publisher

In another shell:
ros2 run wall_distance_publisher visualize_node

In another shell:
rviz2 -d rviz/ultrasonic_display.rviz

---
With this in place, **anyone** can:
1. git clone  
2. colcon build  
3. Upload the .ino  
4. ros2 run  
5. Open RViz2  
