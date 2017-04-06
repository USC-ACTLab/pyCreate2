from ..vrep import vrep as vrep
import math
import numpy as np

class Tracker:
  def __init__(self, client_id, tag_id, time, port=5555, rate=10,
    sd_x=0.01, sd_y=0.01, sd_theta=0.01):
    self._clientID = client_id
    rc, self._create = vrep.simxGetObjectHandle(self._clientID, "create",
      vrep.simx_opmode_oneshot_wait)
    self.tag_id = tag_id
    self.time = time
    self.port = port
    self.rate = rate
    self.sd_x = sd_x
    self.sd_y = sd_y
    self.sd_theta = sd_theta
    self.queried_time = time.time()

  def query(self):
    t = self.time.time()
    if t > self.queried_time + 1.0 / self.rate:
      # if np.random.random() < 0.05: # 5% chance of not detecting the tag
      #   return None
      rc, xyz = vrep.simxGetObjectPosition(
        self._clientID,
        self._create,
        -1,
        vrep.simx_opmode_oneshot)

      if rc != 0:
        return None

      x, y, z = xyz
      x += np.random.normal(0, self.sd_x)
      y += np.random.normal(0, self.sd_y)

      rc, rpy = vrep.simxGetObjectOrientation(
        self._clientID,
        self._create,
        -1,
        vrep.simx_opmode_oneshot)
      
      if rc != 0:
        return None

      roll, pitch, yaw = rpy
      yaw = math.fmod(yaw + np.random.normal(0, self.sd_theta), 2 * math.pi)

      self.queried_time = t

      return {
        'id': self.tag_id,
        'time': t,
        'position': dict(zip('xyz', (x, y, z))),
        'orientation': dict(zip('rpy', (roll, pitch, yaw)))
      }

    return None

  def close(self):
    self.running = False