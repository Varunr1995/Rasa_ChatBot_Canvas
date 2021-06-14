# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# Class function just to print the input provided the user

# from typing import Any, Text, Dict, List
# 
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.forms import FormAction
# 
# class ActionHelloWorld(FormAction):
# 
#     def name(self) -> Text:
#         return "painting_form"
# 
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         print("required_slots(tracker: Tracker)")
#         return["art_type", "size", "frame", "finishing", "orientation"]
# 
#     def submit(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict]:
# 
#         dispatcher.utter_message(template="utter_submit")
# 
#         return []

# Class function to validate the input from the user and print the results

from typing import Any, Text, Dict, List
from rasa_sdk import Action Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, FormValidationAction

class ValidatePaintingQuereForm(FormValidationAction):

    def name(self) -> Text:
        return "painting_form"
    
    @staticmethod
    def painting_db() -> List[Text]:
        """Database of supported painting canvases."""

        return [
            "Graphite",
            "Charcoal",
            "Coloured Pencil Art",
            "Oil Painting"
        ]

    @staticmethod
    def size_db() -> List[Text]:
        """Database of supported size canvases."""

        return [
            "A1",
            "A2",
            "A3",
            "A4"
        ]

    @staticmethod
    def frame_db() -> List[Text]:
        """Database of supported frame canvases."""

        return [
            "No Frame",
            "Standard",
            "Designer"
        ]

    @staticmethod
    def finishing_db() -> List[Text]:
        """Database of supported finishing painting canvases."""

        return [
            "Maple",
            "Walnut",
            "Black",
            "White",
            "Graphite",
            "Brass",
            "German Silver"
        ]

    @staticmethod
    def orientation_db() -> List[Text]:
        """Database of supported orientation of canvases."""

        return [
            "Landscape",
            "Potrait",
            "Artist Choice"
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_art_type(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate art_type value."""

        if value.lower() in self.painting_db():
            # validation succeeded, set the value of the "cuisine" slot to value
            return {"art_type": value}
        else:
            dispatcher.utter_message(response="utter_wrong_art_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"art_type": None}

    def validate_size(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate art_type value."""

        if value.lower() in self.size_db():
            # validation succeeded, set the value of the "size" slot to value
            return {"size": value}
        else:
            dispatcher.utter_message(response="utter_wrong_size_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"size": None}

    def validate_frame(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate frame_type value."""

        if value.lower() in self.frame_db():
            # validation succeeded, set the value of the "Frame" slot to value
            return {"frame": value}
        else:
            dispatcher.utter_message(response="utter_wrong_frame_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"frame": None}

    def validate_finishing(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate finishing value."""

        if value.lower() in self.finishing_db():
            # validation succeeded, set the value of the "size" slot to value
            return {"finishing": value}
        else:
            dispatcher.utter_message(response="utter_wrong_finishing_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"finishing": None}

    def validate_orientation(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate orientation value."""

        if value.lower() in self.orientation_db():
            # validation succeeded, set the value of the "orientation" slot to value
            return {"orientation": value}
        else:
            dispatcher.utter_message(response="utter_wrong_orientation_type")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"orientation": None}

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print("required_slots(tracker: Tracker)")
        return["art_type", "size", "frame", "finishing", "orientation"]

    def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")

        return []