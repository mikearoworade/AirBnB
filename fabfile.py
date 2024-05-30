#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
from fabric import task, Connection
import os
import shutil
from datetime import datetime

@task
def hello(c):
    print("Hello, Fabric!")

@task
def hostname(c):
    result = c.run('hostname')
    
@task
def pack(c):
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    
    # try:
    if not os.path.exists("versions"):
        os.mkdir("versions")
    else:
        shutil.rmtree("versions")
        os.mkdir("versions")
    
    print(f'Packing web_static to {file}..')
    c.run(f'tar -cvzf {file} web_static')
    check_stat = c.run(f'stat --format="%s" {file}', hide=True)
    file_size = int(check_stat.stdout.strip())
    print(f'web_static packed: {file} -> {file_size}')
    return file

@task
def deploy(c):
    dt = datetime.utcnow()
    file_path = "versions/web_static_{}{}{}{}{}{}.tar.gz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    
    # try:
    if not os.path.exists("versions"):
        os.mkdir("versions")
    else:
        os.rmdir("versions")
        os.mkdir("versions")

    c.run(f'tar -czvf {file_path} web_static')

    hosts = ["54.237.119.135", "54.160.71.201"]
    if os.path.isfile(file_path) is False:
        return False
    file = file_path.split("/")[-1]
    name = file.split(".")[0]
    print(f'{file_path}, {file}, {name}')
    for host in hosts:
        config = {
            'host': f'ubuntu@{host}',
            'connect_kwargs': {
                'key_filename': '../school',
            }
        }
        with Connection(**config) as conn:
            print(f'{host} - Connected Successfully')
            conn.put(file_path, "/tmp/{}".format(file))
            conn.run("rm -rf /data/web_static/releases/{}/".format(name))
            conn.run("mkdir -p /data/web_static/releases/{}/".format(name))
            conn.run("tar xzvf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)) 
            conn.run("rm /tmp/{}".format(file))
            conn.run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name))
            conn.run("rm -rf /data/web_static/releases/{}/web_static".format(name))
            conn.run("rm -rf /data/web_static/current")
            conn.run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name))