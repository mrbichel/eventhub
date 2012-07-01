from fabric.api import env, run, prefix, cd, local

env.user = 'eventhub'
env.hosts = ['tango.johan.cc']
env.directory = '/home/eventhub/srv/eventhub'
env.activate = 'source /home/johan/.virtualenvs/eventhub/bin/activate'

def deploy():
    local('git push')
    with cd(env.directory):
        with prefix(env.activate):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py cleanup')
            run('touch eventhub/wsgi.py') # this triggers a graceful reload
