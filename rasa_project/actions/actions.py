# This files contains your custom actions which can be used to run
# custom Python code.
#

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# call backend api
# Backend endpoint
API_SERVER = "http://localhost:5000/tasks"  # Change to your actual backend

class ActionFetchTasks(Action):

    def name(self) -> Text:
        return "action_fetch_tasks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        try:
            response = requests.get(API_SERVER, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                tasks = data.get("tasks", [])
                
                if tasks:
                    task_list = "\n".join([f"{i+1}. {t}" for i, t in enumerate(tasks)])
                    dispatcher.utter_message(text=f"Here are your tasks for today:\n{task_list}")
                else:
                    dispatcher.utter_message(text="You have no tasks for today 🎉")
            
            else:
                dispatcher.utter_message(text="I couldn't fetch your tasks right now. Please connect with backend!")
        
        except Exception as e:
            dispatcher.utter_message(text="Error fetching tasks from the backend.")
            print(f"Error in action_fetch_tasks: {e}")
        return []


class ActionMeetingSchedule(Action):

    def name(self) -> Text:
        return "action_fetch_meetings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Placeholder for meeting fetching logic
        dispatcher.utter_message(text="Fetching meetings is not implemented yet.")
        return []

