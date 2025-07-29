import requests

BASE_URL = "http://localhost:5000"  # Change as needed

def handle_intent(tag, user_input, user_id="123"):  # Simulated user ID for now
    if tag == "task_status":
        try:
            res = requests.get(f"{BASE_URL}/tasks/{user_id}")
            if res.ok:
                tasks = res.json().get("tasks", [])
                if not tasks:
                    return " You have no pending tasks!"
                task_list = "\n".join([f"🔸 {task['title']} (Due: {task['deadline']})" for task in tasks])
                return f"📋 Here are your tasks:\n{task_list}"
            else:
                return " Could not fetch tasks. Try again later."
        except:
            return " Error connecting to Task Service."

    elif tag == "attendance":
        try:
            res = requests.post(f"{BASE_URL}/attendance/checkin", json={"user_id": user_id})
            if res.ok:
                return " Attendance marked successfully!"
            else:
                return " Failed to mark attendance."
        except:
            return " Error connecting to Attendance Service."

    elif tag == "hr_help":
        return (
            " To apply for leave:\n"
            "1. Go to the HR Panel → Leave Request\n"
            "2. Fill your dates and reason\n"
            "3. Submit for approval"
        )

    elif tag == "greeting":
        return " Hello! How can I help you in the Virtual Office today?"

    
    else:
        return " I'm not sure how to help with that yet. Try rephrasing your question."
