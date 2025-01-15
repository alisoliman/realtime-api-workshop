from invoke import task

@task
def start(c, port = 8081):
    c.run(f"chainlit run --watch --port {port} .\chat.py")