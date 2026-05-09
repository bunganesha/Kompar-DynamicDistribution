from multiprocessing import Process, Queue
import time
import random

# Fungsi worker
def worker(worker_id, task_queue, result_queue):
    while not task_queue.empty():
        try:
            task = task_queue.get_nowait()

            print(f"Worker {worker_id} mengerjakan task {task}")

            # simulasi waktu proses berbeda-beda
            process_time = random.randint(1, 5)
            time.sleep(process_time)

            result_queue.put((worker_id, task, process_time))

        except:
            break


if __name__ == "__main__":

    # daftar task
    tasks = [f"Task-{i}" for i in range(1, 11)]

    task_queue = Queue()
    result_queue = Queue()

    # masukkan task ke queue
    for task in tasks:
        task_queue.put(task)

    workers = []

    start_time = time.time()

    # membuat 3 worker
    for i in range(3):
        p = Process(target=worker, args=(i + 1, task_queue, result_queue))
        workers.append(p)
        p.start()

    # tunggu semua worker selesai
    for p in workers:
        p.join()

    end_time = time.time()

    print("\nHASIL DISTRIBUSI DINAMIS")
    while not result_queue.empty():
        worker_id, task, process_time = result_queue.get()
        print(f"{task} selesai oleh Worker {worker_id} dalam {process_time} detik")

    total_time = round(end_time - start_time, 2)

    print(f"\nEstimasi waktu optimal tercapai dalam {total_time} detik")