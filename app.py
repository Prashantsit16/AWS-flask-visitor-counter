from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

conn_params = {
    'host': 'database-1.cdcw2yymq8wg.ap-south-1.rds.amazonaws.com',
    'port': 5432,
    'database': 'myapp_db',
    'user': 'postgres',
    'password': 'prashantDB28'
}

@app.route('/')
def counter():
    try:
        conn = psycopg2.connect(**conn_params)
        cur = conn.cursor()
        visitor_ip = request.remote_addr
        cur.execute("INSERT INTO visits (ip_address) VALUES (%s)", (visitor_ip,))
        conn.commit()
        cur.execute("SELECT COUNT(*) FROM visits")
        count = cur.fetchone()[0]
        cur.close()
        conn.close()
        return render_template('index.html', visit_count=count, visitor_ip=visitor_ip)
    except Exception as e:
        return f"Database error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
