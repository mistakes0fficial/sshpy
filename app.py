from flask import Flask, render_template
import paramiko

app = Flask(__name__)

@app.route('/console')
def console():
    private_key = paramiko.RSAKey.from_private_key_file('/path/to/private.pem')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('remote_server_ip', username='user', pkey=private_key)
    chan = ssh.invoke_shell()
    return render_template('console.html', chan=chan)
@app.route('/console/output')
def console_output():
    output = chan.recv(1024).decode('utf-8')
    return output



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
