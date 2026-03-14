#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import serial
import time

# Initialize serial communication with Arduino
arduinoData = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2)  # Wait for Arduino to reset

class SerialNode(Node):
    def __init__(self):
        super().__init__("motor_serial_node")

        # Create subscriber for motor control
        self.subscription = self.create_subscription(
            String,
            'motor_control',
            self.command_callback,
            10
        )

        self.get_logger().info("✅ Motor Serial Node Initialized")
        self.get_logger().info("Enter '1'=Forward, '0'=Backward, 's'=Stop")

        # Interactive input loop
        while True:
            myCmd = input("Enter command: ").strip()
            if myCmd in ['1', '0', 's']:
                arduinoData.write(myCmd.encode())
                self.get_logger().info(f"Sent command: {myCmd}")
            else:
                self.get_logger().warn("Invalid input. Use '1', '0', or 's'.")

    def command_callback(self, msg):
        """Callback for topic messages"""
        cmd = msg.data.strip()
        if cmd in ['1', '0', 's']:
            arduinoData.write(cmd.encode())
            self.get_logger().info(f"Sent command from topic: {cmd}")
        else:
            self.get_logger().warn("Invalid topic command received.")


def main(args=None):
    rclpy.init(args=args)
    serial_node = SerialNode()
    rclpy.spin(serial_node)
    serial_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
