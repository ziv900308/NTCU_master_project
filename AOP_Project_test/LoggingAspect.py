from AOP import *


@Aspect
class Logging_Aspect:
    def __init__(self):
        print("This is Aspect code...")

    # ========== Question 1 ==========

    # @Pointcut(Joinpoint="execution", Pattern="* Question1.sequential_search.search")
    # def PointcutMethods(self):
    #     pass

    # @Around(PointcutMethods)
    # def logAround(func, *args, **kwargs):
    #     for i in range(len(args[1])):
    #         if args[0] <= args[1][i]:
    #             return i
    #         else:
    #             pass
    #     return len(args[1])
    
    # ========== Question 2 ==========

    # @Pointcut(Joinpoint="execution", Pattern="* Question2.dates_and_months.unique_day")
    # def PointcutMethods(self):
    #     pass

    # @Pointcut(Joinpoint="execution", Pattern="* Question2.dates_and_months.unique_month")
    # def PointcutMethods2(self):
    #     pass

    # @Pointcut(Joinpoint="execution", Pattern="* Question2.dates_and_months.contains_unique_day")
    # def PointcutMethods3(self):
    #     pass

    # @Around(PointcutMethods)
    # def logAround(func, *args, **kwargs):
    #     all_days = ()
    #     for i in args[1]:
    #         all_days += (i[1],)
    #     return all_days.count(args[0]) == 1
    
    # @Around(PointcutMethods2)
    # def logAround2(func, *args, **kwargs):
    #     all_months = ()
    #     for i in args[1]:
    #         all_months += (i[0],)
    #     return all_months.count(args[0]) == 1
    
    # @Around(PointcutMethods3)
    # def logAround3(func, *args, **kwargs):
    #     all_day_in_given_month = ()
    #     for i in args[1]:
    #         if i[0] == args[0]:
    #             all_day_in_given_month += (i[1],)
    #     for i in all_day_in_given_month:
    #         if unique_day(i, args[1]):
    #             return True
    #     return False

    # ========== Question 3 ==========

    # @Pointcut(Joinpoint="execution", Pattern="* Question3.duplicate_elimination.remove_extras")
    # def PointcutMethods(self):
    #     pass

    # @Around(PointcutMethods)
    # def logAround(func, *args, **kwargs):
    #     new_lst = []
    #     for i in args[0]:
    #         if i not in new_lst:
    #             new_lst.append(i)
    #         else:
    #             continue
    #     return new_lst

    # ========== Question 4 ==========

    # @Pointcut(Joinpoint="execution", Pattern="* Question4.sorting_tuples.sort_age")
    # def PointcutMethods(self):
    #     pass

    # @Around(PointcutMethods)
    # def logAround(func, *args, **kwargs):
    #     output = []
    #     for i in range(len(args[0])):
    #         largest = max(args[0], key=lambda p: p[1])
    #         args[0].remove(largest)
    #         output.append(largest)
    #     return output

    # ========== Question 5 ==========

    # @Pointcut(Joinpoint="execution", Pattern="* Question5.top_K.top_k")
    # def PointcutMethods(self):
    #     pass

    # @Around(PointcutMethods)
    # def logAround(func, *args, **kwargs):
    #     res = []
    #     for i in range(args[1]):
    #         res.append(max(args[0]))
    #         args[0].remove(max(args[0]))
    #     return res


    # =====================================================================================================================================================
    

    #@Pointcut(Joinpoint="execution", Pattern="* Countdown_timer.main.countdown") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* Billing_system.biling_system.Bill_App.*(..)")
    #@Pointcut(Joinpoint="execution", Pattern="* Digital_clock.digital_clock.time")
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.app2.Animal.speak") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.app5.Document.show") #Pass
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_test.app.Service.*(..)")
    #@Pointcut(Joinpoint="execution", Pattern="* AOP_Project_Test.app6.error_function")

    # @Pointcut(Joinpoint="execution", Pattern="* Employees System Project.FrontendManager.FrontendManager.print_menu")
    # @Pointcut(Joinpoint="execution", Pattern="* Employees System Project.EmployeesManager.EmployeesManager.list_employee")
    # @Pointcut(Joinpoint="execution", Pattern="* Countdown_timer.main.countdown")
    # @Pointcut(Joinpoint="execution", Pattern="* Employees System Project.FrontendManager.FrontendManager.*(..)")
    # @Pointcut(Joinpoint="execution", Pattern="* tool.python_execute._run_code")
    @Pointcut(Joinpoint="execution", Pattern="* utils.html.strip_tags")
    def PointcutMethods(self):
        pass

    @Around(PointcutMethods)
    def logAround(func, *args, **kwargs):
        print("Args:", args)
        func()

    # @Around(PointcutMethods)
    # def logAround(func, *args, **kwargs):
    #     import re

    #     BANNED_PATTERNS = [
    #         r"\beval\s*\(",
    #         r"\bexec\s*\(",
    #         r"\bcompile\s*\(",
    #         r"\b__import__\s*\(",
    #         r"\bos\.system\s*\(",
    #         r"\bos\.popen\s*\(",
    #         r"\bsubprocess\.(call|run|Popen|check_output)\s*\(",
    #     ]

    #     warnings = []
    #     for pattern in BANNED_PATTERNS:
    #         matches = list(re.finditer(pattern, args[1]))
    #         for match in matches:
    #             line_no = args[1][:match.start()].count("\n") + 1
    #             warnings.append((pattern, line_no))

    #     if warnings:
    #         print("*"*100)
    #         print("Detect command injection:")
    #         print("*"*100)
    #         for pattern, line in warnings:
    #             print(f" - pattern `{pattern}` at line {line}")
    #         return
        
    #     print("*"*100)
    #     print("This function is safe...")
    #     print("*"*100)
    #     func()

        # print("Catch code information...:", args[1])
        # if args[1] == 0:
        #     print("This is not safe...")
        # else: 
        #     func()


    # @Before(PointcutMethods)
    # def logBefore(func):
    #     print("This is logBefore...")
    
    # @After(PointcutMethods)
    # def logAfter(func):
    #     print("This is logAfter...")

    

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