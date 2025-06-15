import time
import psutil
import os
import threading
from AOP import *

def my_test():
    @Aspect
    class Logging_Aspect:
        def __init__(self):
            print("This is Aspect code...")

        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Calculate_age/calculate.py", Function="month_days") #Pass
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="app.py", Function="Service") #Pass
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="app.py", Function="call_Service1") #Pass
        @Pointcut(Joinpoint="execution", Pattern="* AOP_Project_test.app.Service.*(..)")
        #@Pointcut(Joinpoint="execution", Pattern="* Billing_system.biling_system.Bill_App.*(..)")
        #@Pointcut(Joinpoint="execution", Pattern="* Compute_IoU.Compute_IoU.Cal_IoU.*(..)")
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Alarm clock/alarm_clock.py", Function="alarm") #Pass
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Billing_system/biling_system.py", Function="clear_data") #Pass
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Countdown_timer/main.py", Function="countdown") #Pass
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Create_a_simple_stopwatch/stopwatch.py", Function="count") #Pass
        #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="test.py", Function="set_number_of_wheels") #Pass
        def PointcutMethods(self):
            pass

        @Before(PointcutMethods)
        def logBefore():
            print("This is logBefore...")
        
        @After(PointcutMethods)
        def logAfter():
            print("This is logAfter...")

class HardwareMonitor:
    def __init__(self, interval=1.0):
        self.proc = psutil.Process(os.getpid())
        self.interval = interval
        self.running = False
        self.cpu_log = []
        self.mem_log = []

    def _monitor(self):
        while self.running:
            cpu = self.proc.cpu_percent(interval=None)
            mem = self.proc.memory_info().rss / (1024 ** 2)
            self.cpu_log.append(cpu)
            self.mem_log.append(mem)
            print(f"[Monitor] CPU: {cpu:.2f}% | Memory: {mem:.2f} MB")
            time.sleep(self.interval)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._monitor, daemon=True)
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()

    def summary(self):
        avg_cpu = sum(self.cpu_log) / len(self.cpu_log) if self.cpu_log else 0
        max_mem = max(self.mem_log) if self.mem_log else 0
        return {
            "avg_cpu": avg_cpu,
            "max_mem": max_mem,
            "samples": len(self.cpu_log)
        }
    
if __name__ == "__main__":
    monitor = HardwareMonitor(interval=0.2)
    
    print("[啟動監控]")
    monitor.start()

    start = time.perf_counter()
    
    # ✅ 呼叫你 AOP 框架切入過的程式
    for _ in range(100):
        my_test()
    #service.run()  # 或呼叫你要測的 methods
    
    end = time.perf_counter()
    monitor.stop()

    print("[執行完成]")
    print(f"總耗時: {end - start:.4f} 秒")
    
    stats = monitor.summary()
    print(f"平均 CPU 使用率: {stats['avg_cpu']:.2f}%")
    print(f"最高記憶體使用: {stats['max_mem']:.2f} MB")
    print(f"採樣次數: {stats['samples']}")