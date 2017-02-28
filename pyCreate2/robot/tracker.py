import sys
import time
import socket
import pickle
import threading

class Tracker:
  def __init__(self, tag_id, port = 5555):
    self.tag_id = tag_id
    self.port = port
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.sock.bind(('', self.port))
    self.sock.settimeout(3)
    self.running = True
    self.queried_frame = -1
    self.new_data = None
    self.thread = threading.Thread(target=self.spin, args=(self.data_callback,))
    self.thread.start()

  def data_callback(self, data):
    self.new_data = data

  def spin(self, callback):
    while self.running:
      try:
        data, addr = self.sock.recvfrom(10240)
        data = pickle.loads(data)
        callback(data)
      except socket.timeout:
        pass

  def query(self):
    data = self.new_data
    # print(data)
    if data is not None and data['frame_id'] > self.queried_frame:
      found = None
      for detection in data['detections']:
        if detection['id'] == self.tag_id:
          found = detection
          break
      self.queried_frame = data['frame_id']
      return found
    return None

  def close(self):
    self.running = False