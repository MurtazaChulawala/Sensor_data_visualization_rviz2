import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from visualization_msgs.msg import Marker

class DistanceVisualizer(Node):
    def __init__(self):
        super().__init__('distance_visualizer')
        self.subscription = self.create_subscription(
            String,
            'sensor_data',
            self.listener_callback,
            10)
        self.publisher = self.create_publisher(Marker, 'visualize', 10)
        self.get_logger().info('Distance Visualizer Node Started.')

    def listener_callback(self, msg):
        try:
            distance = float(msg.data.split('=')[-1].strip())
        except ValueError:
            self.get_logger().warn(f"Failed to parse: {msg.data}")
            return

        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "wall_marker"
        marker.id = 0
        marker.type = Marker.CUBE
        marker.action = Marker.ADD

        marker.pose.position.x = distance / 200.0  # place cube halfway between robot and wall
        marker.pose.position.y = 0.0
        marker.pose.position.z = 0.0
        marker.pose.orientation.w = 1.0

        marker.scale.x = distance / 100.0  # wall thickness = distance
        marker.scale.y = 0.01  # very thin wall visually
        marker.scale.z = 0.3   # height of the wall (adjust as needed)

        marker.color.a = 1.0
        marker.color.r = 0.2
        marker.color.g = 0.5
        marker.color.b = 1.0

        self.publisher.publish(marker)
        self.get_logger().info(f'Visualized wall at {distance:.2f} cm')

def main(args=None):
    rclpy.init(args=args)
    node = DistanceVisualizer()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
