import logging
from functools import wraps
def create_logger():
	logger = logging.getLogger('logger')
	logger.setLevel(logging.INFO)
	logfile = logging.FileHandler('logger.log')
	fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
	formatter = logging.Formatter(fmt)
	logfile.setFormatter(formatter)
	logger.addHandler(logfile)
	return logger
logger = create_logger()
print(logger)
def exception(logger):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			try:
				return func(*args, **kwargs)
			except:
				issue = "exception in "+func.__name__+"\n"
				issue = issue+"-------------------------------------------------------------------------\n"
				logger.exception(issue)
			raise
		return wrapper
	return decorator
@exception(logger)
def divideStrByInt():
	return "Hello"/7
if __name__ == '__main__':
	divideStrByInt()
