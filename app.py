from flask import Flask, render_template
import paramiko

app = Flask(__name__)

@app.route('/console')
def console():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('localhost', username='user', password='password')
    chan = ssh.invoke_shell()
    return render_template('console.html', chan=chan)
@app.route('/console/output')
def console_output():
    output = chan.recv(1024).decode('utf-8')
    return output
