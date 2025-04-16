import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.subscription = self.create_subscription(String, 'chatter', self.listener_callback, 10)
        self.subscription1 = self.create_subscription(String, 'numeric_chatter', self.listener_callback_int, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: {msg.data!r}')


def main(args=None):
    rclpy.init(args=args)
    node = NumericListener()
    rclpy.spin(NumericListener)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
