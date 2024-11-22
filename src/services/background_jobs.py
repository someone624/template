from celery import Celery

# Configure Celery
app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def send_email_task(to_email, subject, body):
    """
    Background task to send an email.
    """
    from .email_service import send_email
    send_email(to_email, subject, body)
    print(f"Background email sent to {to_email}")

@app.task
def schedule_task(task_name, delay):
    """
    Simulates scheduling a task with a delay.
    """
    import time
    print(f"Scheduling task '{task_name}' to run after {delay} seconds...")
    time.sleep(delay)
    print(f"Task '{task_name}' executed.")

def run_scheduled_jobs():
    """
    Runs all scheduled background jobs.
    """
    # Example usage
    schedule_task.apply_async(("test_task", 5))
    send_email_task.apply_async(("recipient@example.com", "Hello", "This is a test email."))
