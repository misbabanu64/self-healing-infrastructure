from flask import Flask, request, jsonify
import subprocess
import logging

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/alert", methods=["POST"])
def receive_alert():
    data = request.get_json(silent=True) or {}

    for alert in data.get("alerts", []):
        if alert.get("labels", {}).get("alertname") == "ApplicationDown":
            logging.warning("ApplicationDown alert received")

            try:
                result = subprocess.run(
                    [
                        "ansible-playbook",
                        "/ansible/recovery.yml"
                    ],
                    capture_output=True,
                    text=True,
                    timeout=60
                )

                logging.info(result.stdout)

                if result.returncode != 0:
                    logging.error(result.stderr)
                    return jsonify({"status": "recovery_failed"}), 500

            except Exception:
                logging.exception("Recovery execution failed")
                return jsonify({"status": "recovery_failed"}), 500

    return jsonify({"status": "alert_processed"}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
