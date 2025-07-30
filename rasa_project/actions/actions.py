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


from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionScheduleMeeting(Action):
    def name(self):
        return "action_schedule_meeting"

    def run(self, dispatcher, tracker, domain):
        # TODO: Implement logic to schedule meeting
        dispatcher.utter_message("Meeting scheduled successfully.")
        return []

class ActionAssignTask(Action):
    def name(self):
        return "action_assign_task"

    def run(self, dispatcher, tracker, domain):
        # TODO: Implement task assignment logic
        dispatcher.utter_message("Task assigned successfully.")
        return []

class ActionMeetingSummary(Action):
    def name(self):
        return "action_meeting_summary"

    def run(self, dispatcher, tracker, domain):
        # TODO: Call summarizer
        dispatcher.utter_message("Here's the meeting summary...")
        return []

class ActionGetAttendance(Action):
    def name(self):
        return "action_get_attendance"

    def run(self, dispatcher, tracker, domain):
        # TODO: Check attendance from logs
        dispatcher.utter_message("Attendees: Riya, Aman, John")
        return []

class ActionSearchDocument(Action):
    def name(self):
        return "action_search_document"

    def run(self, dispatcher, tracker, domain):
        # TODO: Search local DB / file system
        dispatcher.utter_message("Found document: Q1_Sales_Report.pdf")
        return []

class ActionMatchResume(Action):
    def name(self):
        return "action_match_resume"

    def run(self, dispatcher, tracker, domain):
        # TODO: Call resume matcher
        dispatcher.utter_message("Top matches: Riya Sharma, Aman Gupta")
        return []

