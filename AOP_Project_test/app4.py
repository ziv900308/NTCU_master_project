def after_returning(advice_func):
    def decorator(target_func):
        def wrapper(*args, **kwargs):
            result = target_func(*args, **kwargs)
            advice_func(result)  # 只有當 target_func 正常返回時才呼叫
            print("This is after returning...")
            return result
        return wrapper
    return decorator

# 建立 AfterReturning 的 advice（只在正常返回時呼叫）
def log_result(return_value):
    print(f"[AfterReturning] Return value: {return_value}")

# 套用到一個目標函式上
@after_returning(log_result)
def compute_sum(a, b):
    print("This is compute_sum function...")
    return a + b

# 測試
compute_sum(10, 20)

