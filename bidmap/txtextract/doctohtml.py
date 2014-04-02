import os
import sys
import signal
import tempfile
import StringIO

def sigchld(signo, frame):
    while True:
        try:
            (pid, exit_status) = os.waitpid(-1, os.WNOHANG)
        except OSError, e:
            if e.errno == os.errno.ECHILD:
                break
            else:
                sys.stderr.write('Waitpid failed: %s' % e.strerror)
                raise
        else:
            if pid <= 0:
                break

def doctohtml(data):
    """ 
    Convert .doc data into HTML. Write HTML back
    on stdout 
    """
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(data)
    f.close()

    signal.signal(signal.SIGCHLD, sigchld)

    #
    #   parent    child
    #   r <------ w (stdout) 
    #
    r,w = os.pipe()
    try:
        pid = os.fork()
        if pid == 0: # child 
            os.dup2(w, 1)
            os.close(r)
            os.close(w)
            os.execlp('java', 'java', '-jar', '/usr/local/bin/tika-app.jar',  '-h', f.name)
        else: # parent 
            os.close(w)

            buf = ''
            while True:
                try:
                    c = os.read(r, 1)
                except OSError, e:
                    if e.errno == os.errno.EINTR:
                        continue
                    else:
                        raise

                if c == '':
                    break
                buf += c

            os.close(r)

    except OSError, e:
        os.unlink(f.name)
	raise

    os.unlink(f.name)
    return StringIO.StringIO(buf)
