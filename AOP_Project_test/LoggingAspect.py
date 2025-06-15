from AOP import *

@Aspect
class Logging_Aspect:
    def __init__(self):
        print("This is Aspect code...")
        
    #@Pointcut(Joinpoint="execution", Pattern="* Countdown_timer.main.countdown") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* Billing_system.biling_system.Bill_App.*(..)")
    #@Pointcut(Joinpoint="execution", Pattern="* Digital_clock.digital_clock.time")
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.app2.Animal.speak") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.app5.Document.show") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_test.app.Service.*(..)")
    @Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.app6.error_function")
    @Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.refactoring.search")
    def PointcutMethods(self):
        pass

    # @Before(PointcutMethods)
    # def logBefore(func):
    #     print("This is logBefore...")
    
    # @After(PointcutMethods)
    # def logAfter(func):
    #     print("This is logAfter...")

    @Around(PointcutMethods)
    def logAround(func, *args, **kwargs):
        for i in range(len(args[1])):
            if args[0] <= args[1][i]:
                return i
            else:
                pass
        return len(args[1])

    # @Before(PointcutMethods)
    # def logBefore2():
    #     print("This is logBefore222...")
    #     print("This is asdflogBefore222...")

    # @After(PointcutMethods)
    # def logAfter2():
    #     print("This is logAfter222...")
    #     print("This is asdflogAfter222...")

# Optimize: 
# Before, After function (針對無法呼叫多個Before After function進行優化)
# 完善After function功能
# Verify: survey paper tp find method


#@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Calculate_age/calculate.py", Function="month_days") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="app.py", Function="Service") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="app.py", Function="call_Service1") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_test.app.Service.*(..)")
    #@Pointcut(Joinpoint="execution", Pattern="* Billing_system.biling_system.Bill_App.*(..)") # Pass
    #@Pointcut(Joinpoint="execution", Pattern="* Calculate_age.calculate.judge_leap_year") # Pass
    #@Pointcut(Joinpoint="execution", Pattern="* Create_a_simple_stopwatch.stopwatch.Start") #Pass
    
    #@Pointcut(Joinpoint="execution", Pattern="* Digital_clock.digital_clock.time") # Pass (2 Join Point, 4 execution)
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Alarm clock/alarm_clock.py", Function="alarm") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Billing_system/biling_system.py", Function="clear_data") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Countdown_timer/main.py", Function="countdown") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="C:/Users/Boss Hsu/Python_Code/python-mini-projects-master/projects/Create_a_simple_stopwatch/stopwatch.py", Function="count") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="MethodPattern", Filepath="test.py", Function="set_number_of_wheels") #Pass


    # Test: 透過開發的東西去修正(Vulnerability、Refactor...)甚麼...
    # 常見的、(常見的 Python Design作法 (在設計時可能會遇到甚麼問題..) )
    # Sample: Inherient
    # Inherient OOP Python

    # Survey design pattern or design principle in python
    

# Refactoring  Discussion
# 1. 錯誤檢測與更改，將錯誤的function作為Crosscutting concern，將其模組化成Aspect後，利用所開發的工具進行Refactoring (以Around進行覆寫)