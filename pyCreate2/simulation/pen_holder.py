"""
Module to control a virtual Servo.
"""

from ..vrep import vrep as vrep
import math


class PenHolder:
    """
    Class to control a virtual servo in V-REP.
    The servo is modeled as joint, using an integrated position controller in V-REP.
    """
    def __init__(self, client_id):
        """Constructor.

        Args:
            client_id (integer): V-REP client id.
        """
        self._clientID = client_id
        # query objects
        rc, self._joint = vrep.simxGetObjectHandle(self._clientID, "Prismatic_joint", vrep.simx_opmode_oneshot_wait)
        print(rc, self._joint)

    def go_to(self, height):
        """Go to specified target height.

        Args:
            height (float): TIODODODODODODO -90 - 90 degrees. 0 means facing forward. Negative numbers turn to the left.
        """
        vrep.simxSetJointPosition(self._clientID, self._joint, height,
                                        vrep.simx_opmode_oneshot_wait)
