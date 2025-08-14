# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFetchTasks(Action):
    
    def name(self) -> Text:
        return "action_fetch_tasks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you would typically fetch tasks from a database or an API
        tasks = [
            {"task": "Complete the project report", "due_date": "2023-10-15"},
            {"task": "Prepare for the team meeting", "due_date": "2023-10-20"},
            {"task": "Review the code changes", "due_date": "2023-10-18"}
        ]

        # Format the tasks into a message
        task_messages = "\n".join([f"{task['task']} (Due: {task['due_date']})" for task in tasks])
        
        dispatcher.utter_message(text=f"Here are your tasks:\n{task_messages}")

        return []
    

class ACtionFetchFile(Action):
    
    def name(self) -> Text:
        return "action_fetch_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you would typically fetch a file from a database or an API
        file_url = "https://example.com/path/to/your/file.pdf"
        
        dispatcher.utter_message(text=f"You can download the file from here: {file_url}")

        return []