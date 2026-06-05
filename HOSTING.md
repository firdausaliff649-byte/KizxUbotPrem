# KizxUbot Premium - Deployment & Hosting Guide

## 🌐 Hosting Platform Recommendation

### Fastest Deploy (Recommended)
1. **Railway.app** - Easiest setup
2. **Render** - Free tier available
3. **Heroku** - Popular choice
4. **VPS** - Full control

---

## 📦 Railway.app (Recommended)

### Setup dalam 5 menit:

1. **Create account** di https://railway.app
2. **Connect GitHub**
   - Fork repository ini
   - Link Railway dengan GitHub
3. **Deploy**
   ```
   railway up
   ```
4. **Set environment variables**
   - Go to Variables
   - Add: BOT_TOKEN, ADMIN_IDS, API_KEY_OPENAI
5. **Done!** ✅

---

## 🐳 Docker Hosting

### AWS EC2
```bash
# SSH ke instance
ssh -i key.pem ubuntu@your-instance.com

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Clone & Deploy
git clone https://github.com/firdausaliff649-byte/KizxUbotPrem.git
cd KizxUbotPrem
docker-compose up -d
```

### DigitalOcean App Platform
1. Create App
2. Connect GitHub repo
3. Select Dockerfile
4. Set env vars
5. Deploy

---

## 🖥️ VPS Linux Hosting

### Ubuntu 22.04 Setup

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python
sudo apt install python3.11 python3.11-venv -y

# Clone repo
git clone https://github.com/firdausaliff649-byte/KizxUbotPrem.git
cd KizxUbotPrem

# Setup
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Copy config
cp .env.example .env
nano .env  # Edit konfigurasi

# Run background with screen
screen -S kizx-bot
python main.py

# Detach: Ctrl+A, D
# Reattach: screen -r kizx-bot
```

### Systemd Service (Auto-start)

```bash
# Create service file
sudo nano /etc/systemd/system/kizx-bot.service
```

Content:
```ini
[Unit]
Description=KizxUbot Premium Service
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/home/your_user/KizxUbotPrem
Environment="PATH=/home/your_user/KizxUbotPrem/venv/bin"
ExecStart=/home/your_user/KizxUbotPrem/venv/bin/python main.py
Restart=always
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
sudo systemctl enable kizx-bot
sudo systemctl start kizx-bot
sudo systemctl status kizx-bot
```

---

## ☁️ PythonAnywhere

1. Create account di https://pythonanywhere.com
2. Upload files
3. Create virtual env
4. Install requirements
5. Create "always-on task"
6. Run: `python main.py`

---

## 💾 Database Setup

### SQLite (Default)
- Automatic setup
- File: `data/bot_database.db`

### PostgreSQL (Production)

```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Create database
sudo -u postgres createdb kizx_bot
sudo -u postgres createuser kizx_user
sudo -u postgres psql -c "ALTER USER kizx_user WITH PASSWORD 'password';"

# Update .env
DB_TYPE=postgresql
DATABASE_URL=postgresql://kizx_user:password@localhost:5432/kizx_bot
```

---

## 📊 Monitoring & Logs

### View real-time logs
```bash
tail -f logs/bot.log

# Docker logs
docker-compose logs -f bot
```

### Monitoring services
- **UptimeRobot** - Monitor bot status
- **LogRocket** - Error tracking
- **Sentry** - Exception tracking

---

## 🔐 Security Best Practices

1. **Never commit `.env` file**
2. **Use strong bot token**
3. **Restrict admin IDs**
4. **Enable HTTPS/SSL**
5. **Regular backups**
6. **Update dependencies**

```bash
# Regular updates
pip install --upgrade -r requirements.txt
```

---

## 🚀 Auto-restart on Crash

### Using Supervisor
```bash
sudo apt install supervisor -y
sudo nano /etc/supervisor/conf.d/kizx-bot.conf
```

Content:
```ini
[program:kizx-bot]
command=/home/user/KizxUbotPrem/venv/bin/python /home/user/KizxUbotPrem/main.py
directory=/home/user/KizxUbotPrem
user=user
autostart=true
autorestart=true
stderr_logfile=/var/log/kizx-bot.err.log
stdout_logfile=/var/log/kizx-bot.out.log
```

Start supervisor:
```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start kizx-bot
```

---

## 💰 Cost Estimation

| Platform | Price | Notes |
|----------|-------|-------|
| Railway | ~$5/month | Free tier available |
| Render | Free | Limited resources |
| Heroku | $7/month | Eco dyno |
| DigitalOcean | $5/month | Basic droplet |
| AWS | Variable | Cheap with free tier |
| VPS | $3-10/month | Full control |

---

## ✅ Checklist Deployment

- [ ] Repository forked/cloned
- [ ] `.env` configured
- [ ] Bot token verified
- [ ] Admin IDs set
- [ ] Database ready
- [ ] Dependencies installed
- [ ] Test bot locally
- [ ] Deploy to hosting
- [ ] Verify bot responding
- [ ] Setup monitoring
- [ ] Enable auto-restart

---

**Ready to deploy? Start with Railway! 🚀**
