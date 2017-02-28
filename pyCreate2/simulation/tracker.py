from ..vrep import vrep as vrep

class Tracker:
  def __init__(self, client_id, tag_id, time, port = 5555, rate = 10):
    self._clientID = client_id
    rc, self._create = vrep.simxGetObjectHandle(self._clientID, "create",
      vrep.simx_opmode_oneshot_wait)
    self.tag_id = tag_id
    self.time = time
    self.port = port
    self.rate = rate
    self.queried_time = time.time()

  def query(self):
    t = self.time.time()
    if t > self.queried_time + 1.0 / self.rate:
      self.queried_time = t
      rc, xyz = vrep.simxGetObjectPosition(
        self._clientID,
        self._create,
        -1,
        vrep.simx_opmode_oneshot)

      rc, rpy = vrep.simxGetObjectOrientation(
        self._clientID,
        self._create,
        -1,
        vrep.simx_opmode_oneshot)

      return {
        'id': self.tag_id,
        'time': t,
        'position': dict(zip('xyz', xyz)),
        'orientation': dict(zip('rpy', rpy))
      }

    return None

  def close(self):
    self.running = False