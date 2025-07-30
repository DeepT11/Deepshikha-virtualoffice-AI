# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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


# Fetch Tasks
class ActionFetchTasks(Action):

    def name(self) -> Text:
        return "action_fetch_tasks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you would typically fetch tasks from a database or an API
        tasks = ["Task 1: Complete the report", "Task 2: Attend the meeting", "Task 3: Review the code"]

        if tasks:
            task_list = "\n".join(tasks)
            dispatcher.utter_message(text=f"Here are your tasks for today:\n{task_list}")
        else:
            dispatcher.utter_message(text="You have no tasks for today.")

        return []
    

# Fetch Meetings
class ActionFetchMeetings(Action):
    def name(self) -> Text:
        return "action_fetch_meetings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you would typically fetch meetings from a database or an API
        meetings = ["Meeting 1: Project kickoff at 10 AM", "Meeting 2: Team sync at 2 PM"]

        if meetings:
            meeting_list = "\n".join(meetings)
            dispatcher.utter_message(text=f"Here are your meetings for today:\n{meeting_list}")
        else:
            dispatcher.utter_message(text="You have no meetings scheduled for today.")

        return []
    

# Fetch FAQ
class ActionFetchFAQ(Action):
    def name(self) -> Text:
        return "action_fetch_faq"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Here you would typically fetch FAQs from a database or an API
        faqs = {
            "password reset": "To reset your password, go to the settings page and click on 'Reset Password'.",
            "file locations": "You can find your files in the 'Documents' folder.",
            "tech support": "For tech support, please contact the IT department at it-support@example.com."
        }
        query = tracker.latest_message.get('text', '').lower()
        response = faqs.get(query, "I'm sorry, I don't have information on that topic.")
        dispatcher.utter_message(text=response)
        return []