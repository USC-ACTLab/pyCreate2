"""
Module to control a pen holder (prismatic joint)
"""

from ..vrep import vrep as vrep
import math


class PenHolder:
    """
    Class to control a virtual pen holder in V-REP.
    The pen holder is modeled as prismatic joint and the position is set directly.
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
            height (float): target height in cm
        """
        vrep.simxSetJointPosition(self._clientID, self._joint, height,
                                        vrep.simx_opmode_oneshot_wait)
