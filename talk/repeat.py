import subprocess
import tempfile


def jtalk_run(message, out_wav='/tmp/voice.wav', speed=1.0):

    jtalk_dir = "/usr/local/Cellar/open-jtalk/1.11/"
    dic_path = jtalk_dir + "/dic"
    voice_path = jtalk_dir + "/voice/mei/mei_normal.htsvoice"

    with tempfile.NamedTemporaryFile(mode='w+') as tmp:
        tmp.write(message)
        tmp.seek(0)
        command = 'open_jtalk -x {} -m {} -r {} -ow {} {}'.format(
            dic_path, voice_path, speed, out_wav, tmp.name)
        command = command + '; afplay ' + out_wav
        # print(command)
        subprocess.run(command, shell=True)
