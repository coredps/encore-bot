import subprocess
import requests
import time

URL = 'http://xyz.com:5567'
sleep_time = 10

# This gets the output of docker stats command , formatted accordingly
def monitor_docker():
    result = subprocess.run(['docker', 'stats', '--no-stream', '--format',
                             "table {{.Container}}\t{{.Name}}\t{{.CPUPerc}}\t{{.MemPerc}}"], stdout=subprocess.PIPE)
    data = str(result.stdout, 'utf-8').split()

    # remove the unnecessary characters
    data = list(filter(lambda x: x != '/', data))
    data = list(filter(lambda x: x != '%', data))

    return data


def docker_stats():
    result = subprocess.run(
        ['docker', 'ps', '--format', "table {{.Image}}\t{{.ID}}"], stdout=subprocess.PIPE)
    data = str(result.stdout, 'utf-8').split()
    return data[3:]


while True:
    time.sleep(sleep_time)
    jdata = {'stats': ','.join(monitor_docker()),
             'ids': ','.join(docker_stats())}
    r = requests.post(URL, data=jdata)
    print(jdata)
    print(r.status_code, r.reason)
