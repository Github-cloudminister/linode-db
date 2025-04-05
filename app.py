from flask import Flask
import psycopg2
from psycopg2 import OperationalError

app = Flask(__name__)

@app.route('/')
def test_connection():
    response = []
    response.append("📍 Step 1: Starting the PostgreSQL connection test...")

    # Connection details
    host = "a269046-akamai-prod-5563659-default.g2a.akamaidb.net"
    database = "defaultdb"
    user = "akmadmin"
    password = "AVNS_s8eoy6y-vRb4FJ1kM34"
    port = 20107

    response.append(f"🔍 Step 2: Using connection details:")
    response.append(f"  Host: {host}")
    response.append(f"  Database: {database}")
    response.append(f"  User: {user}")
    response.append(f"  Port: {port}")
    response.append(f"  SSL Mode: require")
    response.append(f"  Timeout: 5 seconds")

    try:
        response.append("🚀 Step 3: Attempting to connect to PostgreSQL...")
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password,
            port=port,
            sslmode='require',
            connect_timeout=5
        )
        response.append("✅ Step 4: PostgreSQL connection successful!")
        response.append("🔌 Step 5: Closing the connection...")
        conn.close()
        response.append("👋 Step 6: Connection closed. Done!")
    except OperationalError as e:
        response.append(f"❌ Error: PostgreSQL connection failed:<br>{e}")

    return "<br>".join(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
