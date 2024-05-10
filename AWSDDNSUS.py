import os
import time
import requests
import threading
import subprocess

class AWSDDNSUS:
    def __init__(self):
        self.__file_path = "/aws-ddns-us.txt"
        self.__aws_lambda = os.environ.get('AWS_LAMBDA')

    def _get_file_content(self, file_path):
        content = ""
        with open(file_path, "r") as f:
            content = f.read()
        os.remove(file_path)
        self.__log(f"{file_path}:{content}")
        return content

    def _start(self):
        thread_refresh = threading.Thread(target=self._start_thread, name="t1", args=())
        thread_refresh.start()

    def _start_thread(self):
        while True:
            try:
                self.__log(f"sending IP")
                self._post_ip_to_AWS_DNS()
                self.__log(f"sended IP")
                time.sleep(30)
            except Exception as e:
                self.__log("[Error]_start_thread"+str(e))

    def _post_ip_to_AWS_DNS(self):
        try:
            # Update IPv4
            ipv4_curl_command = f"curl '{self.__aws_lambda}'"
            ipv4_result = subprocess.run(ipv4_curl_command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            self.__log(f"IPv4 CURL Output: {ipv4_result.stdout}")
            if ipv4_result.stderr:
                self.__log(f"IPv4 CURL Error: {ipv4_result.stderr}")

        except subprocess.CalledProcessError as e:
            # Log the error for the failed curl command
            self.__log(f"CURL Command Failed: {e.stderr}")
        except Exception as e:
            # Log any other unexpected errors
            self.__log(f"Unexpected Error: {str(e)}")


    def __log(self, result):
        with open(self.__file_path, "a+") as f:
            f.write(result+"\n")
        if os.path.getsize(self.__file_path) > 1024*128:
            with open(self.__file_path, "r") as f:
                content = f.readlines()
                os.remove(self.__file_path)

if __name__ == '__main__':
    ss = AWSDDNSUS()
    ss._start()
