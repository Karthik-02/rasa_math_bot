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
from rasa_sdk.events import SlotSet, EventType
import operator


class ActionMathOperations(Action):
    def name(self) -> Text:
        return "action_math_operations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        operation = tracker.get_slot("operation")
        first_number = float(tracker.get_slot("first_number"))
        second_number = float(tracker.get_slot("second_number"))
        
        result = None

        if operation == "addition":
            result = operator.add(first_number, second_number)
        elif operation == "subtraction":
            result = operator.sub(first_number, second_number)
        elif operation == "multiplication":
            result = operator.mul(first_number, second_number)
        elif operation == "division":
            if second_number == 0:
                dispatcher.utter_message(template="utter_divide_by_zero_error")
                return [SlotSet("second_number", None)]
            else:
                result = operator.truediv(first_number, second_number)
        
        if result is not None:
            dispatcher.utter_message(text=f"The result of {operation} of {first_number} and {second_number} is {result}.")
        
        return []


class ActionMoreOperations(Action):
    def name(self) -> Text:
        return "action_more_operations"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(template="utter_ask_operation")
        return [SlotSet("operation", None), SlotSet("first_number", None), SlotSet("second_number", None)]


class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Adding Restarted event and AllSlotsReset event to the tracker
        return [Restarted(), AllSlotsReset()]

