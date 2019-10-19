import docker

def run_container(image, ports, auto_remove=True):
    client = docker.from_env()
    cont = client.containers.run(image=image, ports=ports, auto_remove=auto_remove)
    client.containers.prune()
    return cont

def build_image(path, labels, tag):
    client = docker.from_env()
    res = client.images.build(path=path, labels=labels, tag=tag)
    return res[0].id
    
def remove_image(id):
    client = docker.from_env()
    client.images.remove(image=id, force=True)
    
#run_container("testimage", {80:80})
build_image(".", {"purpose": "test"}, "testpybuild")