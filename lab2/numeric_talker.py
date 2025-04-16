import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int8


class NumericTalker(Node):
    def __init__(self):
        super().__init__('numeric_talker')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.int_pub = self.create_publisher(Int8, 'numeric_chatter', 10)

        timer_in_seconds = 0.5
        self.timer = self.create_timer(timer_in_seconds, self.talker_callback)
        self.counter = 0

    def talker_callback(self):
        msg = String()
        msg.data = f'Hello World, {self.counter}'
        self.publisher.publish(msg)
        
        int_msg = Int8()
        int_msg.data = self.counter
        self.int_pub.publish(int_msg)
        
        self.get_logger().info(f'Publishing: {msg.data}, {int_msg.data}')
        self.counter = (self.counter + 1) % 128
        



def main(args=None):
    rclpy.init(args=args)
    node = NumericTalker()
    rclpy.spin(node)
    rclpy.shutdown()

 
if __name__ == '__main__':
    main()


