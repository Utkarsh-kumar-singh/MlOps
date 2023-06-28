import mlflow 

def cal_sum(a,b):
    result = a+b
    return result

if __name__ == '__main__':
    with mlflow.start_run():
        a,b = 10,20
        z = cal_sum(a,b)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_metric("z",z)