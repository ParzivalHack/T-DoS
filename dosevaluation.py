from flask import Flask, jsonify
from collections import deque
import time
import threading

app = Flask(__name__)

# Stores timestamps of received packets
request_times = deque(maxlen=100000)  # Store up to 100k timestamps
attack_start = None
attack_end = None
total_requests = 0

lock = threading.Lock()


@app.route("/")
def handle_request():
    global attack_start, attack_end, total_requests

    with lock:
        now = time.time()
        request_times.append(now)
        total_requests += 1

        # Detect attack start
        if attack_start is None:
            attack_start = now

        # Update attack end time
        attack_end = now

    return "Monitoring requests...", 200


@app.route("/stats")
def get_stats():
    with lock:
        now = time.time()

        # Cleanup old requests (>1 sec)
        while request_times and request_times[0] < now - 1:
            request_times.popleft()

        # Calculate stats
        rps = len(request_times)  # Requests in the last second
        attack_duration = (attack_end - attack_start) if attack_start else 0

        stats = {
            "requests_per_second": rps,
            "total_requests": total_requests,
            "attack_duration_seconds": round(attack_duration, 2) if attack_duration > 0 else 0,
            "attack_active": attack_start is not None and (now - attack_end) < 5,  # Consider attack stopped if no requests in 5s
        }

    return jsonify(stats)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
