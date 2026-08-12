import schedule
import time
from datetime import datetime

# -------------------------------------------------------------
# 1. Define the Task (The Job)
# -------------------------------------------------------------
def fetch_latest_data():
    """This function contains the code we want to run automatically."""
    
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # In the real world, your API call or Selenium scrape would go here!
    print(f"[{current_time}] RUNNING JOB: Connecting to API... Data saved!")

print("Scheduler started. Waiting for the next trigger...")

# -------------------------------------------------------------
# 2. Set the Schedule
# -------------------------------------------------------------
# For testing, let's run it every 5 seconds
schedule.every(5).seconds.do(fetch_latest_data)

# Real-world examples you could use instead:
# schedule.every().day.at("08:00").do(fetch_latest_data)
# schedule.every().monday.do(fetch_latest_data)
# schedule.every(2).hours.do(fetch_latest_data)

# -------------------------------------------------------------
# 3. Keep the Script Alive
# -------------------------------------------------------------
try:
    while True:
        # Check if any scheduled jobs are due to run right now
        schedule.run_pending()
        
        # Tell the script to pause for 1 second so it doesn't max out your Mac's CPU
        time.sleep(1)
        
except KeyboardInterrupt:
    # This cleanly catches when you press Ctrl+C to stop the loop
    print("\nScheduler manually stopped. Goodbye!")