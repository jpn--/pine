
from . import configure

_time_format = '%b %d %H:%M:%S'
_mess_format = '%(asctime)15s %(name)s %(level)s %(message)s'

def new_worker(scheduler=None, name=None, **kwargs):

	cfg = configure.load()
	if 'worker_log' in cfg.cluster:
		import logging, logging.handlers
		handler = logging.handlers.RotatingFileHandler(cfg.cluster['worker_log'], 'a', 10000, 10)
		formatter = logging.Formatter(fmt=_mess_format, datefmt=_time_format)
		handler.setFormatter(formatter)
		logging.getLogger('distributed').addHandler(handler)
		logging.getLogger('distributed').setLevel(logging.DEBUG)

	if 'scheduler' not in cfg.cluster and scheduler is None:
		raise ValueError('no scheduler known, set one in pines.configure .cluster')

	if scheduler is None:
		scheduler = cfg.cluster['scheduler']

	from distributed import Worker
	from tornado.ioloop import IOLoop
	from threading import Thread

	if name is None:
		import socket
		name = socket.getfqdn()

	loop = IOLoop.current()
	t = Thread(target=loop.start, daemon=True)
	t.start()

	w = Worker(f'tcp://{scheduler}:8786', loop=loop, name=name, **kwargs)
	w.start()  # choose randomly assigned port
	
	t.join()
	
if __name__=='__main__':
	w=new_worker()

	