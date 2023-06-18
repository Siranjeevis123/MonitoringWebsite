import psutil
import platform
import subprocess
from flask import Flask, render_template
from datetime import datetime
import subprocess


app = Flask(__name__)

def get_running_apps():
    running_apps = []
    for proc in psutil.process_iter(['name', 'pid', 'create_time']):
        process_info = {
            'name': proc.info['name'],
            'pid': proc.info['pid'],
            'create_time': datetime.fromtimestamp(proc.info['create_time']).strftime("%H:%M:%S"),
            'command': 'kill ' + str(proc.info['pid'])
        }
        running_apps.append(process_info)
    return running_apps

def get_used_ports():
    used_ports = []
    net_connections = psutil.net_connections()
    for conn in net_connections:
        if conn.status == psutil.CONN_LISTEN:
            port_info = {
                'port': conn.laddr.port,
                'pid': conn.pid,
                'process_name': psutil.Process(conn.pid).name(),
                'command': 'kill ' + str(conn.pid)
            }
            used_ports.append(port_info)
    return used_ports



@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent
    battery_percent = psutil.sensors_battery().percent
    wifi_status = subprocess.getoutput(
        "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/state/ {print $NF}'")
    wifi_speed = subprocess.getoutput(
        "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | awk '/maxRate/ {print $NF}'")
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%Y-%m-%d")
    mac_version = platform.mac_ver()[0]
    free_memory = psutil.virtual_memory().available

    disk_usage = psutil.disk_usage('/')
    network_stats = psutil.net_io_counters()

    running_apps = get_running_apps()
    used_ports = get_used_ports()
    

    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric,
                           battery_percent=battery_percent, wifi_status=wifi_status,
                           wifi_speed=wifi_speed, current_time=current_time, current_date=current_date,
                           mac_version=mac_version, free_memory=free_memory, disk_usage=disk_usage,
                           network_stats=network_stats, running_apps=running_apps,
                           used_ports=used_ports)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
