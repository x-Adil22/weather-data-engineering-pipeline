import psycopg2


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="weather_db",
            user="aimlock",
            password="9125",
            host="postgres",
            port="5432"
        )
        return conn
    except Exception as e:
        print("❌ DB Connection Error:", e)
        raise e


def load_data(df):
    conn = None
    cursor = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        for _, row in df.iterrows():
            cursor.execute("""
                INSERT INTO weather_data (temperature, windspeed, winddirection, time)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (time) DO NOTHING;
            """, (
                row["temperature"],
                row["windspeed"],
                row["winddirection"],
                row["time"]
            ))

        conn.commit()
        print("✅ Data loaded into PostgreSQL")

    except Exception as e:
        print("❌ Load Error:", e)
        raise e

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()