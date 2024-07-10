#exemplo usando "with" do py
from airflow import DAG
from airflow.operators.bash_operator import BashOperator  
from datetime import datetime

with DAG('quarta_dag', description='quarta dag exemplo curso',
            schedule_interval=None, start_date=datetime(2024, 7, 9),  
            catchup=False) as dag:

    # schedule_interval -> define o intervalo de execuções
    # catchup -> executa intervalos passados, quando esta false evita esse comportamento

    # definição das tasks   id da task     comando executado      sinaliza a qual tag essa task pertence
    task1 = BashOperator(task_id='tsk1', bash_command='sleep 5')
    task2 = BashOperator(task_id='tsk2', bash_command='sleep 5')
    task3 = BashOperator(task_id='tsk3', bash_command='sleep 5')

    #usando set_upstream para definir a ordem de exec das tasks, porem menos intuitivo do que o outro método
    task1.set_upstream(task2)
    task2.set_upstream(task3)
