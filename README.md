# 🔭 Discord Monitoring with Prometheus + Alertmanager + Discord Webhook Proxy

This project sets up a monitoring stack with Prometheus, Alertmanager, and Node Exporter, sending alerts to **Discord** via a lightweight custom webhook proxy.

---

## 📦 What’s Included?

- **Prometheus** — Time series monitoring & alerting system.
- **Node Exporter** — For exposing machine metrics.
- **Alertmanager** — Handles alert routing, grouping & notification.
- **Discord Webhook Proxy** — Small Flask server to format alerts and forward them to Discord.

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/edensitko/discord-monitoring.git
cd discord-monitoring
```

### 2. Update Discord Webhook URL

In the file [`webhook-proxy/app.py`](webhook-proxy/app.py), edit the following line to include your **own Discord webhook URL**:

```python
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your-webhook-id/your-token"
```

> ⚠️ You can create a webhook in Discord via:  
> Channel Settings → Integrations → Webhooks → New Webhook

---

### 3. Run Setup

```bash
chmod +x setup-all.sh
./setup-all.sh
```

This script will:

- Install Docker + Docker Compose
- Add your user to the Docker group
- Build and run all containers

---

## 🔎 Accessing Services

| Service         | URL                            |
|-----------------|---------------------------------|
| Prometheus      | http://<your-server-ip>:9090    |
| Alertmanager    | http://<your-server-ip>:9093    |
| Node Exporter   | http://<your-server-ip>:9100/metrics |
| Discord Proxy   | http://<your-server-ip>:5000    |

---

## 🔔 Example Alert

When `node-exporter` goes down or comes back up, you’ll receive a Discord message like:

```
[🔥 FIRING] Node Exporter is DOWN
🔻 Target: node-exporter:9100
```

Or:

```
[✅ RESOLVED] Node Exporter is UP
📡 Target: node-exporter:9100
```

---

## 🧾 Files Overview

```bash
discord-monitoring/
├── alert_rules.yml         # Prometheus alerting rules
├── alertmanager.yml        # Alertmanager config
├── docker-compose.yml      # Docker stack
├── prometheus.yml          # Prometheus config
├── discord.tmpl            # (Optional) Custom Alertmanager template
├── webhook-proxy/          # Flask proxy app
│   ├── app.py              # The main webhook handler
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Docker setup for proxy
├── setup-all.sh            # Full install & run script
└── README.md
```

---

## 💬 Support

If you have issues or want to contribute, feel free to open an issue or PR.

---

## 🛡 License

MIT © 2025 Eden Sitkovetsky
