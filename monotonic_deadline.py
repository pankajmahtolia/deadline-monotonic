MAX_JOB_ACCEPT_TIME = 250
def add(tasks):
	sm= 0
	for i in tasks:
		sm += i.rem_bt
	return sm
class Job:
	def __init__(self, at, relative_deadline, bt, task_no):
		self.at, self.relative_deadline, self.bt = int(at), int(relative_deadline), int(bt)
		self.rem_bt = self.bt
		self.execution_seconds = list()
		self.task_no = task_no
		self.absolute_deadline = self.at+self.relative_deadline
	def execute(self, time):
		self.execution_seconds.append(time)
		self.rem_bt -= 1
	def is_finished(self):
		return True if self.rem_bt==0 else False
	def display_status(self):
		print ("Task No =",self.task_no,
			"Job: A.T =",self.at,
			", relative_deadline = ",self.relative_deadline,
			", Finished within deadline = ",len(self.execution_seconds)>0 and self.execution_seconds[-1]<=self.absolute_deadline,
			", Burst = ",self.bt,
			", Finished = ",self.is_finished(),
			", Remaining burst = ",self.rem_bt,
			", Execution at =",self.execution_seconds)

print("Enter no. of processes?")
n = int(input())
all_Jobs = list()
queue = list()
for task_no in range(n):
	at, p, et, rd = map(int, input("Enter task AT, Period, Execution time, and relative deadline:\n:").split())
	i = 0
	while at+p*i<MAX_JOB_ACCEPT_TIME:
		all_Jobs.append(Job(at+p*i,rd,et, task_no))
		i+=1
all_Jobs.sort(key = lambda Job: Job.relative_deadline)
curr_time = -1
while add(all_Jobs)!=0:
	curr_time+=1
	for Job in all_Jobs:
		if Job.at==curr_time:
			queue.append(Job)
	queue.sort(key = lambda Job: Job.relative_deadline)
	while len(queue)>0 and queue[0].is_finished():
		queue.pop(0)
	if len(queue)==0: continue
	queue[0].execute(curr_time)
for Job in all_Jobs:
	Job.display_status()
	print("\n")

"""
3
50 50 25 100
0 62 10 20
0 125 25 50
"""
