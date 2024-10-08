import docker

client = docker.from_env()

def run_code_in_docker(repo_path, script_name):
    client.containers.run(
        "python:3.9",
        f"python {script_name}",
        volumes={repo_path: {'bind': '/code', 'mode': 'rw'}},
        detach=True
    )
