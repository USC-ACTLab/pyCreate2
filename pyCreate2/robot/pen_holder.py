"""
Module to control a pen holder.
"""

import servo
import math


class PenHolder:
    def __init__(self, number):
        self.servo = servo.Servo(number)

    def go_to(self, height):
        """Go to specified target height.

        Args:
            height (float): TIODODODODODODO -90 - 90 degrees. 0 means facing forward. Negative numbers turn to the left.
        """
        self.servo.go_to(height * 20)
