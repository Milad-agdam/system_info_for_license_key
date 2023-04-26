
import GPUtil
import psutil
from uuid import getnode as get_mac


def HexToBin(h):
    return bin(int(h, 16))


def create_key():
    # get cpu id
    cpufreq = psutil.cpu_freq()
    cpu_id = cpufreq.max
    # get mac id
    mac = get_mac()
    # get gpu id
    gpus = GPUtil.getGPUs()
    list_gpus = []
    for gpu in gpus:
        gpu_uuid = gpu.uuid
        list_gpus.append(gpu_uuid)
        new_gpu_id = str(list_gpus).split('-')[-2]
        gpu_id = int(new_gpu_id,  16)
    key = str(cpu_id) + str(mac) + str(gpu_id)
    return key


unique_number = create_key()
print(unique_number)

