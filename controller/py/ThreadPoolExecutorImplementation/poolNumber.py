
from concurrent.futures import ThreadPoolExecutor

def task(n):
	print("Processing {}".format(n))

def main():
	print("Starting ThreadPoolExecutor")
	with ThreadPoolExecutor(max_workers=2) as executor:
	   future = executor.submit(task, (3))
	   future = executor.submit(task, (2))
	   future = executor.submit(task, (4))
	   future = executor.submit(task, (5))
	   future = executor.submit(task, (6))
	   future = executor.submit(task, (7))
	   future = executor.submit(task, (8))
	   future = executor.submit(task, (9))
	   future = executor.submit(task, (10))
	   future = executor.submit(task, (11))
	   future = executor.submit(task, (12))
	   future = executor.submit(task, (13))
	   future = executor.submit(task, (14))
	   future = executor.submit(task, (15))
	   
	print("All tasks complete")
  
if __name__ == '__main__':
 main()
