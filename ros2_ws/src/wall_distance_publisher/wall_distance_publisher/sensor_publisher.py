import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

class SensorPublisher(Node):
    def __init__(self):
        super().__init__('sensor_publisher')
        self.publisher_ = self.create_publisher(String, 'sensor_data', 10)

        try:
            self.ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
            time.sleep(3)
        except serial.SerialException as e:
            self.get_logger().error(f"Failed to open serial port: {e}")
            self.ser = None

        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        if self.ser and self.ser.is_open:
            if self.ser.in_waiting > 0:
                line = self.ser.readline().decode('utf-8').strip()
                msg = String()
                msg.data = line
                self.get_logger().info(f'Published: "{msg.data}"')
                self.publisher_.publish(msg)
        else:
            self.get_logger().warn('Serial port is not open!')

    
def main(args=None):
    rclpy.init(args=args)
    node = SensorPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        print("KeyboardInterrupt received. Shutting down.")
        node.ser.close()
        node.destroy_node()
        rclpy.shutdown()