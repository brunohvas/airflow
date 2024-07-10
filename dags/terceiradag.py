from airflow import DAG
from airflow.operators.bash_operator import BashOperator  
from datetime import datetime

dag = DAG('terceira_dag', description='terceira dag exemplo curso',
            schedule_interval=None, start_date=datetime(2024, 7, 9),  
            catchup=False)

# schedule_interval -> define o intervalo de execuções
# catchup -> executa intervalos passados, quando esta false evita esse comportamento

# definição das tasks   id da task     comando executado      sinaliza a qual tag essa task pertence
task1 = BashOperator(task_id='tsk1', bash_command='sleep 5', dag=dag)
task2 = BashOperator(task_id='tsk2', bash_command='sleep 5', dag=dag)
task3 = BashOperator(task_id='tsk3', bash_command='sleep 5', dag=dag)

# definição de execução das dags
[task1, task2] >> task3
