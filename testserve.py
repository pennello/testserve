# chris 070815

import socket
import sys

from argparse import ArgumentParser

bufsize = 4096

def main():
  descr = ('Test TCP server. Prints received data to standard out. '
    'Handles one connection only and does not automatically disconnect.')
  parser = ArgumentParser(description=descr)
  parser.add_argument('host', help='host to bind to')
  parser.add_argument('port', type=int, help='port on which to bind')
  args = parser.parse_args()

  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind((args.host,args.port))
  s.listen(0)
  try:
    conn,addr = s.accept()
    while True:
      data = conn.recv(bufsize)
      sys.stdout.write(data)
  except KeyboardInterrupt: pass

  # This server is generic, so there is no detection of when we're done.
  # Just Ctrl+C (and deal with TIME-WAIT).
  # Sockets closed implicitly on process termination.

main()
